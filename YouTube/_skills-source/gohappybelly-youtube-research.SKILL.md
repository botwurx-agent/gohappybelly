---
name: gohappybelly-youtube-research
description: Research and reverse-engineer what drives YouTube growth in the gut-health/functional-medicine niche for Go Happy Belly. Use when Steve wants to study a channel, find viral topics, discover new channels to learn from, research a YouTube strategist's method, or update the reference playbook. Trigger phrases: "tear down this channel", "research YouTube", "find viral topics", "find channels to study", "study Ben Azadi", "update the playbook", "what's working on YouTube". Anchor is Ben Azadi (Keto Kamp) but never limited to him. Research public content only; never contact anyone; never commit personal contact details.
---

# GoHappyBelly YouTube Research

You are researching YouTube for Alina Nazari, FDN-P, of Go Happy Belly. Steve operates the business and directs this research. Alina does not use this skill.

## Purpose

This skill reverse-engineers proven YouTube growth instead of guessing at it. It studies channels that are already winning in gut health, functional medicine, hormones/perimenopause, and functional nutrition, plus the documented methods behind that growth, and turns what it finds into concrete, reusable production rules. Everything this skill produces feeds `YouTube/00_Strategy/Reference_Playbook.md`, which is the file the `gohappybelly-youtube` production skill (Task 4) reads before writing a single script or thumbnail brief. Research that never becomes a rule in that playbook did not do its job.

This skill has four functions: Channel Teardown, Discover, Strategist/Method Research, and Synthesize. Run the one Steve is asking for; do not run all four unprompted.

## Function A: Channel Teardown

**Input:** a channel URL or handle.

**Steps:**

1. Try Claude-in-Chrome first. Navigate to `<channel>/videos`, sort by **Popular**, and read the real view counts, titles, and approximate upload dates for the top 10-15 videos. This is the highest-fidelity data source because it reflects actual YouTube analytics, not search-engine estimates.
2. If Chrome or YouTube permission is unavailable, fall back to Firecrawl (scrape the channel's videos page) and then WebSearch to fill any gaps. When this fallback is used, log it explicitly: set the teardown's "Data source" field to "Firecrawl/WebSearch (reduced depth)" instead of "Chrome Popular sort", so anyone reading the teardown later knows the numbers are less precise.
3. Establish the channel's recent average views (a baseline from roughly the last 10-20 uploads, excluding obvious outliers). For each of the top 10-15 videos, compute the outlier ratio: video views divided by that channel recent average.
4. Fill out `YouTube/_Templates/channel-teardown-template.md` completely, no placeholders left in the copy you save. Cover cadence and format, the outlier videos table (with the outlier ratio column populated), title formulas with real examples, thumbnail style, hook patterns from the first 15-30 seconds of the top videos, playlist/series architecture, topic categories that overperform, and gut-health adaptation notes written in pattern language, never diagnostic.
5. Save the completed teardown to `YouTube/01_Research/teardowns/<slug>.md`, where `<slug>` is the channel name in lowercase with hyphens (for example, `keto-kamp.md`).
6. Append one row to `YouTube/01_Research/Reference_Channels.md` for this channel: Channel/Source, URL, Niche, Subscribers, Why It Matters, and Status set to `studied`. If the channel already has a `candidate` row from a prior Discover pass, update that row instead of duplicating it.

## Function B: Discover

**Input:** a niche or seed term. Default niches to search: gut health, functional medicine, perimenopause/hormones, functional nutrition. Steve may also name a specific niche.

**Steps:**

1. Use WebSearch and Firecrawl (search and map) to find channels that are growing quickly or consistently producing outlier videos in the given niche.
2. For each candidate, capture: channel name, URL, niche, an approximate subscriber count, and one clear line on why it matters (what they are doing well that Go Happy Belly could learn from).
3. Add each candidate to `YouTube/01_Research/Reference_Channels.md` with Status set to `candidate`. Do not run a full teardown on a candidate unless Steve asks for one; Discover surfaces channels, Function A studies them.
4. This function runs on demand only, when Steve asks. There is no scheduled or automatic discovery run yet.

## Function C: Strategist / Method Research

Channel teardowns show what worked. This function studies the documented *methods* behind growth, the packaging principles a strategist teaches, because those principles transfer across niches even when the channel content does not.

**Priority subject:** Jeremy Stickney, Ben Azadi's strategist and growth partner (also connected to Evan Carmichael's team), credited with growing channels past 2M subscribers. Study his method and the broader Evan Carmichael system alongside any channel-specific work.

Because a strategist's method usually lives in interviews, podcast appearances, and talks rather than a clean written article, use this process:

