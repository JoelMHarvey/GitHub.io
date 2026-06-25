# Faresay — Financial Model

> Working draft — structure + **directional benchmark ranges from research** (see
> `market-research-synthesis.md`). Numbers are **starting ranges to validate**, not facts: the
> research confirmed market *direction* but several specific unit-economics figures were unreliable,
> so tune everything to Faresay's own UK data first. Bootstrapped lens: optimise for
> **contribution-margin-positive growth and CAC payback**, not blitz-scaling.
> Last updated: 26 June 2026

## 0. Benchmark ranges (directional — validate before relying)
| Driver | Starting range | Confidence | Note |
|--------|----------------|-----------|------|
| Cash-pay session price (P) | ~$100–200 | 🟡 directional | Use Faresay's actual UK price + intended US price |
| Take rate (t) | **15%** | 🟢 fixed | Low vs rivals' 20–30% → volume/retention must carry it |
| Sessions per client (S) | model 6–12 as a band | 🟡 estimate | Therapy courses vary widely; drive with retention |
| Blended CAC | **treat as high** | ⚠️ unknown | No hard benchmark; cash-pay is paid-marketing heavy → model conservatively, push organic |
| Payment processing | ~2.9% + fixed | 🟡 standard | Processor-dependent |
| LTV:CAC target | ≥ 3 | — | Standard health-marketplace bar |
| CAC payback target | ≤ a few sessions | — | The make-or-break test in cash-pay |

> **Headline tension to model honestly:** a 15% take on, say, a $150 session = ~$22.50 net revenue
> per session. If CAC is high and sessions/client is modest, payback is slow — so the model's job is
> to find the **CAC × sessions-per-client** combinations where Faresay is contribution-positive, and
> to show how much **organic/referral acquisition** is needed to get there.

## 1. Model philosophy
Cash-pay marketplace. Revenue = **15% of session fees**. The whole model hinges on three driver
families: **(a) liquidity** (bookings per market), **(b) unit economics** (CAC vs LTV), and
**(c) retention** (sessions per client). Bootstrapped → keep fixed costs low and let contribution
margin fund growth.

## 2. Revenue drivers
| Driver | Symbol | Placeholder | Source |
|--------|--------|-------------|--------|
| Avg session price (cash-pay) | P | [ASSUMPTION: $/£ per session] | research benchmark |
| Platform take rate | t | **15%** | fixed (CONTEXT) |
| Revenue per session | P × t | = derived | — |
| Sessions per client (lifetime) | S | [ASSUMPTION: # sessions] | research/retention |
| Active clients | N | model output | growth model |
| Repeat/retention rate | r | [ASSUMPTION: %] | research benchmark |

**Revenue ≈ N × S × P × t.** Sensitivity is highest on S (sessions/client) and N (acquisition).

## 3. Unit economics (per client)
| Metric | Formula | Placeholder |
|--------|---------|-------------|
| Gross marketplace value (GMV)/client | S × P | derived |
| Net revenue/client | S × P × t | derived |
| **CAC** | blended acquisition $ / new client | [ASSUMPTION: $] — research |
| Payment processing | ~[ASSUMPTION: 2.9%+fee] of GMV | processor pricing |
| Contribution/client | net rev − processing − support | derived |
| **LTV** | net revenue/client × margin | derived |
| **LTV:CAC** | target ≥ 3:1 | derived |
| **CAC payback** | CAC / (net rev per session) | target ≤ a few sessions |

> ⚠️ In a cash-pay model CAC is the make-or-break number (R-17). If a client does, say,
> [ASSUMPTION: S] sessions at [ASSUMPTION: P] with a 15% take, net revenue/client is small — so
> **either CAC must be low (organic/referral) or sessions-per-client must be high**. The research
> step quantifies realistic ranges; this model then shows the break-even frontier.

## 4. Cost structure (bootstrapped)
- **Variable:** CAC/marketing, payment processing, telehealth video per-minute (if usage-priced),
  licensure-verification per provider.
- **Semi-fixed:** hosting/infra, support, trust & safety.
- **Fixed/step:** compliance (entity + per-state qualification + registered agents — phased),
  insurance (tech/cyber E&O), core team, software.
- **Compliance is a step-cost** as states are added — model it per-state-cluster (ties to legal
  roadmap), not all-50 up front.

## 5. Projection structure (to build in `financial-model.csv`)
- **Granularity:** monthly for Y1–Y2, quarterly/annual Y3.
- **Geography rollout:** UK base → US state clusters phased in (gated by legal qualification).
- **Build-up:** new clients/month → active clients (with retention) → sessions → GMV → net revenue
  → minus variable costs → contribution → minus fixed/compliance → EBITDA/cash → running runway.
- **Scenarios:** Conservative / Base / Stretch (vary CAC, sessions/client, growth).
- **Outputs:** monthly cash & runway, break-even point, LTV:CAC by cohort, contribution margin.

## 6. Key questions the model answers
1. At what **CAC** and **sessions-per-client** does Faresay break even per client?
2. How much **runway** does a bootstrapped rollout need before contribution covers fixed costs?
3. What **state-rollout pace** is affordable given per-state compliance step-costs?
4. Is **15%** sufficient, or are premium/B2B revenue lines needed to hit target margins?

## 7. The working calculator (`financial-model.csv`)
`financial-model.csv` is now a **live scenario calculator** — open it in Google Sheets or Excel and
the OUTPUT rows recompute as you edit the INPUTS. Three blocks:
1. **Unit-economics calculator** — edit Base/Conservative/Stretch inputs (price, take, sessions/
   client, CAC, processing, support); it computes contribution/session, LTV, LTV:CAC, CAC payback,
   and the max affordable CAC for a 3:1 ratio.
2. **Break-even frontier** — max affordable CAC across price × sessions-per-client.
3. **Illustrative 12-month ramp** — a worked Base build showing the path and Y1 cash burn (~$103k).

### The headline finding (the honest one)
At a **$130 cash-pay session and a 15% take, Faresay nets ~$19.50/session, ~$15.40 after card
processing.** So over **8 sessions** the lifetime contribution is only **~$113** — meaning to hit a
healthy **3:1 LTV:CAC the CAC must stay under ~$38**. Implications:
- **The 15% cash-pay model is economically tight.** It works only with **low CAC** (organic, SEO,
  referrals, therapist-invited clients) **or materially more sessions per client** (retention) **or
  a higher price point**. Paid-acquisition-led growth at typical mental-health CACs will not pay back.
- This is the quantitative case for the GTM emphasis on **retention + organic acquisition**, and a
  data point for the **insurance-enablement / higher-take** option flagged in the business plan §5.

### Still to tune (with Faresay's own data)
- Replace P, S, CAC, fixed-cost, and ramp assumptions with Faresay's **actual UK numbers**.
- Reconcile the fixed/compliance step-costs with the legal roadmap's phased state plan.
- Add cohort-level retention accounting if you want monthly active-client precision.
