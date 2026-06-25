# Faresay — Product Requirements Document (PRD)

> Working draft. Consistent with `CONTEXT.md` (cash-pay therapy marketplace, 15% platform fee,
> UK now → US all-50-states, bootstrapped). ⚠️ Items tied to legal/clinical sign-off are flagged.
> Last updated: 26 June 2026

## 1. Vision & overview
Faresay is a two-sided marketplace that connects people seeking therapy with vetted, licensed
therapists, and handles discovery, matching, scheduling, secure video sessions, and payments.
Clients pay out of pocket; Faresay takes a **15% platform fee**. The product must feel
**trustworthy, fast, and private** — it handles sensitive mental-health data and must make the
**"not a crisis service"** boundary unmistakable.

## 2. Goals & non-goals
**Goals**
- Let a client find, book, and pay for a suitable licensed therapist with minimal friction.
- Let a therapist get matched clients and run sessions with low admin, keeping 85% of the fee.
- Enforce **trust & safety**: verification, privacy, crisis signposting, compliance.
- Support **US multi-state** operation (licensure tied to the client's location).

**Non-goals (initial)**
- Insurance billing / claims (cash-pay only initially).
- Faresay providing clinical care itself (clinicians are independent).
- Crisis/emergency intervention (explicitly out of scope; signpost only).
- Prescribing / medication management.

## 3. Personas
- **Client (self-pay adult):** wants a good-fit therapist quickly, transparent price, easy booking.
- **Therapist (licensed independent):** wants filled calendar, low admin, fair terms, autonomy.
- **Clinical/Trust-&-Safety admin (Faresay):** verifies providers, monitors safety, handles issues.
- **Ops/Compliance admin (Faresay):** manages state coverage, licensure checks, payouts.

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
  **location/state capture** (required for US licensure matching) ⚠️ COUNSEL.
- **Matching/discovery**: browse + recommended matches; therapist profiles (credentials, specialisms,
  verified badge, price, availability, reviews).
- **Booking & calendar**: real-time availability, time-zone aware, reminders, reschedule/cancel.
- **Payments**: pay per session; transparent pricing; the 15% fee handled in the split ⚠️ COUNSEL on
  how the fee is presented; receipts; cancellation/no-show rules per ToS.
- **Secure video sessions** (HIPAA-eligible telehealth) ⚠️ SECURITY; in-session crisis resources.
- **Messaging** (async, boundaried, non-emergency) with safety disclaimers.
- **Reviews/feedback** and outcome measures (optional) per clinical governance.
- **Crisis signposting** persistently accessible (988/911 US; 999/111/Samaritans UK) ⚠️ verify.

### 5.2 Therapist-side
- **Application & onboarding**; document upload (licence, insurance, ID).
- **Credentialing/verification**: licensure check in operating state(s), interstate-compact handling
  (PSYPACT/Counseling/Social Work), background/DBS, insurance — with **ongoing monitoring** ⚠️.
- **Profile management**; availability/calendar; service/pricing settings (within platform rules).
- **Session management**: upcoming/past, secure video, notes link-out (clinician owns the record —
  Faresay does not store the clinical record by default) ⚠️ COUNSEL/CLINICAL.
- **Earnings & payouts**: balance, payout schedule, statements, tax docs ⚠️.
- **Policy acknowledgement**: Therapist Agreement, clinical governance, crisis/safeguarding.

### 5.3 Admin / trust & safety
- Verification queue & audit log; provider suspension/offboarding.
- **State-coverage controls** (which states are live for booking) tied to legal roadmap.
- Incident/complaint logging; safeguarding workflow; reporting.
- Payments/refunds/chargeback handling.

## 6. Non-functional requirements
- **Security & privacy** (see `security-data-protection-policy.md`): encryption in transit/at rest,
  RBAC, MFA, audit logging; data minimisation; PHI/special-category handling.
- **Compliance**: UK GDPR/DPA 2018 now; HIPAA + state privacy on US launch ⚠️ COUNSEL; BAAs with
  any PHI sub-processor (video, storage, payments-adjacent) ⚠️.
- **Reliability/availability**: target [PLACEHOLDER: e.g. 99.9%]; resilient booking/video/payments.
- **Performance**: fast match/search and booking; low-latency video.
- **Accessibility**: WCAG 2.2 AA target; inclusive design for distressed users.
- **Auditability**: trace verification, consent, payments, and safety actions.
- **Data residency**: UK/EU vs US considerations ⚠️ COUNSEL/SECURITY.

## 7. US-specific requirements
- **Licensure-by-client-location**: a client can only book a therapist licensed (or compact-
  authorised) in the client's state at session time. Hard rule ⚠️ COUNSEL.
- **State on/off switches** for booking, gated by legal qualification + provider coverage.
- **Informed consent to telehealth** captured per state ⚠️ COUNSEL.
- **MSO/PC structure** reflected in contracting/payment flows where required ⚠️ COUNSEL.

## 8. MVP vs later
**MVP (UK first, then first US state cluster):** account, intake, matching, profiles, booking,
payments + 15% split, secure video, messaging, verification, crisis signposting, core admin.
**Later:** advanced matching/ML, outcome analytics, employer/B2B, premium therapist tools,
native apps, insurance (if model expands), broader state automation.

## 9. Success metrics
- **Liquidity**: % of client searches that result in a booking; therapist utilisation.
- **Acquisition/economics**: CAC, CAC payback, sessions-per-client, retention/churn, LTV
  (quantified in `financial-model.md`).
- **Quality/safety**: client-reported outcomes/satisfaction, complaint/incident rate, verification
  pass-rate, zero compliance breaches.
- **Marketplace health**: supply/demand balance per live market.

## 10. Dependencies & open questions
- Payment processor with **marketplace split + payouts** and (where needed) BAA ⚠️.
- **HIPAA-eligible video** vendor ⚠️ SECURITY.
- Licensure-verification / background-check vendor.
- ⚠️ COUNSEL: minors in scope? fee presentation? clinical-record custody? per-state consent?
- ⚠️ CLINICAL: screening/exclusion thresholds (see clinical-governance & crisis-safeguarding).
