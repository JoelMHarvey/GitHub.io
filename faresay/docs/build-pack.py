#!/usr/bin/env python3
"""
Assemble the UK solicitor pre-meeting pack from the branded rendered docs.

Outputs (in faresay/docs/):
  pack-uk-solicitor/            folder with the 9 UK HTML docs + cover index.html
  faresay-uk-solicitor-pack.zip zipped version of that folder (email attachment)
  faresay-uk-pack-combined.html single scrollable/printable file (one attachment)

Run after build-branded-docs.py:  python3 faresay/docs/build-pack.py
"""
import os
import re
import shutil
import datetime
import zipfile

DOCS = os.path.dirname(os.path.abspath(__file__))
RENDERED = os.path.join(DOCS, "rendered")
PACK_DIR = os.path.join(DOCS, "pack-uk-solicitor")
ZIP_PATH = os.path.join(DOCS, "faresay-uk-solicitor-pack.zip")
COMBINED = os.path.join(DOCS, "faresay-uk-pack-combined.html")

TEAL, DARK = "#1F6F6B", "#15514e"
TODAY = datetime.date.today().strftime("%-d %B %Y")

FAVICON = (
    '<svg width="34" height="34" viewBox="0 0 28 28" xmlns="http://www.w3.org/2000/svg">'
    f'<circle cx="14" cy="14" r="14" fill="{TEAL}"/>'
    '<path d="M9 18c0-3 2-5 5-5s5 2 5 5M9.5 11.5c.8-1.2 2.3-2 4.5-2s3.7.8 4.5 2" '
    'fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/></svg>'
)

# Order matters: context first, then the ask, then the drafts to redline.
PACK = [
    ("uk-business-overview.html", "UK Business Overview", "One-page context — what Faresay is and how it works."),
    ("uk-legal-regulatory-brief.html", "UK Legal & Regulatory Brief", "Our positions and the open questions, area by area."),
    ("uk-questions-for-solicitor.html", "Questions for Solicitor", "The agenda / checklist for the meeting."),
    ("uk-privacy-policy.html", "UK Privacy Policy", "DRAFT for sign-off."),
    ("uk-terms-of-service.html", "UK Terms of Service", "DRAFT for sign-off."),
    ("uk-therapist-agreement.html", "UK Therapist Agreement", "DRAFT for sign-off."),
    ("uk-clinical-governance-policy.html", "UK Clinical Governance Policy", "DRAFT for sign-off."),
    ("uk-crisis-safeguarding-policy.html", "UK Crisis & Safeguarding Policy", "DRAFT for sign-off."),
    ("uk-security-data-protection-policy.html", "UK Security & Data Protection Policy", "DRAFT for sign-off."),
]

COVER_CSS = f"""
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;color:#2b3338;line-height:1.6;margin:0;background:#eceff0}}
.page{{max-width:820px;margin:24px auto;background:#fff;box-shadow:0 1px 6px rgba(0,0,0,.12);border-radius:6px;overflow:hidden}}
header{{display:flex;align-items:center;justify-content:space-between;padding:26px 56px 18px;border-bottom:3px solid {TEAL}}}
header .brand{{display:flex;align-items:center;gap:12px}}.wm{{font-size:26px;font-weight:700;letter-spacing:.5px;color:{DARK}}}
.tag{{font-size:13px;color:#6b7a80}}
.body{{padding:28px 56px 40px}}
h1{{font-size:30px;color:{DARK};margin:0 0 6px}}
.sub{{color:#6b7a80;font-size:13.5px;margin:0 0 22px}}
ol{{padding-left:20px}}li{{margin:12px 0}}
li a{{color:{TEAL};font-weight:600;text-decoration:none;font-size:16px}}
li .d{{display:block;color:#6b7a80;font-size:13px;margin-top:2px}}
.note{{background:#f6faf9;border-left:4px solid {TEAL};padding:12px 18px;margin:6px 0 22px;font-size:13.5px;color:#42565a}}
footer{{border-top:1px solid #e6eaea;margin:0 56px;padding:14px 0 20px;font-size:11.5px;color:#8a979d}}
footer a{{color:{TEAL};text-decoration:none}}
"""


