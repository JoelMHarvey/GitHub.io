> ⚠️ DRAFT v0.1 — for security + legal review. NOT legal advice. Must be validated before use. Last updated: [PLACEHOLDER: date]

# Faresay Security & Data Protection Policy

Faresay operates an online therapy / mental-health marketplace that connects clients with licensed mental-health professionals. Because the Platform handles **mental-health information** — among the most sensitive categories of personal data that exist — Faresay applies a correspondingly high standard of security and data protection across its people, processes and technology.

This policy sets out the controls Faresay maintains to protect the confidentiality, integrity and availability of the data it processes. It is written to support:

- **United Kingdom (now):** the **UK GDPR** (in particular **Article 32 — Security of processing**) and the **Data Protection Act 2018**; clinical data is **special-category** health data; Faresay is registered with the **ICO**.
- **United States (planned expansion, all 50 states + DC):** the **HIPAA Security Rule** (45 CFR Part 160 and Part 164, Subparts A and C) and the **HIPAA Breach Notification Rule**, plus state health-privacy and consumer-protection laws (e.g. Washington **My Health My Data Act**, California **CCPA/CPRA**).

> This policy should be read alongside the [Privacy Policy](privacy-policy.md), the [Terms of Service](terms-of-service.md), the [Therapist Agreement](therapist-agreement.md), and the shared [CONTEXT.md](CONTEXT.md) fact sheet. It is an internal operational policy; client-facing commitments live in the Privacy Policy.

⚠️ **COUNSEL / SECURITY — overarching note.** This is a first draft for review. Faresay is **bootstrapped** and early-stage; several controls below describe a **target state** rather than a control that is fully implemented today. Each section flags where this is the case. Counsel and a security specialist must validate scope, the UK/EU vs US data-residency model, the controller / processor / covered-entity / business-associate analysis, and all breach-notification obligations before this policy is relied upon.

---

## 1. Purpose & scope

### 1.1 Purpose
This policy defines how Faresay protects the data it processes, establishes accountability for security and data protection, and demonstrates — for UK GDPR Article 32 and, on US launch, the HIPAA Security Rule — that Faresay implements appropriate technical and organisational measures (TOMs) proportionate to the risk to individuals.

### 1.2 Scope
This policy applies to:
- All Faresay personnel: employees, founders, contractors, and any worker with access to Faresay systems or data.
- All Faresay information systems and services, including the **marketplace application**, supporting infrastructure, code repositories, administrative tooling, and corporate accounts (email, collaboration tools).
- All data processed by Faresay, with **mental-health data / Protected Health Information (PHI)** treated as the highest-sensitivity class (Section 2).
- Third parties and sub-processors that process Faresay data on Faresay's behalf (Section 9).

### 1.3 Role boundary
Faresay provides the **platform**; the **clinician** provides the clinical service and owns the clinical relationship and clinical record (see [CONTEXT.md](CONTEXT.md) and the [Therapist Agreement](therapist-agreement.md)). The split of data-protection roles — controller / processor / joint controller (UK/EU) and covered entity / business associate (US HIPAA) — is being finalised by counsel and affects which obligations in this policy fall on Faresay versus the clinician. ⚠️ **COUNSEL.**

---

## 2. Data classification

Faresay classifies data so that controls are applied proportionately. Mental-health data is always treated at the highest level.

| Class | Examples | Handling baseline |
|---|---|---|
| **Class 1 — Highest sensitivity: mental-health data / PHI / special-category health data** | The fact a person is seeking or receiving therapy; intake/assessment information; session-related clinical information and notes; safeguarding/crisis information; messages relating to care. | Strict least-privilege access; encryption in transit and at rest; full audit logging; no use in non-production environments; breach-notification regimes apply (Section 14). |
| **Class 2 — Confidential** | Account & identity data; authentication data; payment-related data; clinician licensing/verification data; internal financials; security configuration. | Role-based access; encryption in transit and at rest; logged access. |
| **Class 3 — Internal** | Internal documents, non-sensitive operational data. | Access limited to personnel; standard controls. |
| **Class 4 — Public** | Marketing pages, published clinician profile information the clinician has agreed to publish. | Integrity controls; no confidentiality requirement. |

Notes:
- **Mental-health data is inherently sensitive.** Even the bare fact that an individual is a Faresay client is Class 1 data and must be protected accordingly.
- Where Faresay acts as a **processor / business associate** for clinical records, the clinician (as controller / covered entity) sets the lawful basis and permitted uses; Faresay processes only on documented instructions. ⚠️ **COUNSEL.**
- Payment card data: Faresay intends to use a **PCI-DSS-compliant payment processor** so that Faresay does not store raw card data. [PLACEHOLDER: payment processor]. ⚠️ **SECURITY** — confirm cardholder-data flows and PCI scope.

