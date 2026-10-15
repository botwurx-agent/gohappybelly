# Moving gohappybelly.com from Netlify to Kajabi

Written 2026-10-15. All DNS values below were read live from the domain on
that date, not copied from memory.

## Current state

| Thing | Value |
|---|---|
| Registrar / DNS host | **GoDaddy** (`ns29.domaincontrol.com`, `ns30.domaincontrol.com`) |
| Apex `gohappybelly.com` | A record to `75.2.60.5` (Netlify's load balancer) |
| `www.gohappybelly.com` | CNAME to `gohappybelly-site.netlify.app` |
| Today's canonical | the **bare** domain; `www` 301s to it |
| Email | **Google Workspace** (`aspmx.l.google.com` + 4 alts) |
| Live site size | a single page, one path `/` |

Records that must survive the move untouched:

| Type | Host | Value |
|---|---|---|
| MX | `@` | `aspmx.l.google.com` (1), `alt1`/`alt2` (5), `alt3`/`alt4` (10) |
| TXT | `@` | `google-site-verification=ocHgbPBQ9mMRTIGcUmXvAh64z7w7p4RMWXJsgT701qk` |
| TXT | `@` | `v=spf1 include:dc-aa8e722993._spfm.gohappybelly.com ~all` |
| TXT | `dc-aa8e722993._spfm` | `v=spf1 include:_spf.google.com ~all` |

Only two records change: the apex `A` and the `www` `CNAME`.

## Which method, and why

Kajabi offers two. They are not equivalent for this domain.

**Nameserver method** hands all of DNS to Kajabi (which runs on Cloudflare).
Kajabi's own documentation warns that changing nameservers can break email on
Google Workspace, and every MX and TXT record above would have to be
re-created correctly inside Kajabi's DNS panel. That is a live-email risk taken
for no gain.

**CNAME method** leaves DNS at GoDaddy. Email is never touched because the MX
records never move. This is the method to use.

The one thing the CNAME method cannot do is serve the bare domain, because
Kajabi cannot verify a root domain by CNAME. That is solved with a GoDaddy
forwarding rule from the apex to `www`.

This does flip the canonical hostname from `gohappybelly.com` to
`www.gohappybelly.com`. Worth knowing, but it is not a reason to prefer the
nameserver route: connecting a root domain through Kajabi's nameservers also
creates a `www` version and redirects the root to it. Both routes end at `www`,
so take the one that cannot break email.

## Phase 0 — do not start until these are true

1. **The Kajabi homepage setting is fixed.** Settings → Site Details →
   Homepage is still set to "Show a Landing Page", so the site root serves the
   2024 landing page. It has to be "Show the Template Home Page" or the domain
   will land on the old design.
2. **The pages exist.** Home, Private Coaching and Shop are rebuilt. Anything
   else in the Kajabi nav still points at 2024 pages.
3. **Netlify stays deployed.** Do not delete the Netlify site. It is the
   rollback, and it costs nothing to leave running once DNS no longer points
   at it.

## Phase 1 — lower the TTL (do this a day ahead)

In GoDaddy DNS, set the TTL on the apex `A` record and the `www` `CNAME` to
**600 seconds**. Leave it 24 hours before Phase 2.

This is the step that makes a rollback take minutes instead of a day. Skipping
it is the single most common way a cutover becomes an outage.

## Phase 2 — get the target value from Kajabi

1. Kajabi → **Settings** → **Site settings** → **Domain** → **Set up custom
   domain**.
2. Choose **Create subdomain for Kajabi site** (the CNAME option), not
   "Connect domain to Kajabi".
3. Enter `www.gohappybelly.com`.
4. Copy the **Host** and **Target/Value** exactly as Kajabi displays them.

The target is account-specific. Do not use a value from a blog post or an
older help article, and do not use a `mailgun.org` target, which belongs to
Kajabi's email sending setup, not to connecting a website.

Note: a Kajabi site can only have one custom domain connected at a time.

## Phase 3 — change the two records at GoDaddy

GoDaddy → My Products → Domains → gohappybelly.com → **DNS**.

Before editing, screenshot the whole record list.

1. **Edit** the existing `www` CNAME. Change its value from
   `gohappybelly-site.netlify.app` to the target Kajabi gave you. Edit it;
   do not add a second `www` record.
2. **Delete** the apex `A` record pointing to `75.2.60.5`.
3. Leave every MX and TXT record exactly as it is.

## Phase 4 — point the bare domain at www

GoDaddy → the domain → **Domain Settings** → **Forwarding** → Add.

- Forward to: `https://www.gohappybelly.com`
- Type: **Permanent (301)**
- Masking: **off** (masking hides the real URL and wrecks SEO and analytics)

GoDaddy creates its own apex A record for this automatically, which is why the
Netlify A record has to be gone first. A leftover A record silently beats the
forwarding rule.

## Phase 5 — verify

1. Back in Kajabi, click **Done**, then **verify domain**.
2. Kajabi issues SSL through Cloudflare automatically. Allow up to 24 hours,
   though it is usually much faster. Kajabi waits about an hour before it
   flags a CNAME as failed, so an early error is not necessarily real.
3. Then check, in this order:
   - `https://www.gohappybelly.com` serves the new Kajabi home page
   - the padlock is valid, with no certificate warning
   - `https://gohappybelly.com` 301s to the `www` address
   - `/private-coaching` and `/shop` load
   - **send yourself an email at the domain and reply to it** — this is the
     check people skip

## Phase 6 — after it is live

- Repoint every outbound link: Instagram link in bio, the ScoreApp quiz,
  Mailchimp templates and the 35 sequence emails, Calendly, Guthub.
- Google Search Console: add `www.gohappybelly.com` as a property. The old
  bare-domain property keeps working through the 301 but stops collecting.
- Keep Netlify deployed for about 30 days.

## Rollback

If the Kajabi site is wrong and it has to go back:

1. Delete the GoDaddy forwarding rule.
2. Recreate the apex `A` record to `75.2.60.5`.
3. Point the `www` CNAME back to `gohappybelly-site.netlify.app`.

With TTL at 600 this takes effect in about ten minutes. Email is unaffected
throughout, because no MX record was ever touched.

## Aside, unrelated to the cutover

The domain has no DMARC record (`_dmarc.gohappybelly.com` is empty). SPF is
present and correct. Adding DMARC would help deliverability on the Mailchimp
sequences, but it is a separate job and should not be bundled into this change.
