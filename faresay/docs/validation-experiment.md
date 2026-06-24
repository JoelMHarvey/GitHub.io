# Faresay — Validation Experiment (do this BEFORE building anything else)

> Why this doc exists: a six-perspective review (investor, VC, lawyer, competitor, critic, operator)
> independently reached the same conclusion — **the whole company rests on one unvalidated number,
> and you can test it this week for under £200.** Don't seed therapists, build features, or pay for
> per-corridor legal until this passes. Last updated: [PLACEHOLDER: date]

---

## The one assumption that decides everything
**That English-speaking expats will (a) pay ~£120/session and (b) be acquirable at a CAC under ~£57
through organic/community/referral.** Everything downstream (the 15% model, Stage 0, the expat pivot)
is a hypothesis stacked on this. It currently has **zero sourced data** (`market-research-synthesis.md`
§2.5; `financial-model.md` §0). If real willingness-to-pay clears at £70–80, or CAC lands at £150
(normal for cash-pay mental health), the model is underwater — and no amount of building fixes it.

## Test design — a concierge / fake-door, not a product
**Build nothing. No platform. No panel.** Stand up the smallest thing that produces real buying signal.

1. **One landing page** for the legally-cleanest corridor (see `cross-border-legal-gate.md` — *not*
   necessarily Tokyo). Real positioning, **real £120 price shown**, real CTA: "Book a free 15-min
   consult." [PLACEHOLDER: corridor + domain/subdomain.]
2. **CTA → a Calendly the founder personally answers.** You are the concierge: you do the consult,
   you hand-match to 1–3 real therapists you've lined up informally, you take the first payment
   manually (Stripe payment link). No code.
3. **Drive traffic two ways, instrumented separately** (so you can read each channel's true cost):
   - **Organic:** genuine posts/answers in 3–5 corridor expat communities + one founder LinkedIn post.
     Cost = time. (Heed the anti-self-promo reality — `gtm-strategy.md`: ask admins, add value, don't spam.)
   - **Paid:** **£150 of Google Ads** on exact high-intent terms ("English speaking therapist <city>").
     Measure cost-per-booked-consult directly.

## What to measure (the funnel tracker)
| Stage | Organic | Paid | Notes |
|-------|---------|------|-------|
| Spend (£ / hours) | | | keep separate per channel |
| Landing-page visitors | | | from analytics |
| Enquiries / consult bookings | | | the real signal |
| Consults held | | | founder-run |
| **Paid first sessions @ £120** | | | the only number that matters |
| **Second sessions booked** | | | early retention proxy |
| Cost per booked consult | | | paid CAC read |
| Cost per paying client | | | the headline |

> A landing page that converts visitors→enquiry at **2–4%** is strong for cash-pay therapy. Below ~1%
> the offer/trust/price is wrong, not the channel.

## Decision rules (set before you start — no moving the goalposts)
- **KILL the thesis** if, after ~3 weeks: **fewer than ~10 booked consults organically** → the cheap,
  high-trust acquisition engine the whole plan assumes **does not exist.** Stop, save 12 months.
- **PAID won't pay back** if cost-per-booked-consult is already **> £57 before** the consult→paid
  drop-off → paid can't carry it; you need organic to work or you stop.
- **PRICE is dead** if consults book but **nobody pays £120** after the free call → the £120
  assumption (the load-bearing wall of `financial-model.md`) is false.
- **PASS** = a handful of real people **pay £120 and book a second session** from acquisition that
  projects to a blended CAC under ~£57. Only then is seeding supply + clearing corridor legal worth spend.

## Landing-page copy skeleton (starting point)
- **Headline:** Therapy that understands international life.
- **Sub:** English-speaking, verified therapists for [expats in <city>]. Book a free 15-minute consult.
- **Trust line:** Every therapist is licensed, identity-verified and personally interviewed by our founder.
- **Price (shown):** £120 / 50-min session · money-back first session · cancel free 24h ahead.
- **Founder line + photo:** "I'm [name], an expat myself. I personally vet every therapist. Here's my email."
- **CTA:** Book your free consult → [Calendly].

## What this deliberately does NOT do
No platform build, no 25-therapist panel, no per-corridor legal spend, no paid scaling, no second
corridor. Those all come *after* a pass. The point is to risk **£200 and two weeks**, not six months.

## If it passes — the next three moves (in order)
1. **Cross-border legal memo** for that corridor (`cross-border-legal-gate.md`) before any supply spend.
2. **Seed 5–6 founding therapists** who bring a client book; concentrate demand on them (`gtm-strategy.md`).
3. Run the **30-day operator plan** (`gtm-strategy.md` §8) on the proven funnel.

## Linked documents
- `financial-model.md` (the £120 / CAC math this tests) · `gtm-strategy.md` (the funnel + 30-day plan)
- `cross-border-legal-gate.md` (corridor choice) · `market-research-synthesis.md` (the unsourced gaps)
