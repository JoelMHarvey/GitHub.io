# Email Setup — legal@ / enquiries@ → agent mailbox

**Goal:** `legal@faresay.com` and `enquiries@faresay.com` both deliver into one mailbox the
agent can read/draft/label via the Gmail tools. Joel owns the `faresay.com` domain.

Do this **once**, with Joel, before operating the inbox. It involves DNS/mail changes on a
domain Joel owns — so it is itself an **approval-gated** action: propose the exact records,
get approval, then make the change (or have Joel make it).

## Decide the agent mailbox first

The Gmail tools operate on a connected Google mailbox. Simplest robust setup:
- A dedicated Gmail/Google Workspace mailbox (e.g. `faresay.agent@gmail.com` or a Workspace
  user) that is the one connected to these tools.
- `legal@faresay.com` and `enquiries@faresay.com` **forward** into that mailbox.
- Outbound, when Joel sends, should appear **from** the faresay.com address (send-as alias), so
  replies thread correctly. Configure send-as/alias in the mailbox settings with domain
  verification.

## Path A — Domain on Google Workspace (cleanest)

1. Add `legal@` and `enquiries@` as **users** or, cheaper, as **aliases / Google Groups** that
   forward to the agent mailbox.
2. Configure **send-as** so outbound can use `legal@faresay.com` / `enquiries@faresay.com`.
3. Confirm SPF/DKIM/DMARC are set so mail is trusted.

## Path B — Domain on WordPress.com (MCP can help)

The connected WordPress.com tools can manage DNS, nameservers, and mail service for a domain:
- `wpcom-domain-set-mail-service`, `wpcom-domain-update-dns-records`,
  `wpcom-domain-restore-default-dns-records`, `wpcom-domain-update-nameservers`.

Steps:
1. Confirm `faresay.com` is the domain and check its current mail service / DNS.
2. Either enable a mailbox/forwarding mail service on the domain, **or** set MX + forwarding
   records so `legal@` / `enquiries@` forward to the agent Gmail.
3. Verify SPF/DKIM/DMARC for deliverability.
4. **Propose the exact record changes to Joel as an approval request before applying them.**

## Path C — Other registrar/host (Cloudflare, GoDaddy, Namecheap, etc.)

1. In the host's DNS, use the provider's **email forwarding** (many offer free forwarding):
   create forwards `legal@faresay.com → agent mailbox` and `enquiries@faresay.com → agent mailbox`.
2. If no native forwarding, point MX to a forwarding service (e.g. Cloudflare Email Routing —
   free) and add the forward rules there.
3. Set up send-as alias in the agent Gmail and verify the domain.
4. Confirm SPF/DKIM/DMARC.

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
