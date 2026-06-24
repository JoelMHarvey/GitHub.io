# Faresay — Business Plan

> Internal operating plan (bootstrapped). Therapy marketplace, UK today → US (all 50 states),
> cash-pay / out-of-network, **15% platform fee**. Market figures are research-grounded but
> **directional** — see `market-research-synthesis.md` for confidence tags and sources; refresh
> hard numbers from primary sources before any external/investor use.
> Last updated: [PLACEHOLDER: date]

---

## 1. Executive summary
Faresay is a two-sided marketplace connecting people seeking therapy with vetted, licensed
mental-health professionals. It operates in the UK today and plans a phased expansion into the
United States, state by state, ultimately covering all 50 states + DC. Clients pay out of pocket
(cash-pay / out-of-network); Faresay earns a **15% platform fee**, characterised as a
technology + marketing platform fee rather than a split of the clinician's professional fee.

The US mental-health market is large (total treatment market **~$118B in 2025, ~$159B by 2030**)
and tele-mental-health is among the fastest-growing segments. Crucially, the market is
**demand-constrained, not supply-constrained** — the scarce, expensive side is *clients*, not
therapists. Faresay's strategy is therefore to (a) seed therapist supply cheaply per market,
(b) win on **fit, trust, and therapist-friendly economics** (a low 15% take vs. 20–30% at
insurance-enablement rivals), and (c) grow capital-efficiently to contribution-margin-positive
unit economics before scaling state coverage.

This is a **bootstrapped** plan: success is defined by **CAC payback and contribution margin**,
not by raising and burning. The single biggest external dependency is **US healthcare-regulatory
structuring** (CPOM / fee-splitting → MSO/friendly-PC), which is being progressed in parallel
(see `.claude/skills/faresay-legal-authority/`).

## 2. Company & product
- **What it is:** a marketplace — discovery, matching, scheduling, secure telehealth video,
  payments — between independent licensed therapists and self-pay clients.
- **What it is not:** not a healthcare provider itself; not a crisis service; no insurance billing
  (initially); no prescribing.
- **Today:** UK (clinicians registered with bodies such as BACP/HCPC/UKCP).
- **Product detail:** see `product-requirements-document.md`. **One-page model:**
  `business-model-canvas.md`.

## 3. Market opportunity
*(Directional — see synthesis for confidence. Use ranges, not point values, externally.)*
- **TAM:** US total mental-health treatment market **~$118B (2025) → ~$159B (2030)**, ~6.9% CAGR.
- **Growth vector:** tele-mental-health is among the fastest-growing telehealth segments
  (telepsychiatry ~18% CAGR range to 2030); demand structurally elevated post-2021.
- **SAM (Faresay):** US adults willing to **pay out of pocket** for telehealth therapy — a real but
  **smaller, more price-sensitive** slice than the insurance-covered majority (see §5).
- **SOM (initial):** clients in the first launch state-cluster who can be acquired at a CAC that
  pays back within an acceptable number of sessions. Quantified in `financial-model.md`.
- **Demand-constrained market:** the binding constraint for scaling players is **filling client
  demand**, not recruiting therapists — this shapes the entire GTM (§7).

## 4. Competitive landscape
Three distinct US models:

