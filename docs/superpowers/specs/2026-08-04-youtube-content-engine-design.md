# Go Happy Belly — YouTube Content Engine (Design Spec)

**Date:** 2026-08-04
**Owner:** Steve Nazari (operator) for Alina Nazari, FDN-P
**Status:** Approved design, pending spec review

---

## 1. Purpose

Stand up Alina's YouTube channel as the **central content hub** for Go Happy Belly. YouTube becomes the source that feeds all other platforms (Instagram, TikTok, YouTube Shorts). The build models the proven playbook of Ben Azadi (a well-known figure in the space Alina worked closely with) as a *starting anchor*, but is deliberately NOT limited to him: it includes a research system that studies multiple successful channels in the adjacent niche and can discover new ones.

The goal is a repeatable, sustainable engine, not a one-off content dump.

## 1a. North-Star Goal

**Grow to at least 100,000 subscribers within one year** (target ~2026-08). This is aggressive and requires disciplined topic selection and packaging, not volume alone. Every decision in this system serves that goal. Alina's on-camera charisma is the retention multiplier; the system's job is to get the click and pick topics with proven demand.

## 2. Success Criteria

- A local `YouTube/` workspace exists at the project root with a clear, package-per-video structure.
- Two dedicated skills exist: one for channel research/intelligence, one for content production.
- A reverse-engineered, cross-channel `Reference_Playbook.md` exists (anchored on Ben Azadi, expandable).
- A Channel Foundation Kit exists (name/handle, banner concept, About copy, playlists, SEO).
- A seeded `Video_Backlog.md` with a first wave of topics + Ben-style titles.
- Steve can say "let's do a batch" and the engine produces scripts + thumbnail briefs + repurposing packages for that batch.

## 3. Key Decisions (from brainstorming)

| Decision | Choice |
|----------|--------|
| Reference sourcing | Blend: research live to draft, Steve corrects with firsthand knowledge |
| Scope beyond Ben | NOT limited to Ben. A research system studies + discovers multiple channels |
| Production model | Batch film, steady release. **Target: 2 long-form/week** |
| Agent's role | Owns full pipeline: topic/title engine, full scripts, thumbnail concepts, repurposing |
| Channel foundation | Channel does not exist yet — include full foundation kit |
| Primary CTA | **Grow first, sell later.** Soft CTAs (subscribe, quiz-in-description) now; funnel CTAs phase in with traction |
| File location | Top-level `YouTube/` folder at project root (not nested under `Documents/`) |
| Structure model | Package-per-video (each video is a self-contained folder) |
| Skill architecture | Two skills: research (intelligence) feeds production (engine) |
| Discovery automation | Manual/on-demand for now; automate as a routine later once there's momentum |

## 4. File Structure

Top-level, at `Desktop/GoHappyBelly/YouTube/`:

```
YouTube/
├── 00_Strategy/
│   ├── Reference_Playbook.md      # SYNTHESIS of patterns across ALL studied channels.
│   │                              # This is the source of truth the production engine reads.
│   ├── Channel_Foundation.md      # name/handle, banner concept, About copy, playlists, SEO keywords
│   └── Content_Strategy.md        # content pillars, archetype/avatar mapping, CTA phasing plan
├── 01_Research/
│   ├── Reference_Channels.md      # watchlist: every tracked channel (URL, niche, why relevant, status)
│   └── teardowns/
│       ├── ben-azadi.md           # structured teardown, one file per channel
│       └── [channel-slug].md
├── 02_Backlog/
│   └── Video_Backlog.md           # running, prioritized topics + Ben-style titles + target archetype/avatar
├── 03_Videos/
│   └── YT-001_slug/               # one folder per video = the "package"
│       ├── script.md
│       ├── thumbnail-brief.md     # thumbnail text + visual concept (+ generated mockups)
│       └── repurpose.md           # Shorts/Reels/TikTok cuts + captions + distribution plan
├── 04_Published/
│   └── Channel_Tracker.md         # what's live: dates, links, performance notes
└── _Templates/
    ├── channel-teardown-template.md
    ├── script-template.md
    ├── thumbnail-brief-template.md
    └── repurpose-template.md
```

**Rationale for package-per-video:** In a batch model, each video moves through stages as a unit and hands cleanly to Alina (to film) and later an editor (to cut). Everything for one video lives in one place.

## 5. Skills

### 5.1 `gohappybelly-youtube-research` (intelligence layer)
Three functions:
1. **Teardown** — input a channel URL, output a structured analysis using `channel-teardown-template.md`: title formulas, thumbnail style, upload cadence, video length distribution, series/playlist structure, hook patterns, top-performing videos, topic categories. Saved to `01_Research/teardowns/`.
2. **Discover** — input the niche (gut health, functional medicine, perimenopause/hormones, functional nutrition), find other successful channels worth studying, add to `Reference_Channels.md`. On-demand only.
3. **Strategist / methodology research** — study documented YouTube-growth *methods*, not just channels. Priority target: **Jeremy Stickney** (Ben Azadi's strategist, Evan Carmichael's business partner, 2M+ subscribers grown) and the **Evan Carmichael system** he descends from. His method lives mostly in audio/video (talks, podcast appearances), so teardown requires transcribing that content + mapping Carmichael's documented framework. Output saved alongside teardowns and folded into the playbook. NOTE: research public content only; do NOT contact Jeremy or anyone else without explicit instruction from Steve. Do NOT commit personal contact details (e.g. private emails) to the repo.
4. **Synthesize** — roll all teardowns + methodology research into `00_Strategy/Reference_Playbook.md`, the pattern distillation the production engine consumes. Common format keeps sources comparable.

