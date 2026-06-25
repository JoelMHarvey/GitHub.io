#!/usr/bin/env python3
"""
Build the Faresay UK Legal & Compliance Pack — one combined, print-ready PDF
containing the policy/contract/compliance documents a UK solicitor reviews.

Renders a branded cover + contents, then each document on its own page(s),
then drives headless Chrome to produce a single PDF.

Usage:  python3 faresay/docs/build-solicitor-pack.py
Output: faresay/docs/rendered/uk-legal-pack.html
        faresay/docs/rendered/Faresay-UK-Legal-Pack.pdf
"""
import os
import re
import subprocess
import markdown

DOCS_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(DOCS_DIR, "rendered")
TEAL, DARK = "#1F6F6B", "#15514e"

FAVICON = (
    '<svg width="40" height="40" viewBox="0 0 28 28" xmlns="http://www.w3.org/2000/svg">'
    f'<circle cx="14" cy="14" r="14" fill="{TEAL}"/>'
    '<path d="M9 18c0-3 2-5 5-5s5 2 5 5M9.5 11.5c.8-1.2 2.3-2 4.5-2s3.7.8 4.5 2" '
    'fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/></svg>'
)

# Pack order — the documents a solicitor reviews, grouped.
PACK = [
    ("Client & customer terms", [
        ("privacy-policy.md", "Privacy Policy"),
        ("terms-of-service.md", "Terms of Service"),
        ("therapist-agreement.md", "Therapist Agreement"),
    ]),
    ("Data protection (processor model)", [
        ("data-processing-agreement.md", "Data Processing Agreement (UK GDPR Art 28)"),
        ("technical-organisational-measures.md", "Technical & Organisational Measures (Annex 2)"),
        ("sub-processor-list.md", "Sub-processor List (Annex 3)"),
        ("record-of-processing-activities.md", "Record of Processing Activities (Art 30)"),
        ("data-protection-impact-assessment.md", "Data Protection Impact Assessment (Art 35)"),
    ]),
    ("Operational policies", [
        ("security-data-protection-policy.md", "Security & Data Protection Policy"),
        ("clinical-governance-policy.md", "Clinical Governance Policy"),
        ("crisis-safeguarding-policy.md", "Crisis & Safeguarding Policy"),
    ]),
]

CSS = f"""
@page {{ size:A4; margin:18mm 16mm; }}
* {{ box-sizing:border-box; }}
html {{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
body {{ font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
  color:#2b3338; line-height:1.55; margin:0; font-size:12.5px; }}
.cover {{ height:248mm; display:flex; flex-direction:column; justify-content:center;
  page-break-after:always; padding:0 6mm; }}
.cover .brand {{ display:flex; align-items:center; gap:14px; }}
.cover .wm {{ font-size:34px; font-weight:700; color:{DARK}; letter-spacing:.5px; }}
.cover h1 {{ font-size:30px; color:{DARK}; margin:34px 0 6px; }}
.cover .sub {{ color:#6b7a80; font-size:14px; }}
.cover .draft {{ margin-top:26px; padding:12px 16px; background:#fdf3e7; border:1px solid #f0d6ad;
  border-radius:8px; color:#9a5b14; font-size:12.5px; max-width:520px; }}
.cover ol {{ margin-top:22px; color:#33474a; font-size:13px; line-height:1.9; }}
.cover .grp {{ font-weight:700; color:{DARK}; margin-top:10px; }}
.doc {{ page-break-before:always; }}
.doc h1.t {{ font-size:24px; color:{DARK}; border-bottom:3px solid {TEAL}; padding-bottom:8px; margin:0 0 16px; }}
h1 {{ font-size:19px; color:{DARK}; border-bottom:1px solid #e6eaea; padding-bottom:5px; margin:26px 0 12px; }}
h2 {{ font-size:16px; color:{DARK}; margin:22px 0 9px; }}
h3 {{ font-size:14px; color:#33474a; margin:18px 0 7px; }}
p,li {{ margin:7px 0; }}
ul,ol {{ padding-left:20px; }}
a {{ color:{TEAL}; text-decoration:none; }}
table {{ border-collapse:collapse; width:100%; margin:13px 0; font-size:11.5px; }}
th {{ background:#e7f1f0; color:{DARK}; text-align:left; padding:7px 10px; }}
td {{ border-bottom:1px solid #e6eaea; padding:7px 10px; vertical-align:top; }}
blockquote {{ margin:12px 0; padding:8px 16px; border-left:4px solid {TEAL}; background:#f3f8f7;
  color:#33474a; font-size:11.5px; }}
code {{ background:#f1f4f4; padding:1px 5px; border-radius:4px; font-size:11.5px; }}
hr {{ border:0; border-top:1px solid #e6eaea; margin:22px 0; }}
"""


def convert(md_text):
    md_text = re.sub(r"\A\s*#\s+.*\n", "", md_text, count=1)  # drop leading H1 (becomes section title)
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    return md.convert(md_text)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    n = sum(len(d) for _, d in PACK)

    # Cover + contents.
    contents = ""
    i = 0
    for group, docs in PACK:
        contents += f'<div class="grp">{group}</div><ol start="{i+1}">'
        for _, title in docs:
            contents += f"<li>{title}</li>"
            i += 1
        contents += "</ol>"

    sections = ""
    for _, docs in PACK:
        for fn, title in docs:
            path = os.path.join(DOCS_DIR, fn)
            if not os.path.exists(path):
                print(f"  ! missing {fn} — skipped")
                continue
            with open(path, encoding="utf-8") as f:
                body = convert(f.read())
            sections += f'<div class="doc"><h1 class="t">{title}</h1>{body}</div>'

    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="cover">
  <div class="brand">{FAVICON}<span class="wm">Faresay</span></div>
  <h1>UK Legal &amp; Compliance Pack</h1>
  <div class="sub">Practice-management platform for therapists · Faresay as data processor, therapist as controller</div>
  <div class="draft"><strong>DRAFT for professional sign-off.</strong> These are working drafts prepared to support a UK launch. They are not legal advice and must be reviewed and finalised by a qualified solicitor before reliance. Placeholders marked [PLACEHOLDER] require completion.</div>
  <div><strong>{n} documents</strong></div>
  {contents}
</div>
{sections}
</body></html>"""

    html_path = os.path.join(OUT_DIR, "uk-legal-pack.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓ {html_path}")

    pdf_path = os.path.join(OUT_DIR, "Faresay-UK-Legal-Pack.pdf")
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if os.path.exists(chrome):
        subprocess.run([
            chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}", "file://" + html_path,
        ], check=True, capture_output=True)
        print(f"  ✓ {pdf_path}")
    else:
        print("  ! Chrome not found — open uk-legal-pack.html and Print → Save as PDF")


if __name__ == "__main__":
    main()
