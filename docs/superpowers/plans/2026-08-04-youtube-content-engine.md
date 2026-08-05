# YouTube Content Engine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Tasks 3 and 4 (skill authoring) additionally require superpowers:writing-skills.

**Goal:** Stand up Alina's YouTube channel as Go Happy Belly's central content hub, with a research-driven engine that reverse-engineers proven viral content and produces batch-ready video packages.

**Architecture:** A top-level `YouTube/` workspace holds strategy, research, a video backlog, and per-video package folders. Two skills drive it: `gohappybelly-youtube-research` (intelligence: channel teardowns, discovery, strategist-method research, synthesis) feeds `gohappybelly-youtube` (production: topics, titles, long-form scripts, thumbnail briefs, repurposing). Research output (`Reference_Playbook.md`) is the source of truth the production skill reads.

**Tech Stack:** Markdown workspace files; Claude Code skills (SKILL.md + YAML frontmatter); Claude-in-Chrome, Firecrawl, WebSearch/WebFetch, and Higgsfield `virality_predictor` as data/analysis tools.

## Global Constraints

Copied verbatim from the spec and CLAUDE.md. Every task implicitly includes these.

- **North-star:** 100,000 subscribers within one year (~2026-08). Topic selection and packaging serve this.
- **No em dashes anywhere.** Use commas, parentheses, or rewrite.
- **Banned words:** transform, journey, empower, authentic, passionate, innovative, creative (marketing sense), unique, elevate, synergy.
- **Pattern/archetype language only. Never diagnostic.** "Your pattern suggests," never "you have SIBO/Candida/Leaky Gut." No "cure"/"treat." Use "address"/"work with" the pattern.
- **GI-MAP framing:** always "optional clinical recommendation" decided after the initial consultation.
- **Sign-off (where relevant), locked exactly:** `In Gut Health,` / `Alina Nazari` / `FDN-P`.
- **Brand colors:** Navy #1B2D4F, Sage #7BA987, Terracotta #C67B5C, Warm Cream #FAF6F0, Body #374151, Soft Gray #6B7280.
- **5 gut archetypes** (with locked analogy + aha line): Wired-and-Tired, Reactive, Sugar-Driven, Underactive, Bloated-and-Backed-Up. **7 avatars** per CLAUDE.md.
- **CTA phasing:** Phase 1 (now) = grow-first (subscribe primary; quiz soft in description + pinned comment). Phase 2 (with traction) = quiz-first, then Guthub.ai ($13), then Gut Breakthrough Call.
- **Privacy:** research public content only; do NOT contact any strategist/creator without explicit instruction from Steve; NEVER commit personal contact details (private emails, phone numbers) to the repo.
- **Approval:** do not publish, post, or activate anything externally without Steve's explicit confirmation.

**Prerequisites (confirm before Tasks 5-6):** Firecrawl skill active, and Claude-in-Chrome granted YouTube site permission. If neither is available, Tasks 5-6 fall back to WebSearch/WebFetch with a logged note that view-count depth is reduced.

**Key paths:**
- Workspace root: `/Users/synastudio/Desktop/GoHappyBelly/YouTube/`
- Skills live (and load) from: `/Users/synastudio/.claude/skills/<name>/SKILL.md` (OUTSIDE the git repo)
- Repo: `/Users/synastudio/Desktop/GoHappyBelly` (remote `origin` → github.com/botwurx-agent/gohappybelly)
- Skill source mirror (for version history, since live skills are outside the repo): `/Users/synastudio/Desktop/GoHappyBelly/YouTube/_skills-source/`

---

### Task 1: Scaffold the YouTube workspace

**Files:**
- Create dir tree under `/Users/synastudio/Desktop/GoHappyBelly/YouTube/`
- Create: `YouTube/00_Strategy/Reference_Playbook.md` (header stub)
- Create: `YouTube/00_Strategy/Channel_Foundation.md` (header stub)
- Create: `YouTube/00_Strategy/Content_Strategy.md` (header stub)
- Create: `YouTube/01_Research/Reference_Channels.md` (watchlist table header)
- Create: `YouTube/02_Backlog/Video_Backlog.md` (backlog table header)
- Create: `YouTube/04_Published/Channel_Tracker.md` (tracker table header)
- Create: `YouTube/01_Research/teardowns/.gitkeep`, `YouTube/03_Videos/.gitkeep`, `YouTube/_skills-source/.gitkeep`