| Model | Players | How they earn | Note for Faresay |
|-------|---------|---------------|------------------|
| **Cash-pay / D2C** *(Faresay's lane)* | BetterHelp, Talkspace | Subscriptions / per-session, paid-marketing heavy | High CAC; **Talkspace is pivoting toward insurance** (a tell) |
| **Insurance-enablement marketplace** | Headway (~$2.3B val), Alma ($130M Series D), Grow Therapy | Take-rate on insurance reimbursement; credentialing/billing is the wedge | The current growth story; ~20–30% take; **bigger, stickier pool** |
| **Employer / EAP** | Lyra (~$4.6B), Spring Health | Sell to employers | Future B2B option, not initial comp |

**Where Faresay fits:** a cash-pay marketplace differentiated by **better-fit matching, a
trust-first experience, and clinician-friendly economics** (15% vs. 20–30%). The low take rate is a
**supply-acquisition weapon** but compresses margin — so retention and sessions-per-client must
carry the model.

## 5. Strategic thesis — the critical model call
**Honest framing:** the weight of market evidence (Headway/Alma growth, insurer venture money,
Talkspace's pivot) shows US therapy demand **concentrating where insurance is accepted** — clients
want to use benefits, and the **credentialing/billing burden is the wedge** that insurance-
enablement platforms solve. Pure cash-pay addresses the smaller, higher-CAC slice.

**The chosen path (per Joel): cash-pay as the beachhead** — deliberately, because it is:
- **Faster & lighter:** no payer contracting, no claims infrastructure, lighter compliance.
- **Capital-efficient:** fits a bootstrapped build; fewer moving parts to launch a state.
- **A clean test** of matching quality, trust, and therapist economics before heavier investment.

**Deliberate optionality:** insurance-enablement is the **larger long-term pool** and a credible
**Phase-2 expansion** once cash-pay liquidity and the multi-state legal structure are proven. The
plan keeps that door open rather than betting the company on cash-pay forever. **This is the most
important strategic decision to revisit with data after the beachhead.**

## 6. Business model & unit economics
- **Revenue:** 15% of each completed paid session. **Revenue ≈ clients × sessions/client × price
  × 15%.**
- **The 15% is low by market standards** (rivals 20–30%) → attractive to therapists (helps the
  easy side of the marketplace) but thin per-session economics → **volume + retention are
  existential.**
- **CAC is the swing factor.** In cash-pay, acquisition is paid-marketing-heavy and the binding
  constraint is demand. The model must prove **CAC payback within a small number of sessions** and
  **LTV:CAC ≥ 3**. Full driver model, scenarios, and break-even frontier: `financial-model.md`
  (+ `financial-model.csv`).
- **Levers that make 15% work:** lower CAC via organic/referral/SEO and therapist-driven client
  invites; higher sessions-per-client via fit and retention; disciplined fixed costs.

## 7. Go-to-market
**Principle (from the demand-constrained finding): weight effort toward the CLIENT side; seed
supply first to guarantee liquidity.**
- **Per-market launch playbook:** (1) recruit a focused panel of therapists in a target state →
  (2) ensure legal qualification + licensure coverage → (3) switch the state "on" → (4) drive
  client demand into a liquid panel → (5) optimise match/retention → (6) move to the next state.
- **Supply (therapists):** professional networks, referrals, the 15%-take pitch, low-admin value
  prop. Supply is the *easier* side — don't over-invest here.
- **Demand (clients):** SEO/content, paid search/social (measured against CAC payback), referrals,
  therapist-initiated client invites, and eventually partnerships (universities, communities,
  employers). Healthcare advertising rules apply (⚠️ legal review).
- **Geographic sequencing** is gated by the legal roadmap (entity qualification + registered agent
  per state) — a tier-1 cluster first to prove the playbook, then scale. See the legal skill.
- **Defensibility:** supply density + trust/brand + the hard-won multi-state compliance moat.

## 8. Clinical & regulatory structure (summary)
- **Structure:** US parent + **MSO**, with a **friendly PC** where a state's corporate-practice /
  fee-splitting doctrine requires it; the **15% framed as a technology/marketing fee**, not a
  clinical fee-split. ⚠️ COUNSEL validates per state.
- **Licensing:** therapists licensed in the **client's state**; leverage **PSYPACT / Counseling
  Compact / Social Work Compact** to widen supply.
- **Compliance foundations:** HIPAA + state privacy, telehealth consent, clinical governance,
  crisis/safeguarding. See the policy drafts in this folder and the full legal roadmap in
  `.claude/skills/faresay-legal-authority/references/legal-roadmap.md`.

## 9. Operations & technology
- Core platform: matching, scheduling, **HIPAA-eligible telehealth video**, marketplace payments
  (15% split + payouts), messaging, verification, admin. Detail: `product-requirements-document.md`.
- Security & data protection to a high bar (special-category / PHI): `security-data-protection-policy.md`.
- Lean ops: credentialing/verification, trust & safety, support — outsource selectively.

## 10. Team & organisation
- **Founder-led, bootstrapped, lean.** [PLACEHOLDER: founder & team details.]
- Key early hires/advisors to line up: **clinical lead/advisor** (governance, crisis, exclusion
  criteria), **fractional compliance/ops**, plus retained **US healthcare-regulatory counsel**.
- Roles map to the Risk Register owners until headcount grows.

## 11. Financial plan
- **Philosophy:** contribution-margin-positive growth; compliance treated as a **phased step-cost**
  per state cluster (not 50 states up front); tight burn; milestone-gated spend (every cost runs
  through the approval gate per the legal skill).
- **Model:** `financial-model.md` + `financial-model.csv` — drivers (price, sessions/client,
  retention, CAC, processing), 3 scenarios (Conservative/Base/Stretch), monthly Y1–Y2 build,
  break-even and CAC×sessions sensitivity.
- **What must be true to work:** low-enough CAC and high-enough sessions-per-client that a 15%
  take on cash-pay sessions covers acquisition + ops with margin to spare. The model surfaces the
  exact thresholds.

## 12. Risks (top)
From `risk-register.md` (full register, 28 risks scored):
- **R-01 Fee-splitting / CPOM** (the 15% characterisation) — mitigated by MSO/PC + counsel.
- **R-17 CAC > LTV** — the core cash-pay risk; mitigated by organic acquisition + retention focus.
- **R-22 Two-sided cold-start** — mitigated by seed-supply-first, narrow launch geography.
- **R-02/03 Operating authority & licensure** — state on/off gating tied to the legal roadmap.
- **R-12 Data breach / R-07 client crisis** — security & crisis/safeguarding policies.

## 13. Roadmap & milestones
1. **Now:** UK operations; stand up legal@/enquiries@; retain US healthcare-regulatory counsel;
   finalise structure (MSO/PC + 15% characterisation).
2. **Foundation:** US entity + first-state qualification + registered agent; compliance baseline
   (HIPAA posture, policies finalised with counsel/clinical lead); product ready for a US pilot.
3. **Beachhead:** launch one US state-cluster cash-pay; prove liquidity, CAC payback, retention.
4. **Scale:** roll out state-by-state per the legal roadmap; tune economics.
5. **Decision point:** evaluate **insurance-enablement** expansion on real data.

## 14. Linked documents
- `business-model-canvas.md` · `product-requirements-document.md` · `financial-model.md` (+ `.csv`)
- `risk-register.md` · `market-research-synthesis.md`
- Policies: `terms-of-service.md` · `privacy-policy.md` · `therapist-agreement.md` ·
  `clinical-governance-policy.md` · `crisis-safeguarding-policy.md` · `security-data-protection-policy.md`
- Legal authorisation workstream: `.claude/skills/faresay-legal-authority/`
