#!/usr/bin/env python3
"""
Render Faresay markdown docs into branded, print-ready HTML.

Each doc gets the Faresay letterhead (favicon mark + wordmark + teal rule),
a title block with status badge, styled tables/headings, and a confidential
footer. Open any output in a browser and "Print → Save as PDF" for a polished,
client-ready document.

Usage:  python3 faresay/docs/build-branded-docs.py
Output: faresay/docs/rendered/*.html  +  index.html
"""
import os
import re
import datetime
import markdown

DOCS_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(DOCS_DIR, "rendered")

BRAND_TEAL = "#1F6F6B"
BRAND_DARK = "#15514e"

# Favicon mark — teal circle + smile (matches site favicon / email letterhead).
FAVICON_SVG = (
    '<svg width="34" height="34" viewBox="0 0 28 28" xmlns="http://www.w3.org/2000/svg">'
    f'<circle cx="14" cy="14" r="14" fill="{BRAND_TEAL}"/>'
    '<path d="M9 18c0-3 2-5 5-5s5 2 5 5M9.5 11.5c.8-1.2 2.3-2 4.5-2s3.7.8 4.5 2" '
    'fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round"/></svg>'
)

# Per-doc presentation: title + status badge. Anything not listed → "Confidential".
DRAFT = "DRAFT — for professional sign-off"
CONF = "Confidential"
META = {
    "uk-business-overview.md": ("UK Business Overview", CONF),
    "uk-legal-regulatory-brief.md": ("UK Legal & Regulatory Brief", CONF),
    "uk-questions-for-solicitor.md": ("Questions for Solicitor — UK Launch", CONF),
    "uk-privacy-policy.md": ("UK Privacy Policy", DRAFT),
    "uk-terms-of-service.md": ("UK Terms of Service", DRAFT),
    "uk-therapist-agreement.md": ("UK Therapist Agreement", DRAFT),
    "uk-clinical-governance-policy.md": ("UK Clinical Governance Policy", DRAFT),
    "uk-crisis-safeguarding-policy.md": ("UK Crisis & Safeguarding Policy", DRAFT),
    "uk-security-data-protection-policy.md": ("UK Security & Data Protection Policy", DRAFT),
    "business-plan.md": ("Business Plan", CONF),
    "gtm-strategy.md": ("Go-To-Market Strategy (v1)", CONF),
    "customer-persona.md": ("Customer Personas", CONF),
    "market-research-synthesis.md": ("Market Research Synthesis", CONF),
    "business-model-canvas.md": ("Business Model Canvas", CONF),
    "product-requirements-document.md": ("Product Requirements Document", CONF),
    "risk-register.md": ("Risk Register", CONF),
    "financial-model.md": ("Financial Model", CONF),
    "privacy-policy.md": ("Privacy Policy", DRAFT),
    "terms-of-service.md": ("Terms of Service", DRAFT),
    "therapist-agreement.md": ("Therapist Agreement", DRAFT),
    "clinical-governance-policy.md": ("Clinical Governance Policy", DRAFT),
    "crisis-safeguarding-policy.md": ("Crisis & Safeguarding Policy", DRAFT),
    "security-data-protection-policy.md": ("Security & Data Protection Policy", DRAFT),
}
# Internal/meta docs — skip (not client-facing deliverables).
SKIP = {"CONTEXT.md", "HANDOFF.md", "README.md"}

