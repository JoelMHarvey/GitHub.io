# Faresay — Documents Workspace

Working drafts for Faresay (therapy marketplace, UK → US, cash-pay, 15% fee, bootstrapped).
Start with **`CONTEXT.md`** — the shared fact sheet every document is kept consistent with.

> **Status legend:** ✅ review-ready draft · 🧩 structure drafted, numbers pending research ·
> ⚠️ needs professional (legal/clinical/security) sign-off before use.

| # | Document | File | Status |
|---|----------|------|--------|
| — | Shared fact sheet | `CONTEXT.md` | ✅ |
| ★ | **Business Plan** | `business-plan.md` | ✅ |
| ★ | Market Research Synthesis | `market-research-synthesis.md` | ✅ (directional) |
| 1 | Business Model Canvas | `business-model-canvas.md` | ✅ |
| 2 | Product Requirements Document | `product-requirements-document.md` | ✅ |
| 3 | Therapist Agreement | `therapist-agreement.md` | ✅ ⚠️ counsel |
| 4 | Terms of Service | `terms-of-service.md` | ✅ ⚠️ counsel |
| 5 | Privacy Policy | `privacy-policy.md` | ✅ ⚠️ counsel |
| 6 | Clinical Governance Policy | `clinical-governance-policy.md` | ✅ ⚠️ clinical |
| 7 | Crisis & Safeguarding Policy | `crisis-safeguarding-policy.md` | ✅ ⚠️ clinical |
| 8 | Financial Model | `financial-model.md` + `.csv` | ✅ structure + benchmark ranges |
| 9 | Risk Register | `risk-register.md` | ✅ |
| 10 | Security & Data Protection Policy | `security-data-protection-policy.md` | ✅ ⚠️ counsel/security |

## How these fit together
- **Business plan** (being assembled from market research) is the parent narrative; the **Business
  Model Canvas** is its one-page summary and the **Financial Model** its numbers.
- The **legal/clinical policies** are review-ready first drafts so retained counsel and a clinical
  advisor *edit* rather than draft from scratch (saves fees). Every one is watermarked and flags
  the specific points needing sign-off with `⚠️ COUNSEL` / `⚠️ CLINICAL` / `⚠️ SECURITY`.
- The **legal authorisation workstream** (entity, CPOM/fee-splitting, 50-state qualification,
  counsel shortlist) lives in the skill: `.claude/skills/faresay-legal-authority/`.

## Cross-cutting items most needing professional sign-off
1. **15%-fee characterisation & MSO/PC structure** (CPOM/fee-splitting) — affects Therapist
   Agreement, ToS, Business Model Canvas. ⚠️ COUNSEL
2. **HIPAA covered-entity vs business-associate + controller/processor roles** — affects Privacy,
   Security, Therapist Agreement. ⚠️ COUNSEL
3. **Clinical screening/exclusion thresholds & duty-to-warn/mandatory-reporting matrix** — affects
   Clinical Governance and Crisis/Safeguarding. ⚠️ CLINICAL/COUNSEL

## Next
- Populate the Financial Model and the business plan's market/competitive/unit-economics sections
  when the research completes.
