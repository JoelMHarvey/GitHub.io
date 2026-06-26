# Faresay — sales & recruitment collateral

Built on the [design system](../design-system/) (tokens, fonts, mark). Current model — software subscription + small card commission, therapist owns their clients, **not** a marketplace.

| Piece | File | Pages |
|---|---|---|
| Therapist recruitment brochure | `therapist-recruitment-brochure.html` | 3 |
| Product one-pager | `product-one-pager.html` | 1 |
| Investor one-pager (confidential) | `investor-one-pager.html` | 1 |
| Pricing sheet | `pricing-sheet.html` | 1 |

Print-ready PDFs in `rendered/`.

## Build

```bash
python3 build-collateral.py   # HTML → A4 PDFs (needs Chrome; fonts load from Google Fonts)
```

## Already in the design system (no rebuild needed)
- **Social media kit** — `../design-system/social/` (LinkedIn, Instagram, Facebook, X, YouTube at native sizes).
- **Marketing + app UI kits** — `../design-system/ui_kits/`.
- **Onboarding video** — `../design-system/video/`.

> Heads-up: some bundled DS copy/examples still use the **old marketplace model** ("15%", "up to 90%", "matched with clients"). The visual system is current; reword any copy to the subscription/ownership model before publishing. See the note at the top of `../design-system/readme.md`.
