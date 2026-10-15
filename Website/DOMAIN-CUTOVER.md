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
2. **Check the imported records BEFORE touching GoDaddy.** Adding the domain
   creates the zone and auto-imports the current records. Open Kajabi's DNS
   settings and confirm all five MX records and all three TXT records above
   are there. Add any that are missing.

   Doing this before the nameserver change is what removes the risk entirely:
   there is then no window in which mail could resolve to a zone that has no
   MX records.
3. **GoDaddy** → gohappybelly.com → Nameservers → **Change** → *I'll use my own
   nameservers* → paste Kajabi's two, replacing `ns29`/`ns30.domaincontrol.com`.
   Screenshot the DNS record list first.
4. Back in Kajabi, click **Done, verify domain**. Then send yourself an email
   at the domain and reply to it.
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

## What this move does not affect

The quiz funnel does not run through this domain's DNS, so none of it is at
risk:

| Step | Runs on | Affected |
|---|---|---|
| Quiz | `gut-pattern-quiz.scoreapp.com` | no |
| ScoreApp to Mailchimp | API | no |
| The 7 archetype emails | Mailchimp's servers | no |
| Zapier tagging `booked-call` from Calendly | API | no |

The records that change are the apex `A` and the `www` `CNAME`, which only
decide which server answers a browser. Campaign email never consults them.

MX is the one record that matters, and it is a separate concern from the quiz
flow: MX is inbound mail **to** `@gohappybelly.com`, Alina's own inbox. Step 2
above covers it.

## Pre-existing, not caused by the move

The domain has no Mailchimp authentication: no DKIM records (`k1`, `k2`,
`k3._domainkey` and `mandrill._domainkey` are all empty) and the SPF chain
authorises Google only, not Mailchimp. The sequence emails therefore send
unauthenticated for this domain and show as "via mcsv.net" to recipients.

This is already true today and will behave identically after the move. It is
worth fixing for deliverability, along with the missing DMARC record, but as
its own job. Do not bundle either into the cutover.

---

## Outcome (2026-10-15)

The move was done with the nameserver method. Nameservers are now
`jermaine.ns.cloudflare.com` / `joyce.ns.cloudflare.com`.

Verified after the cutover:

| Check | Result |
|---|---|
| `www.gohappybelly.com` | 200, valid SSL |
| `gohappybelly.com` | 301 to `https://www.gohappybelly.com/` |
| Build serving | theme `2156348838`, all 12 new Encore sections |
| `/private-coaching`, `/shop` | 200 |
| MX | all five Google records imported |
| `google-site-verification` TXT | imported |

### One record did not import

The apex SPF record came across, but the subdomain it depends on did not:

```
gohappybelly.com                      TXT  v=spf1 include:dc-aa8e722993._spfm.gohappybelly.com ~all   present
dc-aa8e722993._spfm.gohappybelly.com  TXT  (none)                                                     MISSING
```

SPF therefore pointed at a non-existent domain, which is a permerror on
outbound Google Workspace mail. It was valid before the move, so this was a
regression introduced by Cloudflare's zone import. This is the exact failure
mode the runbook predicted: the record is on a subdomain rather than the apex,
which is why an import drops it.

Fixed by collapsing the chain into a single apex TXT record, which is what it
resolved to anyway:

```
v=spf1 include:_spf.google.com ~all
```

The `_spfm` indirection was a GoDaddy "SPF merge" artifact and had no purpose
once DNS left GoDaddy. Nothing references it now.

**Lesson for any future registrar move on this domain:** check subdomain TXT
records by name after an import. A zone import reliably carries apex records
and MX; it is the records hanging off a subdomain that go missing, and they
fail silently because nothing stops resolving, it just stops validating.

### Still outstanding

- Repoint outbound links: Instagram link in bio, ScoreApp quiz, Mailchimp
  templates and the 35 sequence emails, Calendly, Guthub.
- Add `www.gohappybelly.com` as a Google Search Console property.
- Mailchimp has no DKIM on this domain and the domain has no DMARC record.
  Both predate the move and are unchanged by it. Worth doing for sequence
  deliverability, as their own job.
