# $1,497 onboarding: final copy

Three pieces, one sequence. Written 2026-10-22, ready to deploy.

Every word below is final except the three URLs, which are marked
`{{FACEBOOK_GROUP_URL}}`, `{{LAB_PROFILE_URL}}` and, if the consultation moves
off Google Calendar, `{{CONSULT_BOOKING_URL}}`. Those tokens are deliberately
unusable so nothing can ship half-finished.

A fourth step gets inserted everywhere if Alina has an intake form.

---

## Why the same content appears twice

The thank-you page is a tab she can close. The email is the copy she finds
again at 9pm when she finally sits down to do the lab profile. So the email
repeats every link in full and never says "see the page you just left".

## Why the order is what it is

The lab profile is second, not last, because it is the only step with a
delivery dependency hanging off it. No profile means Alina cannot order the
GI-MAP, which means no kit arrives, which means the test she paid for sits
still. It is also the dullest step and the one most likely to be skipped, so
the copy says out loud what it blocks.

The consultation is first because it is the appointment, and because a booked
date gives the other two steps a deadline.

---

# 1. The thank-you page

Landing page `2150005925`, theme `2156349886`.

Replaces the current text block. The Google Calendar scheduler, Alina's photo,
the support line and the confetti all stay.

> ## You're in.
>
> Alina will be working with you for the next three months, and the first
> thing she needs is to meet you properly.
>
> Three things to do now, in this order. Fifteen minutes in total.
>
> ### 1. Book your initial consultation
>
> Sixty minutes, and it is where everything starts. Pick a time below.
>
> [ the existing scheduler sits here ]
>
> ### 2. Set up your lab profile
>
> This is the step that gets your GI-MAP test shipped to you. You will enter
> your name, address and phone number, and Alina is notified the moment it is
> done.
>
> **She cannot order your kit until this profile exists**, so it is worth doing
> today rather than leaving it until the weekend.
>
> → `{{LAB_PROFILE_URL}}`
>
> ### 3. Join the private group
>
> This is where you can ask things between calls, and see what other women in
> the program are working through.
>
> → `{{FACEBOOK_GROUP_URL}}`
>
> ---
>
> All three of these are in your welcome email as well, so you do not need to
> keep this page open.
>
> Anything at all: **support@gohappybelly.com**

---

# 2. The welcome email

Kajabi automation, draft only. Trigger: purchase of offer `2149705539`.
Sent immediately.

**Subject:** You're in. Three things to do this week.

**Preview text:** One of them gets your test in the mail, so it is worth doing
today.

> Hi {{first_name}},
>
> You are in, and I am glad you are here.
>
> For the next three months we are going to work out what is actually driving
> your symptoms rather than guessing at it. Before we start, there are three
> things I need from you. Fifteen minutes in total, and then you are set.
>
> **1. Book your initial consultation**
>
> Sixty minutes, and it is where everything starts. Bring whatever you have
> been tracking, and anything a doctor has already told you.
>
> {{CONSULT_BOOKING_URL}}
>
> **2. Set up your lab profile**
>
> This is the one that gets your GI-MAP test shipped to you. You will enter
> your name, address and phone number, and I am notified the moment it is
> done.
>
> I cannot order your kit until that profile exists, so please do this today
> rather than leaving it until the weekend. It is the step that holds
> everything else up.
>
> {{LAB_PROFILE_URL}}
>
> **3. Join the private group**
>
> Ask things between our calls, and see what other women in the program are
> working through.
>
> {{FACEBOOK_GROUP_URL}}
>
> That is everything for now. Your Gut Reset Course access is already in your
> account, and you are welcome to start reading, though nothing in it needs
> doing before we speak.
>
> If anything here does not work, reply to this email or write to
> support@gohappybelly.com and we will sort it out.
>
> In Gut Health,
> Alina Nazari
> FDN-P

---

# 3. The day-three nudge

Same automation, after a 3-day wait.

There is no way to detect whether she has set up the lab profile, since it
happens on a site outside Kajabi. So this is written to be comfortable to
receive whether she has done it or not. It does not scold and it does not
assume.

**Subject:** The step people forget

> Hi {{first_name}},
>
> Short one.
>
> If your lab profile is already set up, ignore me and I will see you on our
> call.
>
> If it is not, that is the step worth doing today. It is the one that gets
> your GI-MAP kit in the mail, and I cannot order it until the profile exists.
> It takes about five minutes.
>
> {{LAB_PROFILE_URL}}
>
> And if something about it did not work, tell me rather than wrestling with
> it. That happens occasionally and it is quick to fix.
>
> In Gut Health,
> Alina Nazari
> FDN-P

---

## Before any of this is armed

1. **Make a test purchase** and see what Kajabi sends on its own, now that the
   Gut Reset Course is attached to the offer. If it already sends a product
   welcome, fold this content into that rather than stacking a second email on
   a $1,497 buyer.
2. **Resolve the Calendly question.** If the initial consultation stays on the
   existing Google Calendar scheduler, the page keeps its embed and the email
   needs a URL for that scheduler rather than a Calendly link.
3. **Ask about the intake form.** If one exists it becomes step 2, the lab
   profile moves to 3, the group to 4, and "three things" becomes "four
   things" in both subject lines and both openings.

## How it gets built

`create_automation`, trigger `offer purchased` on `2149705539`, then
`email_send`, then a 3-day `wait`, then a second `email_send`. It is created as
a **draft**. Nothing sends until Steve arms it in the Kajabi admin, which keeps
the standing rule about not sending email without explicit confirmation.

---

## Status, 2026-10-22

**The thank-you page is built**, on the website design system, in its interim
form: the consultation step and the scheduler, plus a block saying the welcome
email carries the rest. See `Website/COACHING-THANK-YOU-PAGE.md` for the rebuild
record and the exact four-part swap that turns it into the numbered three-step
page above.

The two emails are not built. They go in as a draft automation once the URLs
land and once a test purchase shows what Kajabi already sends on its own.

## Blocked inputs, as of 2026-10-22

| Input | Status |
|---|---|
| Consultation booking URL | **Resolved.** `https://calendly.com/gohappybelly/60-minute-consultation`, now embedded on the thank-you page |
| Lab profile URL | Waiting on Alina |
| Facebook group URL | Waiting on Alina |
| Intake form before the consult? | Waiting on Alina. If yes, it becomes step 2 and the rest shift down |
