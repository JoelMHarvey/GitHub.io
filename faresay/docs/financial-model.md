# Faresay — Financial Model

> Working draft — structure + **directional ranges** (see `market-research-synthesis.md`). Numbers
> are **starting ranges to validate**, not facts. Modelled in **GBP** (UK home base + expat
> beachhead; many expat hubs are naturally cash-pay). Bootstrapped lens: optimise for
> **contribution-margin-positive growth and CAC payback**, gated by **Stage 0** (§0a).
> Last updated: [PLACEHOLDER: date]

## 0. Benchmark ranges (directional — validate before relying)
| Driver | Starting range | Confidence | Note |
|--------|----------------|-----------|------|
| Session price (P) — UK | ~£40–60 | 🟡 directional | Faresay's actual UK list price (~£40–55) |
| Session price (P) — **expat hub** | ~£90–150 | 🟡 estimate | Internationally mobile professionals, private-pay, less price-sensitive — **[RESEARCH NEEDED per corridor]** |
| Take rate (t) | **15%** (10% founding) | 🟢 fixed | Low vs rivals' 20–30% → volume/retention must carry it |
| Sessions per client (S) | model 6–12 as a band | 🟡 estimate | Drive with retention |
| Blended CAC | **niche-lowered, model ≤ £100** | 🟡 target | Expat communities/referrals/SEO → lower than paid-generalist CAC; Stage 0 caps it at £100 |
| Payment processing | ~2.9% + £0.30 | 🟡 standard | Processor-dependent |
| LTV:CAC target | ≥ 3 | — | Standard bar |
| CAC payback target | **≤ ~4 sessions** | — | Stage 0 gate |

> **Why the expat price point matters financially (not just for marketing):** a 15% take on a **£55**
> UK session nets ~£8.25 (~£6.35 after card processing). At **£120** (expat hub) it nets ~£18
> (~£14.20 after processing) — **more than double the contribution per session**. The niche is what
> makes the unit economics close (see §0a).

## 0a. Stage 0 — the proof-of-concept gate (model this explicitly)
Before any geographic expansion, Faresay must hit (per `business-plan.md` §11):

| Stage 0 target | Value |
|----------------|-------|
| Verified therapists | **25** |
| Paying clients | **100** |
| Blended CAC | **< £100** |
| CAC payback | **within ~4 sessions** |
| Month-2 retention | **> 60%** |

**The honest tension to model:** "CAC < £100" and "payback ≤ ~4 sessions" only **co-hold at a
high-enough price/contribution.** Payback sessions = CAC ÷ contribution-per-session:

| Price (15% take) | Contribution/session (after proc.) | Max CAC for ≤4-session payback | £100 CAC pays back in |
|------------------|-----------------------------------|-------------------------------|------------------------|
| £55 (UK) | ~£6.35 | ~£25 | ~16 sessions ❌ |
| £90 | ~£10.95 | ~£44 | ~9 sessions |
| £120 (expat base) | ~£14.20 | ~£57 | ~7 sessions |
| £150 | ~£17.45 | ~£70 | ~6 sessions |

**Read:** at **UK price points the two Stage-0 targets conflict** (4-session payback implies CAC ≈
£25, not £100). They **reconcile at expat-hub price points** (£90–150) **and/or** higher
sessions-per-client. This is the quantitative case for the expat beachhead: higher contribution per
session **plus** niche-driven lower CAC is what lets the model pay back fast. Stage 0 proves it
empirically on 25 therapists / 100 clients before scaling spend.

## 1. Model philosophy
Cash-pay marketplace. Revenue = **15% of session fees**. Hinges on **(a) liquidity** (bookings per
corridor), **(b) unit economics** (CAC vs LTV), **(c) retention** (sessions per client). Bootstrapped
→ low fixed costs; contribution margin funds growth; **Stage 0 gates expansion.**

