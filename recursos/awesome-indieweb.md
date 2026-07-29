# Awesome IndieWeb

> A large, annotated catalog of protocols, platforms, services, libraries, and tools for publishing, interacting, distributing, preserving, and operating an independent personal website — on your own domain, with durable URLs, connected to the rest of the web through open standards.

IndieWeb is not a product, a social network, or an official stack. It is an approach centered on **publishing first in a space you control** (normally your own domain), keeping URLs durable, and connecting that site to the wider web through open standards. This list therefore separates resources that are **native to the IndieWeb** from **adjacent** tools that solve important parts of the problem well.

This file is a **research compilation** meant to feed a future GitHub `awesome-indieweb` list. It merges an original, curated set of **300 resources** with **287 additional resources** found through extended research — **587 total**. Original items keep their category; new items are grouped under a clearly marked **"Additional (research)"** block inside each category so provenance stays obvious. (This deliberately overshoots a "moderate" target so the final curation step has a rich, pre-labeled pool to cut from rather than to expand.)

---

## Labels

- **Core** — a standard or concept directly tied to IndieWeb architecture.
- **Recommended** — a mature or especially useful component for a real deployment.
- **Adjacent** — not IndieWeb by itself, but composes well into an independent presence.
- **Experimental** — interesting for testing; verify maintenance and compatibility.
- **Reference** — valuable for study, inspiration, or code reuse; not necessarily installable.
- **Historical** — important for understanding the ecosystem, but not a first choice for a new install.
- **Commercial** — useful but paid and/or with lock-in risk; keep an export strategy.

Status, prices, and compatibility were checked around **July 2026**. Community projects change fast — confirm recent releases, docs, issues, and export procedures before adopting a critical component.

---

## 1. Maps, directories & "awesome" lists