**Interfaces:**
- Produces: the folder skeleton every later task writes into; the three tables (Reference_Channels, Video_Backlog, Channel_Tracker) with fixed column headers other tasks append rows to.

- [ ] **Step 1: Define acceptance criteria**

The tree matches spec §4 exactly: `00_Strategy/`, `01_Research/teardowns/`, `02_Backlog/`, `03_Videos/`, `04_Published/`, `_Templates/`, plus `_skills-source/`. Stub files exist with headers; empty dirs hold `.gitkeep`.

- [ ] **Step 2: Create the directory tree**

```bash
cd /Users/synastudio/Desktop/GoHappyBelly
mkdir -p YouTube/00_Strategy YouTube/01_Research/teardowns YouTube/02_Backlog \
         YouTube/03_Videos YouTube/04_Published YouTube/_Templates YouTube/_skills-source
touch YouTube/01_Research/teardowns/.gitkeep YouTube/03_Videos/.gitkeep YouTube/_skills-source/.gitkeep
```

- [ ] **Step 3: Write the stub strategy files**

`YouTube/00_Strategy/Reference_Playbook.md`:
```markdown
# Reference Playbook

> Synthesis of patterns across every studied channel + strategist method.
> This is the source of truth the `gohappybelly-youtube` production skill reads.
> Populated in Task 7. Do not hand-edit output sections; re-run synthesis.

## Status
Not yet synthesized. See `01_Research/teardowns/`.
```

`YouTube/00_Strategy/Channel_Foundation.md`:
```markdown
# Channel Foundation Kit

> Channel name/handle, banner concept, About copy, playlist architecture, SEO keywords.
> Populated in Task 8.
```

`YouTube/00_Strategy/Content_Strategy.md`:
```markdown
# Content Strategy

> Content pillars, archetype/avatar mapping, CTA phasing plan.
> Populated in Task 8.
```

- [ ] **Step 4: Write the three table files with fixed headers**

`YouTube/01_Research/Reference_Channels.md`:
```markdown
# Reference Channels (Watchlist)

Channels and methods we study. Ben Azadi (Keto Kamp) is the anchor; not the ceiling.

| Channel / Source | URL | Niche | Subscribers | Why It Matters | Status |
|---|---|---|---|---|---|
```

`YouTube/02_Backlog/Video_Backlog.md`:
```markdown
# Video Backlog

Prioritized topics with proven-demand packaging. Fuel for batch film days.
Priority: P1 (film next batch), P2 (soon), P3 (parking lot).

| ID | Working Title | Angle / Hook | Archetype | Avatar | Priority | Source Signal | Status |
|---|---|---|---|---|---|---|---|
```

`YouTube/04_Published/Channel_Tracker.md`:
```markdown
# Channel Tracker

| Video ID | Title (as published) | Publish Date | URL | Views (30d) | Notes / Outlier? |
|---|---|---|---|---|---|
```

- [ ] **Step 5: Verify structure**

Run: `cd /Users/synastudio/Desktop/GoHappyBelly && find YouTube -type f -o -type d | sort`
Expected: every directory from spec §4 present; six stub/table files present; three `.gitkeep` files present.

- [ ] **Step 6: Commit**

```bash
cd /Users/synastudio/Desktop/GoHappyBelly
git add YouTube/
git commit -m "feat(youtube): scaffold YouTube content engine workspace"
```

---

### Task 2: Author the four pipeline templates

**Files:**
- Create: `YouTube/_Templates/channel-teardown-template.md`
- Create: `YouTube/_Templates/script-template.md`
- Create: `YouTube/_Templates/thumbnail-brief-template.md`
- Create: `YouTube/_Templates/repurpose-template.md`

**Interfaces:**
- Produces: `channel-teardown-template.md` (consumed by Tasks 5-6); `script-template.md`, `thumbnail-brief-template.md`, `repurpose-template.md` (consumed by the production skill in Task 4 and every batch). Field names defined here are referenced verbatim by the skills.

- [ ] **Step 1: Define acceptance criteria**

Four templates exist, each with concrete fill-in fields (not prose instructions), each honoring Global Constraints. The teardown template captures data needed for the Outlier Framework (view counts, outlier ratio, title formula, thumbnail pattern, cadence, playlists, hooks).

