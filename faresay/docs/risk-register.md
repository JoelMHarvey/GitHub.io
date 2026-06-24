# Faresay — Risk Register

> Working draft. Consistent with `CONTEXT.md`. Living document — review at least quarterly and on
> any material change. Scoring: Likelihood (L) and Impact (I) each 1–5; Rating = L×I
> (1–8 Low · 9–14 Medium · 15–25 High). Owners are roles, not named individuals yet.
> Last updated: [PLACEHOLDER: date]

## How to use
Each risk has an ID, category, description, L, I, Rating, mitigation(s), and owner. Re-score after
mitigations land (residual risk). ⚠️ flags cross-link to the policy/skill that addresses it.

---

## A. Regulatory & legal
| ID | Risk | L | I | Rating | Mitigation | Owner |
|----|------|---|---|--------|-----------|-------|
| R-01 | **Fee-splitting / CPOM:** the 15% is recharacterised as an unlawful split of clinical fees in some US states | 4 | 5 | **20 High** | Frame 15% as technology/marketing platform fee; MSO/friendly-PC where required; per-state counsel sign-off (see legal skill) ⚠️ COUNSEL | Founder/Legal |
| R-02 | **Operating without authority** in a US state (entity not qualified / not registered) | 3 | 5 | **15 High** | State-by-state qualification + registered agent before enabling bookings; state on/off switches gated by legal status | Legal/Ops |
| R-03 | **Clinician licensure gap** — client served by therapist not licensed in client's state | 3 | 5 | **15 High** | Hard product rule: licensure-by-client-location; compact handling; ongoing licence monitoring | Product/Clinical |
| R-04 | **Telehealth consent / modality** non-compliance per state | 3 | 4 | 12 Med | Per-state informed consent capture; counsel review ⚠️ COUNSEL | Legal/Product |
| R-05 | **Healthcare advertising** rules breached (claims, testimonials) | 2 | 3 | 6 Low | Marketing/legal review of claims; review controls | Marketing/Legal |
| R-06 | **Regulatory change** (telehealth policy, state laws) outpaces compliance | 3 | 3 | 9 Med | Monitoring cadence; counsel relationship; agile state controls | Legal |

## B. Clinical & safety
| ID | Risk | L | I | Rating | Mitigation | Owner |
|----|------|---|---|--------|-----------|-------|
| R-07 | **Client harm / crisis** (suicide, self-harm) where platform/therapist response is inadequate | 2 | 5 | **15 High** | Crisis & Safeguarding Policy; screening/exclusion; persistent signposting (988/999); therapist training ⚠️ CLINICAL | Clinical Lead |
| R-08 | **Unsuitable presentation** taken on by cash-pay telehealth (high-acuity) | 3 | 4 | 12 Med | Defined exclusion criteria & triage at intake (clinical governance) ⚠️ CLINICAL | Clinical Lead |
| R-09 | **Poor quality of care** / practitioner competence issues | 2 | 4 | 8 Low | Credentialing, scope-of-practice limits, outcome monitoring, complaints route | Clinical Lead |
| R-10 | **Duty-to-warn / mandatory reporting** mishandled (state-variable) | 2 | 5 | **10 Med** | Per-state matrix of triggers/recipients/timeframes; therapist training ⚠️ COUNSEL/CLINICAL | Clinical/Legal |
| R-11 | **Safeguarding** of minors/vulnerable adults fails | 2 | 5 | 10 Med | Safeguarding leads, reporting workflow, adults-only scope decision ⚠️ | Clinical Lead |