---

## 3. Governance, roles & responsibilities

### 3.1 Accountability
Faresay's leadership (founder/management) is ultimately accountable for information security and data protection and for approving this policy.

### 3.2 Key roles
- **Security Lead** — [PLACEHOLDER: named individual]. Owns this policy, the risk treatment plan, vendor security review, incident response coordination, and the security roadmap. In an early-stage bootstrapped company this may initially be a founder; ⚠️ **SECURITY** — confirm whether a fractional/virtual CISO or external security advisor is engaged.
- **Data Protection Officer (DPO) / privacy lead** — [PLACEHOLDER: DPO or privacy contact]. ⚠️ **COUNSEL** — confirm whether a statutory **DPO is required** under UK GDPR Art 37 (likely triggered by large-scale processing of special-category health data) and, if so, appoint and register the DPO with the ICO. The DPO/privacy lead owns DPIAs, records of processing (Art 30), data-subject rights handling, and the ICO relationship.
- **HIPAA Security Official & Privacy Official (US)** — ⚠️ **COUNSEL** — the HIPAA Security Rule requires a designated **Security Official** (45 CFR §164.308(a)(2)) and the Privacy Rule a **Privacy Official**; these must be named before US launch if Faresay is a covered entity or business associate.
- **All personnel** — responsible for following this policy, completing training, reporting incidents promptly, and protecting credentials and devices.

### 3.3 Decision-making & review
Security risks are tracked in the [risk-register.md](risk-register.md). Material security decisions, exceptions and accepted risks are recorded with an owner and review date.

---

## 4. Access control

### 4.1 Principles
- **Least privilege** — personnel receive the minimum access required for their role; broad/admin access is the exception, justified and time-bound where possible.
- **Role-Based Access Control (RBAC)** — access is granted by role, not individually, wherever the platform and tooling support it.
- **Need-to-know for Class 1 data** — access to mental-health data / PHI is restricted to roles with a genuine operational need and is logged (Section 11).
- **Separation of duties** — production access, code-deployment rights and security administration are separated where headcount allows; ⚠️ **SECURITY** — document compensating controls given small team size.

### 4.2 Authentication
- **Multi-factor authentication (MFA)** is required for all administrative and production-system access, code repositories, the hosting provider, DNS, email, and any system holding Class 1 or Class 2 data.
- Strong, unique passwords managed via a password manager; no shared accounts for administrative access.
- ⚠️ **SECURITY** — adopt SSO with enforced MFA across corporate SaaS where feasible. [PLACEHOLDER: identity provider / SSO].

### 4.3 Joiner / mover / leaver (JML)
- **Joiner** — access provisioned by role on a documented request; principle of least privilege; security onboarding and confidentiality agreement before access to Class 1/Class 2 data.
- **Mover** — access reviewed and adjusted on role change; entitlements no longer needed are revoked.
- **Leaver** — all access revoked promptly on departure (target: same business day; immediately for involuntary departures); credentials rotated; devices returned/wiped.
- **Periodic access reviews** — entitlements (especially to Class 1 data and admin roles) reviewed at least [PLACEHOLDER: quarterly] and stale access removed.

---

## 5. Encryption & key management

### 5.1 In transit
- **TLS** (current secure version, [PLACEHOLDER: TLS 1.2+ / 1.3]) enforced for all connections to the Platform and between services. HTTP redirected to HTTPS; HSTS enabled.
- TLS termination and edge security are provided via **Cloudflare** (DNS) and **Vercel** (web hosting) for the marketplace web app. ⚠️ **SECURITY** — confirm certificate management and that all backend/API and database connections are also encrypted.

### 5.2 At rest
- Class 1 and Class 2 data encrypted at rest using strong, industry-standard algorithms (e.g. AES-256). [PLACEHOLDER: database / storage provider and their at-rest encryption].
- Backups encrypted at rest (Section 13).

### 5.3 Key management
- Encryption keys and secrets (API keys, database credentials) managed via a dedicated secrets manager / platform environment-variable store, never committed to source control. [PLACEHOLDER: secrets management solution].
- Key access restricted, logged, and keys rotated on a defined schedule and on suspected compromise. ⚠️ **SECURITY** — define key-rotation cadence and ownership.

