# Faresay — Validation Experiment Setup (runbook)

> The hands-on steps to run the demand test in `validation-experiment.md`. **Mode chosen:
> demand-only, corridor-agnostic** — measure intent + price tolerance + CAC with **no therapy
> delivered and zero legal exposure during the test.** Assets live in `faresay/validation/`
> (`index.html` landing page, `funnel-tracker.csv`). Budget: ~£150 + a domain. Last updated: [PLACEHOLDER: date]

---

## What we're measuring (and the honest promise)
- **Intent** — `Lead` event (early-list signup).
- **Price tolerance** — `PriceIntent_120` event (clicked "Reserve my first session" at the £120 price).
- **CAC** — cost per lead, organic vs paid.

No session is delivered. Everyone who reserves is told honestly they're on a **priority list**, with
**no charge**. This sidesteps the cross-border legal gate entirely for the test phase.

## Setup checklist (≈ an afternoon)

### 1. Edit the landing page (3 placeholders)
Open `faresay/validation/index.html`, replace:
- `PLAUSIBLE_DOMAIN` → the domain you'll deploy to (e.g. `try.faresay.com`).
- `FORM_ENDPOINT` → your lead-capture POST URL (see step 3). *(Left as-is, the page still works and
  shows the thank-you — it just won't store emails. Set it so you capture leads.)*
- `[FOUNDER_NAME]` / `[FOUNDER_EMAIL]` → your name + a real reply address. (Swap the `JH` avatar
  initials too, or drop in a real photo `<img>`.)

### 2. Deploy it (pick one — all free)
- **Netlify Drop** (easiest): drag the `faresay/validation/` folder onto app.netlify.com/drop → instant URL.
- **Vercel:** `vercel` in the folder, or import as a static project.
- **GitHub Pages / Cloudflare Pages:** point at the folder.
- Optional: add a subdomain like `try.faresay.com` (CNAME to the host) so it's on-brand.

### 3. Lead capture (one of)
- **Formspree** (formspree.io) or **Basin** — create a form, paste its POST URL into `FORM_ENDPOINT`.
  The page submits via fetch and shows the inline thank-you. Leads land in your inbox/dashboard.
- **Tally / Google Form** — alternatively embed one and skip `FORM_ENDPOINT`.

### 4. Analytics — Plausible (you already use it)
- Add the **deploy domain** as a site in Plausible.
- Create two **custom-event goals**: `Lead` and `PriceIntent_120` (and optionally `CTA_Hero`).
- That's it — the page already fires these events.

### 5. Paid traffic — Google Ads (£150 cap)
- New Search campaign, objective **Leads**, **£5–10/day** (≈ £150 over 3 weeks).
- **Conversion:** import the Plausible `Lead` goal, or set a Google Ads conversion on the thank-you
  state. Track **cost per lead** directly.
- **Geo:** target English-speaking expat hubs (e.g. Japan, Singapore, UAE, Hong Kong, major EU
  cities) — language: English.
- **Keywords (exact/phrase), broad-expat intent:**
  - `english speaking therapist abroad`, `therapist for expats`, `online therapy for expats`,
    `expat therapy`, `english speaking counsellor abroad`, `therapy living abroad`,
    `expat mental health`, `culture shock therapy`, `relocation stress therapy`.
- **Ad copy (starting point):**
  - H: *Therapy that understands expat life* · *English-speaking, verified therapists*
  - D: *Living abroad is hard. Talk to a therapist who gets it — verified, English-speaking, in your timezone. Join the early list.*
- Negative keywords: `free`, `jobs`, `training`, `course`, `salary`.

### 6. Organic traffic (founder time — heed the rules)
- **Reddit/Facebook expat communities ban self-promo.** Do NOT drop links. Build standing: answer
  real questions for a week, then either (a) ask an admin's permission for one value-add post, or
  (b) put the link only where rules allow (some subs have a "promo" day / classifieds thread).
- **LinkedIn:** one founder post — why expat mental health is hard + the early-list link.
- Tag organic traffic with a UTM (e.g. `?utm_source=reddit`) so Plausible separates it from paid.

### 7. Run for ~3 weeks, log weekly in `funnel-tracker.csv`
Fill organic vs paid each week; the OUTPUT rows compute conversion %, cost per lead, cost per
price-intent.

## Decision rules (set now — don't move them)
- **KILL (thesis):** < ~10 leads **organically** in 3 weeks → the cheap high-trust engine doesn't exist.
- **KILL (paid):** paid **cost-per-lead > ~£40** before any delivery → paid can't carry it.
- **KILL (price):** leads sign up but **`PriceIntent_120` rate ≈ 0** → £120 willingness-to-pay is false.
- **PASS:** ≥ ~20 leads **and** Lead→Price-intent **> ~25%** **and** blended cost-per-lead projects a
  CAC **< ~£57** → proceed.

## If it PASSES — next three moves (in order)
1. **Cross-border legal memo** for the cleanest corridor (`cross-border-legal-gate.md`) before any supply spend.
2. **Seed 5–6 founding therapists** who bring a client book; concentrate demand (`gtm-strategy.md`).
3. Run the **30-day operator plan** (`gtm-strategy.md` §8) on the proven funnel.

## Ethics / safety notes
- Be honest: no charge, priority list, "not a crisis service" stated on the page and thank-you.
- Don't collect more data than email + (optional) country + free-text. Don't store anything sensitive.
- If a respondent signals crisis, reply pointing to local emergency/crisis resources — do not attempt support.

## Linked documents
- `validation-experiment.md` (the why + kill/pass) · `gtm-strategy.md` (funnel + 30-day plan)
- `cross-border-legal-gate.md` (corridor choice for after a pass) · `financial-model.md` (£120/CAC math)
- Assets: `faresay/validation/index.html` · `faresay/validation/funnel-tracker.csv`