## 2. Revenue drivers
| Driver | Symbol | Placeholder | Source |
|--------|--------|-------------|--------|
| Avg session price | P | [ASSUMPTION: £ per session — UK vs expat hub] | benchmark §0 |
| Platform take rate | t | **15%** (10% founding) | fixed (CONTEXT) |
| Revenue per session | P × t | = derived | — |
| Sessions per client (lifetime) | S | [ASSUMPTION: # sessions] | retention |
| Active clients | N | model output | growth model |
| Month-2 retention | r | [ASSUMPTION: % — Stage 0 > 60%] | gate |

**Revenue ≈ N × S × P × t.** Sensitivity highest on **S** (sessions/client), **P** (corridor price),
and **N** (acquisition).

## 3. Unit economics (per client)
| Metric | Formula | Placeholder |
|--------|---------|-------------|
| GMV/client | S × P | derived |
| Net revenue/client | S × P × t | derived |
| **CAC** | blended acquisition £ / new client | [ASSUMPTION — Stage 0 < £100] |
| Payment processing | ~2.9% + £0.30 of each session | processor pricing |
| Contribution/client (LTV) | net rev − processing − support | derived |
| **LTV:CAC** | target ≥ 3:1 | derived |
| **CAC payback** | CAC ÷ contribution-per-session | **target ≤ ~4 sessions** |

> ⚠️ CAC is the make-or-break number (R-17). The **expat niche is the primary CAC lever** (community,
> referral, intent SEO) **and** the price lever (higher corridor price). Both push the model toward
> the Stage-0 bar.

## 4. Cost structure (bootstrapped)
- **Variable:** CAC/marketing, payment processing, telehealth video, licensure-verification per provider.
- **Semi-fixed:** hosting/infra, support, trust & safety.
- **Fixed/step:** compliance **per corridor** (UK now; cross-border legal mapping per expat hub as
  opened — **not** all markets up front; US MSO/friendly-PC machinery only if/when a US phase is
  triggered), insurance (tech/cyber E&O), core team, software.
- **Compliance is a phased step-cost per corridor**, tied to the expat rollout — model it that way.

## 5. Projection structure (in `financial-model.csv`)
- **Granularity:** monthly Stage 0 + Y1; quarterly/annual thereafter.
- **Geography rollout:** UK base → **Stage 0 gate** → first expat corridor(s) → further corridors
  (each gated by per-corridor legal mapping). Not a US-state machine.
- **Build-up:** new clients/month → active clients (retention) → sessions → GMV → net revenue →
  minus variable costs → contribution → minus fixed/compliance → EBITDA/cash → runway.
- **Scenarios:** Conservative / Base (expat hub) / Stretch.
- **Outputs:** monthly cash & runway, **Stage 0 gate check**, break-even, LTV:CAC by cohort.

## 6. Key questions the model answers
1. At what **CAC** and **sessions-per-client** does Faresay clear the **Stage 0** gate per corridor?
2. What **price point** does a corridor need so CAC < £100 pays back in ≤ ~4 sessions?
3. How much **runway** before contribution covers fixed costs?
4. Is **15%** sufficient, or are premium/B2B lines needed for target margins?

## 7. The working calculator (`financial-model.csv`)
A **live scenario calculator** (Google Sheets/Excel) — OUTPUT rows recompute as you edit INPUTS:
1. **Unit-economics calculator** — Base (expat hub) / Conservative / Stretch inputs (price, take,
   sessions/client, CAC, processing, support) → contribution/session, LTV, LTV:CAC, **CAC payback in
   sessions**, max CAC for 3:1.
2. **Stage 0 gate check** — flags whether each scenario clears CAC < £100 **and** ≤4-session payback.
3. **Break-even frontier** — max affordable CAC across price × sessions-per-client (GBP).
4. **Illustrative Stage 0 ramp** — a worked path to **100 paying clients** and the Y1 cash burn.

### The headline finding (the honest one)
At a **£120 expat-hub session and 15% take, Faresay nets ~£18/session (~£14.20 after processing).**
Over **8 sessions** lifetime contribution is **~£104**, so **CAC under ~£35 hits 3:1**, and **CAC
under ~£57 pays back within 4 sessions.** Implications:
- The 15% model is **tight but workable at expat price points** — and **not workable at UK prices via
  paid acquisition** (£55 × 15% needs sub-£25 CAC for a 4-session payback). So: **higher-price
  corridors + low (niche/organic/referral) CAC + retention** is the whole game.
- This is the quantitative case for **the expat beachhead** and the **GTM emphasis on community/
  referral acquisition**, and for keeping **insurance-enablement / higher-take** as a later option.

### Still to tune (with Faresay's own data)
- Replace P (per corridor), S, CAC, fixed-cost and ramp assumptions with **actual UK + first-corridor
  numbers**.
- Reconcile compliance step-costs with **per-corridor** legal mapping (not US-50-state).
- Add cohort-level retention accounting for monthly active-client precision.