---

## 6. Infrastructure, hosting & data residency

### 6.1 Known stack (per CONTEXT.md)
- **Marketplace application** — the core product.
- **Web hosting:** **Vercel**.
- **DNS:** **Cloudflare**.
- **Application database / backend services / file storage:** [PLACEHOLDER: provider(s) — not specified in CONTEXT]. ⚠️ **SECURITY** — document the full inventory: database, object storage, email, payments, video/session delivery, analytics, error monitoring.

### 6.2 Data residency ⚠️ COUNSEL
- **UK/EU (now):** confirm that personal data — especially Class 1 mental-health data — is stored and processed in the **UK/EU**, or that a lawful **international transfer** mechanism is in place (UK IDTA / Addendum, EU SCCs, adequacy). Vercel and Cloudflare operate globally; **region configuration and routing must be verified**, since default configurations may route or store data outside the UK/EU. ⚠️ **COUNSEL.**
- **US (planned):** determine US data-residency requirements and whether US client data must remain in the US. Confirm that any provider handling PHI will sign a **HIPAA Business Associate Agreement** and offers a HIPAA-eligible configuration (Section 9). ⚠️ **COUNSEL.**
- ⚠️ **SECURITY** — maintain a data-flow map showing where each data class is stored, processed and transmitted, including sub-processor locations.

---

## 7. Secure software development lifecycle (SSDLC)

- **Secure by design** — security and privacy considered from design; a **DPIA** is completed for high-risk processing of special-category data (UK GDPR Art 35). ⚠️ **COUNSEL.**
- **Source control & review** — code held in version control ([PLACEHOLDER: GitHub/GitLab]); changes via pull request with **peer review** before merge to production where headcount allows; protected main branch.
- **Secrets hygiene** — secret scanning enabled; no credentials in code or logs.
- **Dependency & supply-chain security** — automated dependency scanning (e.g. Dependabot/equivalent) and timely patching of vulnerable libraries.
- **Application security** — input validation, output encoding, parameterised queries, authentication/authorisation checks, protection against OWASP Top 10 risks.
- **Environment separation** — production, staging and development environments separated; **production Class 1 data is never used in non-production environments** (use synthetic/anonymised test data).
- **CI/CD** — automated build, test and deploy pipelines with access controls on deployment. [PLACEHOLDER: CI/CD tooling].
- ⚠️ **SECURITY** — formalise security testing (SAST/DAST) in the pipeline as the team matures.

---

## 8. (Reserved — see Section 9 for third-party management)

*Section intentionally consolidated into Section 9.*

---

## 9. Third-party & sub-processor management

### 9.1 Inventory & due diligence
- Faresay maintains a register of all sub-processors / vendors that process Faresay data, the data classes involved, and their locations. [PLACEHOLDER: sub-processor register].
- Vendors handling Class 1/Class 2 data are subject to security due diligence proportionate to risk (e.g. SOC 2 / ISO 27001 evidence, security questionnaire).

### 9.2 Contracts — DPAs and BAAs ⚠️ COUNSEL
- **UK/EU:** a **Data Processing Agreement (DPA)** compliant with UK GDPR Art 28 is required with every processor handling personal data, including appropriate international-transfer terms (IDTA/SCCs).
- **US / HIPAA:** where Faresay is a **covered entity or business associate** and a vendor will create, receive, maintain or transmit **PHI**, a **HIPAA Business Associate Agreement (BAA)** is **mandatory** before any PHI is shared. This includes hosting, storage, email, video/session, and analytics providers that touch PHI. ⚠️ **COUNSEL.**
- ⚠️ **SECURITY / COUNSEL** — confirm which of the current providers (Vercel, Cloudflare, and the to-be-confirmed database/email/payment/video providers) will sign a BAA and offer a HIPAA-eligible plan; some default plans do **not** include a BAA. Do not transmit PHI to any provider without a signed BAA.

---

## 10. (Reserved)

*See Section 11.*

---

## 11. Logging, monitoring & audit trails

