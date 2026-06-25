# Faresay — Business Model Canvas

> Working draft. Consistent with `CONTEXT.md` (cash-pay therapy marketplace, 15% platform fee,
> UK now → US all-50-states, bootstrapped). Market-sizing figures in the business plan / financial
> model supersede any rough numbers here. Last updated: 26 June 2026

Faresay is a **two-sided marketplace**, so segments, value props, and channels are split between
**Clients** (people seeking therapy) and **Therapists** (licensed providers).

---

## 1. Customer Segments
**Clients (demand side)**
- Adults seeking talk therapy who pay **out of pocket** (cash-pay / out-of-network).
- Self-pay clients who value **choice, speed of access, and fit** over using insurance.
- People underserved by local in-person availability (rural/waitlist gaps); telehealth-comfortable.
- UK now; US adults at launch states first, scaling state-by-state.

**Therapists (supply side)**
- Licensed independent practitioners (psychologists, clinical social workers, counsellors,
  psychotherapists) — UK (BACP/HCPC/UKCP-registered) and, in the US, state-licensed clinicians.
- Private-practice clinicians who want **filled calendars without doing their own marketing**,
  and a lighter-touch tech/payments stack.

## 2. Value Propositions
**To clients**
- Fast access to **vetted, licensed** therapists and a good **match** for need, modality, identity.
- Transparent pricing, easy **booking, secure video, and payments** in one place.
- Continuity, reminders, and a trustworthy, privacy-first experience for sensitive care.

**To therapists**
- **Client acquisition** — a steady stream of suitable clients without marketing spend.
- **Lower admin** — scheduling, secure video, payments, and reminders handled.
- **Keep 85%** of the session fee; clinician retains clinical autonomy and owns the clinical record.
- (US) Help navigating **multi-state** practice via the platform's compliant structure.

## 3. Channels
- **Clients:** SEO/content, paid search & social, app stores, referrals/word-of-mouth, partnerships
  (employers, universities, communities — later), the faresay.com web app.
- **Therapists:** direct outreach, professional-body networks, referrals from existing providers,
  directory/SEO, therapist-focused content. ⚠️ healthcare advertising rules apply (see ToS/legal).

## 4. Customer Relationships
- **Self-service** discovery and booking, augmented by **matching** support.
- Trust built through **verification, reviews, transparency**, and responsive support.
- Therapist success/onboarding support; light-touch account management for high-volume providers.
- **Safety-critical boundary:** Faresay is *not* a crisis service — relationships and comms make
  this explicit (see `crisis-safeguarding-policy.md`).

## 5. Revenue Streams
- **Primary: 15% platform fee** on each completed paid session — characterised as a
  **technology + marketing platform fee**, not a clinical fee-split ⚠️ COUNSEL.
- Cash-pay/out-of-network; no insurance billing in the initial US model.
- **Potential future:** premium therapist subscriptions/tools, featured placement, employer/B2B
  packages, no-show fees. (All subject to the same fee-splitting/CPOM scrutiny ⚠️ COUNSEL.)

## 6. Key Resources
- The **marketplace platform** (matching, scheduling, secure telehealth video, payments, messaging).
- The **therapist supply network** (the hard-to-build, defensible asset).
- **Brand & trust**, especially around privacy and safety.
- **Regulatory/compliance posture** (US entity + MSO/PC structure, licensure verification) — a moat
  and a barrier to entry once built.
- Lean founding team + capital efficiency (bootstrapped).

## 7. Key Activities
- **Two-sided growth:** acquire therapists and clients in balance, market-by-market.
- **Credentialing & verification** of providers (licensure, insurance, background) and ongoing
  monitoring.
- **Matching** clients to suitable therapists.
- **Trust & safety / clinical governance** (see clinical-governance & crisis-safeguarding policies).
- **Product development** and reliability of the booking/video/payment core.
- **Regulatory expansion** — qualifying state-by-state (see the legal skill roadmap).

## 8. Key Partnerships
- **Payment processor** (e.g. Stripe-class) for marketplace payouts/split.
- **Telehealth video** infrastructure (HIPAA-eligible) ⚠️ SECURITY/COUNSEL.
- **Licensure-verification / background-check** vendors.
- **US healthcare-regulatory counsel** + **registered-agent / entity-compliance** provider
  (see `assets/counsel-shortlist.md`).
- **Hosting/infra:** Vercel (web), Cloudflare (DNS/CDN).
- (Future) employers/EAPs, universities, professional bodies, insurers (if model expands).

## 9. Cost Structure
- **Client acquisition (CAC)** — the largest variable cost in a cash-pay model; marketing/paid.
- **Payment processing fees.**
- **Platform/infra & telehealth video** hosting.
- **Compliance:** legal (entity formation, multi-state qualification, registered agents), licensure
  verification, insurance (tech/cyber E&O).
- **Product & engineering**, trust & safety / support staff.
- **G&A.** Bootstrapped → tight burn; prioritise contribution-margin-positive growth.

---

### Strategic notes
- The model lives or dies on **two-sided liquidity** and **CAC payback** — cash-pay means
  acquisition cost must be earned back over a client's sessions; retention and sessions-per-client
  are the key levers (quantified in `financial-model.md`).
- The **15% take rate** is light vs. some marketplaces — attractive to therapists (aids supply),
  so volume and retention must carry the economics. Validate vs. market benchmarks (business plan).
- **Defensibility** compounds from supply density + trust/brand + the hard-won multi-state
  compliance posture — not from the software alone.
