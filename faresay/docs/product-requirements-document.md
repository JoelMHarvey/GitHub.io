# Faresay — Product Requirements Document (PRD)

> Working draft. Consistent with `CONTEXT.md` (cash-pay therapy marketplace, 15% platform fee,
> UK first → English-speaking expatriates worldwide → broader markets (incl. the US) later,
> bootstrapped). ⚠️ Items tied to legal/clinical sign-off are flagged.
> Last updated: [PLACEHOLDER: date]

## 1. Vision & overview
Faresay is a two-sided marketplace that connects people seeking therapy with vetted, licensed
therapists, and handles discovery, matching, scheduling, secure video sessions, and payments.
Clients pay out of pocket; Faresay takes a **15% platform fee** (10% for founding therapists;
therapist keeps 85%, or up to 90% as a founding therapist). The product must feel
**trustworthy, fast, and private** — it handles sensitive mental-health data and must make the
**"not a crisis service"** boundary unmistakable.

**Trust is the core product.** The primary promise is that every therapist is manually verified —
licensed, identity-verified, interviewed, and quality-reviewed — with reviews, response times, and
a transparent experience surfaced to clients. **Matching (fit) sits on top of trust**, not the
other way round.

**Beachhead.** After the UK home market, the near-term focus is **internationally mobile,
English-speaking professionals** (e.g. Japan, Singapore, Hong Kong, the UAE, Thailand, Vietnam, and
across Europe) seeking culturally-compatible therapists who understand relocation stress, isolation,
identity, and belonging. Broader markets — including the US and its multi-state machinery — are a
**later, optional phase** (see §7), not the near-term build.

## 2. Goals & non-goals
**Goals**
- Let a client find, book, and pay for a suitable licensed therapist with minimal friction.
- Let a therapist get matched clients and run sessions with low admin, keeping 85% of the fee
  (up to 90% as a founding therapist).
- Make **trust visible and verifiable**: manual verification, identity checks, interviews, quality
  review, reviews, response times — surfaced on every profile.
- Serve **internationally mobile, English-speaking clients**: timezone-aware scheduling,
  cross-cultural/multilingual matching, and country-correct crisis signposting.
- Enforce **trust & safety**: verification, privacy, crisis signposting, compliance.

**Non-goals (initial)**
- Insurance billing / claims (cash-pay only initially).
- Faresay providing clinical care itself (clinicians are independent).
- Crisis/emergency intervention (explicitly out of scope; signpost only).
- Prescribing / medication management.

## 3. Personas
- **Client (self-pay adult, often an expatriate):** internationally mobile English-speaking
  professional living abroad; wants a culturally-compatible, good-fit therapist who understands
  relocation stress and isolation, in their own timezone, with a transparent price and easy booking.
- **Therapist (licensed independent):** wants filled calendar, low admin, fair terms, autonomy;
  may have cross-cultural / expat experience and work across timezones.
- **Clinical/Trust-&-Safety admin (Faresay):** verifies providers, monitors safety, handles issues.
- **Ops/Compliance admin (Faresay):** manages market coverage, licensure/registration checks,
  cross-border permissibility flags, payouts.

## 4. Key user journeys
1. **Client onboarding → match → book → pay → session → follow-up/rebook.**
2. **Therapist application → verification/credentialing → profile live → receive bookings → get
   paid out (session fee minus 15%).**
3. **Safety path:** risk signposting surfaced throughout; exclusion at screening for unsuitable
   presentations; in-session crisis resources (see `crisis-safeguarding-policy.md`).

## 5. Functional requirements

### 5.1 Client-side
- Account creation & secure auth (MFA option); age/eligibility gate ⚠️ COUNSEL (minors policy).
- **Intake/preferences**: needs, modality, therapist preferences (gender, language, specialism),
  **country-of-residence capture** (required for crisis signposting, timezone, and cross-border
  licensure flagging) ⚠️ COUNSEL.
- **Cross-cultural / multilingual preferences**: languages spoken, countries/cultures of experience,
  and expat-relevant specialisms (relocation stress, isolation, identity, belonging) — used as
  matching inputs (see §5.4).