def cover_html(linkify):
    items = "\n".join(
        f'<li><a href="{fn if linkify else "#"+fn[:-5]}">{i}. {title}</a>'
        f'<span class="d">{desc}</span></li>'
        for i, (fn, title, desc) in enumerate(PACK, 1)
    )
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Faresay — UK Launch · Pre-meeting Pack</title><style>{COVER_CSS}</style></head>
<body><div class="page">
<header><div class="brand">{FAVICON}<span class="wm">Faresay</span></div><span class="tag">Therapy, matched.</span></header>
<div class="body">
  <h1>UK Launch — Pre-meeting Pack</h1>
  <p class="sub">Prepared for solicitor review · {TODAY} · Confidential</p>
  <div class="note">These materials are founder-prepared <strong>preparatory drafts, not legal advice</strong>.
  The policy documents are marked <em>DRAFT — for professional sign-off</em> and are intended as a starting
  point for your review and redlining. US/expansion matters are deliberately excluded.</div>
  <ol>{items}</ol>
</div>
<footer><div style="font-weight:600;color:#5a6a70">Faresay</div>
<div><a href="https://faresay.com">faresay.com</a> · <a href="mailto:legal@faresay.com">legal@faresay.com</a> · <a href="mailto:enquiries@faresay.com">enquiries@faresay.com</a></div>
</footer></div></body></html>"""


def inner_page(path):
    """Extract <body>…</body> inner (the .page div) and CSS from a rendered doc."""
    html = open(path, encoding="utf-8").read()
    css = re.search(r"<style>(.*?)</style>", html, re.S)
    body = re.search(r"<body>(.*?)</body>", html, re.S)
    return (css.group(1) if css else ""), (body.group(1) if body else "")


def main():
    # 1) folder pack
    if os.path.isdir(PACK_DIR):
        shutil.rmtree(PACK_DIR)
    os.makedirs(PACK_DIR)
    for fn, _, _ in PACK:
        shutil.copy(os.path.join(RENDERED, fn), os.path.join(PACK_DIR, fn))
    with open(os.path.join(PACK_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(cover_html(linkify=True))

    # 2) zip it
    if os.path.exists(ZIP_PATH):
        os.remove(ZIP_PATH)
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as z:
        for fn in ["index.html"] + [p[0] for p in PACK]:
            z.write(os.path.join(PACK_DIR, fn), arcname=os.path.join("faresay-uk-pack", fn))

    # 3) single combined file (cover + every doc, page-broken)
    shared_css = ""
    sections = []
    for i, (fn, title, _) in enumerate(PACK, 1):
        css, body = inner_page(os.path.join(RENDERED, fn))
        if not shared_css:
            shared_css = css  # template CSS is identical across docs
        anchor = fn[:-5]
        brk = 'style="page-break-before:always"' if i > 1 else ""
        sections.append(f'<div id="{anchor}" {brk}>{body}</div>')
    cover = cover_html(linkify=False)
    cover_body = re.search(r"<body>(.*?)</body>", cover, re.S).group(1)
    combined = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Faresay — UK Launch · Pre-meeting Pack (combined)</title>
<style>{COVER_CSS}\n{shared_css}\n@media print{{.page{{box-shadow:none;margin:0;border-radius:0}}}}</style></head>
<body><div style="page-break-after:always">{cover_body}</div>
{''.join(sections)}
</body></html>"""
    with open(COMBINED, "w", encoding="utf-8") as f:
        f.write(combined)

    print(f"  ✓ {PACK_DIR}/  ({len(PACK)} docs + cover)")
    print(f"  ✓ {ZIP_PATH}")
    print(f"  ✓ {COMBINED}")
    print(f"\nPack: {len(PACK)} UK docs. Email the .zip, or the single combined .html.")


if __name__ == "__main__":
    main()
