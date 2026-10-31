# Transactional email template rewrites

Drafted 2026-10-31. **For Steve to paste**, at
https://app.kajabi.com/admin/sites/2148204891/email_templates

The agent cannot reach these. Confirmed four ways: no email-template tool in
any of the 19 Kajabi toolsets, two full sweeps of the tool surface,
`get_site_summary` exposes no branding or template fields, and the URL is
behind admin auth so WebFetch cannot read it.

---

## Do this first, before any paste

**Fix the button contrast on the Branding tab.** Every button below renders
in `#9ACEAA` with white text at **1.78:1**, which fails AA at any text size.
Change **Font Color** to forest `#162E28` and it becomes **8.10:1**, keeping
the green. Rewriting the copy while the buttons stay unreadable fixes the
smaller half of the problem.

## Constraints these are written to

- **`<a>` tags only.** The UI states: "Only html &lt;a&gt; tags are allowed.
  Please no images, divs, etc." No sage line, no inline styling.
- **Keep `class="btn btn-primary"`** on each link. That is what renders the
  button; without it you get a bare text link.
- **Only liquid each template exposes**, per its own UI note. Nothing is
  invented here; every variable below already appears in the current
  templates.
- Brand rules: no em dashes, no banned words, locked sign-off, no diagnostic
  or cure language.
- `support@gohappybelly.com` is **hardcoded** rather than written as liquid.
  The current Offer Purchase Confirmation uses a `{{ site.support... }}`
  variable, but the screenshot truncated the field name and guessing it would
  risk a broken mailto. The address is confirmed correct in
  `get_site_summary`.

---

## 1. Member Welcome Email

The account-creation email, and the one the whole funnel depends on. Its job
is one thing: get them a password.

**Subject**

```
Set up your {{site.title}} password
```

*Changed from "Your New {{site.title}} Account". It arrives alongside two
other emails, so a subject naming the action helps it get opened.*

**Content**

```
Hi {{member.name}},

Your account is set up. One thing left, which is choosing a password.

<a href="{{invite_url}}" class="btn btn-primary">Set up password</a>

That takes you straight in. Everything you have access to lives in your library, and it will be waiting there.

If the button does not work, reply to this email and we will get you in.

In Gut Health,
Alina Nazari
FDN-P
```

**Note:** `{{member.name}}` renders the full name ("Hi Jane Doe,"), which is
slightly stiff. Kajabi may also expose `{{member.first_name}}`, which would
read better, but it is not listed in the UI note so it is not used here. Try
it with Send Test Email; if it renders, swap it in.

This template also fires on manual and automation grants, not only purchases,
which is why the copy says "everything you have access to" rather than naming
a product.

---

## 2. Offer Purchase Confirmation

**This one has a live defect.** It currently says:

> You can login with your **email and password** at the link below. [Login]

A first-time buyer has no password yet. The receipt sends them to a login
screen they cannot pass, while the email that actually works arrives
separately and may arrive second.

**Subject**

```
Your purchase is confirmed: {{offer.title}}
```

**Content**

```
Hi {{member.name}},

Thank you. Your purchase of {{offer.title}} is confirmed and your access is ready.

<a href="{{site_login_url}}" class="btn btn-primary">Go to my library</a>

If you already set a password, that link takes you in. If you have not set one yet, look for a separate email titled "Set up your {{site.title}} password" and start there instead.

Questions, or something not working? Email support@gohappybelly.com and a person will answer.

In Gut Health,
Alina Nazari
FDN-P
```

**These two templates are now coupled.** This email names the other one by
its subject line. If you change the Member Welcome Email subject, change the
quoted title here to match, or the instruction points at nothing.

---

## 3. Abandoned Checkout

Currently the only Customized template on the site, and live. Three problems:
a **double space** in the subject ("Looks␣␣Like"), it opens "Hey There!"
which is not Alina's voice, and it signs off in a format that is not the
locked one.

**Important constraint:** this fires for **every** offer, from the $27 to the
$1,497 and the lab tests. The copy has to work at all those prices, so it
stays offer-agnostic and makes no claim about what the product does.

**Subject**

```
Still thinking about {{offer.title}}?
```

**Content**

```
Hi there,

You started checking out for {{offer.title}} and did not finish. No problem, and no pressure. Your checkout is still open if you want it.

<a href="{{offer_checkout_url}}" class="btn btn-primary">Finish checking out</a>

If something stopped you, it is worth telling me. Sometimes it is a card that did not go through. Sometimes it is a real question about whether this is the right fit, and I would rather answer that than have you buy something that is not. Either way, reply to this email or write to support@gohappybelly.com.

In Gut Health,
Alina Nazari
FDN-P
```

**No name is available here.** The liquid for this template is `{{email}}`,
`{{offer}}`, `{{site}}` and `{{offer_checkout_url}}`. There is no `member`
object, so "Hi there," is deliberate, not an oversight.

The invitation to reply is doing real work on a practice like this one: an
abandoned $1,497 checkout is worth a conversation, and the reply tells Alina
why people stall.

---

## After pasting

1. **Send Test Email** on each, and read them on a phone.
2. Check the button is legible, which confirms the Branding fix landed.
3. On Member Welcome Email, check whether `{{member.first_name}}` renders if
   you tried it.
4. Then the test purchase, which shows all three in sequence alongside the
   automation's own welcome email.

## Still to decide after that

The automation's welcome email in `1388764` still contains a "Getting in"
paragraph telling buyers to use the Forgot Password link. Once these are
live, that is the **third** login instruction a buyer receives and it should
come out, leaving that email to lead with "Where to start", the only thing no
system template covers. Not changed yet, deliberately: it should be edited
once, after these land.
