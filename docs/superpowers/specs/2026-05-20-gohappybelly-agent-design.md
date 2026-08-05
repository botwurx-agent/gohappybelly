# GoHappyBelly Agent — Design Spec

**Date:** 2026-05-20
**Status:** Approved, ready for implementation
**Operator:** Steve Nazari (husband, business operator)
**Practitioner:** Alina Nazari, FDN-P (client-facing only)

---

## Overview

Set up a local Claude Code agent folder for Go Happy Belly — Alina Nazari's functional nutrition practice. Steve operates this agent as a full business co-pilot covering copywriting, script writing, funnel building, email marketing, social content, and landing page strategy.

The agent mirrors the pattern used by the Botwurx Agents folder at `/Users/synastudio/Desktop/Botwurx Agents/` but is purpose-built for a content-and-funnel-driven nutrition coaching business rather than a production company.

---

## Directory Structure

```
/Users/synastudio/Desktop/GoHappyBelly/
├── CLAUDE.md                        ← Agent brain — all context lives here
├── .env                             ← API keys (Mailchimp, etc.)
├── Scan Inbox/                      ← Drop files here for auto-processing
├── docs/
│   └── superpowers/
│       └── specs/                   ← This file lives here
└── Documents/
    ├── Brand Assets/                ← Voice guide, avatar profiles, color palette, logo notes
    ├── Offer Suite/                 ← Full offer descriptions, pricing, inclusions
    ├── Content Library/             ← Saved scripts, hooks, captions, post ideas
    ├── Funnel Assets/               ← Landing page copy, email sequences, quiz flow docs
    ├── Copy Templates/              ← Reusable templates (emails, DMs, ad copy)
    ├── ManyChat Flows/              ← DM automation scripts and logic maps
    └── Swipe File/                  ← Reference content worth saving for inspiration
```

**Existing assets reference:** Raw business assets (logo, social images, videos, website images, Stripe docs) already exist at `/Users/synastudio/Documents/GoHappyBelly/`. The agent's Documents folder above stores working copy and content assets. CLAUDE.md will reference the existing assets path where relevant.

---

## CLAUDE.md Architecture

The CLAUDE.md is the agent's complete business brain. It contains the following sections:

### 1. What This Agent Is
Defines Steve as the operator, Alina as the practitioner. Establishes that this agent is a full business co-pilot for GoHappyBelly and the Guthub.ai ecosystem.

### 2. Business Overview
- Go Happy Belly: functional nutrition practice, Alina Nazari FDN-P
- Focus: helping women uncover root causes of gut symptoms via 1:1 coaching, testing, and protocols
- Guthub.ai: AI-powered gut health platform (Steve-owned, beta), serves as the lower-priced downsell/entry offer in the ecosystem

### 3. The Seven Client Avatars

Each avatar includes: name/label, age range, primary symptoms, core frustration, emotional driver, funnel entry point, and primary offer match.

| # | Avatar | Age | Primary Entry |
|---|--------|-----|---------------|
| 1 | The Dismissed Patient | 40-55 | Labs "normal," no answers | Full 3-month program |
| 2 | The Burned-Out Professional | 28-40 | IBS symptoms, skin, anxiety | Tests + course |
| 3 | The Postpartum Rebuilder | 28-42 | Post-pregnancy gut disruption | Nurture → coaching |
| 4 | The Frustrated Dieter | 35-55 | Can't lose weight despite "eating right" | OAT / food sensitivity tests |
| 5 | The Health-Conscious Optimizer | 30-50 | Eats well, still feels off | Trust-building → coaching |
| 6 | The Post-Menopausal Woman | 55-65 | Lingering post-menopause symptoms | Full 3-month program |
| 7 | The Caregiver Who Finally Put Herself Last | 45-60 | Neglected her own health for years | Emotionally motivated → coaching |

### 4. The Five Gut Archetypes

The core segmentation mechanism from the ScoreApp quiz. Each archetype has a locked analogy (used in Email 3) and a locked aha line (used in Email 1 and future content).

| Archetype | Analogy | Aha Line |
|-----------|---------|----------|
| The Wired-and-Tired Gut | Car with engine timing off | "The food is fine. The system processing it isn't." |
| The Reactive Gut | Damaged screen door | "The foods aren't the problem. The barrier is." |
| The Sugar-Driven Gut | Squatters in the house | "The cravings aren't yours. They're something else's, broadcasting through you." |
| The Underactive Gut | Stove that isn't hot enough | "The problem isn't what you're eating. It's that your stomach isn't breaking it down." |
| The Bloated and Backed-Up Gut | Bacteria in wrong neighborhood + flooded basement | "The bacteria aren't the problem. The location is." |

### 5. The Offer Suite