- **Matching/discovery**: browse + recommended matches; therapist profiles lead with **trust
  surfaces** (verification badges; credentials body + number verified; identity-verified;
  interviewed; quality-reviewed; reviews; typical response time), then fit (specialisms, languages,
  cultural experience, price, availability).
- **Booking & calendar**: **timezone-aware scheduling** — availability and all times shown in the
  client's locale, with therapist↔client timezone differences handled explicitly; real-time
  availability, reminders, reschedule/cancel.
- **Payments**: pay per session; transparent pricing; the 15% fee (10% founding) handled in the
  split ⚠️ COUNSEL on how the fee is presented; multi-currency display considerations for overseas
  clients ⚠️ COUNSEL; receipts; cancellation/no-show rules per ToS.
- **Secure video sessions** (privacy-compliant telehealth) ⚠️ SECURITY; in-session crisis resources.
- **Messaging** (async, boundaried, non-emergency) with safety disclaimers.
- **Reviews/feedback** and outcome measures (optional) per clinical governance.
- **Crisis signposting** persistently accessible and **resolved to the client's country of
  residence** (e.g. 999/111/Samaritans UK; country-correct equivalents elsewhere — must not default
  to a single UK/US list) ⚠️ verify / ⚠️ COUNSEL.

### 5.2 Therapist-side
- **Application & onboarding**; document upload (licence/registration, insurance, ID).
- **Credentialing/verification** (the trust engine): manual licensure/registration check against the
  therapist's regulatory body (e.g. BACP/UKCP/HCPC in the UK ⚠️ verify), credentials body + number
  verified, **identity verification**, **structured interview**, **quality review**, background/DBS,
  insurance — with **ongoing monitoring**; verification outcomes drive the client-facing trust
  badges in §5.1 ⚠️.
- **Cross-cultural profile fields**: languages spoken, countries/cultures of practice and lived
  experience, expat-relevant specialisms; therapist's registration **jurisdiction** captured for
  cross-border permissibility flagging (see §5.4, §7).
- **Profile management**; **timezone-aware** availability/calendar; service/pricing settings
  (within platform rules).
- **Session management**: upcoming/past, secure video, notes link-out (clinician owns the record —
  Faresay does not store the clinical record by default) ⚠️ COUNSEL/CLINICAL.
- **Earnings & payouts**: balance, payout schedule, statements, tax docs ⚠️.
- **Policy acknowledgement**: Therapist Agreement, clinical governance, crisis/safeguarding.

### 5.3 Admin / trust & safety
- Verification queue & audit log; provider suspension/offboarding.
- **Market-coverage controls** (which client countries / corridors are live for booking) tied to
  the legal roadmap; UK live first, expat corridors enabled as cross-border permissibility is
  confirmed (see §7).
- **Cross-border permissibility flags**: per client-country × therapist-jurisdiction corridor, with
  ⚠️ COUNSEL review status — block or warn where teletherapy is not confirmed permissible.
- Incident/complaint logging; safeguarding workflow; reporting.
- Payments/refunds/chargeback handling.

### 5.4 Matching engine
- **Trust first**: only verified, in-good-standing therapists are eligible to surface; trust state
  is a gate, not a tie-breaker.
- **Fit on top of trust**, weighting cross-cultural/multilingual signals: shared/known languages,
  countries/cultures of experience, expat-relevant specialisms (relocation stress, isolation,
  identity, belonging), modality and preference fit.
- **Timezone feasibility**: rank by realistic overlap between the client's locale and the
  therapist's availability; surface times in the client's timezone.
- **Cross-border gating**: matches respect the §5.3 permissibility flag for the client-country ×
  therapist-jurisdiction corridor ⚠️ COUNSEL.

## 6. Non-functional requirements
- **Security & privacy** (see `security-data-protection-policy.md`): encryption in transit/at rest,
  RBAC, MFA, audit logging; data minimisation; PHI/special-category handling.
- **Compliance**: UK GDPR/DPA 2018 now (see `uk-legal-regulatory-brief.md`); cross-border data
  flows for overseas (expat) clients ⚠️ COUNSEL; HIPAA + US state privacy only if/when the US phase
  is pursued ⚠️ COUNSEL; data-processing agreements (and BAAs where a US footprint applies) with any
  special-category sub-processor (video, storage, payments-adjacent) ⚠️.