- [ ] **Step 2: Write `channel-teardown-template.md`**

```markdown
# Channel Teardown: <Channel Name>

- **URL:** <url>
- **Niche:** <niche>
- **Subscribers:** <count>  |  **Total views:** <count>  |  **Started:** <year>
- **Studied on:** <date>  |  **Data source:** <Chrome Popular sort / Firecrawl / WebSearch>

## Cadence & Format
- Upload frequency: <e.g. 3 long-form/week + daily Shorts>
- Long-form length range: <min-max>
- Shorts usage: <yes/no, how>

## Outlier Videos (sorted by views, top 10-15)
| Title | Views | Approx Date | Outlier Ratio (views ÷ channel avg) | Thumbnail Description |
|---|---|---|---|---|

## Title Formulas (patterns across the outliers)
- <formula 1, with 2 examples>
- <formula 2, with 2 examples>

## Thumbnail Style
- Colors / contrast: <...>
- Face/expression usage: <...>
- Text overlay pattern (word count, placement): <...>
- Recurring visual devices: <...>

## Hook Patterns (first 15-30 sec of top videos)
- <pattern 1>
- <pattern 2>

## Playlist / Series Architecture
- <how content is organized into series/playlists>

## Topic Categories That Overperform
- <category 1>  | <category 2>  | <category 3>

## Gut-Health Adaptation Notes (how Alina applies this, non-diagnostic)
- <note>
```

- [ ] **Step 3: Write `script-template.md`**

Base it on the long-form structure in `gohappybelly-scripts/SKILL.md`, expanded for retention. Fields:
```markdown
# Script: <Working Title>

- **Video ID:** <YT-###>  | **Archetype:** <one of 5>  | **Avatar:** <one of 7>
- **Target length:** <8-15 min>  | **Funnel phase:** <Phase 1 grow-first / Phase 2>
- **Packaging source signal:** <which outlier/pattern this is modeled on>

## [HOOK — first 30 sec]
[SPOKEN]: <viewer's problem + payoff promise; no intro yet>
[TEXT OVERLAY]: <key phrase>

## [CREDENTIAL MOMENT — 30-60 sec]
[SPOKEN]: <brief, natural FDN-P credibility, then back to content>

## [PROBLEM BLOCK — 1-2 min]
[SPOKEN]: <avatar-grounded frustration in their own words>

## [BODY — 3-5 points, 6-10 min]
### Point 1: <name>
[SPOKEN]: <explain simply + analogy + connect back>
[RETENTION LOOP]: <open a curiosity gap you close later>
[VISUAL NOTE]: <b-roll>
### Point 2 ... (repeat structure)

## [BRIDGE / CTA — 1 min]
[SPOKEN]: Phase 1 = soft ("figure out your gut pattern, link in description"). Phase 2 = quiz-first, then Guthub, then call.

## [OUTRO — 30 sec]
[SPOKEN]: <tease a related video + soft subscribe ask>
```

- [ ] **Step 4: Write `thumbnail-brief-template.md`**

```markdown
# Thumbnail Brief: <Working Title>  (<YT-###>)

- **Modeled on:** <outlier/pattern from playbook>
- **Big idea in one glance:** <the single message the thumbnail must convey>

## Text on Thumbnail
- Primary text (<= 4 words): <...>
- Secondary text (optional, <= 3 words): <...>

## Visual Concept
- Subject / expression: <Alina's pose + emotion>
- Background / color: <use brand palette; navy/terracotta/sage; high contrast>
- Visual device: <arrow, circle, before/after, prop, etc.>

## Compliance check
- [ ] No diagnostic claims  - [ ] No banned words  - [ ] No em dashes

## Mockup
- <path to generated mockup image, or "pending">
```

- [ ] **Step 5: Write `repurpose-template.md`**

```markdown
# Repurposing Plan: <Working Title>  (<YT-###>)

Source long-form drives all platforms (YouTube is the hub).

## Clips (3-5 per long-form)
| Clip # | Timestamp in source | Angle | Platform(s) | Caption (Alina's voice, no em dashes) | Hook line |
|---|---|---|---|---|---|

## YouTube Shorts
- <script/notes per short>

## Distribution notes
- Posting order + spacing: <...>
- CTA per platform (Phase 1 soft): <...>
```