| Offer | Price | Notes |
|-------|-------|-------|
| 3-Month Gut Reset (coaching) | $1,497 | Flagship. Includes 1x 60-min consult, 1x 30-min/month follow-up, meal/supplement plans, community, Gut Reset Course, Guthub access |
| Gut Reset Course | $147 | Standalone digital course |
| Guthub.ai | $13/month | Downsell/entry offer. Steve owns. |
| GI-MAP Stool Test | $497 | Comes with reading/consultation |
| H. Pylori Test | $250 | Comes with reading/consultation |
| SIBO Test | $425 | Comes with reading/consultation |
| OAT Test | $497 | Comes with reading/consultation |
| Food Sensitivity Test | $639 | Comes with reading/consultation |

GI-MAP is framed as an optional clinical recommendation decided post-consultation — not a hard upsell.

### 6. Funnel Architecture

```
Instagram / TikTok / YouTube (organic content)
        ↓
Quiz: "What's Your Gut Pattern?" (ScoreApp)
  → scoreapp.com/alina-ckt3qe46
        ↓
Results page (1 of 5 archetypes) — dual CTA:
  [Book a Gut Breakthrough Call] (Calendly) OR [Start Guthub Trial]
        ↓
7-email archetype-specific welcome sequence (21 days, Mailchimp)
  → Exit logic: if booked-call tag applied, exits sequence
        ↓
Gut Breakthrough Call (20 min, free) → 3-Month Gut Reset ($1,497)
  OR
Guthub.ai free trial → $13/month
```

### 7. Current Build Status

As of 2026-05-20:

**Live:**
- ScoreApp quiz (12 questions, weighted multi-outcome scoring)
- 5 results pages
- Quiz landing page
- Calendly Gut Breakthrough Call
- Mailchimp integration (API, custom `Gut Pattern` field, auto-tagging)
- Zapier: Calendly → Mailchimp `booked-call` tag
- Wired-and-Tired Gut email sequence (7 emails, fully live and tested)
- Re-engagement Email 1 (loaded, ready to send)

**Written, needs loading:**
- Reactive Gut sequence (7 emails)
- Sugar-Driven Gut sequence (7 emails)
- Underactive Gut sequence (7 emails)
- Bloated and Backed-Up Gut sequence (7 emails)
- Re-engagement Emails 2 and 3

**Not yet built:**
- 3-Month Gut Reset sales page (call is current sales mechanism)
- ManyChat Instagram DM flows
- Cold traffic funnel (Phase 2)
- Paid ads (Phase 3)

Full technical reference: `/Users/synastudio/Documents/GoHappyBelly/Documents/Claude Handoff Files/Go_Happy_Belly_Funnel_Handoff_v2.md`

### 8. Platform Stack

| Platform | Purpose | Status |
|----------|---------|--------|
| ScoreApp | Quiz + results pages | Live |
| Mailchimp | Email automation, Customer Journeys | Live (paid plan) |
| Calendly | Gut Breakthrough Call booking | Live |
| Zapier | Calendly → Mailchimp booked-call tag | Live |
| SamCart | Checkout / 1-page landing pages | Available, not yet active in funnel |
| ManyChat | Instagram DM automation | Planned |
| Instagram | Primary social (8K followers) | Active |
| TikTok | Social growth | Active |
| YouTube | Long-form content | Active |
| Guthub.ai | AI gut health platform (downsell) | Beta |

### 9. Brand Voice

Alina's voice characteristics:
- Nurturing AND direct — says things how they are without sugarcoating
- Uses analogies to make complex things relatable
- Validates without being saccharine
- Listens deeply — people gravitate to her
- Warm and people-friendly, not clinical

**Sign-off (locked format):**
```
In Gut Health,
Alina Nazari
FDN-P
```

### 10. Brand Design System (Locked)

**Color palette:**
- Navy: #1B2D4F (headings, sign-off, emphasis)
- Sage Green: #7BA987 (accents, dividers, validation moments)
- Terracotta: #C67B5C (primary CTA buttons)
- Warm Cream: #FAF6F0 (page backgrounds, outer email wrapper)
- White: #FFFFFF (inner email content card)
- Testimonial BG: #F5F1EA
- Body Text: #374151
- Soft Gray: #6B7280 (secondary text, P.S., footer)
- Light Border: #E5E7EB