- **Reliability/availability**: target [PLACEHOLDER: e.g. 99.9%]; resilient booking/video/payments.
- **Performance**: fast match/search and booking; low-latency video.
- **Accessibility**: WCAG 2.2 AA target; inclusive design for distressed users.
- **Auditability**: trace verification, consent, payments, and safety actions.
- **Data residency**: UK/EU vs US considerations ⚠️ COUNSEL/SECURITY.

## 7. Cross-border & jurisdiction requirements

### 7.1 Near-term (UK + expat corridors)
- **Cross-border licensure capture**: capture the **client's country of residence** and the
  **therapist's registration/jurisdiction**; every match carries this pair.
- **Permissibility flag (do not assume)**: cross-border teletherapy permissibility must be checked
  **per corridor** — do **not** assert it is automatically allowed. Surface a ⚠️ COUNSEL status per
  client-country × therapist-jurisdiction pair and block/warn where unconfirmed.
- **Corridor on/off switches** for booking, gated by legal qualification + provider coverage; UK
  domestic live first, expat corridors enabled as cleared.
- **Informed consent to teletherapy** captured per corridor ⚠️ COUNSEL.

### 7.2 Later / optional (US multi-state phase)
> Pursued only if/when the US phase is taken on — **not** the near-term build.
- **Licensure-by-client-location**: a client can only book a therapist licensed (or compact-
  authorised, e.g. PSYPACT / counseling / social-work compacts) in the client's state at session
  time. Hard rule ⚠️ COUNSEL.
- **State on/off switches** for booking, gated by legal qualification + provider coverage.
- **Informed consent to telehealth** captured per state ⚠️ COUNSEL.
- **MSO / friendly-PC structure** reflected in contracting/payment flows where required ⚠️ COUNSEL.
- **HIPAA + 50-state privacy** machinery and BAAs ⚠️ COUNSEL/SECURITY.

## 8. MVP vs later
**MVP (UK first, then English-speaking expat corridors):** account, intake (incl. country of
residence + cross-cultural preferences), trust-first matching, profiles with verification/trust
surfaces, **timezone-aware** booking, payments + 15% split (10% founding), secure video, messaging,
manual verification (licence/registration, identity, interview, quality review), **country-correct**
crisis signposting, cross-border permissibility flagging, core admin.
**Later:** advanced matching/ML, outcome analytics, employer/B2B, premium therapist tools,
native apps, insurance (if model expands), and the **US multi-state phase** (§7.2:
licensure-by-state, MSO/friendly-PC, PSYPACT/state compacts, HIPAA + 50-state privacy) if pursued.

## 9. Success metrics
- **Liquidity**: % of client searches that result in a booking; therapist utilisation.
- **Acquisition/economics**: CAC, CAC payback, sessions-per-client, retention/churn, LTV
  (quantified in `financial-model.md`).
- **Quality/safety**: client-reported outcomes/satisfaction, complaint/incident rate, verification
  pass-rate, zero compliance breaches.
- **Trust**: verification pass-rate, % of profiles with full trust surfaces, median response time.
- **Marketplace health**: supply/demand balance per live market (UK + expat corridors).

## 10. Dependencies & open questions
- Payment processor with **marketplace split + payouts**, international payouts and multi-currency
  handling, and (where a US footprint applies) BAA ⚠️.
- **Privacy-compliant video** vendor ⚠️ SECURITY (HIPAA-eligible only required if US phase pursued).
- Licensure/registration-verification / background-check vendor (UK regulatory bodies first).
- **Timezone & locale** library / source of truth for client-locale time display.
- **Country crisis-resource directory** to drive country-correct signposting (see
  `crisis-safeguarding-policy.md` / `uk-crisis-safeguarding-policy.md`).
- ⚠️ COUNSEL: minors in scope? fee presentation? clinical-record custody? **per-corridor
  cross-border teletherapy permissibility & consent?** (UK basis: `uk-legal-regulatory-brief.md`.)
- ⚠️ CLINICAL: screening/exclusion thresholds (see clinical-governance & crisis-safeguarding).
