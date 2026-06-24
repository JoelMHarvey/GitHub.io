# UK Legal & Regulatory Brief

> **Preparatory material for a solicitor consultation — not legal advice.** Prepared by the founder to
> brief counsel and focus the engagement. UK launch scope only; US matters are excluded by design.
> Each item states Faresay's **working assumption** and the **open question** for counsel.

---

## 0. How to read this

For each area: **Position** = our current understanding / intended approach. **Open question** = what we
need counsel to confirm or correct. Items are roughly ordered by how much they could change the model.

---

## 1. Corporate structure & status

**Position.** Faresay will operate as a UK private company limited by shares (Companies House), acting
as an **intermediary marketplace** — introducing clients to independent therapists and providing the
technology and payment rail. Faresay does not itself deliver clinical care.

**Open questions.**
- Is the "marketplace, not provider" characterisation robust, given Faresay sets the session price,
  handles the money, and controls the booking flow? Where is the line at which we'd be treated as
  *providing* the service rather than *facilitating* it?
- Recommended entity structure and any group structure (e.g. separate IP/holding entity) for a
  bootstrapped UK launch.
- Appropriate SIC code(s).

## 2. Is this a CQC-regulated activity?

**Position.** Counselling and psychotherapy delivered by **independent, self-employed** practitioners
are generally **outside** CQC registration; we believe Faresay (a platform that neither employs the
therapists nor directs clinical care) does not "carry on" a regulated activity such as *treatment of
disease, disorder or injury*.

**Open questions.**
- Confirm Faresay does **not** require CQC registration. What facts would flip this (e.g. if we
  employed therapists, triaged clinically, or marketed ourselves as the provider)?
- Does the picture change if any practitioners on the platform are HCPC-registered practitioner
  psychologists or provide anything beyond talking therapy?

## 3. Therapist regulation & vetting

**Position.** "Therapist" / "counsellor" are **not** statutorily protected titles in the UK.
Faresay will require every practitioner to hold membership of an appropriate professional body /
**PSA-accredited register** (BACP, UKCP, NCPS, etc.) or statutory registration where applicable
(HCPC), plus current professional indemnity insurance, and will verify this before go-live.

**Open questions.**
- Is mandating PSA-accredited-register membership (or HCPC) a sufficient and defensible vetting
  standard? Any additional checks counsel would require (DBS, identity, qualification verification)?
- Our liability exposure if a vetted therapist is later struck off or causes harm — and how to
  structure the agreement and disclaimers to manage it.

## 4. Therapist employment status (high priority)

**Position.** Therapists are **self-employed independent contractors**, not employees or workers of
Faresay. They use their own indemnity insurance and are responsible for their own tax.

**Open questions.**
- **Worker-status risk:** Faresay sets/controls the session price, the booking system, and some
  conduct standards. Could a tribunal find therapists are "workers" (entitled to holiday pay, etc.)
  or even employees? What contractual and operational changes reduce that risk (e.g. therapist-set
  pricing, right of substitution, no exclusivity)?
- Status-determination and the platform's tax exposure; relevance of off-payroll / agency
  legislation to this model.

## 5. Data protection — UK GDPR & DPA 2018 (high priority)

**Position.** Faresay processes **special category health data** and will: register with the ICO and
pay the data-protection fee; rely on appropriate Article 6 + Article 9 conditions (e.g. explicit
consent and/or provision of health/social care); complete a **DPIA**; maintain a ROPA, privacy
notice, retention schedule, DSAR process, and 72-hour breach procedure.

**Controller/processor.** Faresay is likely a **controller** for account, booking and payment data;
the therapist is the **controller** for their clinical notes. We will put a data-sharing /
joint-controller or controller-to-controller arrangement in place between Faresay and therapists.

**International transfers (flag).** Parts of our stack use **US-headquartered processors** (auth,
video, email). This creates UK→US (and other) transfer questions.

**Open questions.**
- Correct lawful bases (Art 6 + Art 9) for each processing purpose; is explicit consent the right
  Art 9 condition, or the health/social-care condition?
- The right controller model between Faresay and therapists, and the contract to paper it (DPA,
  joint-controller agreement, or both).
- Transfers: which sub-processors are outside the UK, and what mechanism each needs (UK IDTA / EU
  SCCs + UK Addendum, transfer risk assessment). Should we prefer UK/EU-region processors to reduce
  transfer exposure?
- Confirm DPIA scope and whether prior ICO consultation is ever needed.

## 6. Consumer law (B2C)

**Position.** Client contracts are distance contracts for services. We will provide pre-contract
information, clear pricing, and cancellation/refund terms (full refund if cancelled >24h ahead).

**Open questions.**
- Consumer Contracts Regulations 2013: the 14-day cancellation right and how the "service begins
  with the consumer's agreement before the 14 days expire" waiver should be presented at checkout.
- Consumer Rights Act 2015: our "reasonable care and skill" obligations as the platform vs. the
  therapist's, and how to allocate them in the terms.
- Any unfair-terms exposure in our limitation-of-liability and cancellation clauses.

## 7. Clinical safety, safeguarding & crisis boundaries

**Position.** Faresay is **not a crisis service**. The platform displays crisis signposting (999,
Samaritans 116 123, NHS 111, SHOUT 85258) and operates a safeguarding policy and complaints process.
Clinical responsibility sits with the treating therapist.

**Open questions.**
- Faresay's duty of care to clients as an intermediary, and how to bound it.
- Minimum safeguarding obligations we should impose on therapists (vulnerable adults, children if we
  ever allow under-18s — currently adults only), and our own escalation duties.
- Complaints handling expectations and whether any ADR/ombudsman scheme applies.

## 8. Advertising & claims (ASA/CAP)

**Position.** Marketing will avoid unsubstantiated efficacy or health-outcome claims about therapy.

**Open question.** Review of homepage and marketing claims for CAP Code compliance — what we can and
cannot say about outcomes, "qualified/accredited", and pricing comparisons with competitors.

## 9. Payments & client money (likely low, confirm)

**Position.** Payments run through **Stripe** (the regulated payment institution). Faresay is a
platform/marketplace using Stripe Connect; we do not intend to hold client funds ourselves.

**Open question.** Confirm Faresay does not require FCA authorisation / does not trigger
safeguarding-of-funds or payment-services obligations given Stripe is the PSP and flow-through is
near-immediate.

## 10. Tax / VAT (refer to accountant + counsel)

**Position.** Therapy by registered health professionals may be VAT-exempt, but Faresay's **platform
fee is a separate supply** and may be **standard-rated VAT**.

**Open questions.**
- VAT treatment of the 15% platform fee; VAT registration threshold and timing.
- Any structuring to keep the fee characterisation clean (platform fee, not fee-split).

## 11. Contracts to produce / review

- **Client Terms of Service** (B2C) and **Privacy Notice**.
- **Therapist Agreement** (B2B independent-contractor terms) + data-sharing/DPA.
- **Cancellation & refund policy**, **complaints policy**, **safeguarding policy**.
- Processor agreements / sub-processor list for the data-transfer assessment.

> Draft versions of several of these exist (see the policy documents in this set) and are marked
> *DRAFT — for professional sign-off*. They are starting points for counsel, not finished instruments.

---

## Priority order for the meeting

1. Employment status of therapists (§4)
2. Data protection: controller model, lawful bases, international transfers (§5)
3. CQC / regulated-activity confirmation (§2)
4. Marketplace-vs-provider characterisation & liability (§1, §3, §7)
5. Consumer law terms (§6)
6. VAT on the platform fee (§10)
7. Payments/FCA confirmation (§9), advertising review (§8)
