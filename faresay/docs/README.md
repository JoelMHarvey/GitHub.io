# Faresay — Docs

Working documents for **Faresay Ltd** (company no. 17302034). Faresay is **practice-management software** that UK therapists subscribe to (B2B SaaS) — not a marketplace.

> Marketplace-era strategy/legal drafts have been removed. They remain in git history if ever needed.

## Current documents

| Document | File | Status |
|---|---|---|
| Privacy Policy | `privacy-policy.md` | Draft for counsel |
| Terms of Service | `terms-of-service.md` | Draft for counsel |
| Therapist Agreement | `therapist-agreement.md` | Draft for counsel |
| **Data Processing Agreement (Art 28)** | `data-processing-agreement.md` | Draft for counsel |
| — TOMs (Annex 2) | `technical-organisational-measures.md` | Draft |
| — Sub-processor List (Annex 3) | `sub-processor-list.md` | Draft |
| Record of Processing Activities (Art 30) | `record-of-processing-activities.md` | Draft |
| Data Protection Impact Assessment (Art 35) | `data-protection-impact-assessment.md` | Draft |
| Security & Data Protection Policy | `security-data-protection-policy.md` | Draft |
| Clinical Governance Policy | `clinical-governance-policy.md` | Draft |
| Crisis & Safeguarding Policy | `crisis-safeguarding-policy.md` | Draft |

## Build

```bash
python3 build-branded-docs.py      # md → branded print-ready HTML (rendered/)
python3 build-solicitor-pack.py    # one combined UK Legal & Compliance Pack PDF
```

Brand assets (logos, tokens, guidelines) live in `../brand/`.