### 5.2 `gohappybelly-youtube` (production engine)
Consumes `Reference_Playbook.md` and `Content_Strategy.md`. Owns:
- **Topic & title engine** — generate + prioritize backlog topics with Ben-style titles, mapped to the 5 gut archetypes and 7 avatars.
- **Long-form scripts** — hook → intro → teaching sections with retention loops / pattern interrupts → story → CTA, in Alina's voice. Distinct from short-form; the existing `gohappybelly-scripts` skill stays for standalone Reels/TikToks.
- **Thumbnail briefs** — text + visual concept modeled on studied channels; can generate mockups with image tools for Alina/Steve to finalize.
- **Repurposing** — break each long-form into Shorts/Reels/TikTok scripts + captions + distribution plan.

**Separation rationale:** research feeds production. Running "find new channels" shouldn't drag in the production engine, and vice versa. Each skill stays focused and independently usable.

## 5.3 Viral Topic Acquisition — Tooling & Method

The research skill does not guess topics. It reverse-engineers what has already gone viral in the niche, using real data.

**Tools:**
- **Claude-in-Chrome (browser automation)** — open competitor channels, sort by "Popular," read actual view counts to surface proven winners. Requires YouTube site permission on the extension.
- **Firecrawl (search/scrape/extract)** — pull structured video data (titles, views, dates) across many channels at scale; later powers competitor monitoring.
- **WebSearch / WebFetch** — search-demand and trend signals in gut health.
- **Higgsfield `virality_predictor`** — score our own candidate titles + thumbnail concepts before committing film time.
- **deep-research skill** — periodic wide deep-dives on a topic cluster.

**The Outlier Framework (method):**
1. Find outliers (videos with views far above their channel average), not averages.
2. Reverse-engineer the packaging: title formula + thumbnail + angle. Packaging goes viral, not raw topics.
3. Adapt, don't copy — re-cut proven outliers through Alina's gut-health authority + archetype framing.
4. Score candidate packaging with the virality predictor before batch film days.
5. Double down on Alina's own outliers once they emerge.

**Dependencies to confirm at build time:** Firecrawl access active; Claude-in-Chrome YouTube site permission granted.

## 6. Channel Foundation Kit (one-time, built first)
- Channel name / handle options
- Banner + art concept in the locked brand system (navy #1B2D4F, sage #7BA987, terracotta #C67B5C, Georgia serif)
- About-section copy
- Playlist architecture mapped to the 5 gut archetypes + key avatar themes
- Channel keywords / SEO description

## 7. The Repeatable Batch Loop
1. **Topic engine** pulls next N topics from `Video_Backlog.md` (each carries a title + target archetype/avatar).
2. **Script** each video (long-form, Alina's voice).
3. **Thumbnail brief** each (text + concept + optional mockup).
4. **Alina batch-films** the set.
5. **Repurpose** each into Shorts/Reels/TikTok + captions + distribution.
6. **Publish tracker** logs live videos with grow-first CTAs in descriptions.

## 8. CTA Phasing (grow first, sell later)
- **Phase 1 (now):** primary CTA is *subscribe*; quiz sits soft in description + pinned comment. No hard selling.
- **Phase 2 (with traction):** quiz-first CTAs move up, then Guthub.ai ($13 entry), then the Gut Breakthrough Call. Flip is deliberate, not accidental.

## 9. Compliance & Voice (carried through everything)
- Pattern/archetype language only. Never diagnostic ("your pattern suggests," never "you have SIBO").
- No em dashes. No banned words (transform, journey, empower, authentic, passionate, innovative, creative[marketing], unique, elevate, synergy).
- Locked sign-off where relevant.
- GI-MAP framing: optional clinical recommendation after initial consult.

## 10. Build Order
1. Research the anchor: (a) Ben's channel live (`@KetoKamp`, URL provided) → `ben-azadi.md` teardown; (b) Jeremy Stickney / Evan Carmichael methodology → strategist teardown. Roll into first `Reference_Playbook.md`; Steve corrects with firsthand knowledge from having worked with Ben.
2. Build the `YouTube/` folder structure + all `_Templates/`.
3. Write `gohappybelly-youtube-research` skill.
4. Write `gohappybelly-youtube` skill.
5. Produce the Channel Foundation Kit.
6. Seed `Video_Backlog.md` with a first wave.
7. (Ongoing) run batches on demand.

## 11. Out of Scope (for now)
- Scheduled/automated channel discovery (revisit as a routine once there's momentum).
- Actual thumbnail final art (agent produces briefs + mockups; humans finalize).
- Video editing / filming (Alina films; editor cuts).
- Paid ads and cold-traffic funnel (existing Phase 2/3 priorities, separate).
