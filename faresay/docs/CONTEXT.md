# Faresay — Shared Context Fact Sheet

> Single source of truth for all Faresay documents. Every doc in this folder must stay consistent
> with these facts. If a fact changes, update it here first.

## The company
- **Faresay** — an online **therapy / mental-health marketplace** connecting clients with
  licensed mental-health professionals (psychologists, clinical social workers / counsellors,
  psychotherapists).
- **Current footprint:** United Kingdom. **Goal:** expand into the **United States, all 50
  states + DC.**
- **Stage / posture:** **bootstrapped**, capital-efficient, internal operating focus (no
  near-term external raise).

## Business model
- **Marketplace take rate: 15%** of the session fee.
- **US model (decided): cash-pay / out-of-network** (BetterHelp/Talkspace-style) — clients pay
  out of pocket; Faresay is **not** billing insurance in the initial US model.
- **Fee characterisation (important):** position the 15% as a **technology + marketing platform
  fee** (software, discovery, scheduling, payments, client acquisition) — **not** a split of the
  clinician's professional fee. This framing matters for corporate-practice / fee-splitting law
  and must be confirmed with US counsel.
- Faresay provides the **platform**; the **clinician** provides the clinical service and owns the
  clinical relationship and clinical record.

## Clinical / legal structure (US — to be validated by counsel)
- Likely **MSO (Faresay's commercial entity) + "friendly PC"** where a state's
  corporate-practice-of-medicine (CPOM) / corporate-practice-of-psychology doctrine requires it.
- Therapists must be **licensed in the state where the client is located**; leverage interstate
  compacts (**PSYPACT**, **Counseling Compact**, **Social Work Licensure Compact**).
- Engaged US healthcare-regulatory counsel will validate entity structure, the 15%-fee
  characterisation, and per-state requirements (see the legal skill:
  `.claude/skills/faresay-legal-authority/`).

## Data protection posture
- **UK now:** UK GDPR + Data Protection Act 2018; clinical data is **special-category** health
  data. ICO registration.
- **US expansion:** **HIPAA** (covered-entity vs business-associate status to be confirmed with
  counsel), plus state health-privacy laws (e.g. Washington **My Health My Data Act**, CCPA/CPRA,
  and other state comprehensive privacy laws).
- Sensitive mental-health data → high security + confidentiality bar throughout.

## Voice & standards for these documents
- Professional, clear, plain-English where possible.
- Every legal/clinical document is a **DRAFT for professional (legal/clinical) review** — not
  legal or clinical advice. Mark clearly. Flag every point that genuinely needs counsel or a
  clinical advisor with `⚠️ COUNSEL` / `⚠️ CLINICAL`.
- Use `[PLACEHOLDER: …]` for company specifics not yet known (registered entity name, address,
  DPO contact, governing law venue, etc.). Do not invent facts.
- Cross-reference sibling docs by filename where relevant.

## Document set (this folder)
1. `business-model-canvas.md`
2. `product-requirements-document.md`
3. `therapist-agreement.md` ⚠️ counsel
4. `terms-of-service.md` ⚠️ counsel
5. `privacy-policy.md` ⚠️ counsel
6. `clinical-governance-policy.md` ⚠️ clinical
7. `crisis-safeguarding-policy.md` ⚠️ clinical
8. `financial-model.md` (+ `financial-model.csv`) — follows market research
9. `risk-register.md`
10. `security-data-protection-policy.md` ⚠️ counsel/security