- **[IndieWeb Standards](https://spec.indieweb.org/)** — Core — Compact portal to the most-used specs: Webmention, Micropub, IndieAuth, Microsub, microformats.
- **[IndieWeb Projects](https://indieweb.org/projects)** — Core — Official map of platforms, services, libraries, and experiments built or used by the community.
- **[Category: Building Blocks](https://indieweb.org/Category%3Abuilding-blocks)** — Core — Index of the identity, publishing, reading, interaction, and syndication building blocks.
- **[IndieWeb Guide](https://indieweb.guide/)** — Recommended — A progressive, friendlier guide than the wiki for starting a site and adding capabilities.
- **[Getting Started](https://indieweb.org/Getting_Started)** — Core — Community roadmap for getting a domain, hosting, home page, and your own presence.
- **[Indie Dev Toolkit](https://github.com/thedaviddias/indie-dev-toolkit)** — Adjacent — Broad collection of tools for independent developers (domains, content, metrics, operations).
- **[Awesome Selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)** — Adjacent — Huge catalog of self-hosted software; excellent source for comments, readers, media, analytics, archives.
- **[Awesome Static Generators](https://github.com/myles/awesome-static-generators)** — Adjacent — Historical, comprehensive list of static site generators, themes, editors, and hosts.
- **[Jamstack Generators](https://jamstack.org/generators/)** — Adjacent — Searchable directory to compare generators by language, framework, and popularity.
- **[Awesome RSS](https://github.com/AboutRSS/ALL-about-RSS)** — Recommended — One of the largest collections on RSS: readers, generators, bridges, and discovery tools.
- **[Awesome ActivityPub](https://github.com/BasixKOR/awesome-activitypub)** — Adjacent — Map of Fediverse servers, libraries, and clients for connecting your own site via ActivityPub.
- **[Alternative Internet](https://github.com/redecentralize/alternative-internet)** — Adjacent — Decentralization projects, alternative networks, identity, and publishing outside big platforms.
- **[Awesome Decentralized Web](https://github.com/gdamdam/awesome-decentralized-web)** — Adjacent — Distributed and peer-to-peer tech; useful for exploring frontiers beyond conventional IndieWeb.
- **[Awesome CMS](https://github.com/postlight/awesome-cms)** — Adjacent — Catalog of traditional, headless, Git-based, and API-driven content management systems.
- **[Awesome Personal Websites](https://github.com/logancyang/awesome-personal-websites)** — Recommended — Gallery of personal sites to study structure, content, navigation, and visual identity.

**Additional (research):**

- **[awesome-fediverse](https://github.com/emilebosch/awesome-fediverse)** — Adjacent — Curated list of Fediverse software and resources, closely tied to the decentralization ethos.
- **[awesome-digital-gardens](https://github.com/kyrose/awesome-digital-gardens)** — Recommended — Curated list of digital gardens and tools for building your own; squarely in the personal-site space.
- **[awesome-nostr](https://github.com/aljazceru/awesome-nostr)** — Adjacent — Directory of projects and resources on the decentralized Nostr protocol.
- **[awesome-atproto](https://github.com/awesome-atproto/awesome-atproto)** — Adjacent — Curated list of tools built on the AT Protocol (Bluesky), relevant to open-social builders.
- **[awesome-search-engines](https://github.com/prirai/awesome-search-engines)** — Reference — Catalog of independent, privacy, and niche search engines; a jumping-off point for small-web discovery.

## 2. Fundamental protocols, formats & strategies

- **[Webmention](https://www.w3.org/TR/webmention/)** — Core — W3C Recommendation for one site to notify another that it linked to it, enabling replies, likes, mentions, and distributed conversations.
- **[Micropub](https://www.w3.org/TR/micropub/)** — Core — W3C API to create, edit, and delete posts from clients that are independent of the CMS.
- **[IndieAuth](https://indieauth.spec.indieweb.org/)** — Core — Identity and authorization protocol based on the user's own URL.
- **[microformats2](https://microformats.org/wiki/microformats2)** — Core — HTML class conventions that make people, posts, events, and interactions machine-readable without separating data from the page.
- **[h-card](https://microformats.org/wiki/h-card)** — Core — Format for a person's or organization's name, photo, URL, and details; the site's identity card.
- **[h-entry](https://microformats.org/wiki/h-entry)** — Core — Format for posts, notes, articles, photos, replies, likes, and other content.
- **[h-feed](https://microformats.org/wiki/h-feed)** — Core — Container for a sequence of `h-entry` items so an HTML page can also be read as a feed.
- **[Microsub](https://indieweb.org/Microsub-spec)** — Core — Splits the subscription server from the reading client, mirroring what Micropub does on the publishing side.
- **[WebSub](https://www.w3.org/TR/websub/)** — Core (complementary) — Delivers near-real-time feed updates via a publisher–hub–subscriber architecture.
- **[JF2](https://www.w3.org/TR/jf2/)** — Core (complementary) — Simplified JSON representation of data derived from microformats2.
- **[RSS 2.0](https://www.rssboard.org/rss-specification)** — Recommended — Feed format with near-universal compatibility and low implementation cost.
- **[Atom](https://www.rfc-editor.org/rfc/rfc4287)** — Recommended — IETF-standardized feed format, stricter than RSS on identifiers, dates, and extensibility.
- **[JSON Feed 1.1](https://www.jsonfeed.org/version/1.1/)** — Adjacent — Convenient JSON feed for modern apps and integrations; complements rather than replaces RSS/Atom.
- **[OPML 2.0](http://opml.org/spec2.opml)** — Recommended — List format to export/import subscriptions between readers; essential for portability.
- **[POSSE](https://indieweb.org/POSSE)** — Core — "Publish on your Own Site, Syndicate Elsewhere": your site is the origin, external networks get copies or links.

**Additional (research):**

- **[rel-me](https://microformats.org/wiki/rel-me)** — Reference — `rel="me"` convention linking your profiles bidirectionally to prove a site is yours; basis of RelMeAuth and Mastodon verification.
- **[Pingback](https://www.hixie.ch/specs/pingback/pingback)** — Historical — The XML-RPC linkback predecessor to Webmention; useful for backward compatibility and context.
- **[Vouch](https://indieweb.org/Vouch)** — Experimental — Webmention extension where the sender includes a trusted third-party `vouch` URL so receivers can safely accept mentions from strangers.
- **[Salmention](https://indieweb.org/Salmention)** — Experimental — Chained Webmention pattern that propagates thread updates (comments, likes, RSVPs) so all participants' copies stay in sync.
- **[Post Type Discovery](https://www.w3.org/TR/post-type-discovery/)** — Reference — W3C Note defining an algorithm to derive a post's type (note, article, reply, like, RSVP…) from its microformats2 properties.
- **[Private Webmention](https://indieweb.org/Private-Webmention)** — Experimental — Combines Webmention with IndieAuth/AutoAuth so private posts can notify recipients who then authenticate to fetch content.
- **[IndieAuth Ticket Auth](https://indieweb.org/IndieAuth_Ticket_Auth)** — Experimental — IndieAuth extension that pushes an access "ticket" to another site's endpoint for private/reciprocal access without interactive login.
- **[h-event](https://microformats.org/wiki/h-event)** — Reference — microformats2 vocabulary for events (name, start/end, location) consumable by calendars and parsers.
- **[h-review](https://microformats.org/wiki/h-review)** — Reference — microformats2 vocabulary for structured reviews (rating, item, author).
- **[h-recipe](https://microformats.org/wiki/h-recipe)** — Reference — microformats2 vocabulary for recipes (ingredients, yield, duration, instructions).
- **[h-cite](https://microformats.org/wiki/h-cite)** — Reference — microformats2 vocabulary for citing external works; backbone of reply-context, bookmarks, and quotations.
- **[h-product](https://microformats.org/wiki/h-product)** — Reference — microformats2 vocabulary for describing products (name, price, brand, identifier).
- **[h-resume](https://microformats.org/wiki/h-resume)** — Reference — microformats2 vocabulary for publishing a machine-readable resume/CV.
- **[NodeInfo](https://nodeinfo.diaspora.software/)** — Reference — Standardized `.well-known` endpoint exposing a server's software, version, and capabilities; used across the Fediverse for discovery.

## 3. Platforms & systems with IndieWeb DNA

- **[Micro.blog](https://micro.blog/)** — Recommended — Hosted service with custom domain, feeds, clients, community, and many IndieWeb features; the easiest on-ramp with no server admin.
- **[Known](https://github.com/idno/idno)** — Recommended (verify) — PHP social-publishing platform implementing several IndieWeb standards; check releases and requirements before a new install.
- **[microblog.pub](https://github.com/tsileo/microblog.pub)** — Recommended (technical) — Single-user Python server with ActivityPub, Micropub, IndieAuth, and Webmention; bridges IndieWeb and Fediverse.
- **[Indiekit](https://getindiekit.com/)** — Recommended (technical) — Modular Node.js server that receives Micropub and publishes to Git, filesystem, or other content stores.
- **[Dwell](https://github.com/zoglesby/dwell)** — Experimental — Personal app built with IndieWeb technologies; good architecture reference.
- **[IndieWeb for WordPress](https://wordpress.org/plugins/indieweb/)** — Recommended — Aggregator plugin and entry point to configure identity, Webmention, Micropub, and compatible themes in WordPress.
- **[IndieWeb for Drupal](https://www.drupal.org/project/indieweb)** — Recommended (verify) — Module integrating IndieWeb technologies into Drupal; confirm supported version and related modules.
- **[GoBlog](https://github.com/jlelse/GoBlog)** — Recommended (technical) — Go blog application with Webmention, Micropub, IndieAuth, feeds, and multiple post types.
- **[Koype](https://indieweb.org/Koype)** — Experimental — Personal social hub that aimed to concentrate publishing, identity, and interactions; audit maintenance and locate current code.
- **[Sweetroll](https://indieweb.org/sweetroll)** — Experimental — Personal software inspired by blogroll and social reading; relevant as an exploration of relationships and discovery.
- **[Publ](https://github.com/PlaidWeb/Publ)** — Recommended (Python) — File-based dynamic CMS with categories and templates, used on varied personal sites.
- **[Taproot](https://indieweb.org/Taproot)** — Reference — PHP personal platform whose open parts influenced IndieWeb implementations; not a beginner-ready install.
- **[Dobrado](https://indieweb.org/dobrado)** — Experimental — Multi-user PHP/JS CMS built for simple publishing and decentralized social features.
- **[Bundle](https://indieweb.org/Bundle)** — Reference (experimental) — Python/Django toolset built for a personal site; parts may inspire your own implementations.
- **[Falcon](https://indieweb.org/Falcon)** — Reference — The system running tantek.com; demonstrates a long-lived IndieWeb architecture but isn't shipped as a complete installable package.

**Additional (research):**

- **[Hollo](https://docs.hollo.social/)** — Recommended — Single-user, headless ActivityPub microblog built on Fedify; run a personal Fediverse identity on your own domain.
- **[Postmarks](https://github.com/ckolderup/postmarks)** — Recommended — Single-user, self-hosted del.icio.us-style bookmarking site that federates over ActivityPub.
- **[Site.js](https://sitejs.org/)** — Recommended — Aral Balkan's small-tech tool to develop and host a personal site with automatic TLS and single-command deploy.
- **[Smallweb](https://www.smallweb.run/)** — Experimental — CGI-inspired personal cloud where each subdomain maps to a folder of Deno code; trivial to host many small sites yourself.
- **[twtxt](https://twtxt.readthedocs.io/)** — Experimental — Decentralized, minimalist microblogging built on a single plain-text file served from your own domain.
- **[prose.sh](https://pico.sh/prose)** — Recommended — SSH-powered Markdown blog: publish by rsync/scp of `.md` files, no accounts or dashboards.
- **[Scribbles](https://scribbles.page/)** — Commercial — Minimal, privacy-respecting blogging platform with custom-domain support and Markdown writing.
- **[weblog.lol](https://weblog.lol/)** — Commercial — omg.lol's plain-text blogging service; posts are Markdown synced via GitHub/email, publishable on your own domain with full export.
- **[Pika](https://pika.page/)** — Commercial — Simple blog-and-personal-page builder for makers, with custom domains and a writing focus.
- **[Listed](https://listed.to/)** — Commercial — Minimalist blogging platform by Standard Notes; publish notes as a public blog on a custom domain.
- **[Val Town](https://www.val.town/)** — Adjacent — Social platform for tiny serverless functions and sites; handy for webmention handlers and small IndieWeb glue.

## 4. General, minimal & file-based CMS

- **[WordPress](https://wordpress.org/)** — Recommended — Mature ecosystem, wide export, and the best set of IndieWeb plugins; requires discipline with security, performance, and plugins.
- **[Ghost](https://ghost.org/)** — Recommended (adjacent) — Excellent for publishing and newsletters on your own domain; Webmention and microformats need a theme or add-ons.
- **[WriteFreely](https://writefreely.org/)** — Recommended (adjacent) — Minimalist, federated text platform suited to simple blogs and personal instances.
- **[Bear Blog](https://bearblog.dev/)** — Recommended (adjacent) — Minimalist, fast, script-free hosting; custom domain and feeds make a lean personal base.
- **[Mataroa](https://mataroa.blog/)** — Recommended (adjacent) — Simple hosted blog with export and few distractions; good for writing-first people.
- **[Blot](https://blot.im/)** — Recommended (adjacent) — Turns a folder of files into a website, preserving local content and a very simple publishing flow.
- **[Grav](https://getgrav.org/)** — Recommended (adjacent) — Flexible PHP flat-file CMS with no database; suits shared hosting.
- **[Kirby](https://getkirby.com/)** — Recommended (commercial) — High-quality flat-file CMS, excellent for custom sites; requires a license and implementing the standards you want.
- **[ProcessWire](https://processwire.com/)** — Recommended (technical) — Very flexible PHP CMS/framework; the community has built IndieWeb modules and experiments.
- **[Textpattern](https://textpattern.com/)** — Adjacent — Lightweight, long-lived editorial CMS for people who prefer template and markup control.
- **[Pico](https://picocms.org/)** — Adjacent — Extremely small PHP flat-file CMS for a personal page or blog with no heavy panel.
- **[Automad](https://automad.org/)** — Adjacent — Flat-file CMS with a visual panel and templates, balancing friendly editing and portability.
- **[WonderCMS](https://www.wondercms.com/)** — Adjacent — Tiny, database-free CMS for simple personal sites; extend cautiously and keep backups.
- **[Publii](https://getpublii.com/)** — Recommended (adjacent) — Desktop app that generates and deploys a static site; publish without a terminal.
- **[Datenstrom Yellow](https://datenstrom.se/yellow/)** — Adjacent — Small flat-file CMS, editable in the browser and easy to move between servers.

**Additional (research):**

- **[ClassicPress](https://www.classicpress.net/)** — Recommended — Community-governed WordPress fork without the block editor; lightweight and fully self-hosted.
- **[HTMLy](https://www.htmly.com/)** — Recommended — Databaseless PHP blogging platform storing posts as flat files; easy to host on cheap hosting.
- **[Typemill](https://typemill.net/)** — Recommended — Markdown-based flat-file CMS for docs, handbooks, and personal sites, with eBook export.
- **[Bludit](https://www.bludit.com/)** — Recommended — Simple, fast flat-file (JSON) CMS for blogs and small sites; no database, trivial to move.
- **[FlatPress](https://www.flatpress.org/)** — Recommended — Lightweight databaseless blogging engine that runs on minimal PHP hosting.
- **[Chyrp Lite](https://chyrplite.net/)** — Recommended — Ultra-light, extensible PHP blogging engine (tumblelog-style) supporting many post kinds.
- **[Statamic](https://statamic.com/)** — Commercial — Laravel-based flat-file (or DB) CMS with Git-friendly content; popular for developer-owned sites.
- **[Cockpit](https://getcockpit.com/)** — Recommended — API-first headless CMS light enough to self-host for a personal project's structured content.
- **[October CMS](https://octobercms.com/)** — Adjacent — Laravel-based, file-friendly CMS with version-controllable content.
- **[SPIP](https://www.spip.net/)** — Reference — Long-running French publishing CMS for collaborative editorial sites; a durable community-owned option.
- **[Serendipity (s9y)](https://docs.s9y.org/)** — Historical — Veteran PHP blog engine with native webmention/pingback heritage; minimally maintained but a reference.
- **[GetSimple CMS](http://get-simple.info/)** — Historical — XML flat-file, no-database CMS for tiny sites; a classic of the databaseless lineage.

## 5. Static site generators

- **[Eleventy](https://www.11ty.dev/)** — Recommended — Flexible, unopinionated, great for semantic HTML; many Webmention and microformats examples.
- **[Hugo](https://gohugo.io/)** — Recommended — Fast, mature single binary suited to large sites; simple deployment with few runtimes.
- **[Astro](https://astro.build/)** — Recommended — Combines content, components, and optional JavaScript; great for a modern personal site without a full SPA.
- **[Jekyll](https://jekyllrb.com/)** — Recommended — The historical GitHub Pages generator, with a vast set of themes and IndieWeb examples.
- **[Zola](https://www.getzola.org/)** — Recommended — Rust generator with a single binary, taxonomies, Sass, and built-in search.
- **[Pelican](https://getpelican.com/)** — Recommended (Python) — Mature generator with feeds, plugins, and importers.
- **[Nikola](https://getnikola.com/)** — Recommended (Python) — Supports many input formats, galleries, multilingual, and blog workflows.
- **[Hexo](https://hexo.io/)** — Adjacent — Popular, fast Node.js generator with a huge theme ecosystem.
- **[Gatsby](https://www.gatsbyjs.com/)** — Adjacent — React framework for content; powerful, but usually more complex than a personal IndieWeb site needs.
- **[Next.js](https://nextjs.org/)** — Adjacent — Hybrid React framework for projects needing dynamic routes, APIs, and varied rendering.
- **[Nuxt Content](https://content.nuxt.com/)** — Adjacent — Markdown-based publishing inside the Vue/Nuxt ecosystem.
- **[Bridgetown](https://www.bridgetownrb.com/)** — Adjacent — Modern Jekyll-inspired successor, useful for Ruby developers.
- **[Hakyll](https://jaspervdj.be/hakyll/)** — Adjacent (technical) — Haskell library to generate sites with fully programmable pipelines.
- **[Lume](https://lume.land/)** — Adjacent — Generator for Deno with multi-format support and plugins.
- **[soupault](https://soupault.app/)** — Recommended (hand-made HTML) — Site processor that works directly on HTML and enables automation without imposing a framework.

**Additional (research):**

- **[VitePress](https://vitepress.dev/)** — Recommended — Vite/Vue-powered generator, fast and minimal; great for personal docs, blogs, and knowledge sites.
- **[Docusaurus](https://docusaurus.io/)** — Recommended — React-based generator optimized for docs and knowledge sites, with built-in blog, MDX, and versioning.
- **[mdBook](https://rust-lang.github.io/mdBook/)** — Recommended — Rust tool that turns Markdown into a clean online book/site; ideal for handbooks and gardens.
- **[Quartz](https://quartz.jzhao.xyz/)** — Recommended — Publishes Obsidian/Markdown vaults as interlinked digital gardens on your own domain.
- **[Metalsmith](https://metalsmith.io/)** — Recommended — Extremely pluggable "everything is a plugin" JS generator for fully custom pipelines.
- **[Middleman](https://middlemanapp.com/)** — Recommended — Mature Ruby static generator with a full modern front-end toolchain.
- **[MkDocs](https://www.mkdocs.org/)** — Recommended — Python Markdown-to-static generator (great with Material) for docs, notes, and knowledge bases.
- **[Cecil](https://cecil.app/)** — Recommended — Content-driven PHP static generator (Markdown + Twig) that runs anywhere PHP does.
- **[Cobalt](https://cobalt-org.github.io/)** — Recommended — Fast Jekyll-inspired generator in Rust, single binary, good for a low-maintenance blog.
- **[Publish](https://github.com/JohnSundell/Publish)** — Recommended — Swift static generator (John Sundell) for building sites in Swift with type-safe HTML.
- **[Statiq](https://www.statiq.dev/)** — Recommended — Flexible .NET static site/content generator for building personal sites in C#.
- **[Marmite](https://rochacbruno.github.io/marmite/)** — Experimental — Zero-config Rust generator that turns a folder of Markdown into a blog with almost no setup.
- **[Pollen](https://docs.racket-lang.org/pollen/)** — Reference — Matthew Butterick's Racket system for book-quality personal sites with programmable markup.
- **[Franklin.jl](https://franklinjl.org/)** — Experimental — Julia generator with live-evaluated code and math; popular for technical/research sites.
- **[VuePress](https://vuepress.vuejs.org/)** — Reference — Vue-powered Markdown-centric generator (predecessor to VitePress) for docs-style sites.
- **[Gridsome](https://gridsome.org/)** — Historical — Vue + GraphQL Jamstack generator; effectively unmaintained but historically notable.

## 6. Editors, Git CMS & content layers

- **[Sveltia CMS](https://github.com/sveltia/sveltia-cms)** — Recommended — Modern panel for Git repositories, compatible with Decap CMS configuration.
- **[Decap CMS](https://decapcms.org/)** — Recommended — Open-source CMS to edit static-site content and commit changes to Git.
- **[Pages CMS](https://pagescms.org/)** — Recommended — Simple interface to edit content and media directly in GitHub repositories.
- **[TinaCMS](https://tina.io/)** — Adjacent — Visual editing and structured content for Git-based sites, especially React/Next.js.
- **[Keystatic](https://keystatic.com/)** — Recommended (technical) — CMS that stores content on the filesystem or GitHub; integrates well with Astro and Next.js.
- **[CloudCannon](https://cloudcannon.com/)** — Adjacent (commercial) — Visual editing and editorial workflow for static sites; useful when non-technical authors participate.
- **[Static CMS](https://www.staticcms.org/)** — Adjacent — Community fork of Netlify/Decap CMS focused on maintenance and extra features.
- **[Front Matter CMS](https://frontmatter.codes/)** — Recommended — VS Code extension to manage Markdown, taxonomies, and media locally.
- **[Siteleaf](https://www.siteleaf.com/)** — Adjacent (commercial) — Hosted CMS that syncs content with GitHub and builds Jekyll sites.
- **[Prose](https://prose.io/)** — Reference — Content editor for GitHub that popularized the CMS-over-Git model; verify maintenance before depending on it.
- **[Outstatic](https://outstatic.com/)** — Adjacent — Git-based CMS for Next.js with a built-in panel and Markdown content.
- **[Sanity](https://www.sanity.io/)** — Adjacent (commercial) — Structured content platform and APIs; powerful, but creates lock-in without an export strategy.
- **[Directus](https://directus.io/)** — Adjacent (self-hostable) — Data layer and panel over SQL for sites needing structured content and APIs.
- **[Strapi](https://strapi.io/)** — Adjacent (self-hostable) — Extensible Node.js headless CMS for more complex personal apps.
- **[Payload](https://payloadcms.com/)** — Adjacent (self-hostable) — TypeScript CMS embeddable in modern apps, with schema control and authentication.

**Additional (research):**

- **[Netlify CMS](https://www.netlifycms.org/)** — Historical — The original open-source Git-backed editing CMS; superseded by Decap but foundational to the lineage.
- **[Forestry.io](https://forestry.io/)** — Historical — Early Git-backed content editor; sunset and evolved into TinaCMS, kept for context.
- **[Storyblok](https://www.storyblok.com/)** — Adjacent — Visual, API-first headless CMS with a generous free tier; usable for a developer's personal site.
- **[Hygraph](https://hygraph.com/)** — Adjacent — GraphQL-native headless CMS (formerly GraphCMS) that can back a personal Jamstack site.

## 7. Domains, static hosting & publishing

- **[Porkbun](https://porkbun.com/)** — Recommended — Competitive-price registrar with WHOIS privacy and direct DNS management; check renewal prices.
- **[Namecheap](https://www.namecheap.com/)** — Adjacent — Popular registrar with broad docs; compare renewal and privacy policy per TLD.
- **[Gandi](https://www.gandi.net/)** — Adjacent — Veteran registrar with DNS and APIs; re-check pricing and current bundle before buying.
- **[Cloudflare Registrar](https://www.cloudflare.com/products/registrar/)** — Recommended (caveat) — At-cost registration, but the domain is tied to using Cloudflare DNS.
- **[GitHub Pages](https://pages.github.com/)** — Recommended — Free static hosting integrated with GitHub; simple for Jekyll and build actions.
- **[GitLab Pages](https://docs.gitlab.com/user/project/pages/)** — Recommended — Publishes static sites via GitLab CI/CD pipelines and supports custom domains.
- **[Codeberg Pages](https://codeberg.page/)** — Recommended — Community hosting on Forgejo; interesting for reducing dependence on big platforms.
- **[Cloudflare Pages](https://pages.cloudflare.com/)** — Recommended — Builds, CDN, and custom domain with a good free tier; dynamic functions increase platform dependence.
- **[Netlify](https://www.netlify.com/)** — Recommended (limits) — Easy deploys, previews, and functions; watch quotas and keep the site exportable.
- **[Vercel](https://vercel.com/)** — Adjacent — Great integration with modern frameworks, especially Next.js; avoid proprietary features when portability matters.
- **[Render Static Sites](https://render.com/docs/static-sites)** — Adjacent — Git deploys, TLS, and CDN for static sites.
- **[Neocities](https://neocities.org/)** — Recommended (personal web) — Simple hosting with a maker community and direct HTML/CSS editing.
- **[NearlyFreeSpeech.NET](https://www.nearlyfreespeech.net/)** — Recommended (technical) — Long-lived, pay-per-use hosting suited to small personal sites.
- **[statichost.eu](https://statichost.eu/)** — Adjacent — Simple, Git-oriented static hosting with custom domains and European infrastructure.
- **[Opalstack](https://opalstack.com/)** — Recommended — Independent hosting for static sites and apps, with shell access and varied runtimes.

**Additional (research):**

- **[Njalla](https://njal.la/)** — Recommended — Privacy-first registrar that registers domains as a legal proxy, shielding ownership; crypto payment supported.
- **[Dynadot](https://www.dynadot.com/)** — Recommended — Independent registrar with transparent at-cost pricing, free WHOIS privacy, and a clean API.
- **[INWX](https://www.inwx.com/)** — Recommended — German registrar with wide TLD coverage, DNSSEC, and a robust API.
- **[Hover](https://www.hover.com/)** — Recommended — Domains-and-email-only registrar (no upsell bloat) with free WHOIS privacy.
- **[Spaceship](https://www.spaceship.com/)** — Adjacent — Namecheap-affiliated registrar with aggressive at-cost pricing and free WHOIS privacy.
- **[EasyDNS](https://easydns.com/)** — Adjacent — Independent Canadian registrar and managed-DNS provider with a strong civil-liberties record.
- **[1984 Hosting](https://1984.hosting/)** — Recommended — Iceland-based, privacy- and free-speech-focused registrar and host; accepts anonymous/crypto signups.
- **[Nekoweb](https://nekoweb.org/)** — Recommended — Free "old web" static host (2024) for hand-crafted personal HTML pages, with custom domains.
- **[smol.pub](https://smol.pub/)** — Recommended — Ultra-minimal Gemini-and-web blogging platform embodying small-web simplicity.
- **[Bunny.net](https://bunny.net/)** — Recommended — Affordable European CDN with Edge Storage and static-site hosting on a custom domain.
- **[Fly.io](https://fly.io/)** — Recommended — Runs your Docker/app containers close to users; good for dynamic personal sites with full portability.
- **[Deno Deploy](https://deno.com/deploy)** — Adjacent — Globally distributed JS/TS edge runtime with custom domains; host a site or dynamic endpoints without servers.
- **[Surge.sh](https://surge.sh/)** — Adjacent — Single-command static publishing from the terminal with custom-domain support.
- **[sourcehut Pages](https://srht.site/)** — Recommended — Simple static hosting from the tracking-free sourcehut ecosystem; publish via a build manifest.
- **[tilde.town](https://tilde.town/)** — Core — Friendly public-access Unix community offering shell accounts and `~user` personal pages; a small-web flagship.
- **[SDF Public Access Unix](https://sdf.org/)** — Reference — Long-running non-profit public-access Unix co-op with shell accounts and personal web/email hosting.
- **[Hetzner](https://www.hetzner.com/)** — Commercial — German provider with very low-cost cloud VPS and dedicated servers; a self-hosting favorite.
- **[Mythic Beasts](https://www.mythic-beasts.com/)** — Recommended — UK independent host offering VPS, shell accounts, DNS, and personal web/email hosting.
- **[rsync.net](https://rsync.net/)** — Adjacent — Minimalist offsite storage accessed over SSH/rsync/SFTP; ideal for portable, provider-agnostic backups.

## 8. Servers, TLS, containers & deployment

- **[Caddy](https://caddyserver.com/)** — Recommended — Server and proxy with automatic HTTPS; an excellent default for a small personal server.
- **[nginx](https://nginx.org/)** — Recommended — Widely documented, efficient server and reverse proxy available on nearly every provider.
- **[Apache HTTP Server](https://httpd.apache.org/)** — Recommended — Mature option, especially suited to PHP hosting and per-directory configuration.
- **[lighttpd](https://www.lighttpd.net/)** — Adjacent — Lightweight server for small installs and modest hardware.
- **[Traefik](https://traefik.io/traefik/)** — Adjacent — Dynamic reverse proxy useful when several services run in containers.
- **[HAProxy](https://www.haproxy.org/)** — Adjacent — Robust proxy and load balancer for architectures needing more traffic control.
- **[Let's Encrypt](https://letsencrypt.org/)** — Recommended — Free certificate authority that made HTTPS accessible to personal sites.
- **[Certbot](https://certbot.eff.org/)** — Recommended — Client to issue and renew Let's Encrypt certificates when the server doesn't automate it.
- **[Docker](https://www.docker.com/)** — Adjacent — Packages services and dependencies; useful, but doesn't replace backup, updates, and observability.
- **[Podman](https://podman.io/)** — Adjacent — OCI-compatible containers with good rootless options and systemd integration.
- **[Docker Compose](https://docs.docker.com/compose/)** — Recommended — Describes a small self-hosted stack in a versionable, reproducible file.
- **[Coolify](https://coolify.io/)** — Adjacent — Self-hostable PaaS to deploy apps and databases via a web UI.
- **[CapRover](https://caprover.com/)** — Adjacent — Deployment panel over Docker to run multiple apps on a VPS.
- **[Dokku](https://dokku.com/)** — Adjacent — Compact Heroku-inspired PaaS, driven by Git and the command line.
- **[Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/)** — Adjacent (caveat) — Publishes a service without opening ports; convenient, but adds a proprietary intermediary.

**Additional (research):**

- **[OpenLiteSpeed](https://openlitespeed.org/)** — Recommended — High-performance server with HTTP/3 and built-in caching; a lighter alternative to nginx/Apache.
- **[H2O](https://h2o.examp1e.net/)** — Adjacent — Fast HTTP/1.x, HTTP/2, and HTTP/3 server optimized for low latency.
- **[Angie](https://angie.software/)** — Adjacent — Actively maintained nginx fork (by former nginx developers) adding HTTP/3 and a management API.
- **[acme.sh](https://github.com/acmesh-official/acme.sh)** — Recommended — Pure-shell ACME client with the widest DNS-provider support; dependency-free TLS automation.
- **[lego](https://go-acme.github.io/lego/)** — Recommended — Single-binary Go ACME client/library supporting hundreds of DNS providers.
- **[dehydrated](https://github.com/dehydrated-io/dehydrated)** — Adjacent — Minimal Bash ACME client for Let's Encrypt; auditable and lightweight.
- **[step-ca (Smallstep)](https://smallstep.com/docs/step-ca/)** — Recommended — Self-hosted certificate authority and ACME server for full ownership of your PKI.
- **[mkcert](https://github.com/FiloSottile/mkcert)** — Reference — Zero-config locally-trusted TLS certificates for testing your site over HTTPS locally.
- **[ZeroSSL](https://zerossl.com/)** — Adjacent — Free ACME-compatible certificate authority (alternative to Let's Encrypt) with API and dashboard.
- **[YunoHost](https://yunohost.org/)** — Core — Debian-based OS that one-click installs personal-web apps with automatic TLS and email; a cornerstone of owning your services.
- **[Cloudron](https://cloudron.io/)** — Recommended — Turnkey platform to install and auto-update self-hosted apps with managed backups, TLS, and users.
- **[FreedomBox](https://freedombox.org/)** — Core — Debian-based personal server system for hosting your own web, email, and social services on cheap hardware.
- **[CasaOS](https://casaos.io/)** — Recommended — Simple Docker-based home-server OS with an app-store UI; a friendly on-ramp to self-hosting.
- **[runtipi](https://runtipi.io/)** — Recommended — Lightweight homeserver platform with a one-click app store built on Docker.
- **[Portainer](https://www.portainer.io/)** — Recommended — Web UI for managing Docker/Kubernetes; simplifies the containers behind a self-hosted site.
- **[Kamal](https://kamal-deploy.org/)** — Recommended — Deploy tool (37signals) that ships Docker apps to any bare VPS with zero downtime; frees you from PaaS lock-in.
- **[HestiaCP](https://hestiacp.com/)** — Recommended — Lightweight open-source control panel for web, DNS, mail, and databases on your own VPS.
- **[Dokploy](https://dokploy.com/)** — Recommended — Open-source, self-hostable Vercel/Heroku alternative to deploy apps and databases via a UI.
- **[NixOS](https://nixos.org/)** — Recommended — Linux distribution with declarative, reproducible system configuration; portable, rebuildable servers.
- **[Sandstorm](https://sandstorm.io/)** — Adjacent — Open-source platform to run self-hosted web apps in secure sandboxes with one-click installs.
- **[Ansible](https://www.ansible.com/)** — Reference — Agentless automation to provision and configure servers reproducibly; underpins portable self-hosting.

## 9. Microformats, extraction & validation

- **[php-mf2](https://github.com/microformats/php-mf2)** — Core (PHP) — microformats2 parser used by many IndieWeb tools.
- **[mf2py](https://github.com/microformats/mf2py)** — Core (Python) — Parser to extract microformats2 from HTML.
- **[microformats-parser](https://github.com/microformats/microformats-parser)** — Core (JavaScript) — JavaScript implementation of the parsing algorithm.
- **[go-microformats](https://github.com/willnorris/microformats)** — Core (Go) — microformats2 parser for Go applications and services.
- **[mf2util](https://pypi.org/project/mf2util/)** — Adjacent (Python) — High-level utilities on top of microformats2 data.
- **[XRay](https://github.com/aaronpk/XRay)** — Recommended — PHP parser that turns pages with microformats into objects useful for readers, replies, and endpoints.
- **[Pin13](https://pin13.net/)** — Recommended — Web interface to test how a page is interpreted by microformats parsers.
- **[IndieWebify.Me](https://indiewebify.me/)** — Recommended — Checks identity, `h-card`, posts, and Webmention in didactic steps.
- **[Microformats Test Suite](https://github.com/microformats/tests)** — Core (implementers) — Shared cases to test conformance across parsers.
- **[extruct](https://github.com/scrapinghub/extruct)** — Adjacent — Extracts microformats, JSON-LD, Open Graph, RDFa, and other metadata from pages.
- **[Microformats Wiki](https://microformats.org/wiki/)** — Core — Documentation of the formats, authoring patterns, and compatibility.
- **[Nu Html Checker](https://validator.w3.org/nu/)** — Recommended — Validates modern HTML, avoiding structural errors that also harm parsers.
- **[W3C Markup Validation Service](https://validator.w3.org/)** — Adjacent — Classic validator for HTML and XHTML documents.
- **[W3C Link Checker](https://validator.w3.org/checklink)** — Recommended — Detects broken links and problematic redirects.
- **[Schema.org Validator](https://validator.schema.org/)** — Adjacent — Inspects structured data beyond microformats and flags markup conflicts.

**Additional (research):**

- **[microformats-ruby](https://github.com/microformats/microformats-ruby)** — Recommended (Ruby) — Maintained gem parsing microformats1/2 into Ruby objects, a hash, or JSON.
- **[MicroMicro](https://github.com/jgarber623/micromicro)** — Recommended (Ruby) — Alternative gem focused on strict, modern microformats2 extraction.
- **[microformats2-elixir](https://github.com/ckruse/microformats2-elixir)** — Adjacent (Elixir) — microformats2 parser for the Elixir ecosystem, filling a language gap.

## 10. Webmention & distributed interactions

- **[Webmention.io](https://webmention.io/)** — Recommended — Hosted, open-source endpoint to receive Webmentions without running your own service.
- **[Bridgy](https://brid.gy/)** — Recommended — Syndication and backfeed between your site and supported platforms, converting interactions into Webmentions.
- **[Telegraph](https://telegraph.p3k.io/)** — Recommended — Finds and sends Webmentions from a page, with an API and send monitoring.
- **[webmention.app](https://webmention.app/docs)** — Recommended (static) — Service and build tool that discovers links and sends Webmentions.
- **[webmention.rocks](https://webmention.rocks/)** — Core (testing) — Interoperability test suite for receiving and sending endpoints.
- **[mention-client-php](https://github.com/indieweb/mention-client-php)** — Recommended (PHP) — Library to discover endpoints and send Webmention or Pingback.
- **[webmention-client-ruby](https://github.com/indieweb/webmention-client-ruby)** — Adjacent (Ruby) — Client to send and verify Webmentions in Ruby apps.
- **[webmentiond](https://github.com/zerok/webmentiond)** — Recommended (self-hostable) — Go service to receive and process Webmentions separately from the site.
- **[Go-Jamming](https://github.com/lumenpink/go-jamming)** — Adjacent — Self-hostable Webmention endpoint in Go, aimed at static sites.
- **[Lazymention](https://github.com/strugee/lazymention)** — Adjacent — Minimal endpoint to forward received Webmentions to another flow.
- **[Pushl](https://github.com/PlaidWeb/Pushl)** — Experimental — Service and library for sending Webmentions; verify activity before production.
- **[django-webmention](https://github.com/easy-as-python/django-webmention)** — Adjacent (Django) — Webmention integration for Django applications.
- **[WordPress Webmention](https://wordpress.org/plugins/webmention/)** — Recommended — Receives and sends Webmentions in WordPress and integrates reactions into comments.
- **[eleventy-cache-webmentions](https://github.com/chrisburnell/eleventy-cache-webmentions)** — Adjacent — Helps Eleventy projects fetch and cache Webmentions during the build.
- **[webmention.js](https://github.com/PlaidWeb/webmention.js)** — Adjacent — Client library to display Webmentions on pages, useful for static sites.

**Additional (research):**

- **[willnorris/webmention (Go)](https://github.com/willnorris/webmention)** — Recommended (Go) — Go library and CLI to discover endpoints and send Webmentions.
- **[eleventy-webmentions (Max Böck)](https://github.com/maxboeck/eleventy-webmentions)** — Recommended — Eleventy starter demonstrating fetching and rendering Webmention.io data on a static blog.
- **[gatsby-plugin-webmention](https://github.com/ChristopherBiscardi/gatsby-plugin-webmention)** — Adjacent — Gatsby plugin sourcing Webmention.io data into GraphQL (check activity; somewhat dated).

## 11. Identity, authentication & security

- **[IndieAuth.com](https://indieauth.com/)** — Recommended — Server and compatibility tool for IndieAuth authentication.
- **[IndieLogin.com](https://indielogin.com/)** — Recommended — Login service based on your domain and `rel=me` relations.
- **[IndieAuth.rocks](https://indieauth.rocks/)** — Core (testing) — Tests IndieAuth clients and servers against interoperability cases.
- **[WordPress IndieAuth](https://wordpress.org/plugins/indieauth/)** — Recommended — Turns WordPress into an IndieAuth server and authorizes Micropub clients.
- **[indieauth-client-php](https://github.com/indieweb/indieauth-client-php)** — Recommended (PHP) — Practical reference client to implement IndieAuth login.
- **[RelMeAuth](https://microformats.org/wiki/RelMeAuth)** — Reference — Earlier, still conceptually useful technique to prove identity via reciprocal `rel=me` links.
- **[WebFinger](https://www.rfc-editor.org/rfc/rfc7033)** — Adjacent — Discovery of information about `user@domain` identities, widely used in the Fediverse.
- **[Keyoxide](https://keyoxide.org/)** — Adjacent — Decentralized identity proofs linking cryptographic keys to profiles and domains.
- **[Libravatar](https://www.libravatar.org/)** — Adjacent — Open, federated alternative to Gravatar for hosting avatars.
- **[Mozilla Observatory](https://observatory.mozilla.org/)** — Recommended — Assesses HTTP security headers and suggests improvements.
- **[Qualys SSL Labs](https://www.ssllabs.com/ssltest/)** — Recommended — Tests TLS configuration, certificate chain, and insecure protocols.
- **[Security Headers](https://securityheaders.com/)** — Recommended — Quick check of CSP, HSTS, frame policies, and other headers.
- **[security.txt](https://securitytxt.org/)** — Adjacent — Standard to publish a responsible contact channel for vulnerabilities.
- **[CSP Evaluator](https://csp-evaluator.withgoogle.com/)** — Recommended — Analyzes a Content Security Policy and highlights dangerous permissions.
- **[OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)** — Recommended — Practical reference for authentication, sessions, uploads, headers, and secure development.

**Additional (research):**

- **[WebFinger (WordPress)](https://wordpress.org/plugins/webfinger/)** — Adjacent — Implements the WebFinger discovery endpoint on WordPress, aiding Fediverse and IndieAuth discovery.

## 12. Micropub: clients, endpoints & mobile publishing

- **[Quill](https://quill.p3k.io/)** — Recommended — Versatile web Micropub client for notes, articles, photos, bookmarks, RSVPs, and more.
- **[Micropublish](https://github.com/barryf/micropublish)** — Recommended (self-hostable) — Micropub client with a full interface and support for advanced properties.
- **[Omnibear](https://omnibear.com/)** — Experimental — Browser extension to publish replies, likes, reposts, and bookmarks via Micropub; confirm current compatibility.
- **[iA Writer](https://ia.net/writer)** — Adjacent (commercial) — Editor that can publish via Micropub to compatible platforms; focused desktop/mobile writing.
- **[Micropub.rocks](https://micropub.rocks/)** — Core (testing) — Suite to verify Micropub clients and servers.
- **[WordPress Micropub](https://wordpress.org/plugins/micropub/)** — Recommended — Micropub endpoint for WordPress, enabling publishing from independent clients.
- **[webpage-micropub-to-github](https://github.com/voxpelli/webpage-micropub-to-github)** — Recommended (Git) — Endpoint that converts Micropub requests into files or commits on GitHub.
- **[micro-panel](https://github.com/valpackett/micro-panel)** — Historical — Archived Micropub panel still useful as an interface/implementation reference.
- **[Sparkles](https://indieweb.org/Sparkles)** — Experimental — Micropub client geared toward publishing photos and media.
- **[OwnYourGram](https://ownyourgram.com/)** — Historical (useful) — Demonstrates PESOS by importing photos posted elsewhere into your own site; depends on external APIs.
- **[OwnYourSwarm](https://ownyourswarm.p3k.io/)** — Recommended (check-ins) — Sends Swarm check-ins to your own site via Micropub, subject to the service's APIs.
- **[Teacup](https://indieweb.org/Teacup)** — Experimental — Micropub client specialized in logging what you're drinking.
- **[Compass](https://indieweb.org/Compass)** — Experimental — Location app that can publish data and check-ins to a Micropub endpoint.
- **[IndieBookClub](https://indiebookclub.biz/)** — Recommended — Micropub client to log books, reading status, and reviews.
- **[IndiePass](https://indieweb.org/IndiePass)** — Historical — Integrated Micropub/Microsub client; archived and removed from stores in January 2026, so a reference rather than a new recommendation.

**Additional (research):**

- **[indielib (Go)](https://github.com/hacdias/indielib)** — Recommended (Go) — Go IndieWeb toolkit bundling IndieAuth client/server, Micropub, and discovery helpers.
- **[benjifs/micropub](https://github.com/benjifs/micropub)** — Recommended — Serverless Micropub and media endpoint that publishes posts to a Git-backed static site.
- **[kirby-micropub](https://github.com/sebsel/kirby-micropub)** — Adjacent — Micropub server endpoint for the Kirby CMS (targets Kirby 2; aging).
- **[selfauth](https://github.com/Inklings-io/selfauth)** — Adjacent — Minimal single-user PHP IndieAuth authorization endpoint so you can be your own identity provider.
- **[Indigenous for Android](https://indigenous.realize.be/)** — Recommended — Native Android app acting as a Micropub posting client and Microsub reader.

### WordPress IndieWeb plugin suite

- **[Post Kinds](https://wordpress.org/plugins/indieweb-post-kinds/)** — Core — Adds reply/like/bookmark/RSVP post types with proper microformats2 markup and reply-context.
- **[Syndication Links](https://wordpress.org/plugins/syndication-links/)** — Core — Displays and manages POSSE syndication URLs for cross-posted content.
- **[Semantic Linkbacks](https://wordpress.org/plugins/semantic-linkbacks/)** — Core — Enriches incoming Webmentions/pingbacks into semantic comments (likes, reposts, replies).
- **[Simple Location](https://wordpress.org/plugins/simple-location/)** — Recommended — Adds location and weather metadata (h-geo/h-adr) to posts for check-ins and geotagged notes.
- **[Yarns Microsub Server](https://github.com/jackjamieson2/yarns-microsub-server)** — Recommended — Turns WordPress into a Microsub server so you can host your own social reader feeds.
- **[Parse This](https://github.com/dshanske/parse-this)** — Adjacent — microformats2/feed/JSONFeed parsing library used by Post Kinds and Yarns for reply-context and feeds.
- **[WebSub/PubSubHubbub for WP](https://wordpress.org/plugins/pubsubhubbub/)** — Recommended — Adds WebSub (real-time feed push) publishing to WordPress feeds.

## 13. Feeds, readers & Microsub

- **[Aperture](https://github.com/aaronpk/Aperture)** — Core — Microsub server keeping subscriptions, channels, and read state separate from the interface.
- **[Monocle](https://monocle.p3k.io/)** — Core — Web Microsub client built for social reading and replying via Micropub.
- **[Together](https://github.com/cleverdevil/Together)** — Experimental — Microsub client exploring a personal social-reader experience.
- **[FreshRSS](https://freshrss.org/)** — Recommended — Efficient, extensible self-hosted RSS reader with APIs for external clients.
- **[Miniflux](https://miniflux.app/)** — Recommended — Minimalist, fast self-hosted reader with good feed automation.
- **[Tiny Tiny RSS](https://tt-rss.org/)** — Recommended (caveat) — Mature, extensible self-hosted reader; check the support/update model.
- **[NewsBlur](https://www.newsblur.com/)** — Recommended — Open-source service/software with content training, folders, and social reading.
- **[Feedbin](https://feedbin.com/)** — Recommended (commercial) — Hosted reader with a good interface, search, and newsletter/podcast support.
- **[Inoreader](https://www.inoreader.com/)** — Adjacent (commercial) — Powerful reader with rules and monitoring; keep periodic OPML exports.
- **[Feedly](https://feedly.com/)** — Adjacent (commercial) — Popular, easy reader, though advanced features and automation are increasingly proprietary.
- **[NetNewsWire](https://netnewswire.com/)** — Recommended — Free Apple client, fast and compatible with multiple sync services.
- **[Reeder](https://reederapp.com/)** — Adjacent (commercial) — Refined Apple client for feeds and read-later.
- **[Fluent Reader](https://github.com/yang991178/fluent-reader)** — Recommended — Open-source desktop RSS client with local reading and optional sync.
- **[selfoss](https://selfoss.aditu.de/)** — Adjacent (self-hostable) — Lightweight reader/aggregator that accepts extensible sources.
- **[RSS Guard](https://github.com/martinrotter/rssguard)** — Recommended — Cross-platform, open-source desktop reader compatible with several APIs.

**Additional (research):**

- **[Ekster](https://github.com/pstuifzand/ekster)** — Recommended — Self-hostable Microsub server in Go that aggregates feeds for any Microsub reader client.
- **[FeedLand](https://feedland.com/)** — Reference — Dave Winer's open feed-reading and list-publishing platform; part of the own-your-feeds lineage.

## 14. Syndication, bridges & Fediverse

- **[Bridgy Fed](https://fed.brid.gy/)** — Recommended — Makes an ordinary site participate in the Fediverse via ActivityPub without replacing its canonical URLs.
- **[Granary](https://granary.io/)** — Recommended (technical) — Library and service that convert data between formats and social networks; used by the Bridgy family.
- **[Hatsu](https://github.com/importantimport/hatsu)** — Experimental — Bridge that produces an ActivityPub presence from your site and feed.
- **[ActivityPub for WordPress](https://wordpress.org/plugins/activitypub/)** — Recommended — Federates WordPress authors and posts while keeping your own domain as identity.
- **[Mastodon](https://joinmastodon.org/)** — Adjacent — Syndication and interaction destination; ideally complements, not replaces, your personal site.
- **[Pleroma](https://pleroma.social/)** — Adjacent (self-hostable) — Lightweight, customizable ActivityPub server for federated microblogging.
- **[Akkoma](https://akkoma.social/)** — Adjacent (self-hostable) — Community fork of Pleroma with its own pace and features.
- **[GoToSocial](https://gotosocial.org/)** — Recommended (adjacent) — Lightweight ActivityPub server suited to small or personal instances.
- **[Pixelfed](https://pixelfed.org/)** — Adjacent — Federated photo publishing; can receive copies of a collection whose origin stays on your site.
- **[PeerTube](https://joinpeertube.org/)** — Adjacent — Federated video hosting and distribution under your control.
- **[BookWyrm](https://joinbookwyrm.com/)** — Adjacent — Federated reading network, useful alongside book posts and feeds on your own domain.
- **[Lemmy](https://join-lemmy.org/)** — Adjacent — Federated forums and link aggregation; a possible destination to share articles.
- **[NodeBB](https://nodebb.org/)** — Adjacent — Modern forum with ActivityPub federation work; useful for a community tied to your site.
- **[Fedify](https://fedify.dev/)** — Recommended (development) — TypeScript framework to implement ActivityPub federation with less protocol boilerplate.
- **[ActivityPub Express](https://github.com/immers-space/activitypub-express)** — Adjacent (Node.js) — Library to add ActivityPub endpoints to Express applications.

**Additional (research):**

- **[Misskey](https://misskey-hub.net/)** — Recommended — Feature-rich microblogging server (reactions, MFM) that federates over ActivityPub.
- **[Sharkey](https://joinsharkey.org/)** — Recommended — Actively maintained Misskey fork with quote posts and improved moderation.
- **[Iceshrimp](https://iceshrimp.dev/)** — Recommended — Lean, rewritten Misskey-family server focused on performance and standards compliance.
- **[Firefish](https://joinfirefish.org/)** — Historical — Formerly "Calckey"; a Misskey fork whose development has largely stalled.
- **[snac2](https://codeberg.org/grunfink/snac2)** — Recommended — Tiny C-based single/multi-user ActivityPub server with minimal dependencies.
- **[Honk](https://humungus.tedunangst.com/r/honk)** — Recommended — Minimalist single-user ActivityPub server with no JavaScript; strong "own your server" ethos.
- **[Epicyon](https://libreserver.org/epicyon/)** — Recommended — AGPL, low-resource ActivityPub server designed for small self-hosted communities and old hardware.
- **[Hometown](https://github.com/hometown-fork/hometown)** — Recommended — Mastodon fork adding local-only posting and full-text formatting; run your own small node.
- **[Friendica](https://friendi.ca/)** — Recommended — Decentralized social server federating across ActivityPub, Diaspora, and more; a pioneer of owning your social graph.
- **[Hubzilla](https://hubzilla.org/)** — Recommended — "Nomadic identity" platform with channel cloning and multi-protocol federation; deep portability model.
- **[(streams)](https://codeberg.org/streams/streams)** — Experimental — Nomadic-identity Fediverse server emphasizing account portability and permissions.
- **[Mobilizon](https://joinmobilizon.org/)** — Recommended — Framasoft's federated events and groups platform over ActivityPub; own your event organizing.
- **[Mbin](https://joinmbin.org/)** — Recommended — Community fork of Kbin; a federated link-aggregator/forum speaking ActivityPub.
- **[PieFed](https://join.piefed.social/)** — Recommended — Python/Flask federated link-aggregator with a focus on moderation tooling.
- **[Mitra](https://codeberg.org/silverpill/mitra)** — Experimental — Rust-based federated microblogging server emphasizing content ownership.
- **[Bonfire](https://bonfirenetworks.org/)** — Experimental — Modular, extensible federated social framework (Elixir) for custom ActivityPub communities.
- **[EchoFeed](https://echofeed.app/)** — Recommended — Watches your RSS/Atom feed and cross-posts new items to Mastodon, Bluesky, Micro.blog, Discord, and more; classic feed-driven POSSE.
- **[rss-parrot](https://rss-parrot.net/)** — Recommended — Turns any RSS feed into a followable Mastodon/Fediverse account.
- **[feed2toot](https://gitlab.com/chaica/feed2toot)** — Recommended — Self-hostable Python tool that autoposts RSS/Atom items to a Mastodon account.
- **[feed2fedi](https://codeberg.org/MarvinsMastodonTools/feed2fedi)** — Recommended — Posts RSS/Atom items to Mastodon/Firefish/etc.; self-hosted syndication from your own feed.
- **[feediverse](https://github.com/edsu/feediverse)** — Recommended — Simple Python script to send RSS/Atom feeds to Mastodon; easy to cron for POSSE.
- **[Mastofeed](https://mastofeed.org/)** — Adjacent — Hosted service that pushes your RSS feed to a Mastodon account without self-hosting.
- **[Silo.pub](https://silo.pub/)** — Recommended — Micropub endpoint that publishes to third-party silos; useful as a POSSE target from IndieWeb editors.
- **[moa.party](https://moa.party/)** — Historical — Mastodon↔Twitter/Bluesky cross-poster, largely hobbled by Twitter/X API changes.

## 15. Search, discovery, directories & webrings

- **[Kagi Small Web](https://github.com/kagisearch/smallweb)** — Recommended — Public list feeding blog/small-site discovery experiences.
- **[Wiby](https://wiby.me/)** — Recommended — Search engine oriented toward simple pages and the classic web.
- **[Marginalia Search](https://search.marginalia.nu/)** — Recommended — Independent search favoring non-commercial sites and text content.
- **[Search My Site](https://searchmysite.net/)** — Recommended — Search and directory focused on personal and independent sites.
- **[ooh.directory](https://ooh.directory/)** — Recommended — Editorial directory of blogs organized by subject.
- **[Blogroll.org](https://blogroll.org/)** — Adjacent — Blog-discovery initiative encouraging the return of personal link lists.
- **[BlogDB](https://blogdb.org/)** — Adjacent — Searchable directory of independent blogs and authors.
- **[Personalsit.es](https://personalsit.es/)** — Recommended — Community directory of personal sites with strong small-web affinity.
- **[IndieSeek](https://indieseek.xyz/)** — Adjacent — Search and catalog dedicated to the independent web; check coverage and availability.
- **[1MB Club](https://1mb.club/)** — Recommended — Directory of sites under 1 MB, useful for discovering lightweight projects.
- **[512KB Club](https://512kb.club/)** — Recommended — Collection of lightweight sites ranked by weight and quality.
- **[250KB Club](https://250kb.club/)** — Adjacent — Even stricter list for studying efficient design and publishing.
- **[Neocities Browse](https://neocities.org/browse)** — Recommended — Discovery of personal sites within the Neocities community.
- **[Onionring.js](https://allium.house/garden/onionring/)** — Recommended — Simple JavaScript kit to build a webring with no central platform.
- **[IndieWeb Webring](https://xn--sr8hvo.ws/)** — Recommended — Community webring connecting personal sites with prev/next navigation.

**Additional (research):**

- **[Mojeek](https://www.mojeek.com/)** — Recommended — Independent search engine with its own crawler and index (no Google/Bing/Yandex results).
- **[Teclis](https://teclis.com/)** — Recommended — Non-commercial, ad-free search that down-weights SEO-heavy pages to surface the small web.
- **[Mwmbl](https://mwmbl.org/)** — Recommended — Open-source, non-profit, community-curated search engine you can contribute crawl data to.
- **[Stract](https://stract.com/)** — Experimental — Open-source independent search engine with "optics" for re-ranking toward indie sources.
- **[SearXNG](https://github.com/searxng/searxng)** — Adjacent — Self-hostable, privacy-respecting metasearch engine with no tracking.
- **[TinyGem](https://tinygem.org/)** — Recommended — Human-curated bookmarking and reading-recommendation service for long-form indie content.
- **[Indieblog.page](https://indieblog.page/)** — Core — Sends you to a random post from a vetted pool of personal/indie blogs; the canonical "stumble the IndieWeb" button.
- **[Blog Surf](https://blogsurf.io/)** — Recommended — Searchable directory and search engine focused on independently-owned personal blogs.
- **[BlogScroll](https://blogscroll.com/)** — Recommended — Open, curated directory/aggregator of independent blogs built to route around SEO spam.
- **[The Index (theindex.fyi)](https://theindex.fyi/)** — Recommended — Community-submitted directory of indie-web sites and blogs with an open API.
- **[About Ideas Now](https://aboutideasnow.com/)** — Recommended — Searches the /about, /ideas, and /now pages of thousands of personal sites to find people to talk to.
- **[blogsearch.io](https://blogsearch.io/)** — Recommended — Dedicated search engine indexing personal and independent blogs.
- **[HTMLrev](https://htmlrev.com/)** — Reference — Curated directory of free, lightweight HTML templates for hand-building personal sites.
- **[Fediring](https://fediring.net/)** — Recommended — Webring connecting personal sites of people active in the Fediverse/IndieWeb space.
- **[Hotline Webring](https://hotlinewebring.club/)** — Recommended — Active, popular webring of personal and developer sites with an embeddable widget.
- **[Geekring](https://geekring.net/)** — Recommended — Open webring for personal tech/geek blogs and homepages.
- **[XXIIVV Webring](https://webring.xxiivv.com/)** — Recommended — Long-running webring of artists, developers, and personal sites curated by Devine Lu Linvega.
- **[The Wayward Webring](https://waywardweb.org/)** — Recommended — General-purpose webring for personal and independent websites.
- **[Low Tech Webring](https://emreed.net/LowTech_Directory.html)** — Recommended — Webring/directory for deliberately lightweight, low-tech personal sites.
- **[HTML Hobbyist Webring](https://webring.htmlhobbyist.com/)** — Recommended — Webring for hand-coded, hobbyist HTML personal sites.
- **[Nightfall City](https://nightfall.city/)** — Experimental — Small-web community hub and webring with a retro/indie aesthetic.
- **[Ultimate Webring List](https://tuffgong.nekoweb.org/webring-list.html)** — Reference — Continuously maintained meta-index of active webrings across the small web.

## 16. Comments, forms, newsletter & analytics

- **[Isso](https://isso-comments.de/)** — Recommended — Self-hosted, lightweight comments without depending on a social network.
- **[Remark42](https://remark42.com/)** — Recommended — Self-hosted comment system with moderation, multiple logins, and import.
- **[Schnack](https://schnack.cool/)** — Adjacent — Small Node.js comments designed to avoid tracking and heavy frontend.
- **[Commento++](https://github.com/souramoo/commentoplusplus)** — Adjacent — Community continuation of a lightweight, self-hostable comment system.
- **[Giscus](https://giscus.app/)** — Recommended (dependency) — Uses GitHub Discussions for comments; great for technical audiences but needs an external account.
- **[Cusdis](https://cusdis.com/)** — Adjacent — Minimalist comments with hosted and self-hosted options.
- **[Utterances](https://utteranc.es/)** — Adjacent — Uses GitHub issues as storage; simple but GitHub-dependent.
- **[Staticman](https://staticman.net/)** — Adjacent (technical) — Converts submissions into commits or pull requests, enabling comments on static sites.
- **[Formspree](https://formspree.io/)** — Adjacent (commercial) — Form backend for static sites; check quotas, spam, and export.
- **[Basin](https://usebasin.com/)** — Adjacent (commercial) — Form processing, spam filters, and webhooks without your own backend.
- **[Buttondown](https://buttondown.com/)** — Recommended (commercial) — Writing-focused newsletter with feeds, custom domain, and export; a good extension of a canonical site.
- **[listmonk](https://listmonk.app/)** — Recommended (self-hostable) — High-performance newsletter and mailing lists; needs reliable SMTP and consent management.
- **[Plausible](https://plausible.io/)** — Recommended — Simple, privacy-focused analytics, hosted or self-hosted.
- **[Umami](https://umami.is/)** — Recommended (self-hostable) — Traffic metrics with a clean interface and less invasive collection.
- **[GoatCounter](https://www.goatcounter.com/)** — Recommended — Lightweight, open-source analytics suited to personal sites.

**Additional (research):**

- **[Waline](https://waline.js.org/)** — Recommended — Lightweight, self-hosted (serverless-friendly) comments with Markdown, reactions, and privacy focus.
- **[Twikoo](https://twikoo.js.org/)** — Recommended — Simple, free, self-hostable comment system that runs on serverless backends.
- **[Artalk](https://artalk.js.org/)** — Recommended — Self-hosted Go + JS comment system with dashboard, notifications, and moderation; single binary.
- **[Cactus Comments](https://cactus.chat/)** — Experimental — Comment system built on Matrix, giving federated, self-hostable threads on any static page.
- **[Talkyard](https://www.talkyard.io/)** — Recommended — Open-source, self-hostable embedded comments plus full forum features.
- **[Gitalk](https://github.com/gitalk/gitalk)** — Adjacent — Comment widget backed by GitHub Issues (like Utterances/Giscus); keeps data in your repo.
- **[Web3Forms](https://web3forms.com/)** — Recommended — Access-key form-to-email for static sites; no backend code, privacy-friendly.
- **[Getform](https://getform.io/)** — Recommended — Form endpoint for static/Jamstack sites with file uploads, spam filtering, and integrations.
- **[Formsubmit](https://formsubmit.co/)** — Recommended — Zero-signup form-to-email endpoint for static HTML forms.
- **[Netlify Forms](https://docs.netlify.com/manage/forms/setup/)** — Adjacent — Built-in form handling for Netlify-hosted sites; convenient but host-tied.
- **[Keila](https://www.keila.io/)** — Recommended — Open-source, self-hostable newsletter tool (Elixir) that works with your own SMTP/SES.
- **[Mautic](https://www.mautic.org/)** — Recommended — Mature open-source marketing-automation and newsletter platform you fully self-host.
- **[Mailcoach](https://mailcoach.app/)** — Recommended — Self-hosted (or SaaS) newsletter/automation app (Laravel) using your own sending service.
- **[Mailtrain](https://mailtrain.org/)** — Recommended — Free, self-hosted Node.js newsletter app supporting large lists via your own SMTP/SES.
- **[Postal](https://postalserver.io/)** — Recommended — Open-source, self-hosted mail delivery server; the sending backbone for newsletter infrastructure.
- **[EmailOctopus](https://emailoctopus.com/)** — Commercial — Low-cost hosted newsletter service that can run on Amazon SES; freemium.
- **[Substack](https://substack.com/)** — Commercial — Popular hosted newsletter platform; usable as a POSSE target but flag content/audience lock-in.
- **[Tinylytics](https://tinylytics.app/)** — Recommended — IndieWeb-friendly, privacy-first analytics with built-in webmentions, kudos, and uptime; built for personal sites.
- **[Matomo](https://matomo.org/)** — Recommended — The leading open-source, self-hostable Google Analytics alternative.
- **[Fathom Analytics](https://usefathom.com/)** — Commercial — Simple, GDPR-compliant, cookie-free hosted analytics.
- **[Ackee](https://ackee.electerious.com/)** — Recommended — Self-hosted, cookie-free analytics with a clean GraphQL API.
- **[Shynet](https://github.com/milesmcc/shynet)** — Recommended — Self-hosted, cookie-free, JS-optional analytics (Django).
- **[Offen Fair Web Analytics](https://www.offen.dev/)** — Recommended — Self-hosted, transparent analytics that lets visitors see and delete their own data.
- **[Counter.dev](https://counter.dev/)** — Recommended — Free/open-source, privacy-friendly analytics with no cookies or personal data.
- **[GoatCounter alternatives: Pirsch](https://pirsch.io/)** — Commercial — Cookie-free, open-source-core analytics (Go) with a hosted service.
- **[Simple Analytics](https://www.simpleanalytics.com/)** — Commercial — Privacy-first, no-cookie hosted analytics with a clean one-page dashboard.
- **[Swetrix](https://swetrix.com/)** — Recommended — Open-source, self-hostable, cookieless analytics with a hosted option.
- **[Cabin](https://withcabin.com/)** — Recommended — Carbon-aware, privacy-first analytics with no cookies or personal tracking.

## 17. Photos, audio, video, podcasts, bookmarks & archives

- **[Owncast](https://owncast.online/)** — Recommended — Self-hosted live streaming with chat and federation, keeping your own identity and player.
- **[PhotoPrism](https://www.photoprism.app/)** — Recommended (self-hostable) — Organizes and searches a personal photo library with a web interface.
- **[Immich](https://immich.app/)** — Recommended (separate backup) — Photo/video backup and browsing; should not be your only copy of the originals.
- **[Piwigo](https://piwigo.org/)** — Recommended — Mature, extensible web gallery suited to publishing public albums.
- **[Lychee](https://lycheeorg.github.io/)** — Recommended — Elegant, relatively simple self-hosted gallery.
- **[Thumbsup](https://thumbsup.github.io/)** — Adjacent — Generates static galleries from photos and videos; excellent for portable archives.
- **[Faircamp](https://simonrepp.com/faircamp/)** — Recommended — Generates static sites for musicians to sell and present music without a central platform.
- **[Castopod](https://castopod.org/)** — Recommended — Self-hosted podcast hosting with RSS, analytics, and Fediverse integration.
- **[Funkwhale](https://www.funkwhale.audio/)** — Adjacent — Federated audio library and publishing, suited to collections and channels.
- **[Podlove Publisher](https://docs.podlove.org/podlove-publisher/)** — Recommended (WordPress) — Mature podcast publishing, feeds, and player tools.
- **[Audiobookshelf](https://www.audiobookshelf.org/)** — Adjacent — Personal audiobook and podcast server for private access to your own library.
- **[Linkding](https://linkding.link/)** — Recommended — Simple self-hosted bookmark manager with an API.
- **[Shaarli](https://github.com/shaarli/Shaarli)** — Recommended — Link publishing/organization with tags and feeds; suits a public commonplace book.
- **[Wallabag](https://wallabag.org/)** — Recommended — Self-hosted read-later with import, export, and apps.
- **[ArchiveBox](https://archivebox.io/)** — Recommended — Archives pages, media, and metadata in various formats for a searchable collection.

**Additional (research):**

- **[Photoview](https://photoview.github.io/)** — Recommended — Self-hosted gallery that indexes an existing folder of original photos in place.
- **[LibrePhotos](https://github.com/LibrePhotos/librephotos)** — Recommended — Self-hosted, privacy-focused Google Photos alternative with face/object recognition.
- **[Nextcloud Memories](https://github.com/pulsejet/memories)** — Recommended — Fast timeline photo/video app for Nextcloud, turning a self-hosted cloud into a photo archive.
- **[Ente Photos](https://ente.io/)** — Recommended — End-to-end encrypted, open-source, self-hostable photo backup.
- **[Sigal](https://github.com/saimn/sigal)** — Recommended — Python tool that builds a fast, static HTML photo/video gallery you can host anywhere.
- **[Zenphoto](https://www.zenphoto.org/)** — Adjacent — Long-running self-hosted CMS focused on photo galleries and multimedia.
- **[MediaGoblin (GNU)](https://mediagoblin.org/)** — Recommended — Federated, self-hosted platform for publishing your own photos, video, and audio.
- **[MediaCMS](https://mediacms.io/)** — Recommended — Modern self-hosted video and media platform for running your own video site.
- **[Navidrome](https://www.navidrome.org/)** — Core — Lightweight self-hosted Subsonic-compatible music server to stream your own library.
- **[Ampache](https://ampache.org/)** — Recommended — Long-established web-based personal audio/video streaming server.
- **[Koel](https://koel.dev/)** — Recommended — Clean self-hosted personal audio streaming app (Laravel/Vue).
- **[Feishin](https://github.com/jeffvli/feishin)** — Recommended — Full-featured desktop Subsonic/Navidrome/Jellyfin client for your self-hosted music.
- **[gonic](https://github.com/sentriz/gonic)** — Recommended — Minimal, efficient Subsonic-compatible music server in Go.
- **[AzuraCast](https://www.azuracast.com/)** — Recommended — Self-hosted, all-in-one web radio platform for broadcasting your own audio.
- **[Podcast Generator](https://podcastgenerator.net/)** — Recommended — Self-hosted PHP app to publish and manage your own podcast feed.
- **[Podgrab](https://github.com/akhilrex/podgrab)** — Recommended — Self-hosted podcast download/archive manager for a personal audio library.
- **[Reel2Bits](https://reel2bits.org/)** — Experimental — Self-hosted, ActivityPub-federated SoundCloud-like platform for your own tracks.
- **[Karakeep](https://karakeep.app/)** — Recommended — Self-hosted "bookmark everything" app (links, notes, images) with AI tagging and search; formerly Hoarder.
- **[Readeck](https://readeck.org/)** — Recommended — Self-hosted read-it-later and bookmarking app that saves clean, durable article copies.
- **[LinkAce](https://www.linkace.org/)** — Recommended — Self-hosted bookmark manager that archives links and monitors them for rot.
- **[Linkwarden](https://linkwarden.app/)** — Recommended — Self-hosted collaborative bookmarking that snapshots pages (HTML/PDF/screenshot).
- **[Shiori](https://github.com/go-shiori/shiori)** — Recommended — Simple, portable self-hosted bookmark manager in Go, single binary with offline archive.
- **[Espial](https://github.com/jonschoning/espial)** — Recommended — Open-source, Pinboard-style bookmarking server oriented toward IndieWeb sharing.
- **[Grimoire](https://github.com/goniszewski/grimoire)** — Recommended — Self-hosted bookmark manager with categories, tags, and metadata.
- **[Buku](https://github.com/jarun/buku)** — Recommended — Powerful command-line bookmark manager storing links in a portable SQLite database.
- **[floccus](https://floccus.org/)** — Recommended — Sync browser bookmarks across devices via your own storage (WebDAV/Nextcloud/Git).

## 18. Preservation, backup, import & monitoring

- **[Internet Archive Save Page Now](https://web.archive.org/save/)** — Recommended — Requests a public capture in the Wayback Machine; not a substitute for private backup.
- **[ArchiveTeam Warrior](https://wiki.archiveteam.org/index.php/ArchiveTeam_Warrior)** — Adjacent (community) — Lets you collaborate on preserving threatened services and sites.
- **[HTTrack](https://www.httrack.com/)** — Recommended — Creates browsable mirrors of sites, useful for migration and reference copies.
- **[GNU Wget](https://www.gnu.org/software/wget/)** — Recommended — Recursively downloads pages and files; a basic building block for automation and preservation.
- **[rsync](https://rsync.samba.org/)** — Recommended — Efficiently synchronizes file trees between machines and servers.
- **[Restic](https://restic.net/)** — Recommended — Encrypted, deduplicated, verifiable backups to many destinations.
- **[BorgBackup](https://www.borgbackup.org/)** — Recommended — Deduplicated, encrypted backup, especially good over SSH.
- **[rclone](https://rclone.org/)** — Recommended — Copies and syncs data between local storage and many providers.
- **[Git](https://git-scm.com/)** — Recommended — Distributed history for content, templates, and config; not enough as backup when the remote is a single point.
- **[git-annex](https://git-annex.branchable.com/)** — Adjacent — Manages large files distributed across disks and services without storing them inside Git.
- **[Healthchecks.io](https://healthchecks.io/)** — Recommended — Alerts when backups, builds, or scheduled tasks fail to run.
- **[Uptime Kuma](https://github.com/louislam/uptime-kuma)** — Recommended — Self-hosted monitoring of availability, certificates, and endpoints.
- **[changedetection.io](https://changedetection.io/)** — Recommended — Detects page changes; useful for feedless sources and watching dependencies.
- **[Lychee Link Checker](https://lychee.cli.rs/)** — Recommended — Validates links in Markdown, HTML, and other files during the build.
- **[urlwatch](https://thp.io/2008/urlwatch/)** — Recommended — Monitors URL changes from the command line and sends notifications.

**Additional (research):**

- **[SingleFile](https://github.com/gildas-lormeau/SingleFile)** — Core — Browser extension/CLI that saves a complete page as one self-contained HTML file.
- **[monolith](https://github.com/Y2Z/monolith)** — Recommended — Fast Rust CLI that bundles a page and all assets into a single portable HTML file.
- **[obelisk](https://github.com/go-shiori/obelisk)** — Recommended — Go package/CLI to save a web page as a single HTML file; pairs with Shiori.
- **[Webrecorder / Browsertrix](https://webrecorder.net/)** — Core — Open-source suite for high-fidelity WARC/WACZ capture of complex, dynamic pages.
- **[ReplayWeb.page](https://replayweb.page/)** — Recommended — Fully client-side viewer to browse WARC/WACZ archives with no server.
- **[pywb](https://github.com/webrecorder/pywb)** — Recommended — Python toolkit to replay and serve your own WARC-based archive collections.
- **[grab-site](https://github.com/ArchiveTeam/grab-site)** — Recommended — Archivist's web crawler producing WARC files with a live dashboard and ignore patterns.
- **[Kiwix](https://www.kiwix.org/)** — Recommended — Store and browse entire sites offline as ZIM files; durable and portable.
- **[Perkeep](https://perkeep.org/)** — Experimental — Content-addressed personal storage system (formerly Camlistore) for permanently keeping your data.
- **[Conifer](https://conifer.rhizome.org/)** — Historical — Hosted high-fidelity web archiving (formerly Webrecorder.io); superseded by the self-hostable tools above.
- **[Kopia](https://kopia.io/)** — Core — Fast, cross-platform, end-to-end encrypted backup to your own cloud or local storage.
- **[Syncthing](https://syncthing.net/)** — Core — Continuous, peer-to-peer, encrypted file sync with no central server.
- **[Backrest](https://github.com/garethgeorge/backrest)** — Recommended — Web UI and scheduler for restic backups, making a great CLI easy to run reliably.
- **[Vorta](https://vorta.borgbase.com/)** — Recommended — Desktop GUI for BorgBackup, simplifying encrypted, deduplicated backups.
- **[Duplicati](https://www.duplicati.com/)** — Recommended — Free encrypted backup software with a web UI for many cloud/storage backends.
- **[autorestic](https://github.com/cupcakearmy/autorestic)** — Recommended — Declarative YAML wrapper for restic to automate multi-location backups.
- **[Gatus](https://github.com/TwiN/gatus)** — Core — Lightweight, config-driven health/uptime dashboard and status page you self-host.
- **[Kener](https://kener.ing/)** — Recommended — Modern, self-hosted, batteries-included status page and uptime monitor.
- **[Statping-ng](https://github.com/statping-ng/statping-ng)** — Recommended — Self-hosted status page and service monitoring with notifications.
- **[Cachet](https://cachethq.io/)** — Recommended — Well-known open-source status page system to communicate site/service health.
- **[muffet](https://github.com/raviqqe/muffet)** — Recommended — Fast website link-checker CLI that crawls your live site to catch link rot.
- **[htmltest](https://github.com/wjdp/htmltest)** — Recommended — Tests generated HTML for broken links and bad references; ideal in a static-site CI pipeline.
- **[LinkChecker](https://github.com/linkchecker/linkchecker)** — Recommended — Mature tool to recursively check websites for broken links.

## 19. Design, accessibility, performance & sustainability

- **[MDN Web Docs](https://developer.mozilla.org/)** — Recommended — The primary reference for HTML, CSS, JavaScript, HTTP, accessibility, and web APIs.
- **[Can I Use](https://caniuse.com/)** — Recommended — Web-feature compatibility across browsers and versions.
- **[WAVE](https://wave.webaim.org/)** — Recommended — Visual evaluation of page accessibility problems.
- **[axe-core](https://github.com/dequelabs/axe-core)** — Recommended — Automated accessibility engine embeddable in tests and browsers.
- **[Pa11y](https://pa11y.org/)** — Recommended — Command-line tools and dashboard for recurring accessibility tests.
- **[Lighthouse](https://developer.chrome.com/docs/lighthouse/)** — Recommended — Audit of performance, accessibility, best practices, and technical SEO.
- **[WebPageTest](https://www.webpagetest.org/)** — Recommended — Detailed load testing on real devices, locations, and connections.
- **[PageSpeed Insights](https://pagespeed.web.dev/)** — Recommended — Combines lab data and, when available, real Chrome metrics.
- **[Yellow Lab Tools](https://yellowlab.tools/)** — Adjacent — Detects excess JavaScript, CSS, fonts, DOM, and other weight problems.
- **[Squoosh](https://squoosh.app/)** — Recommended — Local image conversion and compression in the browser.
- **[ImageMagick](https://imagemagick.org/)** — Recommended — Automates image resizing, conversion, and optimization.
- **[Eleventy Image](https://www.11ty.dev/docs/plugins/image/)** — Recommended (Eleventy) — Generates modern formats, sizes, and responsive images during the build.
- **[Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/)** — Recommended — W3C guidelines to reduce environmental impact and improve digital durability.
- **[HTML5 Boilerplate](https://html5boilerplate.com/)** — Adjacent — Tested base for web documents, metadata, and server config.
- **[The A11Y Project](https://www.a11yproject.com/)** — Recommended — Checklist, patterns, and practical resources to make personal sites inclusive.

**Additional (research):**

- **[WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)** — Reference — Canonical color-contrast checker for meeting WCAG requirements.
- **[Sa11y](https://sa11y.netlify.app/)** — Recommended — In-page accessibility QA assistant that flags content issues visually for authors.
- **[Colorable](https://colorable.jxnblk.com/)** — Reference — Interactive tool to test text/background color combinations against contrast ratios.
- **[HTMLHint](https://htmlhint.com/)** — Recommended — Configurable static linter for HTML to keep markup clean and valid.
- **[SVGO](https://github.com/svg/svgo)** — Core — Node tool to optimize/shrink SVG files, reducing page weight.
- **[Sharp](https://sharp.pixelplumbing.com/)** — Core — High-performance Node image-processing library for resizing and compressing images.
- **[oxipng](https://github.com/oxipng/oxipng)** — Recommended — Fast multithreaded lossless PNG optimizer.
- **[pngquant](https://pngquant.org/)** — Recommended — Lossy PNG compressor that greatly reduces size with minimal quality loss.
- **[jpegoptim](https://github.com/tjko/jpegoptim)** — Recommended — Utility to optimize and compress JPEG files for lighter pages.
- **[PurgeCSS](https://purgecss.com/)** — Recommended — Removes unused CSS to shrink stylesheets, improving speed and sustainability.
- **[critical](https://github.com/addyosmani/critical)** — Recommended — Extracts and inlines above-the-fold critical CSS to speed up first render.
- **[Website Carbon Calculator](https://www.websitecarbon.com/)** — Reference — Estimates a page's carbon emissions, supporting the sustainability principle.
- **[Ecograder](https://ecograder.com/)** — Reference — Scores a website's environmental impact and gives efficiency recommendations.
- **[CO2.js](https://developers.thegreenwebfoundation.org/co2js/)** — Reference — Open library to estimate the carbon emissions of digital services.
- **[Green Web Foundation](https://www.thegreenwebfoundation.org/)** — Reference — Checks whether a site runs on green hosting and provides open datasets/tools.
- **[Modern Font Stacks](https://modernfontstacks.com/)** — Core — Curated system-font stacks that render instantly with zero downloads; the fast/sustainable typography choice.
- **[Fontsource](https://fontsource.org/)** — Recommended — Self-host open-source fonts via npm packages, removing third-party font CDNs.
- **[Fontshare](https://www.fontshare.com/)** — Recommended — Free, high-quality typeface library with self-hostable font files.
- **[Inter](https://rsms.me/inter/)** — Reference — Widely used open-source UI typeface (OFL) you can self-host.
- **[IBM Plex](https://github.com/IBM/plex)** — Reference — Comprehensive open-source (OFL) typeface family suitable for self-hosting.
- **[Pico.css](https://picocss.com/)** — Recommended — Minimal, semantic, classless CSS framework for elegant, lightweight sites out of the box.
- **[Water.css](https://watercss.kognise.dev/)** — Recommended — Drop-in classless stylesheet that styles plain HTML with no markup changes.
- **[Simple.css](https://simplecss.org/)** — Recommended — Classless CSS starter that makes semantic HTML look good with almost no page weight.
- **[Sakura](https://oxal.org/projects/sakura/)** — Adjacent — Tiny classless CSS theme for minimalist personal pages.
- **[MVP.css](https://andybrewer.github.io/mvp/)** — Adjacent — Minimalist classless stylesheet for quickly styling HTML-only sites.
- **[Tufte CSS](https://edwardtufte.github.io/tufte-css/)** — Reference — Stylesheet emulating Tufte's book typography with sidenotes; popular for essay-style sites.
- **[98.css / XP.css](https://jdan.github.io/98.css/)** — Experimental — Design systems recreating classic Windows UIs for playful, characterful personal sites.
- **[modern-normalize](https://github.com/sindresorhus/modern-normalize)** — Reference — Small, modern CSS normalization for consistent cross-browser rendering.

## 20. Community, learning & ongoing inspiration

- **[IndieWebCamp](https://indieweb.org/IndieWebCamp)** — Core — Collaborative meetups where participants discuss, design, and implement their own sites.
- **[Homebrew Website Club](https://indieweb.org/Homebrew_Website_Club)** — Core — Informal meetings to work on personal sites and trade practical help.
- **[IndieWeb Chat](https://chat.indieweb.org/)** — Core — Public support channels on dev, WordPress, events, and general use.
- **[IndieWeb Events](https://events.indieweb.org/)** — Recommended — Calendar of online and in-person meetups.
- **[IndieWeb Principles](https://indieweb.org/principles)** — Core — Principles like owning your data, using what you build, documenting, and prioritizing experience.
- **[IndieMark](https://indieweb.org/IndieMark)** — Reference — A levels model to visualize identity, publishing, syndication, and interaction capabilities.
- **[IndieWeb Examples](https://indieweb.org/IndieWeb_Examples)** — Recommended — Real sites to study implementations, post types, and design solutions.
- **[IndieWeb Tutorials](https://indieweb.org/tutorials)** — Recommended (caution) — Index of tutorials and practical guides; confirm dates since technical instructions age.
- **[IndieWeb Carnival](https://indieweb.org/IndieWeb_Carnival)** — Recommended — Monthly round of themed writing distributed across participating blogs.
- **[32-Bit Cafe](https://32bit.cafe/)** — Recommended — Community and resources for building personal sites, learning HTML, and escaping standardized layouts.
- **[Neocities (community)](https://neocities.org/)** — Recommended — Beyond hosting, an active community of hand-made site authors.
- **[Bring Back Blogging](https://bringback.blog/)** — Adjacent — Campaign and directory to encourage frequent publishing on your own blog.
- **[People and Blogs](https://peopleandblogs.com/)** — Recommended — Interviews with personal-blog authors, useful for discovering tools, routines, and motivations.
- **[Web We Want](https://webwewant.fyi/)** — Adjacent — Collection of needs and ideas for a more human, open, interoperable web.
- **[A Website Is a Room](https://a-website-is-a-room.net/)** — Inspiration — Collective exploration of the site as a personal, social, and creative space beyond the platform feed.

**Additional (research):**

- **[Tildeverse](https://tildeverse.org/)** — Recommended — Federation of public-access UNIX "tilde" servers where members build personal pages; a small-web pillar.
- **[HTML Energy](https://html.energy/)** — Recommended — Community/movement celebrating hand-written HTML and personal websites, with events and jams.
- **[MelonLand Forum](https://forum.melonland.net/)** — Recommended — Active forum and wiki for the old/personal-web revival, webrings, and Neocities-style building.
- **[SadGrl.online](https://sadgrl.online/)** — Recommended — Hub of webmastering guides, a layout generator, and resources encouraging indie sites.
- **[Blaugust](https://blaugust.net/)** — Recommended — Annual month-long event encouraging people to (re)start personal blogging, with mentors and a Discord.
- **[Recurring Creative Challenges](https://challenges.stefanbohacek.com/)** — Recommended — Directory of recurring indie-web/creative challenges that drive personal-site activity.
- **[Yesterweb](https://yesterweb.org/)** — Historical — Influential anti-corporate "reclaim the web" community and webzine; wound down in 2023 but a key reference.

## 21. Learning to build for the web

*New category (extended research): beginner-friendly resources for people learning to hand-build and own a website — squarely in the "make your own website" IndieWeb spirit.*

- **[HTML for People](https://htmlforpeople.com/)** — Core — Free, friendly book teaching absolute beginners to build a website by hand, in the make-your-own-website spirit.
- **[Interneting Is Hard](https://internetingishard.netlify.app/)** — Recommended — Polished, beginner-friendly HTML & CSS tutorial series for people starting from zero.
- **[Learn to Code HTML & CSS (Shay Howe)](https://learn.shayhowe.com/)** — Recommended — Classic, clearly written beginner-to-intermediate HTML/CSS guide.
- **[The Odin Project](https://www.theodinproject.com/)** — Recommended — Free, open-source full-stack curriculum; a strong path for building and hosting your own site.
- **[web.dev Learn](https://web.dev/learn/)** — Reference — Structured modern courses on HTML, CSS, and responsive design.
- **[Josh Comeau's Blog](https://www.joshwcomeau.com/)** — Reference — Deep, approachable CSS/JavaScript tutorials for leveling up a hand-built site.

---

## What actually makes up an IndieWeb architecture

A coherent deployment can be understood as eight layers. Not all need to exist on day one.

| Layer | Function | Minimum viable | Possible evolution |
|---|---|---|---|
| Identity | Make the domain the primary identity | domain, HTTPS, `h-card`, `rel=me` links | IndieAuth, WebFinger, verifiable keys |
| Content | Publish at your own URLs | CMS or generator, HTML, permalinks | post types, taxonomies, search, archives |
| Discovery | Make updates subscribable | RSS or Atom | JSON Feed, h-feed, WebSub, directories |
| Interaction | Converse between sites | plain links | Webmention, replies, likes, moderation |
| Authoring | Publish from devices and apps | CMS panel or Git | Micropub and specialized clients |
| Reading | Follow other people | RSS reader with OPML | Microsub server and social client |
| Distribution | Find an audience without losing the origin | manual sharing | POSSE, Bridgy, ActivityPub, newsletter |
| Resilience | Keep the site alive and migratable | export and local copy | 3-2-1 backups, monitoring, archiving |

## Six recommended stacks

**1. Beginner, no server admin** — Own domain + Micro.blog + RSS/JSON Feed + optional Buttondown. The shortest route to publishing under your own domain with mobile clients and community, no infrastructure. Test export, permalink structure, and redirects before migrating important content.

**2. Best balance for most** — WordPress on reliable hosting + a semantically simple theme + IndieWeb + Webmention + Semantic Linkbacks + IndieAuth + Micropub + external backups. A familiar panel with media, search, comments, and export. The risk is plugin/theme sprawl; use few components, auto-update where appropriate, protect accounts with MFA, and keep copies off the host.

**3. Static, fast, versioned** — Eleventy, Hugo, or Astro + Git + Codeberg/GitHub + Cloudflare Pages/Netlify + microformats2 + RSS + Webmention.io + webmention.app + Bridgy Fed + GoatCounter. Excellent for developers. Content stays in files, but receiving interactions, forms, and mobile publishing need external services or endpoints. Store local copies of Webmentions if they are part of your archive.

**4. Compact self-hosting** — GoBlog + Caddy + SQLite + Docker Compose or systemd + Restic + Uptime Kuma. GoBlog concentrates many features in one app and reduces gluing components together. Do a test install, validate import/export, and watch the project's pace before making it a many-year archive.

**5. Git publishing with Micropub** — Indiekit + Eleventy/Astro + Git repo + Quill/Micropublish + Webmention.io or webmentiond. Separates authoring, storage, build, and hosting. Very powerful but with more moving parts; document tokens, key rotation, webhooks, queues, and recovery when a build fails.

**6. Hand-made and minimal** — Hand-written HTML/CSS + h-card/h-entry/h-feed + RSS + static hosting + Webmention.io. No framework or JavaScript required. A light, readable page with stable URLs and a feed already fulfills more IndieWeb principles than a complex platform without portability.

## Priorities by phase

**Phase 1 — ownership and permanence:** register a domain in your own account (with MFA and recovery data); choose simple URLs that survive platform changes; publish a home page, about, contact, and at least one feed; set up HTTPS, export, and off-provider backup.

**Phase 2 — legibility and interoperability:** add an `h-card` for the author; mark posts as `h-entry` and indexes as `h-feed`; validate HTML, microformats, feed, and links; implement Webmention to receive first, then to send.

**Phase 3 — independent publishing and reading:** add IndieAuth and a Micropub endpoint when there's a real benefit; test a client like Quill or Micropublish; use an RSS reader with OPML export; adopt Microsub only if the server/client split is useful.

**Phase 4 — reach:** syndicate via POSSE without swapping the canonical URL for the copy; evaluate Bridgy Fed or ActivityPub for the Fediverse; add a newsletter only with consent, unsubscribe, and export; submit the site to directories, webrings, and small-web engines.

**Phase 5 — longevity:** automate backups and test restoration; monitor availability, certificates, builds, and broken links; keep an inventory of external services and a migration alternative; periodically archive important pages in browsable formats.

## Choices by need

| Need | First choice | Alternative | Note |
|---|---|---|---|
| Start with no code | Micro.blog | Bear Blog or Mataroa | Micro.blog has the broadest IndieWeb integration |
| Full CMS | WordPress + IndieWeb plugins | Known | WordPress has a more predictable ecosystem and maintenance |
| Files + Git | Eleventy | Hugo or Astro | Choose by language and workflow, not micro-benchmarks |
| Publish from phone | Micropub + Quill | compatible native client | Verify create, edit, media, and categories |
| Receive Webmentions on static site | Webmention.io | webmentiond | Export/store copies if interactions matter |
| Send Webmentions | webmention.app | Telegraph | Integrate into the build to avoid manual work |
| Join the Fediverse | Bridgy Fed | WordPress ActivityPub plugin | Preserve your own URLs as canonical |
| Self-hosted reader | FreshRSS | Miniflux | Both export OPML and have good clients |
| Private analytics | GoatCounter | Plausible or Umami | Collect only what you need |
| Local comments | Remark42 | Isso | Webmention can coexist with traditional comments |
| Public photos | Piwigo | Lychee | Immich is better as a personal library than a sole public gallery |
| Podcast | Castopod | Podlove | Keep the domain and feed under your control |
| Public bookmarks | Shaarli | Linkding | Shaarli favors publishing; Linkding favors organization |
| Page archiving | ArchiveBox | HTTrack | Also back up the original files |
| Backup | Restic | BorgBackup | Test restoration, not just the run |

## Pitfalls and limits

**Not all "decentralized" software is IndieWeb.** ActivityPub, IPFS, Nostr, AT Protocol, and P2P networks can be interesting, but don't guarantee your own domain, durable URLs, export, or publishing on the ordinary web. Judge them by concrete outcomes, not the label.

**Self-hosting everything is not required.** You can practice IndieWeb with managed hosting as long as you control your domain, preserve content, and can migrate. Self-hosting without updates, backups, and security can produce less autonomy, not more.

**Static sites move complexity elsewhere.** Static HTML is simple to serve, but comments, Webmentions, forms, search, Micropub, and builds create a chain of services. List every dependency and define how to replace it.

**URLs matter more than the tool.** A CMS migration is manageable when old URLs keep working. Before switching platforms, export data, preserve slugs, create redirects, and check internal links.

**Interactions need moderation.** Webmentions shouldn't be shown without validation. Fetch the source page, confirm it really points to the target, sanitize HTML, limit size, and offer blocking and removal.

**POSSE depends on other people's APIs.** Platforms close APIs and change formats. Syndication should fail without preventing publishing on your own site. The external copy should never be the only one.

**Small projects need evaluation.** Before installing an experimental project, check the last release date, repo activity, update docs, backup procedure, license, and whether real users exist. "Open source" doesn't automatically mean maintained or secure.

## Practical recommendation

For someone who wants to start now and grow calmly: (1) buy and protect a domain; (2) choose **Micro.blog** if you don't want to run tech, **WordPress** if you want a panel and extensions, or **Eleventy/Hugo/Astro** if you prefer files and Git; (3) publish RSS/Atom from day one; (4) implement `h-card`, `h-entry`, and `h-feed`; (5) receive Webmentions via Webmention.io and send them via webmention.app; (6) join the Fediverse via Bridgy Fed only after the base is solid; (7) keep export, automated backup, and restore testing; (8) add a blogroll page, join a webring, and list the site in small-web directories.

A small, understood, recoverable stack beats a huge collection of fragile integrations. Use this list as a parts catalog: add a capability only when it solves a need observed in your own use.

---

## About this compilation

- **Original curated resources:** 300 (categories 1–20), ported to English from the source research.
- **Additional resources (extended research):** 287, grouped under "Additional (research)" blocks and in new category 21.
- **Total:** 587 resources.
- Duplicates against the original 300 and across research passes were removed; items already present (e.g. Neocities, Bear Blog, Mataroa, Shaarli, Castopod, Funkwhale) were not re-added as "new".
- **Currency:** compiled around **July 2026**. Community projects, hosted services, prices, APIs, and compatibility change fast. Confirm releases, docs, export policy, and operational status at the official sources before any important deployment.
- **Next step:** this file is research input for building the final GitHub `awesome-indieweb` list (badges, contribution guide, table of contents, link-checking, and awesome-lint compliance) with Claude Code.
