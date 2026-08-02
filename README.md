# Awesome IndieWeb [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of protocols, platforms, services, libraries, and tools for publishing and owning an independent personal website (on your own domain, with durable URLs, connected to the rest of the web through open standards).

The [IndieWeb](https://indieweb.org/) is not a product, a social network, or an official stack. It is an approach centered on **publishing first in a space you control** (normally your own domain), keeping URLs durable, and connecting that site to the wider web through open standards.

This list spans both resources **native to the IndieWeb** (standards and building blocks) and **adjacent** tools that solve important parts of the problem well. Statuses change fast, confirm recent releases, docs, and export procedures before adopting a critical component.

**Contributions are welcome.** Open a [pull request](https://source.tube/pmurad/awesome-indieweb/pulls) to add, update, or remove an entry, or file an [issue](https://source.tube/pmurad/awesome-indieweb/issues/new/choose) to suggest a resource or report a broken link. Please read the [contribution guidelines](CONTRIBUTING.md) first.

Links are checked automatically on the first of each month. Entries found permanently unreachable are flagged **(link no longer exists)** next to them. Please open a PR to fix or remove any you spot.

## Contents

- [Directories and Awesome Lists](#directories-and-awesome-lists)
- [Protocols and Formats](#protocols-and-formats)
- [IndieWeb Platforms](#indieweb-platforms)
- [Content Management Systems](#content-management-systems)
- [Static Site Generators](#static-site-generators)
- [Git-Based and Visual Editors](#git-based-and-visual-editors)
- [Domains and Hosting](#domains-and-hosting)
- [Servers, TLS and Deployment](#servers-tls-and-deployment)
- [Microformats and Validation](#microformats-and-validation)
- [Webmention and Interactions](#webmention-and-interactions)
- [Identity, Authentication and Security](#identity-authentication-and-security)
- [Micropub and Publishing Clients](#micropub-and-publishing-clients)
- [Feeds, Readers and Microsub](#feeds-readers-and-microsub)
- [Syndication, Bridges and Fediverse](#syndication-bridges-and-fediverse)
- [Search, Discovery and Webrings](#search-discovery-and-webrings)
- [Comments, Forms, Newsletters and Analytics](#comments-forms-newsletters-and-analytics)
- [Media, Bookmarks and Archives](#media-bookmarks-and-archives)
- [Preservation, Backup and Monitoring](#preservation-backup-and-monitoring)
- [Design, Accessibility and Performance](#design-accessibility-and-performance)
- [Community and Inspiration](#community-and-inspiration)
- [Learning Web Development](#learning-web-development)
- [IndieWeb Architecture](#indieweb-architecture)
- [Recommended Stacks](#recommended-stacks)
- [Choices by Need](#choices-by-need)
- [Contributing](#contributing)

## Directories and Awesome Lists

- [IndieWeb Standards](https://spec.indieweb.org/) - Compact portal to the most-used specs: Webmention, Micropub, IndieAuth, Microsub, microformats.
- [IndieWeb Projects](https://indieweb.org/projects) - Official map of platforms, services, libraries, and experiments built or used by the community.
- [Category: Building Blocks](https://indieweb.org/Category%3Abuilding-blocks) - Index of the identity, publishing, reading, interaction, and syndication building blocks.
- [IndieWeb Guide](https://indieweb.guide/) - A progressive, friendlier guide than the wiki for starting a site and adding capabilities.
- [Getting Started](https://indieweb.org/Getting_Started) - Community roadmap for getting a domain, hosting, home page, and your own presence.
- [Getting Started (Portuguese)](https://indieweb.org/Primeiros_passos) - Portuguese-language getting-started guide covering domain, home page, and connecting to the community.
- [IndieWeb Wiki (Portuguese)](https://indieweb.org/Main_Page-pt) - Portuguese-language entry point to IndieWeb concepts and practices for Lusophone readers.
- [IndieWeb Adjacent Communities](https://indieweb.org/communities) - Wiki page mapping communities that overlap with or sit adjacent to the IndieWeb, spanning microformats, the Social Web, and small-web groups.
- [IndieWeb Cities](https://indieweb.org/cities) - Index of cities tied to IndieWeb meetups and organizing, useful for finding local and historical gatherings.
- [IndieNews](https://news.indieweb.org/en) - Community news aggregator of posts submitted via Webmention; a good way to discover active blogs and implementation write-ups.
- [Indie Dev Toolkit](https://github.com/thedaviddias/indie-dev-toolkit) - Broad collection of tools for independent developers (domains, content, metrics, operations).
- [Awesome Selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) - Huge catalog of self-hosted software; excellent source for comments, readers, media, analytics, and archives.
- [Awesome Static Generators](https://github.com/myles/awesome-static-generators) - Comprehensive list of static site generators, themes, editors, and hosts.
- [Jamstack Generators](https://jamstack.org/generators/) - Searchable directory to compare generators by language, framework, and popularity.
- [Awesome RSS](https://github.com/AboutRSS/ALL-about-RSS) - One of the largest collections on RSS: readers, generators, bridges, and discovery tools.
- [Awesome ActivityPub](https://github.com/BasixKOR/awesome-activitypub) - Map of Fediverse servers, libraries, and clients for connecting your own site via ActivityPub.
- [Alternative Internet](https://github.com/redecentralize/alternative-internet) - Decentralization projects, alternative networks, identity, and publishing outside big platforms.
- [Awesome Decentralized Web](https://github.com/gdamdam/awesome-decentralized-web) - Distributed and peer-to-peer tech for exploring frontiers beyond conventional IndieWeb.
- [Awesome CMS](https://github.com/postlight/awesome-cms) - Catalog of traditional, headless, Git-based, and API-driven content management systems.
- [Awesome Personal Websites](https://github.com/logancyang/awesome-personal-websites) - Gallery of personal sites to study structure, content, navigation, and visual identity.
- [awesome-fediverse](https://github.com/emilebosch/awesome-fediverse) - Curated list of Fediverse software and resources, closely tied to the decentralization ethos.
- [awesome-digital-gardens](https://github.com/kyrose/awesome-digital-gardens) - Curated list of digital gardens and tools for building your own.
- [awesome-nostr](https://github.com/aljazceru/awesome-nostr) - Directory of projects and resources on the decentralized Nostr protocol.
- [awesome-atproto](https://github.com/awesome-atproto/awesome-atproto) - Curated list of tools built on the AT Protocol (Bluesky).
- [awesome-search-engines](https://github.com/prirai/awesome-search-engines) - Catalog of independent, privacy, and niche search engines; a jumping-off point for small-web discovery.

## Protocols and Formats

- [Webmention](https://www.w3.org/TR/webmention/) - W3C Recommendation for one site to notify another that it linked to it, enabling replies, likes, mentions, and distributed conversations.
- [Micropub](https://www.w3.org/TR/micropub/) - W3C API to create, edit, and delete posts from clients that are independent of the CMS.
- [IndieAuth](https://indieauth.spec.indieweb.org/) - Identity and authorization protocol based on the user's own URL.
- [microformats2](https://microformats.org/wiki/microformats2) - HTML class conventions that make people, posts, events, and interactions machine-readable without separating data from the page.
- [h-card](https://microformats.org/wiki/h-card) - Format for a person's or organization's name, photo, URL, and details; the site's identity card.
- [h-entry](https://microformats.org/wiki/h-entry) - Format for posts, notes, articles, photos, replies, likes, and other content.
- [h-feed](https://microformats.org/wiki/h-feed) - Container for a sequence of `h-entry` items so an HTML page can also be read as a feed.
- [Microsub](https://indieweb.org/Microsub-spec) - Splits the subscription server from the reading client, mirroring what Micropub does on the publishing side.
- [WebSub](https://www.w3.org/TR/websub/) - Delivers near-real-time feed updates via a publisher-hub-subscriber architecture.
- [JF2](https://www.w3.org/TR/jf2/) - Simplified JSON representation of data derived from microformats2.
- [RSS 2.0](https://www.rssboard.org/rss-specification) - Feed format with near-universal compatibility and low implementation cost.
- [Atom](https://www.rfc-editor.org/rfc/rfc4287) - IETF-standardized feed format, stricter than RSS on identifiers, dates, and extensibility.
- [JSON Feed 1.1](https://www.jsonfeed.org/version/1.1/) - Convenient JSON feed for modern apps and integrations; complements rather than replaces RSS/Atom.
- [OPML 2.0](http://opml.org/spec2.opml) - List format to export and import subscriptions between readers; essential for portability.
- [POSSE](https://indieweb.org/POSSE) - "Publish on your Own Site, Syndicate Elsewhere": your site is the origin, external networks get copies or links.
- [rel-me](https://microformats.org/wiki/rel-me) - `rel="me"` convention linking your profiles bidirectionally to prove a site is yours; basis of RelMeAuth and Mastodon verification.
- [Pingback](https://www.hixie.ch/specs/pingback/pingback) - The XML-RPC linkback predecessor to Webmention; useful for backward compatibility and context.
- [Vouch](https://indieweb.org/Vouch) - Webmention extension where the sender includes a trusted third-party `vouch` URL so receivers can safely accept mentions from strangers.
- [Salmention](https://indieweb.org/Salmention) - Chained Webmention pattern that propagates thread updates (comments, likes, RSVPs) so all participants' copies stay in sync.
- [Post Type Discovery](https://www.w3.org/TR/post-type-discovery/) - W3C Note defining an algorithm to derive a post's type (note, article, reply, like, RSVP) from its microformats2 properties.
- [Private Webmention](https://indieweb.org/Private-Webmention) - Combines Webmention with IndieAuth/AutoAuth so private posts can notify recipients who then authenticate to fetch content.
- [IndieAuth Ticket Auth](https://indieweb.org/IndieAuth_Ticket_Auth) - IndieAuth extension that pushes an access "ticket" to another site's endpoint for private or reciprocal access without interactive login.
- [h-event](https://microformats.org/wiki/h-event) - microformats2 vocabulary for events (name, start/end, location) consumable by calendars and parsers.
- [h-review](https://microformats.org/wiki/h-review) - microformats2 vocabulary for structured reviews (rating, item, author).
- [h-recipe](https://microformats.org/wiki/h-recipe) - microformats2 vocabulary for recipes (ingredients, yield, duration, instructions).
- [h-cite](https://microformats.org/wiki/h-cite) - microformats2 vocabulary for citing external works; backbone of reply-context, bookmarks, and quotations.
- [h-product](https://microformats.org/wiki/h-product) - microformats2 vocabulary for describing products (name, price, brand, identifier).
- [h-resume](https://microformats.org/wiki/h-resume) - microformats2 vocabulary for publishing a machine-readable resume or CV.
- [NodeInfo](https://nodeinfo.diaspora.software/) - Standardized `.well-known` endpoint exposing a server's software, version, and capabilities; used across the Fediverse for discovery.

## IndieWeb Platforms

- [Micro.blog](https://micro.blog/) - Hosted service with custom domain, feeds, clients, community, and many IndieWeb features; the easiest on-ramp with no server admin.
- [Known](https://github.com/idno/idno) - PHP social-publishing platform implementing several IndieWeb standards.
- [microblog.pub](https://github.com/tsileo/microblog.pub) - Single-user Python server with ActivityPub, Micropub, IndieAuth, and Webmention; bridges IndieWeb and Fediverse.
- [Indiekit](https://getindiekit.com/) - Modular Node.js server that receives Micropub and publishes to Git, filesystem, or other content stores.
- [Dwell](https://github.com/zoglesby/dwell) - Personal app built with IndieWeb technologies; a good architecture reference.
- [IndieWeb for WordPress](https://wordpress.org/plugins/indieweb/) - Aggregator plugin and entry point to configure identity, Webmention, Micropub, and compatible themes in WordPress.
- [IndieWeb for Drupal](https://www.drupal.org/project/indieweb) - Module integrating IndieWeb technologies into Drupal.
- [GoBlog](https://github.com/jlelse/GoBlog) - Go blog application with Webmention, Micropub, IndieAuth, feeds, and multiple post types.
- [Koype](https://indieweb.org/Koype) - Personal social hub that aimed to concentrate publishing, identity, and interactions.
- [Sweetroll](https://indieweb.org/sweetroll) - Personal software inspired by blogroll and social reading.
- [Publ](https://github.com/PlaidWeb/Publ) - File-based dynamic CMS with categories and templates, used on varied personal sites.
- [Taproot](https://indieweb.org/Taproot) - PHP personal platform whose open parts influenced IndieWeb implementations.
- [Dobrado](https://indieweb.org/dobrado) - Multi-user PHP/JS CMS built for simple publishing and decentralized social features.
- [Bundle](https://indieweb.org/Bundle) - Python/Django toolset built for a personal site; parts may inspire your own implementations.
- [Falcon](https://indieweb.org/Falcon) - The system running tantek.com; demonstrates a long-lived IndieWeb architecture.
- [Hollo](https://docs.hollo.social/) - Single-user, headless ActivityPub microblog built on Fedify; run a personal Fediverse identity on your own domain.
- [Postmarks](https://github.com/ckolderup/postmarks) - Single-user, self-hosted del.icio.us-style bookmarking site that federates over ActivityPub.
- [Site.js](https://sitejs.org/) - Small-tech tool to develop and host a personal site with automatic TLS and single-command deploy.
- [Smallweb](https://www.smallweb.run/) - CGI-inspired personal cloud where each subdomain maps to a folder of Deno code.
- [twtxt](https://twtxt.readthedocs.io/) - Decentralized, minimalist microblogging built on a single plain-text file served from your own domain.
- [prose.sh](https://pico.sh/prose) - SSH-powered Markdown blog: publish by rsync/scp of `.md` files, no accounts or dashboards.
- [Scribbles](https://scribbles.page/) - Minimal, privacy-respecting blogging platform with custom-domain support and Markdown writing.
- [weblog.lol](https://weblog.lol/) - Plain-text blogging service; posts are Markdown synced via GitHub/email, publishable on your own domain with full export.
- [Pika](https://pika.page/) - Simple blog-and-personal-page builder for makers, with custom domains and a writing focus.
- [Listed](https://listed.to/) - Minimalist blogging platform by Standard Notes; publish notes as a public blog on a custom domain.
- [Val Town](https://www.val.town/) - Social platform for tiny serverless functions and sites; handy for webmention handlers and small IndieWeb glue.

## Content Management Systems

- [WordPress](https://wordpress.org/) - Mature ecosystem, wide export, and the best set of IndieWeb plugins.
- [Ghost](https://ghost.org/) - Excellent for publishing and newsletters on your own domain; Webmention and microformats need a theme or add-ons.
- [WriteFreely](https://writefreely.org/) - Minimalist, federated text platform suited to simple blogs and personal instances.
- [Bear Blog](https://bearblog.dev/) - Minimalist, fast, script-free hosting; custom domain and feeds make a lean personal base.
- [Mataroa](https://mataroa.blog/) - Simple hosted blog with export and few distractions; good for writing-first people.
- [Blot](https://blot.im/) - Turns a folder of files into a website, preserving local content and a very simple publishing flow.
- [Grav](https://getgrav.org/) - Flexible PHP flat-file CMS with no database; suits shared hosting.
- [Kirby](https://getkirby.com/) - High-quality flat-file CMS, excellent for custom sites; requires a license.
- [ProcessWire](https://processwire.com/) - Very flexible PHP CMS/framework; the community has built IndieWeb modules and experiments.
- [Textpattern](https://textpattern.com/) - Lightweight, long-lived editorial CMS for people who prefer template and markup control.
- [Pico](https://picocms.org/) - Extremely small PHP flat-file CMS for a personal page or blog with no heavy panel.
- [Automad](https://automad.org/) - Flat-file CMS with a visual panel and templates, balancing friendly editing and portability.
- [WonderCMS](https://www.wondercms.com/) - Tiny, database-free CMS for simple personal sites.
- [Publii](https://getpublii.com/) - Desktop app that generates and deploys a static site; publish without a terminal.
- [Datenstrom Yellow](https://datenstrom.se/yellow/) - Small flat-file CMS, editable in the browser and easy to move between servers.
- [ClassicPress](https://www.classicpress.net/) - Community-governed WordPress fork without the block editor; lightweight and fully self-hosted.
- [HTMLy](https://www.htmly.com/) - Databaseless PHP blogging platform storing posts as flat files.
- [Typemill](https://typemill.net/) - Markdown-based flat-file CMS for docs, handbooks, and personal sites, with eBook export.
- [Bludit](https://www.bludit.com/) - Simple, fast flat-file (JSON) CMS for blogs and small sites; no database.
- [FlatPress](https://www.flatpress.org/) - Lightweight databaseless blogging engine that runs on minimal PHP hosting.
- [Chyrp Lite](https://chyrplite.net/) - Ultra-light, extensible PHP blogging engine (tumblelog-style) supporting many post kinds.
- [Statamic](https://statamic.com/) - Laravel-based flat-file (or DB) CMS with Git-friendly content; popular for developer-owned sites.
- [Cockpit](https://getcockpit.com/) - API-first headless CMS light enough to self-host for a personal project's structured content.
- [October CMS](https://octobercms.com/) - Laravel-based, file-friendly CMS with version-controllable content.
- [SPIP](https://www.spip.net/) - Long-running French publishing CMS for collaborative editorial sites.
- [Serendipity (s9y)](https://docs.s9y.org/) - Veteran PHP blog engine with native webmention/pingback heritage.
- [GetSimple CMS](http://get-simple.info/) - XML flat-file, no-database CMS for tiny sites; a classic of the databaseless lineage.

## Static Site Generators

- [Eleventy](https://www.11ty.dev/) - Flexible, unopinionated, great for semantic HTML; many Webmention and microformats examples.
- [Hugo](https://gohugo.io/) - Fast, mature single binary suited to large sites; simple deployment with few runtimes.
- [Astro](https://astro.build/) - Combines content, components, and optional JavaScript; great for a modern personal site without a full SPA.
- [Jekyll](https://jekyllrb.com/) - The historical GitHub Pages generator, with a vast set of themes and IndieWeb examples.
- [Zola](https://www.getzola.org/) - Rust generator with a single binary, taxonomies, Sass, and built-in search.
- [Pelican](https://getpelican.com/) - Mature Python generator with feeds, plugins, and importers.
- [Nikola](https://getnikola.com/) - Python generator supporting many input formats, galleries, multilingual, and blog workflows.
- [Hexo](https://hexo.io/) - Popular, fast Node.js generator with a huge theme ecosystem.
- [Gatsby](https://www.gatsbyjs.com/) - React framework for content; powerful, but usually more complex than a personal IndieWeb site needs.
- [Next.js](https://nextjs.org/) - Hybrid React framework for projects needing dynamic routes, APIs, and varied rendering.
- [Nuxt Content](https://content.nuxt.com/) - Markdown-based publishing inside the Vue/Nuxt ecosystem.
- [Bridgetown](https://www.bridgetownrb.com/) - Modern Jekyll-inspired successor, useful for Ruby developers.
- [Hakyll](https://jaspervdj.be/hakyll/) - Haskell library to generate sites with fully programmable pipelines.
- [Lume](https://lume.land/) - Generator for Deno with multi-format support and plugins.
- [soupault](https://soupault.app/) - Site processor that works directly on HTML and enables automation without imposing a framework.
- [VitePress](https://vitepress.dev/) - Vite/Vue-powered generator, fast and minimal; great for personal docs, blogs, and knowledge sites.
- [Docusaurus](https://docusaurus.io/) - React-based generator optimized for docs and knowledge sites, with built-in blog, MDX, and versioning.
- [mdBook](https://rust-lang.github.io/mdBook/) - Rust tool that turns Markdown into a clean online book or site; ideal for handbooks and gardens.
- [Quartz](https://quartz.jzhao.xyz/) - Publishes Obsidian/Markdown vaults as interlinked digital gardens on your own domain.
- [Metalsmith](https://metalsmith.io/) - Extremely pluggable "everything is a plugin" JS generator for fully custom pipelines.
- [Middleman](https://middlemanapp.com/) - Mature Ruby static generator with a full modern front-end toolchain.
- [MkDocs](https://www.mkdocs.org/) - Python Markdown-to-static generator (great with Material) for docs, notes, and knowledge bases.
- [Cecil](https://cecil.app/) - Content-driven PHP static generator (Markdown + Twig) that runs anywhere PHP does.
- [Cobalt](https://cobalt-org.github.io/) - Fast Jekyll-inspired generator in Rust, single binary, good for a low-maintenance blog.
- [Publish](https://github.com/JohnSundell/Publish) - Swift static generator for building sites in Swift with type-safe HTML.
- [Statiq](https://www.statiq.dev/) - Flexible .NET static site and content generator for building personal sites in C#.
- [Marmite](https://rochacbruno.github.io/marmite/) - Zero-config Rust generator that turns a folder of Markdown into a blog with almost no setup.
- [Pollen](https://docs.racket-lang.org/pollen/) - Racket system for book-quality personal sites with programmable markup.
- [Franklin.jl](https://franklinjl.org/) - Julia generator with live-evaluated code and math; popular for technical and research sites.
- [VuePress](https://vuepress.vuejs.org/) - Vue-powered Markdown-centric generator (predecessor to VitePress) for docs-style sites.
- [Gridsome](https://gridsome.org/) - Vue + GraphQL Jamstack generator; historically notable.
- [Neato](https://www.neato.pub/) - Neato is a web page publishing system from [Neatnik](https://neatnik.net/) (the guy behind [omg.lol](https://omg.lol/)). Written in PHP.

## Git-Based and Visual Editors

- [Sveltia CMS](https://github.com/sveltia/sveltia-cms) - Modern panel for Git repositories, compatible with Decap CMS configuration.
- [Decap CMS](https://decapcms.org/) - Open-source CMS to edit static-site content and commit changes to Git.
- [Pages CMS](https://pagescms.org/) - Simple interface to edit content and media directly in GitHub repositories.
- [TinaCMS](https://tina.io/) - Visual editing and structured content for Git-based sites, especially React/Next.js.
- [Keystatic](https://keystatic.com/) - CMS that stores content on the filesystem or GitHub; integrates well with Astro and Next.js.
- [CloudCannon](https://cloudcannon.com/) - Visual editing and editorial workflow for static sites; useful when non-technical authors participate.
- [Static CMS](https://www.staticcms.org/) - Community fork of Netlify/Decap CMS focused on maintenance and extra features.
- [Front Matter CMS](https://frontmatter.codes/) - VS Code extension to manage Markdown, taxonomies, and media locally.
- [Siteleaf](https://www.siteleaf.com/) - Hosted CMS that syncs content with GitHub and builds Jekyll sites.
- [Prose](https://prose.io/) - Content editor for GitHub that popularized the CMS-over-Git model.
- [Outstatic](https://outstatic.com/) - Git-based CMS for Next.js with a built-in panel and Markdown content.
- [Sanity](https://www.sanity.io/) - Structured content platform and APIs; powerful, but creates lock-in without an export strategy.
- [Directus](https://directus.io/) - Data layer and panel over SQL for sites needing structured content and APIs.
- [Strapi](https://strapi.io/) - Extensible Node.js headless CMS for more complex personal apps.
- [Payload](https://payloadcms.com/) - TypeScript CMS embeddable in modern apps, with schema control and authentication.
- [Netlify CMS](https://www.netlifycms.org/) - The original open-source Git-backed editing CMS; superseded by Decap but foundational.
- [Forestry.io](https://forestry.io/) - Early Git-backed content editor; evolved into TinaCMS.
- [Storyblok](https://www.storyblok.com/) - Visual, API-first headless CMS with a generous free tier.
- [Hygraph](https://hygraph.com/) - GraphQL-native headless CMS (formerly GraphCMS) that can back a personal Jamstack site.

## Domains and Hosting

- [Porkbun](https://porkbun.com/) - Competitive-price registrar with WHOIS privacy and direct DNS management.
- [Namecheap](https://www.namecheap.com/) - Popular registrar with broad docs; compare renewal and privacy policy per TLD.
- [Gandi](https://www.gandi.net/) - Veteran registrar with DNS and APIs.
- [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/) - At-cost registration, but the domain is tied to using Cloudflare DNS.
- [GitHub Pages](https://pages.github.com/) - Free static hosting integrated with GitHub; simple for Jekyll and build actions.
- [GitLab Pages](https://docs.gitlab.com/user/project/pages/) - Publishes static sites via GitLab CI/CD pipelines and supports custom domains.
- [Codeberg Pages](https://codeberg.page/) - Community hosting on Forgejo; interesting for reducing dependence on big platforms.
- [Cloudflare Pages](https://pages.cloudflare.com/) - Builds, CDN, and custom domain with a good free tier.
- [Netlify](https://www.netlify.com/) - Easy deploys, previews, and functions; watch quotas and keep the site exportable.
- [Vercel](https://vercel.com/) - Great integration with modern frameworks, especially Next.js.
- [Render Static Sites](https://render.com/docs/static-sites) - Git deploys, TLS, and CDN for static sites.
- [Neocities](https://neocities.org/) - Simple hosting with a maker community and direct HTML/CSS editing.
- [NearlyFreeSpeech.NET](https://www.nearlyfreespeech.net/) - Long-lived, pay-per-use hosting suited to small personal sites.
- [statichost.eu](https://statichost.eu/) - Simple, Git-oriented static hosting with custom domains and European infrastructure.
- [Opalstack](https://opalstack.com/) - Independent hosting for static sites and apps, with shell access and varied runtimes.
- [Njalla](https://njal.la/) - Privacy-first registrar that registers domains as a legal proxy, shielding ownership.
- [Dynadot](https://www.dynadot.com/) - Independent registrar with transparent at-cost pricing, free WHOIS privacy, and a clean API.
- [INWX](https://www.inwx.com/) - German registrar with wide TLD coverage, DNSSEC, and a full-featured API.
- [Hover](https://www.hover.com/) - Domains-and-email-only registrar with free WHOIS privacy.
- [Spaceship](https://www.spaceship.com/) - Namecheap-affiliated registrar with aggressive at-cost pricing and free WHOIS privacy.
- [EasyDNS](https://easydns.com/) - Independent Canadian registrar and managed-DNS provider with a strong civil-liberties record.
- [1984 Hosting](https://1984.hosting/) - Iceland-based, privacy- and free-speech-focused registrar and host.
- [Nekoweb](https://nekoweb.org/) - Free "old web" static host for hand-crafted personal HTML pages, with custom domains.
- [smol.pub](https://smol.pub/) - Ultra-minimal Gemini-and-web blogging platform embodying small-web simplicity.
- [Bunny.net](https://bunny.net/) - Affordable European CDN with Edge Storage and static-site hosting on a custom domain.
- [Fly.io](https://fly.io/) - Runs your Docker/app containers close to users; good for dynamic personal sites with full portability.
- [Deno Deploy](https://deno.com/deploy) - Globally distributed JS/TS edge runtime with custom domains.
- [Surge.sh](https://surge.sh/) - Single-command static publishing from the terminal with custom-domain support.
- [sourcehut Pages](https://srht.site/) - Simple static hosting from the tracking-free sourcehut ecosystem.
- [tilde.town](https://tilde.town/) - Friendly public-access Unix community offering shell accounts and `~user` personal pages.
- [SDF Public Access Unix](https://sdf.org/) - Long-running non-profit public-access Unix co-op with shell accounts and personal web/email hosting.
- [Hetzner](https://www.hetzner.com/) - German provider with very low-cost cloud VPS and dedicated servers; a self-hosting favorite.
- [Mythic Beasts](https://www.mythic-beasts.com/) - UK independent host offering VPS, shell accounts, DNS, and personal web/email hosting.
- [rsync.net](https://rsync.net/) - Minimalist offsite storage accessed over SSH/rsync/SFTP; ideal for portable, provider-agnostic backups.
- [Uberspace](https://uberspace.de/en/) - Hosting on Asteroids since 2010. Host your homepage, store git repositories, compile your own software or run your own web service. You can do it all!
- [Reclaim Hosting](https://reclaimhosting.com/) - Paid host popular in education, bundling a first-year domain and support for traditional CMS and personal-site stacks.
- [FastMail Static Sites](https://www.fastmail.com/) - Feature of the paid FastMail email service that serves static websites from storage linked to the account.
- [Puter](https://puter.com/) - Web platform offering static hosting, a file manager, and workers, with custom domains on paid plans.
- [FC2 Web](https://fc2.com/) - Japanese free hosting service with FTP access, useful for old-web-style personal pages.
- [Web 1.0 Hosting](https://1.hosting/) - Free hosting explicitly inspired by the classic web, aimed at personal sites and web nostalgia.

## Servers, TLS and Deployment

- [Caddy](https://caddyserver.com/) - Server and proxy with automatic HTTPS; an excellent default for a small personal server.
- [nginx](https://nginx.org/) - Widely documented, efficient server and reverse proxy available on nearly every provider.
- [Apache HTTP Server](https://httpd.apache.org/) - Mature option, especially suited to PHP hosting and per-directory configuration.
- [lighttpd](https://www.lighttpd.net/) - Lightweight server for small installs and modest hardware.
- [Traefik](https://traefik.io/traefik/) - Dynamic reverse proxy useful when several services run in containers.
- [HAProxy](https://www.haproxy.org/) - High-performance proxy and load balancer for architectures needing more traffic control.
- [Let's Encrypt](https://letsencrypt.org/) - Free certificate authority that made HTTPS accessible to personal sites.
- [Certbot](https://certbot.eff.org/) - Client to issue and renew Let's Encrypt certificates when the server doesn't automate it.
- [Docker](https://www.docker.com/) - Packages services and dependencies; useful, but doesn't replace backup, updates, and observability.
- [Podman](https://podman.io/) - OCI-compatible containers with good rootless options and systemd integration.
- [Docker Compose](https://docs.docker.com/compose/) - Describes a small self-hosted stack in a versionable, reproducible file.
- [Coolify](https://coolify.io/) - Self-hostable PaaS to deploy apps and databases via a web UI.
- [CapRover](https://caprover.com/) - Deployment panel over Docker to run multiple apps on a VPS.
- [Dokku](https://dokku.com/) - Compact Heroku-inspired PaaS, driven by Git and the command line.
- [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) - Publishes a service without opening ports; adds a proprietary intermediary.
- [OpenLiteSpeed](https://openlitespeed.org/) - High-performance server with HTTP/3 and built-in caching; a lighter alternative to nginx/Apache.
- [H2O](https://h2o.examp1e.net/) - Fast HTTP/1.x, HTTP/2, and HTTP/3 server optimized for low latency.
- [Angie](https://angie.software/) - Actively maintained nginx fork adding HTTP/3 and a management API.
- [acme.sh](https://github.com/acmesh-official/acme.sh) - Pure-shell ACME client with the widest DNS-provider support; dependency-free TLS automation.
- [lego](https://go-acme.github.io/lego/) - Single-binary Go ACME client and library supporting hundreds of DNS providers.
- [dehydrated](https://github.com/dehydrated-io/dehydrated) - Minimal Bash ACME client for Let's Encrypt; auditable and lightweight.
- [step-ca (Smallstep)](https://smallstep.com/docs/step-ca/) - Self-hosted certificate authority and ACME server for full ownership of your PKI.
- [mkcert](https://github.com/FiloSottile/mkcert) - Zero-config locally-trusted TLS certificates for testing your site over HTTPS locally.
- [ZeroSSL](https://zerossl.com/) - Free ACME-compatible certificate authority with API and dashboard.
- [YunoHost](https://yunohost.org/) - Debian-based OS that one-click installs personal-web apps with automatic TLS and email.
- [Cloudron](https://cloudron.io/) - Turnkey platform to install and auto-update self-hosted apps with managed backups, TLS, and users.
- [FreedomBox](https://freedombox.org/) - Debian-based personal server system for hosting your own web, email, and social services.
- [CasaOS](https://casaos.io/) - Simple Docker-based home-server OS with an app-store UI.
- [runtipi](https://runtipi.io/) - Lightweight homeserver platform with a one-click app store built on Docker.
- [Portainer](https://www.portainer.io/) - Web UI for managing Docker/Kubernetes; simplifies the containers behind a self-hosted site.
- [Kamal](https://kamal-deploy.org/) - Deploy tool that ships Docker apps to any bare VPS with zero downtime.
- [HestiaCP](https://hestiacp.com/) - Lightweight open-source control panel for web, DNS, mail, and databases on your own VPS.
- [Dokploy](https://dokploy.com/) - Open-source, self-hostable Vercel/Heroku alternative to deploy apps and databases via a UI.
- [NixOS](https://nixos.org/) - Linux distribution with declarative, reproducible system configuration.
- [Sandstorm](https://sandstorm.io/) - Open-source platform to run self-hosted web apps in secure sandboxes with one-click installs.
- [Ansible](https://www.ansible.com/) - Agentless automation to provision and configure servers reproducibly.
- [Uncloud](https://uncloud.run/) - Multi-node Docker Compose for production. Deploy web apps across cloud servers or your own hardware without cluster-management overhead.

## Microformats and Validation

- [php-mf2](https://github.com/microformats/php-mf2) - microformats2 parser (PHP) used by many IndieWeb tools.
- [mf2py](https://github.com/microformats/mf2py) - Parser to extract microformats2 from HTML (Python).
- [microformats-parser](https://github.com/microformats/microformats-parser) - JavaScript implementation of the parsing algorithm.
- [go-microformats](https://github.com/willnorris/microformats) - microformats2 parser for Go applications and services.
- [mf2util](https://pypi.org/project/mf2util/) - High-level utilities on top of microformats2 data (Python).
- [XRay](https://github.com/aaronpk/XRay) - PHP parser that turns pages with microformats into objects useful for readers, replies, and endpoints.
- [Pin13](https://pin13.net/) - Web interface to test how a page is interpreted by microformats parsers.
- [IndieWebify.Me](https://indiewebify.me/) - Checks identity, `h-card`, posts, and Webmention in didactic steps.
- [Microformats Test Suite](https://github.com/microformats/tests) - Shared cases to test conformance across parsers.
- [extruct](https://github.com/scrapinghub/extruct) - Extracts microformats, JSON-LD, Open Graph, RDFa, and other metadata from pages.
- [Microformats Wiki](https://microformats.org/wiki/) - Documentation of the formats, authoring patterns, and compatibility.
- [Nu Html Checker](https://validator.w3.org/nu/) - Validates modern HTML, avoiding structural errors that also harm parsers.
- [W3C Markup Validation Service](https://validator.w3.org/) - Classic validator for HTML and XHTML documents.
- [W3C Link Checker](https://validator.w3.org/checklink) - Detects broken links and problematic redirects.
- [Schema.org Validator](https://validator.schema.org/) - Inspects structured data beyond microformats and flags markup conflicts.
- [microformats-ruby](https://github.com/microformats/microformats-ruby) - Maintained gem parsing microformats1/2 into Ruby objects, a hash, or JSON.
- [MicroMicro](https://github.com/jgarber623/micromicro) - Ruby gem focused on strict, modern microformats2 extraction.
- [microformats2-elixir](https://github.com/ckruse/microformats2-elixir) - microformats2 parser for the Elixir ecosystem.
- [indieweb-endpoints.cc](https://indieweb-endpoints.cc/) - Tool that discovers a site's IndieAuth, Micropub, Microsub, and Webmention endpoints from a single URL.
- [IndieWeb Toolbox](https://toolbox.imoxia.com/) - Web toolbox for diagnosing endpoints, feeds, and other elements of an IndieWeb stack.

## Webmention and Interactions

- [Webmention.io](https://webmention.io/) - Hosted, open-source endpoint to receive Webmentions without running your own service.
- [Bridgy](https://brid.gy/) - Syndication and backfeed between your site and supported platforms, converting interactions into Webmentions.
- [Telegraph](https://telegraph.p3k.io/) - Finds and sends Webmentions from a page, with an API and send monitoring.
- [webmention.app](https://webmention.app/docs) - Service and build tool that discovers links and sends Webmentions.
- [webmention.rocks](https://webmention.rocks/) - Interoperability test suite for receiving and sending endpoints.
- [mention-client-php](https://github.com/indieweb/mention-client-php) - Library to discover endpoints and send Webmention or Pingback (PHP).
- [webmention-client-ruby](https://github.com/indieweb/webmention-client-ruby) - Client to send and verify Webmentions in Ruby apps.
- [webmentiond](https://github.com/zerok/webmentiond) - Go service to receive and process Webmentions separately from the site.
- [Go-Jamming](https://github.com/lumenpink/go-jamming) - Self-hostable Webmention endpoint in Go, aimed at static sites.
- [Lazymention](https://github.com/strugee/lazymention) - Minimal endpoint to forward received Webmentions to another flow.
- [Pushl](https://github.com/PlaidWeb/Pushl) - Service and library for sending Webmentions.
- [django-webmention](https://github.com/easy-as-python/django-webmention) - Webmention integration for Django applications.
- [WordPress Webmention](https://wordpress.org/plugins/webmention/) - Receives and sends Webmentions in WordPress and integrates reactions into comments.
- [eleventy-cache-webmentions](https://github.com/chrisburnell/eleventy-cache-webmentions) - Helps Eleventy projects fetch and cache Webmentions during the build.
- [webmention.js](https://github.com/PlaidWeb/webmention.js) - Client library to display Webmentions on pages, useful for static sites.
- [willnorris/webmention](https://github.com/willnorris/webmention) - Go library and CLI to discover endpoints and send Webmentions.
- [eleventy-webmentions](https://github.com/maxboeck/eleventy-webmentions) - Eleventy starter demonstrating fetching and rendering Webmention.io data on a static blog.
- [gatsby-plugin-webmention](https://github.com/ChristopherBiscardi/gatsby-plugin-webmention) - Gatsby plugin sourcing Webmention.io data into GraphQL.

## Identity, Authentication and Security

- [IndieAuth.com](https://indieauth.com/) - Server and compatibility tool for IndieAuth authentication.
- [IndieLogin.com](https://indielogin.com/) - Login service based on your domain and `rel=me` relations.
- [IndieAuth.rocks](https://indieauth.rocks/) - Tests IndieAuth clients and servers against interoperability cases.
- [WordPress IndieAuth](https://wordpress.org/plugins/indieauth/) - Turns WordPress into an IndieAuth server and authorizes Micropub clients.
- [indieauth-client-php](https://github.com/indieweb/indieauth-client-php) - Practical reference client to implement IndieAuth login.
- [RelMeAuth](https://microformats.org/wiki/RelMeAuth) - Earlier, still conceptually useful technique to prove identity via reciprocal `rel=me` links.
- [WebFinger](https://www.rfc-editor.org/rfc/rfc7033) - Discovery of information about `user@domain` identities, widely used in the Fediverse.
- [Keyoxide](https://keyoxide.org/) - Decentralized identity proofs linking cryptographic keys to profiles and domains.
- [Libravatar](https://www.libravatar.org/) - Open, federated alternative to Gravatar for hosting avatars.
- [Mozilla Observatory](https://observatory.mozilla.org/) - Assesses HTTP security headers and suggests improvements.
- [Qualys SSL Labs](https://www.ssllabs.com/ssltest/) - Tests TLS configuration, certificate chain, and insecure protocols.
- [Security Headers](https://securityheaders.com/) - Quick check of CSP, HSTS, frame policies, and other headers.
- [security.txt](https://securitytxt.org/) - Standard to publish a responsible contact channel for vulnerabilities.
- [CSP Evaluator](https://csp-evaluator.withgoogle.com/) - Analyzes a Content Security Policy and highlights dangerous permissions.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) - Practical reference for authentication, sessions, uploads, headers, and secure development.
- [WebFinger (WordPress)](https://wordpress.org/plugins/webfinger/) - Implements the WebFinger discovery endpoint on WordPress, aiding Fediverse and IndieAuth discovery.

## Micropub and Publishing Clients

- [Quill](https://quill.p3k.io/) - Versatile web Micropub client for notes, articles, photos, bookmarks, RSVPs, and more.
- [Micropublish](https://github.com/barryf/micropublish) - Micropub client with a full interface and support for advanced properties.
- [Omnibear](https://omnibear.com/) - Browser extension to publish replies, likes, reposts, and bookmarks via Micropub.
- [iA Writer](https://ia.net/writer) - Editor that can publish via Micropub to compatible platforms.
- [Micropub.rocks](https://micropub.rocks/) - Suite to verify Micropub clients and servers.
- [WordPress Micropub](https://wordpress.org/plugins/micropub/) - Micropub endpoint for WordPress, enabling publishing from independent clients.
- [webpage-micropub-to-github](https://github.com/voxpelli/webpage-micropub-to-github) - Endpoint that converts Micropub requests into files or commits on GitHub.
- [micro-panel](https://github.com/valpackett/micro-panel) - Archived Micropub panel still useful as an interface and implementation reference.
- [Sparkles](https://indieweb.org/Sparkles) - Micropub client geared toward publishing photos and media.
- [OwnYourGram](https://ownyourgram.com/) - Demonstrates PESOS by importing photos posted elsewhere into your own site.
- [OwnYourSwarm](https://ownyourswarm.p3k.io/) - Sends Swarm check-ins to your own site via Micropub.
- [Teacup](https://indieweb.org/Teacup) - Micropub client specialized in logging what you're drinking.
- [Compass](https://indieweb.org/Compass) - Location app that can publish data and check-ins to a Micropub endpoint.
- [IndieBookClub](https://indiebookclub.biz/) - Micropub client to log books, reading status, and reviews.
- [IndiePass](https://indieweb.org/IndiePass) - Integrated Micropub/Microsub client; archived, kept as a reference.
- [indielib](https://github.com/hacdias/indielib) - Go IndieWeb toolkit bundling IndieAuth client/server, Micropub, and discovery helpers.
- [benjifs/micropub](https://github.com/benjifs/micropub) - Serverless Micropub and media endpoint that publishes posts to a Git-backed static site.
- [kirby-micropub](https://github.com/sebsel/kirby-micropub) - Micropub server endpoint for the Kirby CMS.
- [selfauth](https://github.com/Inklings-io/selfauth) - Minimal single-user PHP IndieAuth authorization endpoint so you can be your own identity provider.
- [Indigenous for Android](https://indigenous.realize.be/) - Native Android app acting as a Micropub posting client and Microsub reader. **(link no longer exists)**
- [Post Kinds](https://wordpress.org/plugins/indieweb-post-kinds/) - WordPress plugin adding reply/like/bookmark/RSVP post types with proper microformats2 markup and reply-context.
- [Syndication Links](https://wordpress.org/plugins/syndication-links/) - WordPress plugin that displays and manages POSSE syndication URLs for cross-posted content.
- [Semantic Linkbacks](https://wordpress.org/plugins/semantic-linkbacks/) - WordPress plugin enriching incoming Webmentions/pingbacks into semantic comments (likes, reposts, replies).
- [Simple Location](https://wordpress.org/plugins/simple-location/) - WordPress plugin adding location and weather metadata (h-geo/h-adr) to posts.
- [Yarns Microsub Server](https://github.com/jackjamieson2/yarns-microsub-server) - Turns WordPress into a Microsub server so you can host your own social reader feeds.
- [Parse This](https://github.com/dshanske/parse-this) - microformats2/feed/JSONFeed parsing library used by Post Kinds and Yarns for reply-context and feeds.
- [WebSub/PubSubHubbub for WP](https://wordpress.org/plugins/pubsubhubbub/) - Adds WebSub (real-time feed push) publishing to WordPress feeds.
- [Sunlit](https://sunlit.io/) - App for publishing photo posts to Micro.blog, WordPress, or any Micropub-compatible blog.
- [micropub-go](https://gitlab.com/jamietanna/micropub-go/) - Go command-line Micropub client for scriptable publishing and automation.
- [Micropub Clients (wiki)](https://indieweb.org/Micropub/Clients) - Community-maintained inventory of known Micropub clients, apps, and experiments.
- [Micropub Extensions](https://indieweb.org/Micropub-extensions) - Catalog of stable and experimental extensions to the Micropub protocol for more advanced stacks.

## Feeds, Readers and Microsub

- [Aperture](https://github.com/aaronpk/Aperture) - Microsub server keeping subscriptions, channels, and read state separate from the interface.
- [Monocle](https://monocle.p3k.io/) - Web Microsub client built for social reading and replying via Micropub.
- [Together](https://github.com/cleverdevil/Together) - Microsub client exploring a personal social-reader experience.
- [FreshRSS](https://freshrss.org/) - Efficient, extensible self-hosted RSS reader with APIs for external clients.
- [Miniflux](https://miniflux.app/) - Minimalist, fast self-hosted reader with good feed automation.
- [Tiny Tiny RSS](https://tt-rss.org/) - Mature, extensible self-hosted reader.
- [NewsBlur](https://www.newsblur.com/) - Open-source service and software with content training, folders, and social reading.
- [Feedbin](https://feedbin.com/) - Hosted reader with a good interface, search, and newsletter/podcast support.
- [Inoreader](https://www.inoreader.com/) - Powerful reader with rules and monitoring; keep periodic OPML exports.
- [Feedly](https://feedly.com/) - Popular, easy reader, though advanced features are increasingly proprietary.
- [NetNewsWire](https://netnewswire.com/) - Free Apple client, fast and compatible with multiple sync services.
- [Reeder](https://reederapp.com/) - Refined Apple client for feeds and read-later.
- [Fluent Reader](https://github.com/yang991178/fluent-reader) - Open-source desktop RSS client with local reading and optional sync.
- [selfoss](https://selfoss.aditu.de/) - Lightweight reader and aggregator that accepts extensible sources.
- [RSS Guard](https://github.com/martinrotter/rssguard) - Cross-platform, open-source desktop reader compatible with several APIs.
- [Ekster](https://github.com/pstuifzand/ekster) - Self-hostable Microsub server in Go that aggregates feeds for any Microsub reader client.
- [FeedLand](https://feedland.com/) - Open feed-reading and list-publishing platform; part of the own-your-feeds lineage.

## Syndication, Bridges and Fediverse

- [Bridgy Fed](https://fed.brid.gy/) - Makes an ordinary site participate in the Fediverse via ActivityPub without replacing its canonical URLs.
- [Granary](https://granary.io/) - Library and service that convert data between formats and social networks; used by the Bridgy family.
- [Hatsu](https://github.com/importantimport/hatsu) - Bridge that produces an ActivityPub presence from your site and feed.
- [ActivityPub for WordPress](https://wordpress.org/plugins/activitypub/) - Federates WordPress authors and posts while keeping your own domain as identity.
- [Mastodon](https://joinmastodon.org/) - Syndication and interaction destination; ideally complements, not replaces, your personal site.
- [Pleroma](https://pleroma.social/) - Lightweight, customizable ActivityPub server for federated microblogging.
- [Akkoma](https://akkoma.social/) - Community fork of Pleroma with its own pace and features.
- [GoToSocial](https://gotosocial.org/) - Lightweight ActivityPub server suited to small or personal instances.
- [Pixelfed](https://pixelfed.org/) - Federated photo publishing; can receive copies of a collection whose origin stays on your site.
- [PeerTube](https://joinpeertube.org/) - Federated video hosting and distribution under your control.
- [BookWyrm](https://joinbookwyrm.com/) - Federated reading network, useful alongside book posts and feeds on your own domain.
- [Lemmy](https://join-lemmy.org/) - Federated forums and link aggregation; a possible destination to share articles.
- [NodeBB](https://nodebb.org/) - Modern forum with ActivityPub federation work; useful for a community tied to your site.
- [Fedify](https://fedify.dev/) - TypeScript framework to implement ActivityPub federation with less protocol boilerplate.
- [ActivityPub Express](https://github.com/immers-space/activitypub-express) - Library to add ActivityPub endpoints to Express applications.
- [Misskey](https://misskey-hub.net/) - Feature-rich microblogging server (reactions, MFM) that federates over ActivityPub.
- [Sharkey](https://joinsharkey.org/) - Actively maintained Misskey fork with quote posts and improved moderation.
- [Iceshrimp](https://iceshrimp.dev/) - Lean, rewritten Misskey-family server focused on performance and standards compliance.
- [Firefish](https://joinfirefish.org/) - A Misskey fork (formerly Calckey) whose development has largely stalled.
- [snac2](https://codeberg.org/grunfink/snac2) - Tiny C-based single/multi-user ActivityPub server with minimal dependencies.
- [Honk](https://humungus.tedunangst.com/r/honk) - Minimalist single-user ActivityPub server with no JavaScript. **(link no longer exists)**
- [Epicyon](https://libreserver.org/epicyon/) - AGPL, low-resource ActivityPub server designed for small self-hosted communities.
- [Hometown](https://github.com/hometown-fork/hometown) - Mastodon fork adding local-only posting and full-text formatting.
- [Friendica](https://friendi.ca/) - Decentralized social server federating across ActivityPub, Diaspora, and more.
- [Hubzilla](https://hubzilla.org/) - "Nomadic identity" platform with channel cloning and multi-protocol federation.
- [(streams)](https://codeberg.org/streams/streams) - Nomadic-identity Fediverse server emphasizing account portability and permissions.
- [Mobilizon](https://joinmobilizon.org/) - Federated events and groups platform over ActivityPub.
- [Mbin](https://joinmbin.org/) - Community fork of Kbin; a federated link-aggregator/forum speaking ActivityPub.
- [PieFed](https://join.piefed.social/) - Python/Flask federated link-aggregator with a focus on moderation tooling.
- [Mitra](https://codeberg.org/silverpill/mitra) - Rust-based federated microblogging server emphasizing content ownership.
- [Bonfire](https://bonfirenetworks.org/) - Modular, extensible federated social framework (Elixir) for custom ActivityPub communities.
- [EchoFeed](https://echofeed.app/) - Watches your RSS/Atom feed and cross-posts new items to Mastodon, Bluesky, Micro.blog, Discord, and more.
- [rss-parrot](https://rss-parrot.net/) - Turns any RSS feed into a followable Mastodon/Fediverse account.
- [feed2toot](https://gitlab.com/chaica/feed2toot) - Self-hostable Python tool that autoposts RSS/Atom items to a Mastodon account.
- [feed2fedi](https://codeberg.org/MarvinsMastodonTools/feed2fedi) - Posts RSS/Atom items to Mastodon/Firefish/etc.; self-hosted syndication from your own feed.
- [feediverse](https://github.com/edsu/feediverse) - Simple Python script to send RSS/Atom feeds to Mastodon; easy to cron for POSSE.
- [Mastofeed](https://mastofeed.org/) - Hosted service that pushes your RSS feed to a Mastodon account without self-hosting.
- [Silo.pub](https://silo.pub/) - Micropub endpoint that publishes to third-party silos; useful as a POSSE target.
- [moa.party](https://moa.party/) - Mastodon-to-Twitter/Bluesky cross-poster, largely hobbled by API changes.

## Search, Discovery and Webrings

- [Kagi Small Web](https://github.com/kagisearch/smallweb) - Public list feeding blog and small-site discovery experiences.
- [Wiby](https://wiby.me/) - Search engine oriented toward simple pages and the classic web.
- [Marginalia Search](https://search.marginalia.nu/) - Independent search favoring non-commercial sites and text content.
- [Search My Site](https://searchmysite.net/) - Search and directory focused on personal and independent sites.
- [ooh.directory](https://ooh.directory/) - Editorial directory of blogs organized by subject.
- [Blogroll.org](https://blogroll.org/) - Blog-discovery initiative encouraging the return of personal link lists.
- [BlogDB](https://blogdb.org/) - Searchable directory of independent blogs and authors.
- [Personalsit.es](https://personalsit.es/) - Community directory of personal sites with strong small-web affinity.
- [IndieSeek](https://indieseek.xyz/) - Search and catalog dedicated to the independent web.
- [1MB Club](https://1mb.club/) - Directory of sites under 1 MB, useful for discovering lightweight projects.
- [512KB Club](https://512kb.club/) - Collection of lightweight sites ranked by weight and quality.
- [250KB Club](https://250kb.club/) - Even stricter list for studying efficient design and publishing.
- [Neocities Browse](https://neocities.org/browse) - Discovery of personal sites within the Neocities community.
- [Onionring.js](https://allium.house/garden/onionring/) - Simple JavaScript kit to build a webring with no central platform.
- [IndieWeb Webring](https://xn--sr8hvo.ws/) - Community webring connecting personal sites with prev/next navigation.
- [Mojeek](https://www.mojeek.com/) - Independent search engine with its own crawler and index.
- [Teclis](https://teclis.com/) - Non-commercial, ad-free search that down-weights SEO-heavy pages to surface the small web.
- [Mwmbl](https://mwmbl.org/) - Open-source, non-profit, community-curated search engine you can contribute crawl data to.
- [Stract](https://stract.com/) - Open-source independent search engine with "optics" for re-ranking toward indie sources.
- [SearXNG](https://github.com/searxng/searxng) - Self-hostable, privacy-respecting metasearch engine with no tracking.
- [TinyGem](https://tinygem.org/) - Human-curated bookmarking and reading-recommendation service for long-form indie content.
- [Indieblog.page](https://indieblog.page/) - Sends you to a random post from a vetted pool of personal and indie blogs.
- [Blog Surf](https://blogsurf.io/) - Searchable directory and search engine focused on independently-owned personal blogs.
- [BlogScroll](https://blogscroll.com/) - Open, curated directory and aggregator of independent blogs built to route around SEO spam.
- [The Index](https://theindex.fyi/) - Community-submitted directory of indie-web sites and blogs with an open API.
- [About Ideas Now](https://aboutideasnow.com/) - Searches the /about, /ideas, and /now pages of thousands of personal sites to find people to talk to.
- [blogsearch.io](https://blogsearch.io/) - Dedicated search engine indexing personal and independent blogs.
- [HTMLrev](https://htmlrev.com/) - Curated directory of free, lightweight HTML templates for hand-building personal sites.
- [Fediring](https://fediring.net/) - Webring connecting personal sites of people active in the Fediverse/IndieWeb space.
- [Hotline Webring](https://hotlinewebring.club/) - Active, popular webring of personal and developer sites with an embeddable widget.
- [Geekring](https://geekring.net/) - Open webring for personal tech and geek blogs and homepages.
- [XXIIVV Webring](https://webring.xxiivv.com/) - Long-running webring of artists, developers, and personal sites.
- [The Wayward Webring](https://waywardweb.org/) - General-purpose webring for personal and independent websites.
- [Low Tech Webring](https://emreed.net/LowTech_Directory.html) - Webring and directory for deliberately lightweight, low-tech personal sites.
- [HTML Hobbyist Webring](https://webring.htmlhobbyist.com/) - Webring for hand-coded, hobbyist HTML personal sites.
- [Nightfall City](https://nightfall.city/) - Small-web community hub and webring with a retro/indie aesthetic.
- [Ultimate Webring List](https://tuffgong.nekoweb.org/webring-list.html) - Continuously maintained meta-index of active webrings across the small web.
- [Indieweb.xyz](https://indieweb.xyz/) - Webmention-based aggregator organized into topic channels for discovering independent posts by subject.
- [Open Mentions](https://indieweb.org/Open_Mentions) - Webmention aggregation approach that builds per-topic or per-URL pages from received mentions, enabling themed discovery without a central platform.
- [RSS Blogroll Network](https://indieweb.org/Discovery#RSS_Blogroll_Network) - Feed- and blogroll-based network for finding interlinked blogs, acting as a distributed discovery mechanism.
- [Microcast.club](https://microcast.club/) - Webring-style directory for microcasts and independent audio creators.

## Comments, Forms, Newsletters and Analytics

- [Isso](https://isso-comments.de/) - Self-hosted, lightweight comments without depending on a social network.
- [Remark42](https://remark42.com/) - Self-hosted comment system with moderation, multiple logins, and import.
- [Schnack](https://schnack.cool/) - Small Node.js comments designed to avoid tracking and heavy frontend.
- [Commento++](https://github.com/souramoo/commentoplusplus) - Community continuation of a lightweight, self-hostable comment system.
- [Giscus](https://giscus.app/) - Uses GitHub Discussions for comments; great for technical audiences.
- [Cusdis](https://cusdis.com/) - Minimalist comments with hosted and self-hosted options.
- [Utterances](https://utteranc.es/) - Uses GitHub issues as storage; simple but GitHub-dependent.
- [Staticman](https://staticman.net/) - Converts submissions into commits or pull requests, enabling comments on static sites.
- [Formspree](https://formspree.io/) - Form backend for static sites; check quotas, spam, and export.
- [Basin](https://usebasin.com/) - Form processing, spam filters, and webhooks without your own backend.
- [Buttondown](https://buttondown.com/) - Writing-focused newsletter with feeds, custom domain, and export.
- [listmonk](https://listmonk.app/) - High-performance self-hosted newsletter and mailing lists.
- [Plausible](https://plausible.io/) - Simple, privacy-focused analytics, hosted or self-hosted.
- [Umami](https://umami.is/) - Traffic metrics with a clean interface and less invasive collection.
- [GoatCounter](https://www.goatcounter.com/) - Lightweight, open-source analytics suited to personal sites.
- [Waline](https://waline.js.org/) - Lightweight, self-hosted (serverless-friendly) comments with Markdown, reactions, and privacy focus.
- [Twikoo](https://twikoo.js.org/) - Simple, free, self-hostable comment system that runs on serverless backends.
- [Artalk](https://artalk.js.org/) - Self-hosted Go + JS comment system with dashboard, notifications, and moderation.
- [Cactus Comments](https://cactus.chat/) - Comment system built on Matrix, giving federated, self-hostable threads on any static page.
- [Talkyard](https://www.talkyard.io/) - Open-source, self-hostable embedded comments plus full forum features.
- [Gitalk](https://github.com/gitalk/gitalk) - Comment widget backed by GitHub Issues; keeps data in your repo.
- [Web3Forms](https://web3forms.com/) - Access-key form-to-email for static sites; no backend code, privacy-friendly.
- [Getform](https://getform.io/) - Form endpoint for static/Jamstack sites with file uploads, spam filtering, and integrations.
- [Formsubmit](https://formsubmit.co/) - Zero-signup form-to-email endpoint for static HTML forms.
- [Netlify Forms](https://docs.netlify.com/manage/forms/setup/) - Built-in form handling for Netlify-hosted sites.
- [Keila](https://www.keila.io/) - Open-source, self-hostable newsletter tool (Elixir) that works with your own SMTP/SES.
- [Mautic](https://www.mautic.org/) - Mature open-source marketing-automation and newsletter platform you fully self-host.
- [Mailcoach](https://mailcoach.app/) - Self-hosted (or SaaS) newsletter/automation app (Laravel) using your own sending service.
- [Mailtrain](https://mailtrain.org/) - Free, self-hosted Node.js newsletter app supporting large lists via your own SMTP/SES.
- [Postal](https://postalserver.io/) - Open-source, self-hosted mail delivery server; the sending backbone for newsletter infrastructure.
- [EmailOctopus](https://emailoctopus.com/) - Low-cost hosted newsletter service that can run on Amazon SES.
- [Substack](https://substack.com/) - Popular hosted newsletter platform; usable as a POSSE target but note content lock-in.
- [Tinylytics](https://tinylytics.app/) - IndieWeb-friendly, privacy-first analytics with built-in webmentions, kudos, and uptime.
- [Matomo](https://matomo.org/) - The leading open-source, self-hostable Google Analytics alternative.
- [Fathom Analytics](https://usefathom.com/) - Simple, GDPR-compliant, cookie-free hosted analytics.
- [Ackee](https://ackee.electerious.com/) - Self-hosted, cookie-free analytics with a clean GraphQL API.
- [Shynet](https://github.com/milesmcc/shynet) - Self-hosted, cookie-free, JS-optional analytics (Django).
- [Offen Fair Web Analytics](https://www.offen.dev/) - Self-hosted, transparent analytics that lets visitors see and delete their own data.
- [Counter.dev](https://counter.dev/) - Free, open-source, privacy-friendly analytics with no cookies or personal data.
- [Pirsch](https://pirsch.io/) - Cookie-free, open-source-core analytics (Go) with a hosted service.
- [Simple Analytics](https://www.simpleanalytics.com/) - Privacy-first, no-cookie hosted analytics with a clean one-page dashboard.
- [Swetrix](https://swetrix.com/) - Open-source, self-hostable, cookieless analytics with a hosted option.
- [Cabin](https://withcabin.com/) - Carbon-aware, privacy-first analytics with no cookies or personal tracking.

## Media, Bookmarks and Archives

- [Owncast](https://owncast.online/) - Self-hosted live streaming with chat and federation, keeping your own identity and player.
- [PhotoPrism](https://www.photoprism.app/) - Organizes and searches a personal photo library with a web interface.
- [Immich](https://immich.app/) - Photo and video backup and browsing; should not be your only copy of the originals.
- [Piwigo](https://piwigo.org/) - Mature, extensible web gallery suited to publishing public albums.
- [Lychee](https://lycheeorg.github.io/) - Elegant, relatively simple self-hosted gallery.
- [Thumbsup](https://thumbsup.github.io/) - Generates static galleries from photos and videos; excellent for portable archives.
- [Faircamp](https://simonrepp.com/faircamp/) - Generates static sites for musicians to sell and present music without a central platform.
- [Castopod](https://castopod.org/) - Self-hosted podcast hosting with RSS, analytics, and Fediverse integration.
- [Funkwhale](https://www.funkwhale.audio/) - Federated audio library and publishing, suited to collections and channels.
- [Podlove Publisher](https://docs.podlove.org/podlove-publisher/) - Mature podcast publishing, feeds, and player tools for WordPress.
- [Audiobookshelf](https://www.audiobookshelf.org/) - Personal audiobook and podcast server for private access to your own library.
- [Linkding](https://linkding.link/) - Simple self-hosted bookmark manager with an API.
- [Shaarli](https://github.com/shaarli/Shaarli) - Link publishing and organization with tags and feeds; suits a public commonplace book.
- [Wallabag](https://wallabag.org/) - Self-hosted read-later with import, export, and apps.
- [ArchiveBox](https://archivebox.io/) - Archives pages, media, and metadata in various formats for a searchable collection.
- [Photoview](https://photoview.github.io/) - Self-hosted gallery that indexes an existing folder of original photos in place.
- [LibrePhotos](https://github.com/LibrePhotos/librephotos) - Self-hosted, privacy-focused Google Photos alternative with face and object recognition.
- [Nextcloud Memories](https://github.com/pulsejet/memories) - Fast timeline photo/video app for Nextcloud.
- [Ente Photos](https://ente.io/) - End-to-end encrypted, open-source, self-hostable photo backup.
- [Sigal](https://github.com/saimn/sigal) - Python tool that builds a fast, static HTML photo/video gallery you can host anywhere.
- [Zenphoto](https://www.zenphoto.org/) - Long-running self-hosted CMS focused on photo galleries and multimedia.
- [MediaGoblin](https://mediagoblin.org/) - Federated, self-hosted platform for publishing your own photos, video, and audio.
- [MediaCMS](https://mediacms.io/) - Modern self-hosted video and media platform for running your own video site.
- [Navidrome](https://www.navidrome.org/) - Lightweight self-hosted Subsonic-compatible music server to stream your own library.
- [Ampache](https://ampache.org/) - Long-established web-based personal audio/video streaming server.
- [Koel](https://koel.dev/) - Clean self-hosted personal audio streaming app (Laravel/Vue).
- [Feishin](https://github.com/jeffvli/feishin) - Full-featured desktop Subsonic/Navidrome/Jellyfin client for your self-hosted music.
- [gonic](https://github.com/sentriz/gonic) - Minimal, efficient Subsonic-compatible music server in Go.
- [AzuraCast](https://www.azuracast.com/) - Self-hosted, all-in-one web radio platform for broadcasting your own audio.
- [Podcast Generator](https://podcastgenerator.net/) - Self-hosted PHP app to publish and manage your own podcast feed.
- [Podgrab](https://github.com/akhilrex/podgrab) - Self-hosted podcast download and archive manager for a personal audio library.
- [Reel2Bits](https://reel2bits.org/) - Self-hosted, ActivityPub-federated SoundCloud-like platform for your own tracks.
- [Karakeep](https://karakeep.app/) - Self-hosted "bookmark everything" app (links, notes, images) with AI tagging and search.
- [Readeck](https://readeck.org/) - Self-hosted read-it-later and bookmarking app that saves clean, durable article copies.
- [LinkAce](https://www.linkace.org/) - Self-hosted bookmark manager that archives links and monitors them for rot.
- [Linkwarden](https://linkwarden.app/) - Self-hosted collaborative bookmarking that snapshots pages (HTML/PDF/screenshot).
- [Shiori](https://github.com/go-shiori/shiori) - Simple, portable self-hosted bookmark manager in Go, single binary with offline archive.
- [Espial](https://github.com/jonschoning/espial) - Open-source, Pinboard-style bookmarking server oriented toward IndieWeb sharing.
- [Grimoire](https://github.com/goniszewski/grimoire) - Self-hosted bookmark manager with categories, tags, and metadata.
- [Buku](https://github.com/jarun/buku) - Powerful command-line bookmark manager storing links in a portable SQLite database.
- [floccus](https://floccus.org/) - Sync browser bookmarks across devices via your own storage (WebDAV/Nextcloud/Git).

## Preservation, Backup and Monitoring

- [Internet Archive Save Page Now](https://web.archive.org/save/) - Requests a public capture in the Wayback Machine; not a substitute for private backup.
- [ArchiveTeam Warrior](https://wiki.archiveteam.org/index.php/ArchiveTeam_Warrior) - Lets you collaborate on preserving threatened services and sites.
- [HTTrack](https://www.httrack.com/) - Creates browsable mirrors of sites, useful for migration and reference copies.
- [GNU Wget](https://www.gnu.org/software/wget/) - Recursively downloads pages and files; a basic building block for automation and preservation.
- [rsync](https://rsync.samba.org/) - Efficiently synchronizes file trees between machines and servers.
- [Restic](https://restic.net/) - Encrypted, deduplicated, verifiable backups to many destinations.
- [BorgBackup](https://www.borgbackup.org/) - Deduplicated, encrypted backup, especially good over SSH.
- [rclone](https://rclone.org/) - Copies and syncs data between local storage and many providers.
- [Git](https://git-scm.com/) - Distributed history for content, templates, and config.
- [git-annex](https://git-annex.branchable.com/) - Manages large files distributed across disks and services without storing them inside Git.
- [Healthchecks.io](https://healthchecks.io/) - Alerts when backups, builds, or scheduled tasks fail to run.
- [Uptime Kuma](https://github.com/louislam/uptime-kuma) - Self-hosted monitoring of availability, certificates, and endpoints.
- [changedetection.io](https://changedetection.io/) - Detects page changes; useful for feedless sources and watching dependencies.
- [Lychee Link Checker](https://lychee.cli.rs/) - Validates links in Markdown, HTML, and other files during the build.
- [urlwatch](https://thp.io/2008/urlwatch/) - Monitors URL changes from the command line and sends notifications.
- [SingleFile](https://github.com/gildas-lormeau/SingleFile) - Browser extension and CLI that saves a complete page as one self-contained HTML file.
- [monolith](https://github.com/Y2Z/monolith) - Fast Rust CLI that bundles a page and all assets into a single portable HTML file.
- [obelisk](https://github.com/go-shiori/obelisk) - Go package and CLI to save a web page as a single HTML file; pairs with Shiori.
- [Webrecorder / Browsertrix](https://webrecorder.net/) - Open-source suite for high-fidelity WARC/WACZ capture of complex, dynamic pages.
- [ReplayWeb.page](https://replayweb.page/) - Fully client-side viewer to browse WARC/WACZ archives with no server.
- [pywb](https://github.com/webrecorder/pywb) - Python toolkit to replay and serve your own WARC-based archive collections.
- [grab-site](https://github.com/ArchiveTeam/grab-site) - Archivist's web crawler producing WARC files with a live dashboard and ignore patterns.
- [Kiwix](https://www.kiwix.org/) - Store and browse entire sites offline as ZIM files; durable and portable.
- [Perkeep](https://perkeep.org/) - Content-addressed personal storage system (formerly Camlistore) for permanently keeping your data.
- [Conifer](https://conifer.rhizome.org/) - Hosted high-fidelity web archiving (formerly Webrecorder.io).
- [Kopia](https://kopia.io/) - Fast, cross-platform, end-to-end encrypted backup to your own cloud or local storage.
- [Syncthing](https://syncthing.net/) - Continuous, peer-to-peer, encrypted file sync with no central server.
- [Backrest](https://github.com/garethgeorge/backrest) - Web UI and scheduler for restic backups.
- [Vorta](https://vorta.borgbase.com/) - Desktop GUI for BorgBackup, simplifying encrypted, deduplicated backups.
- [Duplicati](https://www.duplicati.com/) - Free encrypted backup software with a web UI for many cloud/storage backends.
- [autorestic](https://github.com/cupcakearmy/autorestic) - Declarative YAML wrapper for restic to automate multi-location backups.
- [Gatus](https://github.com/TwiN/gatus) - Lightweight, config-driven health/uptime dashboard and status page you self-host.
- [Kener](https://kener.ing/) - Modern, self-hosted, batteries-included status page and uptime monitor.
- [Statping-ng](https://github.com/statping-ng/statping-ng) - Self-hosted status page and service monitoring with notifications.
- [Cachet](https://cachethq.io/) - Well-known open-source status page system to communicate site and service health.
- [muffet](https://github.com/raviqqe/muffet) - Fast website link-checker CLI that crawls your live site to catch link rot.
- [htmltest](https://github.com/wjdp/htmltest) - Tests generated HTML for broken links and bad references; ideal in a static-site CI pipeline.
- [LinkChecker](https://github.com/linkchecker/linkchecker) - Mature tool to recursively check websites for broken links.

## Design, Accessibility and Performance

- [MDN Web Docs](https://developer.mozilla.org/) - The primary reference for HTML, CSS, JavaScript, HTTP, accessibility, and web APIs.
- [Can I Use](https://caniuse.com/) - Web-feature compatibility across browsers and versions.
- [WAVE](https://wave.webaim.org/) - Visual evaluation of page accessibility problems.
- [axe-core](https://github.com/dequelabs/axe-core) - Automated accessibility engine embeddable in tests and browsers.
- [Pa11y](https://pa11y.org/) - Command-line tools and dashboard for recurring accessibility tests.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/) - Audit of performance, accessibility, best practices, and technical SEO.
- [WebPageTest](https://www.webpagetest.org/) - Detailed load testing on real devices, locations, and connections.
- [PageSpeed Insights](https://pagespeed.web.dev/) - Combines lab data and, when available, real Chrome metrics.
- [Yellow Lab Tools](https://yellowlab.tools/) - Detects excess JavaScript, CSS, fonts, DOM, and other weight problems.
- [Squoosh](https://squoosh.app/) - Local image conversion and compression in the browser.
- [ImageMagick](https://imagemagick.org/) - Automates image resizing, conversion, and optimization.
- [Eleventy Image](https://www.11ty.dev/docs/plugins/image/) - Generates modern formats, sizes, and responsive images during the build.
- [Web Sustainability Guidelines](https://www.w3.org/TR/web-sustainability-guidelines/) - W3C guidelines to reduce environmental impact and improve digital durability.
- [HTML5 Boilerplate](https://html5boilerplate.com/) - Tested base for web documents, metadata, and server config.
- [The A11Y Project](https://www.a11yproject.com/) - Checklist, patterns, and practical resources to make personal sites inclusive.
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) - Canonical color-contrast checker for meeting WCAG requirements.
- [Sa11y](https://sa11y.netlify.app/) - In-page accessibility QA assistant that flags content issues visually for authors.
- [Colorable](https://colorable.jxnblk.com/) - Interactive tool to test text/background color combinations against contrast ratios.
- [HTMLHint](https://htmlhint.com/) - Configurable static linter for HTML to keep markup clean and valid.
- [SVGO](https://github.com/svg/svgo) - Node tool to optimize and shrink SVG files, reducing page weight. **(link no longer exists)**
- [Sharp](https://sharp.pixelplumbing.com/) - High-performance Node image-processing library for resizing and compressing images.
- [oxipng](https://github.com/oxipng/oxipng) - Fast multithreaded lossless PNG optimizer.
- [pngquant](https://pngquant.org/) - Lossy PNG compressor that greatly reduces size with minimal quality loss.
- [jpegoptim](https://github.com/tjko/jpegoptim) - Utility to optimize and compress JPEG files for lighter pages.
- [PurgeCSS](https://purgecss.com/) - Removes unused CSS to shrink stylesheets, improving speed and sustainability.
- [critical](https://github.com/addyosmani/critical) - Extracts and inlines above-the-fold critical CSS to speed up first render.
- [Website Carbon Calculator](https://www.websitecarbon.com/) - Estimates a page's carbon emissions, supporting the sustainability principle.
- [Ecograder](https://ecograder.com/) - Scores a website's environmental impact and gives efficiency recommendations.
- [CO2.js](https://developers.thegreenwebfoundation.org/co2js/) - Open library to estimate the carbon emissions of digital services.
- [Green Web Foundation](https://www.thegreenwebfoundation.org/) - Checks whether a site runs on green hosting and provides open datasets and tools.
- [Modern Font Stacks](https://modernfontstacks.com/) - Curated system-font stacks that render instantly with zero downloads.
- [Fontsource](https://fontsource.org/) - Self-host open-source fonts via npm packages, removing third-party font CDNs.
- [Fontshare](https://www.fontshare.com/) - Free, high-quality typeface library with self-hostable font files.
- [Inter](https://rsms.me/inter/) - Widely used open-source UI typeface (OFL) you can self-host.
- [IBM Plex](https://github.com/IBM/plex) - Comprehensive open-source (OFL) typeface family suitable for self-hosting.
- [Pico.css](https://picocss.com/) - Minimal, semantic, classless CSS framework for elegant, lightweight sites out of the box.
- [Water.css](https://watercss.kognise.dev/) - Drop-in classless stylesheet that styles plain HTML with no markup changes.
- [Simple.css](https://simplecss.org/) - Classless CSS starter that makes semantic HTML look good with almost no page weight.
- [Sakura](https://oxal.org/projects/sakura/) - Tiny classless CSS theme for minimalist personal pages.
- [MVP.css](https://andybrewer.github.io/mvp/) - Minimalist classless stylesheet for quickly styling HTML-only sites.
- [Tufte CSS](https://edwardtufte.github.io/tufte-css/) - Stylesheet emulating Tufte's book typography with sidenotes; popular for essay-style sites.
- [98.css / XP.css](https://jdan.github.io/98.css/) - Design systems recreating classic Windows UIs for playful, characterful personal sites.
- [modern-normalize](https://github.com/sindresorhus/modern-normalize) - Small, modern CSS normalization for consistent cross-browser rendering.

## Community and Inspiration

- [IndieWebCamp](https://indieweb.org/IndieWebCamp) - Collaborative meetups where participants discuss, design, and implement their own sites.
- [Homebrew Website Club](https://indieweb.org/Homebrew_Website_Club) - Informal meetings to work on personal sites and trade practical help.
- [IndieWeb Chat](https://chat.indieweb.org/) - Public support channels on dev, WordPress, events, and general use.
- [IndieWeb Chat (Discord)](https://discord.gg/UEp9p3yNYj) - Official IndieWeb Discord server, mirrored with the IRC and web channels, for those who prefer Discord.
- [IndieWeb Community](https://indieweb.org/community) - Overview of the community, its principles, and ways to take part, centered on personal sites and using what you build.
- [IndieWeb Events](https://events.indieweb.org/) - Calendar of online and in-person meetups.
- [IndieWeb Principles](https://indieweb.org/principles) - Principles like owning your data, using what you build, documenting, and prioritizing experience.
- [IndieMark](https://indieweb.org/IndieMark) - A levels model to visualize identity, publishing, syndication, and interaction capabilities.
- [IndieWeb Examples](https://indieweb.org/IndieWeb_Examples) - Real sites to study implementations, post types, and design solutions.
- [IndieWeb Tutorials](https://indieweb.org/tutorials) - Index of tutorials and practical guides; confirm dates since technical instructions age.
- [IndieWeb Carnival](https://indieweb.org/IndieWeb_Carnival) - Monthly round of themed writing distributed across participating blogs.
- [32-Bit Cafe](https://32bit.cafe/) - Community and resources for building personal sites, learning HTML, and escaping standardized layouts.
- [Bring Back Blogging](https://bringback.blog/) - Campaign and directory to encourage frequent publishing on your own blog.
- [People and Blogs](https://peopleandblogs.com/) - Interviews with personal-blog authors, useful for discovering tools, routines, and motivations.
- [Web We Want](https://webwewant.fyi/) - Collection of needs and ideas for a more human, open, interoperable web.
- [A Website Is a Room](https://a-website-is-a-room.net/) - Collective exploration of the site as a personal, social, and creative space beyond the platform feed.
- [Tildeverse](https://tildeverse.org/) - Federation of public-access UNIX "tilde" servers where members build personal pages.
- [runv.club](https://runv.club/) - Brazilian tilde-style community with free shell accounts, personal web hosting, and IRC, run by the nonprofit Portal IDEA and aimed at learning and small-web publishing. ⭐ *Curator's pick*
- [noctem.cafe](https://noctem.cafe/) - Small Brazilian OpenBSD pubnix offering shell accounts and personal pages, plus Gopher, Gemini, and I2P space for small experiments.
- [The Black Cat](https://theblack.cat/) - Small, invite-only community hosting tiny handmade personal websites, with a browser-based editor and no JavaScript, trackers, or algorithms. ⭐ *Curator's pick*
- [HTML Energy](https://html.energy/) - Community and movement celebrating hand-written HTML and personal websites, with events and jams.
- [MelonLand Forum](https://forum.melonland.net/) - Active forum and wiki for the old/personal-web revival, webrings, and Neocities-style building.
- [SadGrl.online](https://sadgrl.online/) - Hub of webmastering guides, a layout generator, and resources encouraging indie sites.
- [Blaugust](https://blaugust.net/) - Annual month-long event encouraging people to (re)start personal blogging, with mentors and a Discord. **(link no longer exists)**
- [Recurring Creative Challenges](https://challenges.stefanbohacek.com/) - Directory of recurring indie-web and creative challenges that drive personal-site activity.
- [Yesterweb](https://yesterweb.org/) - Influential anti-corporate "reclaim the web" community and webzine.
- [omg.lol](https://omg.lol/) - Community of personal websites built around your own domain, with profile pages carrying h-card and rel=me, a weblog, statuslog and now pages, and the social.lol Mastodon instance. ⭐ *Curator's pick*

## Learning Web Development

- [HTML for People](https://htmlforpeople.com/) - Free, friendly book teaching absolute beginners to build a website by hand.
- [Interneting Is Hard](https://internetingishard.netlify.app/) - Polished, beginner-friendly HTML & CSS tutorial series for people starting from zero.
- [Learn to Code HTML & CSS](https://learn.shayhowe.com/) - Classic, clearly written beginner-to-intermediate HTML/CSS guide by Shay Howe.
- [The Odin Project](https://www.theodinproject.com/) - Free, open-source full-stack curriculum; a strong path for building and hosting your own site.
- [web.dev Learn](https://web.dev/learn/) - Structured modern courses on HTML, CSS, and responsive design.
- [Josh Comeau's Blog](https://www.joshwcomeau.com/) - Deep, approachable CSS/JavaScript tutorials for leveling up a hand-built site.
- [Deploying Your Own IndieWeb Site with Indiekit + Eleventy](https://fulldecent.github.io/dev-indieweb/indieweb/indiekit/eleventy/docker/2026/02/14/deploying-your-own-indieweb-site-with-indiekit-and-eleventy-docker-compose-based.html) - 2026 walkthrough of a Docker-based Indiekit + Eleventy stack, including compatible Micropub clients.

## IndieWeb Architecture

A coherent deployment can be understood as eight layers. Not all need to exist on day one.

| Layer | Function | Minimum viable | Possible evolution |
|---|---|---|---|
| Identity | Make the domain the primary identity | Domain, HTTPS, `h-card`, `rel=me` links | IndieAuth, WebFinger, verifiable keys |
| Content | Publish at your own URLs | CMS or generator, HTML, permalinks | Post types, taxonomies, search, archives |
| Discovery | Make updates subscribable | RSS or Atom | JSON Feed, h-feed, WebSub, directories |
| Interaction | Converse between sites | Plain links | Webmention, replies, likes, moderation |
| Authoring | Publish from devices and apps | CMS panel or Git | Micropub and specialized clients |
| Reading | Follow other people | RSS reader with OPML | Microsub server and social client |
| Distribution | Find an audience without losing the origin | Manual sharing | POSSE, Bridgy, ActivityPub, newsletter |
| Resilience | Keep the site alive and migratable | Export and local copy | 3-2-1 backups, monitoring, archiving |

## Recommended Stacks

- **Beginner, no server admin:** Own domain + Micro.blog + RSS/JSON Feed + optional Buttondown.
- **Best balance for most:** WordPress on reliable hosting + a semantic theme + IndieWeb + Webmention + Semantic Linkbacks + IndieAuth + Micropub + external backups.
- **Static, fast, versioned:** Eleventy/Hugo/Astro + Git + Codeberg/GitHub + Cloudflare Pages/Netlify + microformats2 + RSS + Webmention.io + webmention.app + Bridgy Fed + GoatCounter.
- **Compact self-hosting:** GoBlog + Caddy + SQLite + Docker Compose or systemd + Restic + Uptime Kuma.
- **Git publishing with Micropub:** Indiekit + Eleventy/Astro + Git repo + Quill/Micropublish + Webmention.io or webmentiond.
- **Hand-made and minimal:** Hand-written HTML/CSS + h-card/h-entry/h-feed + RSS + static hosting + Webmention.io.

## Choices by Need

| Need | First choice | Alternative | Note |
|---|---|---|---|
| Start with no code | Micro.blog | Bear Blog or Mataroa | Micro.blog has the broadest IndieWeb integration |
| Full CMS | WordPress + IndieWeb plugins | Known | WordPress has a more predictable ecosystem |
| Files + Git | Eleventy | Hugo or Astro | Choose by language and workflow |
| Publish from phone | Micropub + Quill | Compatible native client | Verify create, edit, media, and categories |
| Receive Webmentions on static site | Webmention.io | webmentiond | Store copies if interactions matter |
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

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work.