CSS = f"""
:root {{ --teal:{BRAND_TEAL}; --dark:{BRAND_DARK}; }}
* {{ box-sizing:border-box; }}
html {{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
body {{ font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
  color:#2b3338; line-height:1.6; margin:0; background:#eceff0; }}
.page {{ max-width:820px; margin:24px auto; background:#fff; padding:0 0 8px;
  box-shadow:0 1px 6px rgba(0,0,0,.12); border-radius:6px; overflow:hidden; }}
header.lh {{ display:flex; align-items:center; justify-content:space-between;
  padding:26px 56px 18px; border-bottom:3px solid var(--teal); }}
header.lh .brand {{ display:flex; align-items:center; gap:12px; }}
header.lh .wm {{ font-size:26px; font-weight:700; letter-spacing:.5px; color:var(--dark); }}
header.lh .tag {{ font-size:13px; color:#6b7a80; }}
.titleblock {{ padding:30px 56px 4px; }}
.titleblock h1.doc {{ font-size:30px; color:var(--dark); margin:0 0 10px; line-height:1.2; }}
.meta {{ font-size:12.5px; color:#6b7a80; display:flex; gap:14px; align-items:center; flex-wrap:wrap; }}
.badge {{ display:inline-block; font-size:11px; font-weight:700; letter-spacing:.4px;
  padding:4px 10px; border-radius:999px; text-transform:uppercase; }}
.badge.conf {{ background:#e7f1f0; color:var(--dark); }}
.badge.draft {{ background:#fdf3e7; color:#9a5b14; border:1px solid #f0d6ad; }}
.content {{ padding:8px 56px 40px; }}
.content h1 {{ font-size:23px; color:var(--dark); border-bottom:1px solid #e6eaea;
  padding-bottom:6px; margin:34px 0 14px; }}
.content h2 {{ font-size:19px; color:var(--dark); margin:28px 0 10px; }}
.content h3 {{ font-size:16px; color:#33474a; margin:22px 0 8px; }}
.content p {{ margin:10px 0; }}
.content ul,.content ol {{ margin:10px 0; padding-left:22px; }}
.content li {{ margin:4px 0; }}
.content a {{ color:var(--teal); }}
.content code {{ background:#f1f4f4; padding:1px 5px; border-radius:4px; font-size:13px;
  font-family:'SF Mono',ui-monospace,Menlo,Consolas,monospace; }}
.content pre {{ background:#f5f7f7; border:1px solid #e6eaea; border-radius:6px;
  padding:14px 16px; overflow:auto; }}
.content pre code {{ background:none; padding:0; }}
.content blockquote {{ margin:14px 0; padding:8px 18px; border-left:4px solid var(--teal);
  background:#f6faf9; color:#42565a; }}
.content table {{ border-collapse:collapse; width:100%; margin:16px 0; font-size:13.5px; }}
.content th {{ background:var(--teal); color:#fff; text-align:left; padding:9px 12px; }}
.content td {{ border-bottom:1px solid #e6eaea; padding:8px 12px; vertical-align:top; }}
.content tr:nth-child(even) td {{ background:#f7faf9; }}
.content hr {{ border:0; border-top:1px solid #e6eaea; margin:26px 0; }}
footer.lh {{ border-top:1px solid #e6eaea; margin:0 56px; padding:14px 0 18px;
  font-size:11.5px; line-height:1.5; color:#8a979d; }}
footer.lh .org {{ font-weight:600; color:#5a6a70; }}
footer.lh a {{ color:var(--teal); text-decoration:none; }}
@media print {{
  body {{ background:#fff; }}
  .page {{ box-shadow:none; margin:0; max-width:none; border-radius:0; }}
  header.lh, .titleblock, .content, footer.lh {{ padding-left:0; padding-right:0; }}
  header.lh, footer.lh {{ margin:0; }}
  .content h1, .content h2, .content h3 {{ page-break-after:avoid; }}
  .content table, .content pre, .content blockquote {{ page-break-inside:avoid; }}
  @page {{ size:A4; margin:18mm 16mm; }}
}}
"""

def doc_html(title, status, body_html):
    badge_cls = "draft" if status == DRAFT else "conf"
    today = datetime.date.today().strftime("%-d %B %Y")
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Faresay — {title}</title><style>{CSS}</style></head>
<body><div class="page">
  <header class="lh">
    <div class="brand">{FAVICON_SVG}<span class="wm">Faresay</span></div>
    <span class="tag">Therapy, matched.</span>
  </header>
  <div class="titleblock">
    <h1 class="doc">{title}</h1>
    <div class="meta">
      <span class="badge {badge_cls}">{status}</span>
      <span>Faresay Ltd</span><span>·</span><span>{today}</span>
    </div>
  </div>
  <div class="content">{body_html}</div>
  <footer class="lh">
    <div class="org">Faresay</div>
    <div><a href="https://faresay.com">faresay.com</a> · <a href="mailto:enquiries@faresay.com">enquiries@faresay.com</a> · <a href="mailto:legal@faresay.com">legal@faresay.com</a></div>
    <div style="margin-top:6px;">Confidential. This document and its contents are the property of Faresay and are intended solely for the named recipient.</div>
  </footer>
</div></body></html>"""


def convert(md_text):
    # Drop a leading H1 (it becomes the title block) to avoid duplication.
    md_text = re.sub(r"\A\s*#\s+.*\n", "", md_text, count=1)
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list", "toc"])
    return md.convert(md_text)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    built = []
    for fn in sorted(os.listdir(DOCS_DIR)):
        if not fn.endswith(".md") or fn in SKIP:
            continue
        title, status = META.get(fn, (fn[:-3].replace("-", " ").title(), CONF))
        with open(os.path.join(DOCS_DIR, fn), encoding="utf-8") as f:
            body = convert(f.read())
        out_name = fn[:-3] + ".html"
        with open(os.path.join(OUT_DIR, out_name), "w", encoding="utf-8") as f:
            f.write(doc_html(title, status, body))
        built.append((title, status, out_name))
        print(f"  ✓ {out_name}")

    # Index page linking every rendered doc.
    rows = "\n".join(
        f'<li><a href="{n}">{t}</a> <span class="badge {"draft" if s==DRAFT else "conf"}">{s}</span></li>'
        for t, s, n in built
    )
    idx = doc_html(
        "Document Index",
        CONF,
        f'<p>Branded, print-ready versions of the Faresay business and policy documents. '
        f'Open any document and use <em>Print → Save as PDF</em> for a client-ready file.</p>'
        f'<ul style="list-style:none;padding-left:0;line-height:2.4;">{rows}</ul>',
    )
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(idx)
    print(f"\nBuilt {len(built)} docs → {OUT_DIR}/  (open index.html)")


if __name__ == "__main__":
    main()
