#!/usr/bin/env python3
"""Render the Faresay sales collateral HTML → print-ready A4 PDFs (Chrome headless).
Usage: python3 faresay/brand/collateral/build-collateral.py
Output: faresay/brand/collateral/rendered/*.pdf"""
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "rendered")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

PIECES = [
    "therapist-recruitment-brochure",
    "product-one-pager",
    "investor-one-pager",
    "pricing-sheet",
]

def main():
    os.makedirs(OUT, exist_ok=True)
    if not os.path.exists(CHROME):
        print("! Chrome not found — open the .html files and Print → Save as PDF")
        return
    for name in PIECES:
        src = os.path.join(HERE, name + ".html")
        pdf = os.path.join(OUT, "Faresay-" + name + ".pdf")
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=5000", f"--print-to-pdf={pdf}", "file://" + src],
                       check=True, capture_output=True)
        print(f"  ✓ {os.path.basename(pdf)}")

if __name__ == "__main__":
    main()
