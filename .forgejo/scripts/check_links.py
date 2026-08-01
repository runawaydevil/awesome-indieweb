#!/usr/bin/env python3

import concurrent.futures
import re
import socket
import urllib.error
import urllib.request

README = "README.md"
MARKER = " **(link no longer exists)**"

# Match a list entry and capture its primary URL: "- [Name](https://...) - ..."
# Table rows ("|...") and Table-of-Contents anchors ("#...") never match.
ENTRY_RE = re.compile(r"^- \[[^\]]+\]\((https?://[^)]+)\)")

UA = (
    "Mozilla/5.0 (compatible; awesome-indieweb-linkcheck/1.0; "
    "+https://source.tube/pmurad/awesome-indieweb)"
)
TIMEOUT = 20


def is_dead(url):
    """Return True only on a definitive dead signal (404/410/NXDOMAIN)."""
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": UA})
    try:
        urllib.request.urlopen(req, timeout=TIMEOUT)
        return False
    except urllib.error.HTTPError as e:
        return e.code in (404, 410)
    except urllib.error.URLError as e:
        # DNS resolution failure means the domain itself is gone.
        return isinstance(e.reason, socket.gaierror)
    except Exception:
        # Anything else is inconclusive; never flag on uncertainty.
        return False


def strip_marker(line):
    """Remove a trailing marker (if present), preserving the newline."""
    body = line.rstrip("\n")
    if body.endswith(MARKER):
        nl = "\n" if line.endswith("\n") else ""
        return body[: -len(MARKER)] + nl
    return line


def main():
    with open(README, encoding="utf-8") as f:
        lines = f.readlines()

    # (line index, url) for every entry, ignoring any existing marker.
    targets = []
    for i, line in enumerate(lines):
        m = ENTRY_RE.match(strip_marker(line))
        if m:
            targets.append((i, m.group(1)))

    urls = {url for _, url in targets}
    dead = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as ex:
        futures = {ex.submit(is_dead, u): u for u in urls}
        for fut in concurrent.futures.as_completed(futures):
            url = futures[fut]
            try:
                dead[url] = fut.result()
            except Exception:
                dead[url] = False

    changed, newly_dead, recovered = 0, [], []
    for i, url in targets:
        base = strip_marker(lines[i])
        was_marked = lines[i] != base
        if dead.get(url):
            nl = "\n" if base.endswith("\n") else ""
            updated = base.rstrip("\n") + MARKER + nl
            if updated != lines[i]:
                lines[i], changed = updated, changed + 1
                newly_dead.append(url)
        elif was_marked:
            lines[i], changed = base, changed + 1
            recovered.append(url)

    if changed:
        with open(README, "w", encoding="utf-8", newline="") as f:
            f.writelines(lines)

    print(f"Checked {len(urls)} unique links across {len(targets)} entries.")
    print(f"Newly marked dead: {len(newly_dead)}")
    for u in newly_dead:
        print(f"  DEAD  {u}")
    print(f"Recovered (marker removed): {len(recovered)}")
    for u in recovered:
        print(f"  ALIVE {u}")
    print(f"Lines changed: {changed}")


if __name__ == "__main__":
    main()
