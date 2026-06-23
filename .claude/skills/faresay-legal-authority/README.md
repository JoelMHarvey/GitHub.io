# Faresay Legal-Authority Agent (Claude skill)

A Claude skill that runs an agent — on Joel's behalf — to drive **Faresay** (a therapy
marketplace) toward **full legal authority to operate in every US state**, and to handle the
correspondence that requires. Every outbound action and every cost is gated behind Joel's
explicit approval.

## What it does

- Sets up and operates the `legal@faresay.com` / `enquiries@faresay.com` mailboxes (forwarding
  into one agent-managed Gmail).
- Triages inbound legal/business mail, drafts outbound correspondence to attorneys, registered-
  agent services, state boards and vendors, and advances a phased state-by-state roadmap.
- Routes **every** send, spend, and commitment through an approval gate. The connected Gmail
  tools can draft and label but **cannot send** — so the agent physically cannot act alone.

## How to use it

In a Claude session with this repo, invoke the skill (`faresay-legal-authority`) and tell it
what to work on (e.g. "set up the mailboxes", "shortlist healthcare-regulatory counsel",
"triage the inbox"). It reads `references/brief.md` for its mandate each time.

## Files

```
SKILL.md                       The playbook Claude follows (rules, session loop, approval gate)
references/
  brief.md                     The mandate — Joel edits this to steer the agent
  legal-roadmap.md             US therapy-marketplace legal landscape + phased plan
  approval-protocol.md         The approve/reject mechanism + Gmail label scheme
  email-setup.md               How to stand up legal@/enquiries@ forwarding
  contact-targets.md           Who to contact, in what order
assets/
  templates/                   Ready-to-fill email + approval-request templates
  state-tracker.csv            50 states + DC progress tracker
  decisions-log.md             Append-only decision/action log
```

## Steering it

Edit `references/brief.md` to change objectives, add instructions, or set focus. The "approve
everything" rule and "agent cannot send" design are deliberate safety guardrails — keep them.

## Not legal advice

This skill coordinates qualified professionals; it does not replace them. The legal structure —
especially the Corporate-Practice-of-Medicine and fee-splitting questions around the 15% fee —
must be validated by licensed US healthcare-regulatory counsel.
