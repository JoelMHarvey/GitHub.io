# Approval Protocol

The core safety mechanism. **Every** outbound action and **every** cost passes through this
gate before it happens. The agent prepares; Joel decides; only then does anything leave.

## Why the gate is airtight

The connected Gmail tools can **read, draft, and label — but not send**. So the agent literally
cannot dispatch mail or commit money on its own. The act of *sending* a draft (a click in
Gmail) is Joel's, and that click is the approval. This is a feature, not a limitation — do not
seek a way around it.

## The approval-request format

For each item needing approval, produce this block. Keep it phone-readable: short, honest,
skimmable. Lead with what it is, what you're asking, the cost, and the risk.

```
FARESAY — APPROVAL NEEDED · [one-line subject]

WHAT THIS IS:   [1–2 plain-English sentences: who/what this concerns]
THE REQUEST:    [the single specific thing to approve — "send this email to X", "pay $Y for Z",
                 "book a 30-min call Tue 3pm", "agree these engagement terms"]
COST:           [exact £/$ amount and what it buys, or "none"]
COMMITMENT:     [what Faresay would be bound to, if anything — scope, term, deadline]
RISK:           [honest, brief: what could go wrong, how reversible it is]
RECOMMENDATION: [your recommendation and one-line why]

→ APPROVE   |   ✗ REJECT   |   ✎ CHANGES
DRAFT: [Gmail draft location / subject line, if the item is an email]
```

### Risk should always answer

- Is this reversible? (an email sent vs. a payment made vs. a signature)
- Does it create an ongoing obligation or recurring cost?
- Does it share anything sensitive externally?
- Is the counterparty trustworthy? (reputation-check unknowns first)

## How an item flows

1. **Prepare.** Compose the outbound email as a Gmail **draft**. Apply label
   `faresay/pending-approval`. Gather the facts for the approval block.
2. **Present.** Show Joel the approval block in-session. Optionally also create a **draft**
   summary email to `joelmharvey@gmail.com` titled `FARESAY — APPROVAL NEEDED · …` containing
   the same block, so he can review on his phone. (Joel sends/forwards it to himself, or simply
   reads it in this session — the agent can't send it for him.)
3. **Decide.** Joel responds:
   - **APPROVE** → he sends the prepared draft (or tells the agent he's sent it). Relabel
     `faresay/sent`. Log it.
   - **REJECT** → discard or archive the draft. Relabel `faresay/rejected`. Log the reason.
   - **CHANGES** → revise the draft and re-present. Stay on `faresay/pending-approval`.
4. **Record.** Append the outcome to `assets/decisions-log.md` and update the state tracker.

## Batching

When several low-risk items are ready (e.g. three near-identical registered-agent quote
requests), present them as a numbered list so Joel can reply "approve 1 and 3, reject 2" in one
message. Never batch anything with a cost or a commitment in with no-cost items silently —
costs are always called out individually.

## Gmail label scheme

| Label | Meaning |
|---|---|
| `faresay/inbound-new` | New incoming mail not yet triaged |
| `faresay/pending-approval` | Outbound draft awaiting Joel's decision |
| `faresay/approved` | Approved, ready for Joel to send |
| `faresay/sent` | Sent (by Joel) |
| `faresay/rejected` | Joel declined |
| `faresay/awaiting-reply` | Sent; waiting on counterparty |
| `faresay/needs-joel` | Inbound item that needs Joel's personal attention/decision |

## Optional future upgrade (not built — needs Joel's go-ahead)

True one-tap email **buttons** that reach Joel's phone require either (a) Gmail send scope +
a small approval web endpoint, or (b) a lightweight hosted approval page (e.g. a serverless
function) that records APPROVE/REJECT and triggers the send. This is a separate build with a
cost; flag it to Joel as an option if the manual draft-and-send flow becomes a bottleneck.
Until then, the draft + in-session approval flow above is the mechanism.