1. Use WebSearch to find public interviews, podcast episodes, and talks featuring the strategist.
2. Use WebFetch and Firecrawl to pull the page content or published transcript for each source found.
3. Summarize the recurring principles in your own words, not a verbatim transcript dump: what they teach about titles, thumbnails, hooks, retention, cadence, and audience research.
4. Save the summary to `YouTube/01_Research/teardowns/<name>-method.md` (for example, `jeremy-stickney-method.md`).

**Guardrail block for this function:**
- Research public content only.
- Do NOT contact anyone. No DMs, no emails, no comments, no outreach to the strategist, their team, or their business, under any circumstance.
- Do NOT write anyone's private email address or phone number into any file this skill produces, even if it surfaces in a publicly available bio, credits page, or contact form. If contact information appears during research, leave it out entirely; do not paraphrase or summarize it either.

## Function D: Synthesize

Roll every completed file in `YouTube/01_Research/teardowns/` (both channel teardowns and strategist method files) into `YouTube/00_Strategy/Reference_Playbook.md`.

The output must be concrete, reusable rules the production skill can act on directly, not a recap of what was read. Cover, at minimum:

- **Title formulas:** patterns that repeat across sources, each with a real example from research and one adapted gut-health example.
- **Thumbnail rules:** color/contrast conventions, face and expression usage, text overlay pattern (word count, placement), recurring visual devices.
- **Cadence:** upload frequency and the long-form-to-Shorts mix that shows up across studied channels.
- **Hook patterns:** first 15-30 second structures that repeat across the outlier videos studied.
- **Overperforming topic categories:** adapted to gut health, always in pattern/archetype language, never diagnostic.

Overwrite the "Not yet synthesized" stub content with the populated sections above. Keep the file's header and status note format intact, but update the Status line to reflect the date last synthesized and how many teardown/method files it draws from. `Reference_Playbook.md` is the single source of truth Task 4's skill reads; never hand-edit its output sections directly outside of this function, and re-run this function whenever a new teardown or method file is added.

## The Outlier Framework

A five-point method that underlies all four functions above:

1. **Find outliers.** Identify videos whose views sit meaningfully above the channel's normal baseline, using the outlier ratio (views ÷ recent average). A ratio of 3x or higher is worth studying closely.
2. **Reverse-engineer packaging.** Break down exactly what made the outlier work: the title formula, the thumbnail composition, the hook structure, the topic choice. Packaging, not luck, explains most outliers.
3. **Adapt, don't copy.** Translate the packaging pattern into Go Happy Belly's world (the right avatar, the right gut archetype, the right offer) instead of imitating the original video's content. Keep the structure, change what fills it.
4. **Score before shooting.** Before a topic, title, and thumbnail combination goes into production, run it through Higgsfield's `virality_predictor` to sanity-check hook strength and predicted engagement before a script or thumbnail gets built.
5. **Double down.** When an adapted pattern performs, look for the next two or three videos in the same formula or topic family before moving to a new idea. Outliers tend to repeat when the underlying packaging is sound.

## Tools Reference

- **Claude-in-Chrome:** primary tool for Function A teardown depth. Requires YouTube permission granted in the extension. Navigate to `<channel>/videos`, sort by Popular, read real view counts. Falls back to Firecrawl/WebSearch when permission is unavailable.
- **Firecrawl:** scrape/search fallback for teardowns (Function A); primary discovery tool for finding candidate channels (Function B); content retrieval for strategist interviews and articles (Function C).
- **WebSearch / WebFetch:** finding candidate channels (Function B); finding and reading strategist interviews, podcasts, and talks (Function C).
- **Higgsfield `virality_predictor`:** the "score before shooting" step of the Outlier Framework (step 4). Use it before any script or thumbnail gets built from a researched pattern.

## Guardrails

- Research public content only. Never contact anyone: no DMs, no emails, no comments, no outreach of any kind to channel owners, strategists, or their teams.
- Never write anyone's private contact details (email address, phone number) into any file this skill produces, even if found in a public bio, credits page, or contact form.
- No diagnostic language, ever, even when adapting a pattern to gut health. Use "this pattern suggests," "this often shows up when," or "the [Archetype] pattern," never a named condition.
- No em dashes anywhere. Use commas, parentheses, or rewrite the sentence.
- No banned words: transform, journey, empower, authentic, passionate, innovative, creative (in the marketing sense), unique, elevate, synergy.
- GI-MAP and other clinical tests stay framed as an optional clinical recommendation decided after consultation; never use them as a hook or CTA driver in research notes. That framing belongs to the funnel and offer skills, not this one.
