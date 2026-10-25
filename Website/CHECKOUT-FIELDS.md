# Checkout form fields

Steve asked to confirm every checkout requires first name, last name, address
and email.

## The agent cannot read or set these

Checkout fields live in each offer's **Checkout** settings in the Kajabi admin.
They are not exposed through MCP:

- `get_offer` returns pricing, products, post-purchase and the theme id. No field data.
- `update_offer` has no parameter for fields.
- The Forms API covers **opt-in forms only**. The site has seven forms, all
  opt-ins: Default, Home Page Optin, Contact Form Opt In, two webinar forms,
  101 Foods, 7-Day Workbook. No checkout form appears among them.

The only route MCP offers is the admin deep link it returns on every offer,
labelled "Customize the checkout page appearance, form fields, and branding".
Those sixteen links are below.

## Two things to decide before doing it sixteen times

### 1. Kajabi's checkout collects one Name field, not two

Kajabi's checkout has historically used a single **Name** field rather than
separate First and Last. If that is still true, "first name and last name" may
not be available as two required fields, and the answer is one Name field.

This is not cosmetic. It is the same problem already flagged for the workbook
Zapier job in `Website/WORKBOOK-LEAD-MAGNET.md`: Mailchimp wants `FNAME`, and a
single `name` value has to be split before it gets there. If checkout feeds
Mailchimp the same way, the same split is needed, and personalised emails
addressed to "Sarah Mitchell" instead of "Sarah" is how it shows up.

**Worth checking on one offer first** before repeating the change fifteen times.

### 2. Requiring an address on digital products costs conversions

Eight of the sixteen offers deliver nothing physical:

| Offer | Price | Delivers |
|---|---|---|
| Gut Foundations | $27 | Instant course access |
| Gut Reset Course | $147 | Instant course access |
| The Gut Fix | $10 | Instant download |
| E-Book | $9.97 | Instant download |
| Essentials Club | $9.97/mo | Email content |
| Group Coaching | $29.97 | Zoom calls |
| Members | free | Access group |
| 3-Month Gut Reset | $1,497 | Calls and course access |

Asking for a home address to buy a $10 ebook adds a step with nothing behind it.
On the cheap front-end offers, where the whole point is a low-friction first
purchase, that is the worst place to add friction.

The eight lab tests are the opposite case, and even there it is worth checking:
their checkout copy says "You will receive all necessary info via email once your
order is completed", and the buyer gives name, address and phone again on the
third-party lab portal. So Kajabi may not need the address at all.

**If the reason is sales tax or VAT rather than shipping**, that changes the
answer and the address belongs everywhere. Worth naming the reason before
choosing.

## The sixteen checkout settings links

| Offer | Price | Checkout settings |
|---|---|---|
| Gut Foundations | $27 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2151464245&resource_type=Offer&view=checkout |
| The Gut Fix | $10 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2151452007&resource_type=Offer&view=checkout |
| E-Book | $9.97 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149818047&resource_type=Offer&view=checkout |
| Essentials Club | $9.97/mo | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149750878&resource_type=Offer&view=checkout |
| Group Coaching | $29.97 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149816026&resource_type=Offer&view=checkout |
| Gut Reset Course | $147 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149370663&resource_type=Offer&view=checkout |
| 3-Month Gut Reset | $1,497 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149705539&resource_type=Offer&view=checkout |
| Members | free | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149742206&resource_type=Offer&view=checkout |
| H. Pylori | $250 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149722778&resource_type=Offer&view=checkout |
| Heavy Metal | $250 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149746783&resource_type=Offer&view=checkout |
| SIBO Breath | $425 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149722775&resource_type=Offer&view=checkout |
| Blood Chemistry | $450 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149722784&resource_type=Offer&view=checkout |
| GI-MAP Stool | $497 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149722769&resource_type=Offer&view=checkout |
| Organic Acids (OAT) | $497 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149722771&resource_type=Offer&view=checkout |
| DUTCH Hormone | $497 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149722777&resource_type=Offer&view=checkout |
| Food Sensitivity | $639 | https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149722672&resource_type=Offer&view=checkout |

Tell the agent what one checkout looks like once it is set the way you want, and
it will be recorded here as the standard so every future offer matches.