- **Audit logging** — access to and changes affecting Class 1 (mental-health/PHI) and Class 2 data are logged with user identity, timestamp and action, to support HIPAA audit-control requirements (45 CFR §164.312(b)) and UK GDPR accountability. ⚠️ **SECURITY** — confirm application-level audit logging covers reads of clinical data, not just writes.
- **Security monitoring** — infrastructure, authentication and application logs collected and reviewed; alerting on suspicious activity (e.g. failed-login spikes, privilege changes). [PLACEHOLDER: logging/monitoring/SIEM tooling].
- **Log protection & retention** — logs protected against tampering and unauthorised access, and retained for [PLACEHOLDER: retention period — align with HIPAA's 6-year documentation retention and ICO guidance]. ⚠️ **COUNSEL.**
- **No sensitive data in logs** — Class 1 content and secrets must not be written to application logs.

---

## 12. Vulnerability management & penetration testing

- **Patch management** — operating systems, dependencies and platform components kept up to date; critical vulnerabilities remediated on a defined SLA (target: [PLACEHOLDER: e.g. critical within 7 days]).
- **Vulnerability scanning** — regular automated scanning of dependencies and, where applicable, infrastructure.
- **Penetration testing** — independent penetration test of the Platform before US launch and at least annually / on major change thereafter. [PLACEHOLDER: pentest provider/cadence]. ⚠️ **SECURITY.**
- **Coordinated disclosure** — a channel for reporting vulnerabilities ([PLACEHOLDER: security@ address]) and a triage process.

---

## 13. Backup, disaster recovery & business continuity

- **Backups** — regular automated backups of production data, encrypted at rest, with backup integrity/restore testing. [PLACEHOLDER: backup solution, frequency, retention].
- **Recovery objectives** — defined **RPO** and **RTO**: [PLACEHOLDER: RPO/RTO targets]. ⚠️ **SECURITY.**
- **Disaster recovery** — documented procedure to restore service after major failure; reliance on managed providers (Vercel, Cloudflare, and the database provider) is noted, with their resilience/SLA considered.
- **Business continuity** — plan for continuity of essential operations (including client safety and crisis pathways — see [crisis-safeguarding-policy.md]) during disruption. ⚠️ **CLINICAL / SECURITY.**

---

## 14. Incident response & breach notification ⚠️ COUNSEL

### 14.1 Incident response
- A documented incident-response process covers detection, triage, containment, eradication, recovery, notification and post-incident review.
- All personnel must report suspected incidents immediately to the Security Lead. [PLACEHOLDER: reporting channel].
- Incidents are logged and assessed for severity and for whether a notifiable personal-data breach has occurred.

### 14.2 UK breach notification
- Where a personal-data breach is likely to result in a risk to individuals' rights and freedoms, Faresay (or the responsible controller) notifies the **ICO without undue delay and within 72 hours** of becoming aware (UK GDPR Arts 33–34).
- Where the breach is likely to result in a **high risk**, affected individuals are notified without undue delay.
- ⚠️ **COUNSEL** — confirm Faresay's notification role given the controller/processor split; a processor must notify the controller without undue delay rather than the regulator directly.

### 14.3 US breach notification (on US launch)
- The **HIPAA Breach Notification Rule** (45 CFR §§164.400–414) requires, for breaches of unsecured PHI, notification to affected individuals (generally within **60 days**), to **HHS**, and — for larger breaches — to the media; business associates must notify the covered entity.
- **State Attorney General / state breach-notification laws** impose additional and varying obligations across the 50 states + DC (timing, content, AG notice), and consumer-health-data laws (e.g. Washington **My Health My Data Act**) may add further requirements.
- ⚠️ **COUNSEL** — build a state-by-state breach-notification matrix before US launch; obligations and deadlines vary materially by state.

---

## 15. Personnel security

- **Background checks** — pre-engagement screening proportionate to role and access to Class 1 data, subject to local law (e.g. UK DBS where appropriate; US background checks). ⚠️ **COUNSEL** — confirm lawful basis/limits for screening in each jurisdiction. (Clinician licensing/verification is handled separately under the [Therapist Agreement](therapist-agreement.md) and clinical governance.)
- **Confidentiality agreements** — all personnel with access to Class 1/Class 2 data sign confidentiality / NDA terms.
- **Security & data-protection training** — at onboarding and at least annually, including phishing awareness and handling of mental-health data; HIPAA workforce training before US launch (45 CFR §164.308(a)(5)).
- **Sanctions** — defined consequences for policy violations.

---

## 16. Physical security

- Faresay is a [PLACEHOLDER: remote-first?] organisation relying primarily on **cloud-hosted** infrastructure; physical data-centre security is inherited from providers (Vercel, Cloudflare, and the database provider) and evidenced via their certifications (e.g. SOC 2 / ISO 27001).
- **Endpoint security** — personnel devices accessing Faresay data must use full-disk encryption, screen lock, current OS/security updates, and reputable endpoint protection; lost/stolen devices reported immediately.
- **Workspace** — Class 1 data must not be viewed in insecure public settings; clear-screen/clear-desk discipline applies.
- ⚠️ **SECURITY** — confirm any office/physical access controls and mobile-device management (MDM). [PLACEHOLDER: MDM solution].

---

## 17. Acceptable use

- Faresay systems and data are used only for authorised business purposes.
- No sharing of credentials; no exporting or copying Class 1 data outside approved systems; no use of unapproved tools/services (including AI tools) to process Class 1/Class 2 data without authorisation.
- Personnel must protect devices and credentials, follow this policy, and report security concerns.
- ⚠️ **SECURITY** — define an approved-tools list and rules for any AI/LLM tooling that could expose mental-health data.

---

## 18. Mapping to HIPAA Security Rule safeguards ⚠️ COUNSEL

The following maps this policy to the HIPAA Security Rule safeguard categories. This is a **planning aid for US launch**, not a confirmation of compliance, and assumes Faresay is a covered entity and/or business associate (to be confirmed). ⚠️ **COUNSEL.**

### 18.1 Administrative safeguards (45 CFR §164.308)
- Security Management Process / risk analysis & risk management — Sections 3, 12; [risk-register.md].
- Assigned Security Responsibility (Security Official) — Section 3. ⚠️ **COUNSEL** (appoint).
- Workforce Security & Information Access Management — Sections 4, 15.
- Security Awareness & Training — Section 15.
- Security Incident Procedures — Section 14.
- Contingency Plan (backup, DR, emergency mode) — Section 13.
- Evaluation — Section 21 (periodic review).
- Business Associate Contracts — Section 9 (BAAs).

### 18.2 Physical safeguards (45 CFR §164.310)
- Facility Access Controls — Section 16 (inherited from providers).
- Workstation Use & Security — Sections 16, 17.
- Device & Media Controls (disposal, re-use, accountability) — Sections 16, 19.

### 18.3 Technical safeguards (45 CFR §164.312)
- Access Control (unique user ID, automatic logoff, encryption/decryption) — Sections 4, 5.
- Audit Controls — Section 11.
- Integrity — Sections 5, 7, 11.
- Person/Entity Authentication — Section 4 (MFA).
- Transmission Security — Section 5 (TLS).

⚠️ **COUNSEL / SECURITY** — a full HIPAA Security Rule gap assessment, risk analysis and documentation set must be completed before US launch.

---

## 19. Data retention, minimisation & secure disposal

- **Minimisation** — Faresay collects and retains only the data necessary for the purposes set out in the [Privacy Policy](privacy-policy.md).
- **Retention** — data retained per a defined retention schedule. Note that **clinical records are typically owned and retained by the clinician** under professional/clinical-records rules; Faresay's retention of platform data is separate. [PLACEHOLDER: retention schedule]. ⚠️ **COUNSEL / CLINICAL.**
- **Secure disposal** — data securely deleted/anonymised at end of retention; media sanitised or providers' certified-destruction processes relied upon; backups age out per the backup retention policy.
- ⚠️ **COUNSEL** — reconcile retention with UK GDPR storage limitation, HIPAA's 6-year documentation retention, and clinical-records retention rules, which differ.

---

## 20. Alignment to a recognised framework (future goal)

Faresay's security programme is structured to align over time with a recognised framework. As a **bootstrapped, early-stage** company, formal certification is a **future goal** rather than a current state. Candidate frameworks:
- **SOC 2 (Type II)** — likely the most market-relevant signal for a US healthtech marketplace and enterprise/clinician trust.
- **ISO/IEC 27001** — internationally recognised ISMS certification.
- **NIST Cybersecurity Framework / NIST 800-53** — useful as a control reference.

⚠️ **SECURITY** — agree the target framework and a realistic roadmap (likely: implement controls now, pursue SOC 2 around US launch).

---

## 21. Policy review cadence

- This policy is reviewed at least **annually** and after any major change to systems, processing, regulation, or following a significant incident.
- The Security Lead owns the review; the DPO/privacy lead and counsel review data-protection and regulatory aspects.
- Version history and review dates are maintained below.

| Version | Date | Author | Notes |
|---|---|---|---|
| v0.1 (DRAFT) | [PLACEHOLDER: date] | [PLACEHOLDER: author] | Initial draft for security + legal review. |

---

> **End of draft.** ⚠️ This document is a v0.1 draft and must be validated by qualified security and legal professionals, with all `[PLACEHOLDER: …]` items resolved, before it is relied upon or published.
