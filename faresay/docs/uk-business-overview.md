# UK Business Overview

> One-page context for advisers. **Preparatory material — not legal advice.** UK launch scope only;
> US plans are deliberately excluded from this document.

## What Faresay is

Faresay is a **two-sided online marketplace** that connects people seeking therapy with vetted,
independent, **UK-registered** mental-health professionals. The platform provides discovery,
matching, scheduling, secure video sessions, and payment handling. Therapists deliver the clinical
work; Faresay provides the technology and the introduction.

- **What it is:** a technology + marketing platform between independent therapists and self-pay clients.
- **What it is not:** not a healthcare provider; not an employer of the therapists; not a crisis
  service; no insurance billing; no prescribing; no NHS contract.

## How it works

1. Client searches and is matched to a suitable therapist.
2. Client books and pays through the platform (card, via Stripe).
3. Therapist and client meet over secure video.
4. Faresay retains a **15% platform fee** (10% for founding therapists) and pays the remainder to the
   therapist. The fee is characterised as a **platform/technology + marketing fee**, not a share of
   the clinician's professional fee.

## Who the therapists are

Independent, self-employed practitioners who must hold membership of an appropriate UK professional
body / **PSA-accredited register** (e.g. BACP, UKCP, NCPS) or statutory registration where relevant
(e.g. HCPC for practitioner psychologists), and carry their own professional indemnity insurance.
Faresay vets credentials before a profile goes live.

## Commercials (directional)

| Item | Value | Note |
|---|---|---|
| Platform fee | 15% | 10% for founding therapists |
| Model | Self-pay / private | No insurance billing |
| Client payment | Per session, upfront | Stripe Connect |
| Therapist status | Self-employed | Not employed by Faresay |
| Stage | Pre-launch (UK) | Companies House + counsel in progress |

## Current technology stack (relevant to data questions)

- **Auth:** Clerk · **Database:** Neon Postgres (EU region) · **Video:** Daily.co · **Email:** Resend ·
  **Payments:** Stripe.
- Several processors are **US-headquartered** — see the data-protection section of the UK Legal &
  Regulatory Brief for the international-transfer question.

## The single biggest open dependency

UK regulatory and contractual structuring — confirmed by a solicitor — before taking live payments.
This document set is the input to that conversation.
