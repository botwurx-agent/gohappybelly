# Moving gohappybelly.com back to Kajabi

Written 2026-10-15. DNS values read live from the domain that day.

This domain was on Kajabi before (apex and www both worked), then moved to
SamCart, then to Netlify. Going back is the same move that worked the first
time: point the nameservers at Kajabi.

## The method

**Use the nameserver method.** Kajabi calls it "Connect domain to Kajabi". It
is the only method that serves a root domain, because Kajabi cannot verify a
root domain by CNAME. Kajabi takes over DNS (it runs on Cloudflare), serves
`www`, and redirects the bare domain to it. That is the setup that worked here
previously.

The CNAME method exists for people who cannot move nameservers. It only
connects a subdomain and leaves the apex needing a registrar forwarding rule.
Not needed here.

## Current state

| Thing | Value |
|---|---|
| Registrar / DNS host | GoDaddy (`ns29.domaincontrol.com`, `ns30.domaincontrol.com`) |
| Apex | A record to `75.2.60.5` (Netlify) |
| `www` | CNAME to `gohappybelly-site.netlify.app` |
| Email | Google Workspace |
| Live Netlify site | a single page, one path `/` |

## The records that have to survive

Pointing nameservers at Kajabi moves DNS hosting. Kajabi's Cloudflare scans
the existing zone and imports what it finds, but the import is not guaranteed
to be complete, so these get checked afterwards. This is the only part of the
job that needs attention:

| Type | Host | Value |
|---|---|---|
| MX | `@` | `aspmx.l.google.com` (1) |
| MX | `@` | `alt1.aspmx.l.google.com` (5), `alt2.aspmx.l.google.com` (5) |
| MX | `@` | `alt3.aspmx.l.google.com` (10), `alt4.aspmx.l.google.com` (10) |
| TXT | `@` | `google-site-verification=ocHgbPBQ9mMRTIGcUmXvAh64z7w7p4RMWXJsgT701qk` |
| TXT | `@` | `v=spf1 include:dc-aa8e722993._spfm.gohappybelly.com ~all` |
| TXT | `dc-aa8e722993._spfm` | `v=spf1 include:_spf.google.com ~all` |

That second SPF record is a GoDaddy "SPF merge" subdomain. It is easy to miss
on an import because it is not on the apex, and without it the apex SPF record
points at nothing.

## Steps

1. **Kajabi** → Settings → Site settings → Domain → **Set up custom domain** →
   **Connect domain to Kajabi**. Enter `gohappybelly.com`. Kajabi shows two
   nameservers, unique to this domain.
2. **GoDaddy** → gohappybelly.com → Nameservers → **Change** → *I'll use my own
   nameservers* → paste Kajabi's two, replacing `ns29`/`ns30.domaincontrol.com`.
   Screenshot the DNS record list first.
3. Back in Kajabi, click **Done, verify domain**.
4. **Check the email records imported.** In Kajabi's DNS settings, confirm all
   five MX records and all three TXT records above are present. Add any that
   are missing. Then send yourself an email at the domain and reply to it.
5. Wait for SSL. Kajabi issues it through Cloudflare automatically. Most
   connections finish within 24 hours; DNS can take up to 48.

Then check: `gohappybelly.com` and `www.gohappybelly.com` both load the Kajabi
site, the padlock is valid, and `/private-coaching` and `/shop` work.

## One thing to fix before pointing the domain

Settings → Site Details → **Homepage** is still set to "Show a Landing Page",
so the Kajabi site root serves the 2024 landing page. Set it to **"Show the
Template Home Page"** first, or the domain will land on the old design.

## After it is live

- Repoint outbound links: Instagram link in bio, the ScoreApp quiz, Mailchimp
  templates and sequence emails, Calendly, Guthub.
- Google Search Console: the site will canonicalise to `www`, so add that
  property.
- Leave the Netlify site deployed for a few weeks as a fallback.

## Rollback

Set the nameservers at GoDaddy back to `ns29.domaincontrol.com` and
`ns30.domaincontrol.com`. GoDaddy keeps the old zone, so the Netlify records
come back with it. Allow a few hours for nameserver changes to propagate,
which is slower than a record-level rollback.

## Aside

The domain has no DMARC record. SPF is fine. Adding DMARC would help
deliverability on the Mailchimp sequences, but it is a separate job.