## C. Data, privacy & security
| ID | Risk | L | I | Rating | Mitigation | Owner |
|----|------|---|---|--------|-----------|-------|
| R-12 | **Data breach** of special-category/PHI mental-health data | 3 | 5 | **15 High** | Security & DP Policy; encryption, RBAC, MFA, logging; pen testing; incident response | Security Lead/DPO |
| R-13 | **No BAA / sub-processor gap** — PHI flows to a vendor without a BAA | 3 | 4 | 12 Med | BAA inventory; block PHI to non-BAA vendors ⚠️ COUNSEL/SECURITY | Security/Legal |
| R-14 | **Unlawful international transfer** (UK/EU → US) | 3 | 3 | 9 Med | SCCs/UK IDTA; transfer risk assessment; residency controls ⚠️ COUNSEL | DPO/Legal |
| R-15 | **Trackers/analytics** on a health site trigger HIPAA/MHMDA exposure | 3 | 4 | 12 Med | No health-data trackers; consent management; privacy review ⚠️ COUNSEL | Product/DPO |
| R-16 | **Breach-notification** timelines missed (ICO 72h / HIPAA / state AG) | 2 | 4 | 8 Low | Incident-response runbook with jurisdiction matrix | Security Lead/DPO |

## D. Financial & commercial
| ID | Risk | L | I | Rating | Mitigation | Owner |
|----|------|---|---|--------|-----------|-------|
| R-17 | **CAC exceeds LTV** — cash-pay acquisition uneconomic | 4 | 4 | **16 High** | Track CAC payback; lean spend; retention/sessions-per-client focus; organic channels (financial model) | Founder/Growth |
| R-18 | **Take-rate pressure** — 15% too low to cover costs, or undercut by rivals | 3 | 3 | 9 Med | Validate vs benchmarks; premium/B2B revenue options; cost discipline | Founder |
| R-19 | **Compliance cost overrun** (50-state legal/registration) as bootstrapped | 4 | 3 | 12 Med | Phase states; fixed-fee scoping; bundled registered-agent; approval gate on spend | Founder/Legal |
| R-20 | **Payment failures / chargebacks / fraud** | 2 | 3 | 6 Low | Reputable processor; fraud controls; clear refund/no-show terms | Ops/Finance |
| R-21 | **Runway risk** (bootstrapped) | 3 | 4 | 12 Med | Tight burn; contribution-margin-positive growth; milestone gating | Founder |

## E. Market & operational
| ID | Risk | L | I | Rating | Mitigation | Owner |
|----|------|---|---|--------|-----------|-------|
| R-22 | **Two-sided cold-start** — can't balance supply & demand in a market | 4 | 4 | **16 High** | Seed supply first per market; narrow launch geography; tight liquidity loops | Founder/Growth |
| R-23 | **Incumbent competition** (BetterHelp, Talkspace, Headway et al.) | 4 | 3 | 12 Med | Differentiation (fit, trust, therapist economics); niche/geographic focus | Founder |
| R-24 | **Therapist churn / disintermediation** (clients & therapists go off-platform) | 3 | 3 | 9 Med | Non-circumvention terms; ongoing platform value (payments, admin, leads) | Product/Ops |
| R-25 | **Key-person / capacity** risk (lean bootstrapped team) | 3 | 3 | 9 Med | Documentation; prioritisation; selective outsourcing | Founder |
| R-26 | **Vendor dependency** (video, payments, hosting outage) | 2 | 3 | 6 Low | Reputable vendors; monitoring; contingency options | Engineering |

## F. Reputational
| ID | Risk | L | I | Rating | Mitigation | Owner |
|----|------|---|---|--------|-----------|-------|
| R-27 | **Safety incident or breach → trust collapse** in a trust-dependent category | 2 | 5 | 10 Med | Strong safety/privacy posture; transparent comms; incident playbook | Founder/Comms |
| R-28 | **Negative reviews / poor matches** erode brand | 3 | 3 | 9 Med | Quality matching, feedback loops, responsive support | Product/Support |

---

### Top risks to watch (rating ≥ 15)
- **R-01** fee-splitting/CPOM · **R-17** CAC>LTV · **R-22** cold-start · **R-16/R-12** data breach ·
  **R-02** operating authority · **R-03** licensure gap · **R-07** client crisis.
These map directly to the legal skill (R-01/02/03), the security & crisis policies (R-12/R-07), and
the financial model / GTM sections of the business plan (R-17/R-22). Re-score quarterly.
