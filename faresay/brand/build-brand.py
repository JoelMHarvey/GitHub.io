#!/usr/bin/env python3
"""
Build the Faresay Brand Guidelines: markdown -> branded print-ready PDF, and
rasterise the SVG logo assets -> transparent PNGs (3x). Mirrors the docs pipeline.

Usage:  python3 faresay/brand/build-brand.py
Output: faresay/brand/rendered/Faresay-Brand-Guidelines.pdf
        faresay/brand/assets/png/*.png
"""
import os, re, subprocess, markdown

BRAND = os.path.dirname(os.path.abspath(__file__))
ASSETS, RENDER = os.path.join(BRAND, "assets"), os.path.join(BRAND, "rendered")
PNG = os.path.join(ASSETS, "png")
TEAL, DARK = "#217567", "#193e39"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = f"""
@page {{ size:A4; margin:18mm 16mm; }}
*{{box-sizing:border-box;}} html{{-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;color:#2b3338;line-height:1.6;margin:0;font-size:12.5px;}}
.cover{{height:250mm;display:flex;flex-direction:column;justify-content:center;page-break-after:always;padding:0 6mm;}}
.cover .wm{{font-family:Georgia,'Times New Roman',serif;font-size:60px;font-weight:700;color:{DARK};letter-spacing:-1px;}}
.cover .sub{{color:#6b7a80;font-size:16px;margin-top:8px;}}
.content{{padding:0 4mm;}}
h1{{font-family:Georgia,serif;font-size:26px;color:{DARK};border-bottom:3px solid {TEAL};padding-bottom:8px;margin:34px 0 16px;page-break-before:always;}}
h1:first-of-type{{page-break-before:avoid;}}
h2{{font-size:17px;color:{DARK};margin:24px 0 8px;}}
h3{{font-size:14px;color:#33474a;margin:18px 0 6px;}}
p,li{{margin:7px 0;}} ul,ol{{padding-left:20px;}}
a{{color:{TEAL};text-decoration:none;}}
img{{max-width:100%;margin:10px 0;}}
code{{background:#f1f4f4;padding:1px 5px;border-radius:4px;font-size:11.5px;}}
blockquote{{margin:12px 0;padding:8px 16px;border-left:4px solid {TEAL};background:#f3f8f7;color:#33474a;font-size:11.5px;}}
hr{{border:0;border-top:1px solid #e6eaea;margin:22px 0;}}
"""

def build_pdf():
    md = open(os.path.join(BRAND, "brand-guidelines.md")).read()
    md = re.sub(r"\A\s*#\s+.*\n", "", md, count=1)  # drop H1 (cover)
    body = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"]).convert(md)
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="cover"><div class="wm">faresay</div><div class="sub">Brand Guidelines · v1.0 · June 2026</div></div>
<div class="content">{body}</div></body></html>"""
    hp = os.path.join(RENDER, "brand-guidelines.html")
    open(hp, "w").write(html)
    pdf = os.path.join(RENDER, "Faresay-Brand-Guidelines.pdf")
    if os.path.exists(CHROME):
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf}", "file://" + hp], check=True, capture_output=True)
        print(f"  ✓ {pdf}")
    else:
        print("  ! Chrome not found — open brand-guidelines.html and Print → PDF")

def build_pngs():
    os.makedirs(PNG, exist_ok=True)
    if not os.path.exists(CHROME):
        print("  ! Chrome not found — skipping PNG export"); return
    for name, w, h in [("logo-primary", 560, 170), ("mark", 160, 160), ("logo-mono-black", 560, 170),
                       ("logo-mono-white", 560, 170), ("favicon", 120, 120), ("pattern-petals", 480, 480)]:
        out = os.path.join(PNG, name + "@3x.png")
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                        "--default-background-color=00000000", "--force-device-scale-factor=3",
                        f"--window-size={w},{h}", f"--screenshot={out}",
                        "file://" + os.path.join(ASSETS, name + ".svg")], check=True, capture_output=True)
        print(f"  ✓ {out}")

if __name__ == "__main__":
    os.makedirs(RENDER, exist_ok=True)
    build_pdf()
    build_pngs()
