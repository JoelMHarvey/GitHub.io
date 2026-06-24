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

### Sending *as* faresay.com — CONFIGURED via Resend
Cloudflare Email Routing is receive-only, so outbound send-as is handled by **Resend** (SMTP relay):
- Gmail **"Send mail as" `legal@faresay.com`** in `totallycosmicturtle@gmail.com`, sending through
  Resend SMTP (`smtp.resend.com`, port 465/587, username `resend`, password = Resend API key —
  **the key lives in Gmail/Resend, NOT in this repo**).
- `faresay.com` verified in Resend with DKIM + SPF in Cloudflare DNS (SPF merged into one record).
- ⚠️ **Final step to complete send-as:** click the Gmail "Send Mail as" confirmation link that
  Gmail emails to `legal@faresay.com` (it routes into the agent inbox). Until clicked, Gmail
  cannot send from the alias.
- Reminder: the Gmail **tools** still cannot send — every send is Joel's manual click on a
  prepared draft. Resend only changes the *From* address.

### Branding — all external outbound on Faresay letterhead
Every external email sent from Faresay must use the **HTML letterhead** template at
`assets/templates/email-letterhead.html` (Faresay wordmark header + standard footer with
`legal@faresay.com`, faresay.com, and a confidentiality line). Internal approval-summary notes to
Joel can be plain text. Drafts the agent prepares should be created as **HTML drafts** built from
the letterhead, with the message body slotted in.

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