**Email design (locked):**
- Font: Georgia (serif)
- Width: 600px max
- Beige outer wrapper (#FAF6F0) + white inner content card (#FFFFFF)
- Logo at top, sage accent line below logo
- Single bold navy "aha moment" line per email
- Sage left-border quote boxes (Alina's voice), terracotta left-border (client testimonials)
- P.S. in italic gray with thin top border
- Mobile-responsive

### 11. Compliance Guardrails

Alina is NOT a doctor. She cannot diagnose conditions. All language uses pattern/archetype framing.

**Never use:** "You have SIBO/Candida/Leaky Gut", direct diagnoses, "cure" or "treat"
**Always use:** "Your pattern suggests", "This often shows up when", "address the pattern", "work with"

### 12. Hard Style Rules

- **NO em dashes** anywhere in copy — use commas, parentheses, or rewrite
- No: "transform", "journey", "empower", "authentic", "passionate", "innovative", "elevate", "synergy"
- Pattern language only, not diagnostic language

### 13. Priorities (in order)

1. Funnel completion and optimization
2. Social content (IG, TikTok, YouTube) — growing audience
3. Email marketing — sequences, campaigns, nurture
4. ManyChat DM automation
5. Sales page and landing page copy (SamCart)
6. Future: paid ads strategy (Phase 3)

### 14. What This Agent Should NOT Do

- Do not send emails or post content without explicit confirmation from Steve
- Do not contact clients or prospects directly
- Do not use diagnostic language under any circumstances
- Do not make assumptions about pricing or offer changes
- Do not create new Mailchimp journeys or campaigns without being asked

### 15. Scan Inbox — Auto-Run at Session Start

At the start of every session, silently check `/Users/synastudio/Desktop/GoHappyBelly/Scan Inbox/` for new files.

| What it is | Move to | Follow-up action |
|------------|---------|-----------------|
| Instagram/TikTok screenshot of a brand or account | `Documents/Swipe File/` | Note what platform, extract caption/concept, flag what made it worth saving |
| Screenshot of content idea or reference | `Documents/Content Library/` | Summarize and tag by archetype or avatar if applicable |
| Email draft or copy | `Documents/Copy Templates/` | Summarize for Steve |
| Funnel asset or landing page | `Documents/Funnel Assets/` | Summarize and confirm placement |
| Client testimonial | `Documents/Brand Assets/Testimonials/` | Format using locked testimonial style, flag for use |
| Anything unclear | `Documents/Brand Assets/` | Show Steve what was found, ask how to categorize |

If inbox is empty: proceed normally, do not mention the check.

---

## The Five Skills

Each skill is a standalone `.md` file stored in `/Users/synastudio/.claude/skills/`. All skills share awareness of: the 7 avatars, 5 archetypes, offer suite, brand voice, compliance rules, and style rules.

### `gohappybelly-content`
Produces social content for Instagram, TikTok, and YouTube. Given an avatar or archetype and a topic, outputs hooks, captions, and content angles in Alina's voice. Knows platform-specific formats: Reels/TikTok short-form, Instagram carousels, YouTube descriptions.

### `gohappybelly-scripts`
Writes video scripts in two formats:
- Short-form (30-90 sec): TikTok/Reels structure — hook, education/story, CTA
- Long-form (5-15 min): YouTube structure — hook, problem, body, CTA
Scripts are always tied to a specific avatar and support a specific offer or funnel stage.

### `gohappybelly-email`
Writes Mailchimp emails and sequences. Knows the locked email design system, the 7-email archetype sequence structure, delay logic, and exit logic. Produces copy in HTML-ready format following the beige/white template. Enforces no-em-dash rule and compliance guardrails throughout.

### `gohappybelly-funnel`
Writes conversion copy for SamCart landing pages, ScoreApp quiz copy, offer page headlines/subheadlines/CTAs, and funnel flow documents. Conversion-focused while staying in Alina's voice. References the full offer ladder and funnel architecture.

### `gohappybelly-manychat`
Designs and writes Instagram DM automation flows. Outputs keyword triggers, branching response scripts, lead qualification logic, and handoff CTAs (booking link or offer page). Structured to match ManyChat's flow builder format.

---

## Key URLs and Credentials

Stored in `/Users/synastudio/Desktop/GoHappyBelly/.env`:
- Mailchimp API key
- Any future integrations (ManyChat, SamCart, etc.)

Live URLs (also referenced in CLAUDE.md):
- Quiz: `https://gut-pattern-quiz.scoreapp.com`
- Booking: `https://calendly.com/gohappybelly/gut-breakthrough-call`
- Guthub: `https://www.guthub.ai`
- Logo (Mailchimp CDN): `https://mcusercontent.com/96c61326f42af27664085aa8e/images/8f2866df-3ecb-abf4-9b68-1bff182362d1.jpg`

---

## Implementation Plan (next step)

1. Create folder structure at `/Users/synastudio/Desktop/GoHappyBelly/`
2. Write `CLAUDE.md` with all sections above
3. Create `.env` placeholder file
4. Create `Scan Inbox/` directory
5. Create all `Documents/` subdirectories
6. Write 5 skill files to `/Users/synastudio/.claude/skills/`
7. Add symlink or reference note in `Documents/Funnel Assets/` pointing to existing handoff doc at `/Users/synastudio/Documents/GoHappyBelly/Documents/Claude Handoff Files/Go_Happy_Belly_Funnel_Handoff_v2.md`

---

*This spec was generated via the brainstorming skill on 2026-05-20. Implementation follows via writing-plans skill.*
