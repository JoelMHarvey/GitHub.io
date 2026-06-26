# Faresay — Brand Assets

Brand Identity Package (v1.0). The single home for logos, tokens and guidelines.

## Contents

```text
brand/
├─ brand-guidelines.md          # the full guidelines (source)
├─ tokens.json                  # colours + type for dev / Figma (Tokens Studio)
├─ build-brand.py               # md → branded PDF + SVG → PNG export
├─ assets/
│  ├─ logo-primary.svg          # mark + wordmark (horizontal lockup)
│  ├─ mark.svg                  # lotus mark alone (icon/avatar)
│  ├─ logo-mono-black.svg       # single-ink lockup (light backgrounds)
│  ├─ logo-mono-white.svg       # single-ink lockup (dark backgrounds)
│  ├─ favicon.svg               # app icon (lotus in teal rounded square)
│  ├─ pattern-petals.svg        # tileable background texture
│  └─ png/                      # 3× transparent PNG exports of the above
└─ rendered/
   └─ Faresay-Brand-Guidelines.pdf   # print-ready guidelines (7 pp)
```

## Formats & how to get the rest

| Need | Have | How |
|---|---|---|
| **SVG** | ✓ `assets/*.svg` | source vectors |
| **PNG** | ✓ `assets/png/*@3x.png` | run `build-brand.py` |
| **PDF** | ✓ `rendered/Faresay-Brand-Guidelines.pdf` | run `build-brand.py` (needs Chrome) |
| **AI** | — | open any SVG in Illustrator → Save As `.ai` |
| **Figma** | — | import `tokens.json` (Tokens Studio plugin) + drag in the SVG kit |

## Build

```bash
python3 faresay/brand/build-brand.py   # regenerates the PDF + PNGs
```

## Notes

- Wordmark is **Fraunces** (display); body is **Inter**. PNG/PDF render with the system serif (Georgia) where Fraunces isn't installed — outline the wordmark in your vector tool for the final locked logo.
- Colours mirror `src/app/globals.css` (the live site) — `tokens.json` is the shared source of truth.
- Photography / screenshots / press photos are not vector-generated — produce them to the style guide in `brand-guidelines.md` §7.