- [ ] **Step 6: Verify templates**

Read all four. Confirm: concrete fields (no vague "add details"), no em dashes in template prose, teardown captures outlier ratio + title/thumbnail/cadence, script has retention loops, thumbnail brief has compliance check.

- [ ] **Step 7: Commit**

```bash
cd /Users/synastudio/Desktop/GoHappyBelly
git add YouTube/_Templates/
git commit -m "feat(youtube): add pipeline templates (teardown, script, thumbnail, repurpose)"
```

---

### Task 3: Write the `gohappybelly-youtube-research` skill

**REQUIRED SUB-SKILL:** superpowers:writing-skills (follow its authoring + verification process).

**Files:**
- Create: `/Users/synastudio/.claude/skills/gohappybelly-youtube-research/SKILL.md`
- Copy to: `YouTube/_skills-source/gohappybelly-youtube-research.SKILL.md` (version-history mirror)

**Interfaces:**
- Consumes: templates from Task 2 (`channel-teardown-template.md`), workspace files from Task 1 (`Reference_Channels.md`, `teardowns/`, `Reference_Playbook.md`).
- Produces: the skill that generates teardowns and the synthesized playbook Task 4's skill reads.

- [ ] **Step 1: Define acceptance criteria**

Valid frontmatter (`name`, `description` with trigger phrases). Body documents four functions (teardown, discover, strategist-method, synthesize), the exact tools each uses, the Outlier Framework, the privacy guardrails, and exact output file paths. Honors Global Constraints.

- [ ] **Step 2: Write the frontmatter verbatim**

```markdown
---
name: gohappybelly-youtube-research
description: Research and reverse-engineer what drives YouTube growth in the gut-health/functional-medicine niche for Go Happy Belly. Use when Steve wants to study a channel, find viral topics, discover new channels to learn from, research a YouTube strategist's method, or update the reference playbook. Trigger phrases: "tear down this channel", "research YouTube", "find viral topics", "find channels to study", "study Ben Azadi", "update the playbook", "what's working on YouTube". Anchor is Ben Azadi (Keto Kamp) but never limited to him. Research public content only; never contact anyone; never commit personal contact details.
---
```

- [ ] **Step 3: Write the body — required sections with this exact content intent**

