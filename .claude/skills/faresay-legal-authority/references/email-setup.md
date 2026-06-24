# Email Setup — legal@ / enquiries@ → agent mailbox

**Goal:** `legal@faresay.com` and `enquiries@faresay.com` both deliver into one mailbox the
agent can read/draft/label via the Gmail tools. Joel owns the `faresay.com` domain.

Do this **once**, with Joel, before operating the inbox. It involves DNS/mail changes on a
domain Joel owns — so it is itself an **approval-gated** action: propose the exact records,
get approval, then make the change (or have Joel make it).

## Current Faresay setup (confirmed)

- **DNS:** Cloudflare. **Site host:** Vercel. → Use **Cloudflare Email Routing** (free) for the
  forwards. It only adds MX/TXT records; it does **not** affect the Vercel site (A/CNAME for the
  web app are untouched).
- **Destination mailbox: DEDICATED — `totallycosmicturtle@gmail.com`** (chosen by Joel; separate
  from his personal Gmail). This mailbox is the Cloudflare-forwarding **destination** and is the
  one that must be **connected to the Gmail tools** (point the Claude Gmail connector at it). The
  agent does **not** touch Joel's personal inbox.

  **Prerequisite order:** (1) Cloudflare Email Routing → forward `legal@`/`enquiries@` to
  `totallycosmicturtle@gmail.com` → (2) point the Gmail connector at that mailbox → (3) agent
  creates `faresay/*` labels and begins triage there.

## Primary path — Cloudflare Email Routing (Joel does this in the dashboard)

There is no Cloudflare tool connected here, so Joel performs these clicks; the agent supplies the
exact values and verifies delivery afterward.

1. Cloudflare dashboard → select `faresay.com` → **Email** → **Email Routing** → enable.
   Cloudflare auto-adds the required **MX** and **TXT (SPF)** records — accept them.
2. **Destination addresses:** add `totallycosmicturtle@gmail.com` and click the Cloudflare
   verification link sent to it (the agent can read that verification email via the Gmail tools
   and surface the link to Joel).
3. **Custom addresses:** create two routes —
   - `legal@faresay.com` → **Send to** → `totallycosmicturtle@gmail.com`
   - `enquiries@faresay.com` → **Send to** → `totallycosmicturtle@gmail.com`
   - ⚠️ Check first for any **existing MX/SPF** records on faresay.com and resolve conflicts before
     enabling (two MX setups will fight). Email Routing only adds MX + TXT — Vercel web records
     (A/CNAME) are untouched.
4. **DMARC (recommended):** add a TXT record `_dmarc.faresay.com` →
   `v=DMARC1; p=none; rua=mailto:legal@faresay.com` to start in monitoring mode.

### Sending *as* faresay.com (so replies look right)

Cloudflare Email Routing is **receive/forward only** — it cannot send. Combined with the Gmail
tools (which also cannot send), every outbound message is a draft Joel sends manually. For
replies to appear **from** `legal@faresay.com`, set up Gmail **"Send mail as"** with that alias.
That requires an SMTP sender for the alias (e.g. a transactional-email provider, or a Google
Workspace mailbox on faresay.com). This is an optional polish step — flag it to Joel as a small
follow-on, not a blocker for receiving and triaging mail.

## Alternative — if the domain ever moves to Google Workspace

Add `legal@`/`enquiries@` as aliases/Groups forwarding to the agent mailbox, configure send-as,
and confirm SPF/DKIM/DMARC. (Not needed while on Cloudflare + Vercel.)

## Verification checklist (any path)

- [ ] Test email to `legal@faresay.com` lands in the agent mailbox.
- [ ] Test email to `enquiries@faresay.com` lands in the agent mailbox.
- [ ] Gmail tools can **search/read** those threads.
- [ ] A draft can be created with **from = the faresay.com alias**.
- [ ] SPF/DKIM/DMARC pass (so Faresay's mail isn't flagged as spam).
- [ ] Labels `faresay/*` created (see `approval-protocol.md`).

## Security note

Run the **Malwarebytes reputation tools** on any unexpected sender, link, or phone number that
arrives at these addresses before trusting or acting on it. Legal/vendor inboxes attract
phishing and invoice fraud — treat payment-detail or "urgent wire" requests with extra scrutiny
and always route to Joel.
