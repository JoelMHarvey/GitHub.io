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

## 2026-06-24 — Email infra live + counsel outreach prepared
- TYPE: draft / approval-request
- WHAT: Mailbox live (totallycosmicturtle@gmail.com via Cloudflare; receiving confirmed). Resend
  send-as legal@faresay.com confirmed. Created 7 faresay/* Gmail labels and the HTML letterhead.
  Prepared EBG outreach as a letterhead HTML Gmail DRAFT to alerman@ebglaw.com (in Drafts, awaiting
  Joel's approve+send; set From to legal@faresay.com). Nixon Gwilt & Cohen = web-form text provided
  to Joel to submit (Cohen likely paid consult — get fee first).
- COST: none yet (watch Cohen consult fee)
- STATUS: awaiting Joel — approve/send EBG draft; submit Nixon Gwilt + Cohen forms
- NEXT: On replies, triage into faresay/* labels and bring scope/fee comparisons for approval.

## 2026-06-23 — Phase 1 counsel: shortlist + chosen 3 + intake routes
- TYPE: note
- WHAT: Researched & shortlisted 5 firms; Joel chose the Recommended 3 — Epstein Becker Green
  (Amy Lerman, alerman@ebglaw.com — Telemental Health Laws survey lead), Nixon Gwilt Law
  (Get Started questionnaire), Cohen Healthcare Law Group (contact form / (310) 844-3173, likely
  paid initial consult). Outreach text drafted for all three. EBG = email (Gmail draft, approve-
  to-send); Nixon Gwilt & Cohen = web-form intakes Joel submits.
- COST: none yet (watch Cohen initial-consult fee — approve before booking)
- STATUS: awaiting dedicated mailbox (for EBG draft) + Joel to submit the two web forms
- NEXT: When mailbox live, create EBG Gmail draft for approval; provide form text for Nixon
  Gwilt & Cohen when Joel is ready to submit.

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