Author these sections (prose in Alina's business voice, no em dashes):
1. **Purpose** — reverse-engineer proven growth, not guess. Feeds the production skill.
2. **Function A — Channel Teardown:** input a channel URL. Use Claude-in-Chrome to open `<channel>/videos`, sort by **Popular**, read real view counts for top 10-15; if Chrome/YouTube permission unavailable, fall back to Firecrawl scrape then WebSearch, and log the reduced-depth note. Fill `_Templates/channel-teardown-template.md`, compute outlier ratio (video views ÷ channel recent average), save to `YouTube/01_Research/teardowns/<slug>.md`, and append a row to `Reference_Channels.md`.
3. **Function B — Discover:** input the niche (gut health, functional medicine, perimenopause/hormones, functional nutrition). Use WebSearch + Firecrawl to find successful channels; add candidates to `Reference_Channels.md` with status `candidate`. On-demand only (no scheduling yet).
4. **Function C — Strategist / Method Research:** study documented growth *methods*, not just channels. Priority: Jeremy Stickney (Ben's strategist, Evan Carmichael's partner, 2M+ grown) and the Carmichael system. Method lives in audio/video, so transcribe/summarize public talks + podcasts via WebFetch/Firecrawl. Save to `YouTube/01_Research/teardowns/<name>-method.md`. Guardrail block: public content only; do NOT contact anyone; do NOT write private emails/phones into any file.
5. **Function D — Synthesize:** roll all teardowns + method files into `YouTube/00_Strategy/Reference_Playbook.md` with concrete reusable rules (title formulas, thumbnail rules, cadence, hook patterns, overperforming topic categories) each adapted to gut-health, non-diagnostic.
6. **The Outlier Framework** — the five-point method from spec §5.3 (find outliers, reverse-engineer packaging, adapt-don't-copy, score before shooting via Higgsfield `virality_predictor`, double down).
7. **Tools reference** — Claude-in-Chrome (needs YouTube permission), Firecrawl, WebSearch/WebFetch, Higgsfield `virality_predictor`.
8. **Guardrails** — Global Constraints (privacy, compliance, no em dashes).

- [ ] **Step 4: Verify the skill**

Confirm frontmatter parses (name matches dir; description has trigger phrases). Confirm all four functions name exact output paths that match Task 1 dirs. Confirm privacy guardrail present. Per writing-skills, sanity-check the description would trigger on Steve's natural phrasing.

- [ ] **Step 5: Mirror + commit**

```bash
cp /Users/synastudio/.claude/skills/gohappybelly-youtube-research/SKILL.md \
   /Users/synastudio/Desktop/GoHappyBelly/YouTube/_skills-source/gohappybelly-youtube-research.SKILL.md
cd /Users/synastudio/Desktop/GoHappyBelly
git add YouTube/_skills-source/
git commit -m "feat(youtube): add gohappybelly-youtube-research skill"
```

---

### Task 4: Write the `gohappybelly-youtube` production skill

**REQUIRED SUB-SKILL:** superpowers:writing-skills.

**Files:**
- Create: `/Users/synastudio/.claude/skills/gohappybelly-youtube/SKILL.md`
- Copy to: `YouTube/_skills-source/gohappybelly-youtube.SKILL.md`

**Interfaces:**
- Consumes: `Reference_Playbook.md` + `Content_Strategy.md` (source of truth), templates from Task 2, `Video_Backlog.md`.
- Produces: per-video packages in `YouTube/03_Videos/YT-###_slug/` (`script.md`, `thumbnail-brief.md`, `repurpose.md`) and backlog rows.

- [ ] **Step 1: Define acceptance criteria**

Valid frontmatter with trigger phrases distinct from the research skill and from `gohappybelly-scripts` (this one owns full YouTube production + batches). Body documents the four production functions, reads the playbook, creates package folders, honors Global Constraints and CTA phasing.

- [ ] **Step 2: Write the frontmatter verbatim**

```markdown
---
name: gohappybelly-youtube
description: Produce Go Happy Belly YouTube content — topic/title ideas, long-form scripts, thumbnail briefs, and repurposing packages — modeled on the reference playbook. Use when Steve wants YouTube video topics or titles, a long-form YouTube script, a thumbnail concept, a repurposing plan, or wants to run a batch. Trigger phrases: "YouTube video ideas", "YouTube titles", "long-form script", "let's do a batch", "thumbnail concept for", "repurpose this video", "add to the backlog". Reads YouTube/00_Strategy/Reference_Playbook.md and Content_Strategy.md as source of truth. Writes per-video package folders. No em dashes, no diagnostic language, grow-first CTAs by default.
---
```

- [ ] **Step 3: Write the body — required sections with this exact content intent**

1. **Purpose + source of truth** — always read `Reference_Playbook.md` and `Content_Strategy.md` first; if `Reference_Playbook.md` is still a stub, tell Steve to run research (Task 7) first.
2. **Function A — Topic & Title Engine:** generate/prioritize backlog topics with playbook-derived title formulas, each mapped to one of 5 archetypes + one of 7 avatars, tagged with a source signal (which outlier/pattern), optionally scored with Higgsfield `virality_predictor`. Append rows to `Video_Backlog.md` using its exact columns.
3. **Function B — Long-form Script:** fill `_Templates/script-template.md` (hook → credential → problem → 3-5 body points with retention loops/pattern interrupts → bridge/CTA → outro), Alina's voice, locked archetype analogies. Save to `YouTube/03_Videos/YT-###_slug/script.md` (create the folder).
4. **Function C — Thumbnail Brief:** fill `_Templates/thumbnail-brief-template.md`; optionally generate a mockup with Higgsfield `generate_image` using brand palette; note humans finalize art. Save `thumbnail-brief.md` in the package.
5. **Function D — Repurposing:** fill `_Templates/repurpose-template.md` (3-5 clips + captions + distribution) per long-form. Save `repurpose.md` in the package.
6. **Batch mode ("let's do a batch"):** pull next N P1 topics from backlog, run B+C+D for each into its package folder, then summarize the batch for Steve.
7. **CTA phasing** — Phase 1 grow-first default; switch to Phase 2 only when Steve says so.
8. **Guardrails** — Global Constraints; existing `gohappybelly-scripts` remains for standalone short-form.

- [ ] **Step 4: Verify the skill**

Frontmatter parses; triggers don't collide destructively with `gohappybelly-scripts` (this owns "batch" + package creation). Output paths match Task 1 structure. Reads playbook before producing.

- [ ] **Step 5: Mirror + commit**

```bash
cp /Users/synastudio/.claude/skills/gohappybelly-youtube/SKILL.md \
   /Users/synastudio/Desktop/GoHappyBelly/YouTube/_skills-source/gohappybelly-youtube.SKILL.md
cd /Users/synastudio/Desktop/GoHappyBelly
git add YouTube/_skills-source/
git commit -m "feat(youtube): add gohappybelly-youtube production skill"
```

---

### Task 5: Anchor channel teardown — Ben Azadi / Keto Kamp

**Prerequisite:** Firecrawl active or Chrome YouTube permission (see Global Constraints).

**Files:**
- Create: `YouTube/01_Research/teardowns/ben-azadi.md`
- Modify: `YouTube/01_Research/Reference_Channels.md` (append row)

**Interfaces:**
- Consumes: research skill Function A, `channel-teardown-template.md`.
- Produces: `ben-azadi.md` teardown consumed by Task 7 synthesis.

- [ ] **Step 1: Define acceptance criteria**

Teardown filled with REAL data from `https://www.youtube.com/@KetoKamp/videos`: top 10-15 videos by views with actual view counts, computed outlier ratios, at least 2 title formulas with examples, thumbnail style description, cadence, playlist architecture, overperforming topic categories, and gut-health adaptation notes. No placeholders.

- [ ] **Step 2: Run the teardown**

Invoke `gohappybelly-youtube-research` (Function A) on `@KetoKamp`. Sort videos by Popular; capture data into the template.

- [ ] **Step 3: Verify data is real, not generic**

Spot-check: view counts are concrete numbers; titles are actual Keto Kamp titles; outlier ratio computed. If the tool could not fetch live view counts, the file must log that limitation explicitly.

- [ ] **Step 4: Steve review checkpoint**

Present the teardown to Steve. He corrects/adds firsthand knowledge from working with Ben. Apply edits.

- [ ] **Step 5: Commit**

```bash
cd /Users/synastudio/Desktop/GoHappyBelly
git add YouTube/01_Research/
git commit -m "feat(youtube): add Ben Azadi / Keto Kamp channel teardown"
```

---

### Task 6: Strategist method research — Jeremy Stickney / Carmichael

**Files:**
- Create: `YouTube/01_Research/teardowns/jeremy-stickney-method.md`
- Modify: `YouTube/01_Research/Reference_Channels.md` (append row, source = method)

**Interfaces:**
- Consumes: research skill Function C.
- Produces: method file consumed by Task 7 synthesis.

- [ ] **Step 1: Define acceptance criteria**

A documented method summary drawn from PUBLIC content: Jeremy Stickney's principles (from his talks/podcast appearances) + the Evan Carmichael system he descends from, distilled into concrete, applicable rules (modeling proven videos, search/keyword-driven titles, consistency, clipping/repurposing, etc.). NO private contact details anywhere in the file.

- [ ] **Step 2: Run the research**

Invoke `gohappybelly-youtube-research` (Function C). Sources to mine: the "What Growing 2,000,000 Subscribers Taught Me" talk, his podcast appearances, and documented Carmichael methodology. Use WebSearch/WebFetch/Firecrawl.

- [ ] **Step 3: Verify**

File contains concrete method principles (not just "he's an expert"), each phrased as something Alina's channel can act on. Confirm no private email/phone present (`grep -i "gmail\|@.*\.com\|phone" file` should surface nothing personal).

- [ ] **Step 4: Commit**

```bash
cd /Users/synastudio/Desktop/GoHappyBelly
git add YouTube/01_Research/
git commit -m "feat(youtube): add Jeremy Stickney / Carmichael method research"
```

---

### Task 7: Synthesize the Reference Playbook

**Files:**
- Modify: `YouTube/00_Strategy/Reference_Playbook.md` (replace stub with full synthesis)

**Interfaces:**
- Consumes: research skill Function D; `ben-azadi.md`, `jeremy-stickney-method.md`, any other teardowns.
- Produces: `Reference_Playbook.md` — the source of truth Task 4's production skill reads.

- [ ] **Step 1: Define acceptance criteria**

Playbook contains, as concrete reusable rules adapted to gut-health (non-diagnostic): title formulas (with gut examples), thumbnail rules, target cadence, hook patterns, overperforming topic categories, and a "packaging checklist" for new videos. Every rule traces to a teardown/method source.

- [ ] **Step 2: Run synthesis**

Invoke `gohappybelly-youtube-research` (Function D) across all files in `teardowns/`.

- [ ] **Step 3: Verify**

Each section has concrete rules + at least one gut-health example; no em dashes; no diagnostic language; sources referenced.

- [ ] **Step 4: Commit**

```bash
cd /Users/synastudio/Desktop/GoHappyBelly
git add YouTube/00_Strategy/Reference_Playbook.md
git commit -m "feat(youtube): synthesize reference playbook from teardowns"
```

---

### Task 8: Channel Foundation Kit

**Files:**
- Modify: `YouTube/00_Strategy/Channel_Foundation.md`
- Modify: `YouTube/00_Strategy/Content_Strategy.md`

**Interfaces:**
- Consumes: `Reference_Playbook.md`, CLAUDE.md brand system, 5 archetypes + 7 avatars.
- Produces: channel foundation + content strategy consumed by the production skill and by Steve for channel setup.

- [ ] **Step 1: Define acceptance criteria**

`Channel_Foundation.md` includes: 3-5 channel name/handle options, banner concept (brand palette + Georgia), About-section copy (Alina's voice, compliant), playlist architecture mapped to the 5 archetypes + key avatar themes, and channel SEO keywords. `Content_Strategy.md` includes: 3-5 content pillars, an archetype/avatar-to-content map, and the Phase 1 → Phase 2 CTA phasing plan.

- [ ] **Step 2: Produce the foundation kit**

Draft both files using the production skill's knowledge + playbook, honoring Global Constraints.

- [ ] **Step 3: Verify**

No em dashes; no banned words; no diagnostic language; About copy uses locked voice; playlists cover all 5 archetypes; SEO keywords are gut-health relevant.

- [ ] **Step 4: Steve review checkpoint**

Steve picks the channel name/handle and approves banner direction before any external channel creation.

- [ ] **Step 5: Commit**

```bash
cd /Users/synastudio/Desktop/GoHappyBelly
git add YouTube/00_Strategy/
git commit -m "feat(youtube): add channel foundation kit and content strategy"
```

---

### Task 9: Seed the Video Backlog

**Files:**
- Modify: `YouTube/02_Backlog/Video_Backlog.md` (append 15-20 rows)

**Interfaces:**
- Consumes: production skill Function A, `Reference_Playbook.md`, `Content_Strategy.md`.
- Produces: the first wave of prioritized topics ready for batch production.

- [ ] **Step 1: Define acceptance criteria**

15-20 backlog rows, each with a working title (playbook title formula), angle/hook, mapped archetype + avatar, priority (P1/P2/P3), and a source signal (which outlier/pattern/demand it's based on). Coverage across multiple archetypes/avatars. Optionally virality-scored. No placeholders, no em dashes, non-diagnostic.

- [ ] **Step 2: Generate the backlog**

Invoke `gohappybelly-youtube` (Function A) to produce 15-20 topics from the playbook + strategy.

- [ ] **Step 3: Verify**

Count is 15-20; every row has all columns filled; archetype/avatar spread is not all-one-bucket; titles follow playbook formulas; compliance clean.

- [ ] **Step 4: Steve review checkpoint**

Steve marks which topics are P1 for the first batch.

- [ ] **Step 5: Commit + push**

```bash
cd /Users/synastudio/Desktop/GoHappyBelly
git add YouTube/02_Backlog/Video_Backlog.md
git commit -m "feat(youtube): seed video backlog with first wave of topics"
git push
```

---

## After the plan

Once Task 9 is committed and pushed, the engine is live: Steve says "let's do a batch," the `gohappybelly-youtube` skill turns P1 backlog topics into per-video packages (script + thumbnail brief + repurposing), Alina batch-films, and the tracker logs results. Discovery and monitoring can be automated later as a routine once there is momentum (spec §11).
