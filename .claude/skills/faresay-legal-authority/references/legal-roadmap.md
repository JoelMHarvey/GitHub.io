# US Legal-Authority Roadmap — Therapy Marketplace

> **Not legal advice.** This is an orchestration map so the agent can brief and coordinate
> licensed US counsel efficiently. Counsel validates and decides. Laws change; the agent must
> verify current requirements (WebSearch / official state sources) and never rely on memory for
> a specific filing fee, deadline, or rule.

## Why a therapy marketplace is the hard mode of "go to all 50 states"

A generic SaaS company just forms an entity and foreign-qualifies. A platform that sits between
clients and **licensed mental-health clinicians** and takes a **percentage of the clinical fee**
runs into healthcare-specific regimes that vary state by state. The four that matter most:

### 1. Corporate Practice of Medicine (CPOM) + fee-splitting — the central question

- Many states bar a **non-clinician-owned company** from owning/controlling a clinical practice,
  employing clinicians to deliver care, or **splitting professional fees** with an unlicensed
  entity. A flat "we take 15% of the therapist's fee" can read as prohibited fee-splitting in
  those states.
- The standard fix is the **MSO + "friendly PC"** model: a **Management Services Organization**
  (Faresay's commercial entity) provides administrative/marketing/tech services to a
  **Professional Corporation/Entity** owned by a licensed clinician, under a Management Services
  Agreement that charges **fair-market-value, administrative-basis fees** (not a raw cut of the
  professional fee). Structuring the 15% to survive this is the single most important legal task.
- States differ sharply: some strictly enforce CPOM (e.g. California, Texas, New York, New
  Jersey), some are lenient, some have profession-specific rules for psychologists/LCSWs/LPCs
  that differ from physician rules. **Counsel must map Faresay's model per state.**

### 2. Clinician licensing + interstate compacts

- A therapist must be licensed **in the state where the *client* is located** at session time.
  Faresay must verify and continuously monitor each provider's license per client-state.
- **Interstate compacts** dramatically reduce friction and should be leveraged:
  - **PSYPACT** — psychologists practising telehealth across member states.
  - **Counseling Compact** — licensed professional counselors (LPC/LMHC).
  - **Social Work Licensure Compact** — clinical social workers (LCSW).
  Member-state lists change; verify current membership.

### 3. Privacy & data

- **HIPAA** (federal) if Faresay is a covered entity or business associate handling PHI —
  expect BAAs, security rule controls, breach-notification readiness.
- **State health-privacy laws** that can exceed HIPAA: Washington **My Health My Data Act**,
  Nevada SB370, Connecticut/others; plus general consumer-privacy laws (CCPA/CPRA in CA, and the
  growing list of state comprehensive privacy laws).
- **42 CFR Part 2** if any substance-use-disorder treatment is involved.

### 4. Telehealth modality + consumer rules

- State telehealth statutes (informed consent, modality, identity/location verification,
  emergency/duty-to-warn protocols). Some states require **out-of-state telehealth registration**.
- Healthcare **advertising** rules (no false/misleading claims), consumer-protection and
  **auto-renewal** laws for subscriptions, enforceable terms of service.

---

## The phased plan

Work top-to-bottom. The first dollar goes to Phase 1 counsel — that decision shapes the rest.

### Phase 0 — Set up & stand the agent up
- [ ] Email infra live: `legal@` + `enquiries@` forwarding to the agent mailbox (`email-setup.md`).
- [ ] Brief confirmed (`brief.md`), trackers initialised (`assets/`).
- [ ] One-page Faresay summary ready to send to attorneys (model, 15% fee, UK status, US goal).

### Phase 1 — Retain US healthcare-regulatory counsel  ← gates everything
- [ ] Shortlist 3–5 firms/attorneys specialising in **digital health / telehealth / behavioral
      health regulatory** with **multi-state CPOM & fee-splitting** experience (`contact-targets.md`).
- [ ] Send intro + scoping inquiry (template). Request fee structure (flat-fee scoping vs hourly).
- [ ] Compare quotes & scope → approval request → Joel engages one.
- [ ] Counsel's first deliverable: validate/design the **entity + MSO/PC + 15%-fee** structure
      and a **state-tiering** of CPOM/fee-splitting risk.

### Phase 2 — Form the structure
- [ ] Form US entities counsel specifies (e.g. Delaware parent + MSO; PC(s) as required).
- [ ] EIN(s), registered agent, banking, governing docs, Management Services Agreement.
- [ ] Provider agreements consistent with the chosen structure.

### Phase 3 — Compliance foundations
- [ ] HIPAA posture + BAA templates; security controls; breach plan.
- [ ] State health-privacy compliance plan (WA MHMDA, CCPA/CPRA, others).
- [ ] Provider-license verification & continuous-monitoring process; compact strategy.
- [ ] Insurance: professional liability (providers), tech/cyber E&O (platform).
- [ ] Telehealth informed-consent + emergency protocols; advertising review; ToS/auto-renewal.

### Phase 4 — Authorise in each state (the "all 50" core)
For each state (track in `assets/state-tracker.csv`):
- [ ] Foreign qualification / certificate of authority + **registered agent**.
- [ ] CPOM/fee-splitting posture confirmed for this state (does the model need a PC here?).
- [ ] Any state-specific telehealth / out-of-state-provider registration.
- [ ] Tax registration where the service creates nexus/obligation (verify per state).
- [ ] Provider-licensing coverage confirmed for clients located in this state.

> Sequencing tip: pilot a **tier-1 cluster** (a few high-value, well-understood states) end-to-end
> first to prove the playbook, then scale to the rest. National **registered-agent** providers can
> cover all states under one account — get quotes (see template); this is usually the most
> cost-efficient route and a natural early approval item.

### Phase 5 — Ongoing compliance (never "done")
- [ ] Annual reports & registered-agent renewals per state.
- [ ] License-expiry & compact-membership monitoring.
- [ ] Privacy-law change monitoring; periodic structure review with counsel.

---

## How the agent should use this

- Always translate a phase step into a **concrete next action**, usually an outbound draft +
  approval request, or a research/comparison task.
- Keep questions for counsel batched and specific (the agent drafts them; Joel approves sending).
- Re-verify any fee, deadline, compact membership, or state rule against a current official
  source before putting it in front of Joel as fact.
- The Lawve_AI catalogue can supply structured legal-research and AI-governance/audit-trail
  methodology — useful for documenting the agent's own delegated decisions — but retained US
  counsel is the authority on the structure.
