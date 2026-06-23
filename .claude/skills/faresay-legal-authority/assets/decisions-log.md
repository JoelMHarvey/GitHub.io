# Faresay Legal-Authority — Decisions & Action Log

Append-only. The agent adds an entry for every draft prepared, approval requested, decision
made, cost flagged, commitment agreed, and notable inbound item. Newest at the top.

Format:

```
## YYYY-MM-DD — {short title}
- TYPE: {draft | approval-request | approved | rejected | sent | inbound | cost | commitment | note}
- WHAT: {what happened, plainly}
- COST: {£/$ or none}
- STATUS: {pending Joel | done | awaiting reply}
- LINK: {Gmail draft/thread or file ref}
- NEXT: {next action + date}
```

---

<!-- entries below -->

## 2026-06-23 — Email infra decisions
- TYPE: note
- WHAT: faresay.com confirmed on Cloudflare DNS + Vercel host. Email infra = Cloudflare Email
  Routing. Mailbox = DEDICATED Faresay mailbox (not Joel's personal Gmail). email-setup.md made
  Cloudflare-specific. Awaiting Joel: create dedicated mailbox → repoint Gmail connector → run
  Cloudflare routing. Agent will create faresay/* labels + triage once connector points to the
  dedicated mailbox (must NOT label Joel's personal inbox).
- COST: none
- STATUS: awaiting Joel (mailbox creation + connector + Cloudflare clicks)
- NEXT: On confirmation the dedicated mailbox is connected, create labels and begin triage; in
  parallel, prep counsel shortlist + intro drafts for approval.

## 2026-06-23 — Skill scaffolded
- TYPE: note
- WHAT: Skill created. Mailbox plan + roadmap + approval protocol established. PR #1 opened
  (Joel merges himself).
- COST: none
- STATUS: done
- NEXT: Email infra (above), then Phase 1 (retain healthcare-regulatory counsel).
