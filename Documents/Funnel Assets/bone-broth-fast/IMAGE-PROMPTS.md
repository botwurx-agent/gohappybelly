# Image prompts: 3-Day Bone Broth Reset

Generated via Higgsfield MCP, `gpt_image_2_5`, 2026-09-22.
Kept so future cohorts, reels and ads stay visually consistent.

## Settings that matter

| Setting | Value | Why |
|---|---|---|
| model | `gpt_image_2_5` | General/photoreal. `marketing_studio_image` adds layout and text treatments we do not want here. |
| quality | `high` | The default is `low`. Low renders at 1024px and looks soft on a sales page. |
| resolution | `2k` | Default is `1k`. 2k gives 2048x1360 at 3:2. |
| aspect_ratio | `3:2` | Works as-is for the checkout image slot and landing page, and crops cleanly to 1:1 for a thumbnail or 4:5 for Instagram. |

Cost: 1 credit for 2 variants at low/1k, 3 credits for 2 variants at high/2k.

## Concept A: single mug

> Editorial food photography still life, warm and calm. A single handmade ceramic mug filled with golden bone broth resting on a pale oatmeal linen cloth, delicate steam rising. Soft diffused natural light from a window on the left, gentle shadows. Warm cream and bone-white palette with a sage green sprig of fresh thyme beside the mug and a small terracotta ramekin softly out of focus behind. Matte ceramic, no glossy highlights, shallow depth of field, generous negative space on the right for text overlay. Nourishing and unhurried, not clinical. No people, no hands, no text, no lettering, no logos, no packaging.

Job IDs: `b3e34bb9-b935-457c-95aa-456adc1d8838`, `030c2eec-b11b-4238-b92e-d4d065d2cc4b`

## Concept B: three mugs (encodes "3-day")

> Editorial food photography still life, warm and calm. Three matching handmade ceramic mugs of golden bone broth arranged in a simple row on a pale oatmeal linen runner, soft steam rising from each. Overhead three-quarter angle. Soft diffused natural window light, gentle shadows. Warm cream and bone-white palette, sage green thyme sprigs scattered between the mugs, one small terracotta dish at the edge of frame. Matte ceramic, shallow depth of field, calm minimal composition with breathing room around the mugs. Nourishing and unhurried, not clinical. No people, no hands, no text, no lettering, no numbers, no logos, no packaging.

Job IDs: `7c052f95-c9e5-4417-88b2-ec9195941448`, `1e8ea361-d9c8-4e8a-bb00-a8c32de905bc`

## Prompt rules for this brand

Include every time:
- "editorial food photography still life, warm and calm"
- Warm cream / bone-white base, sage green accent, terracotta accent (the brand palette)
- Soft diffused natural window light, matte finish, no glossy highlights
- Shallow depth of field
- "Nourishing and unhurried, not clinical"

Always negative-prompt:
- **no people, no hands** (AI hands are unreliable, and a stock-looking stranger undercuts a practitioner brand built on one real person)
- **no text, no lettering, no numbers, no logos** (generated type renders badly and would collide with the real brand mark)
- no packaging (implies a physical product this offer does not ship)

Never generate:
- **Any image of Alina.** Her photo is a real likeness. Use the real file at
  `Documents/Funnel Assets/Alina_Fence.jpg`.
- Anything resembling a client, a testimonial portrait, or a before/after.
- Weight-loss visual tropes: scales, measuring tapes, body comparisons. The offer is framed
  around gut rest and pattern work, not weight, and those visuals invite a claim we do not make.

## Upload path

Kajabi's API cannot accept file uploads. `add_media` only returns an uploader link:
https://app.kajabi.com/admin/sites/2148204891/media_library?open_uploader=image

So the flow is: download from the Higgsfield widget, upload through that link, then the asset can
be placed into theme slots programmatically with `place_media`.
