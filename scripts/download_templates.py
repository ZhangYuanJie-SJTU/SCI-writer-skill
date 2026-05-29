#!/usr/bin/env python3
"""
SCI-writer — Download Elsevier LaTeX templates
Downloads elsarticle.cls and elsarticle-num.bst to the current directory.

Usage: python download_templates.py
"""
import urllib.request, os, sys

TEMPLATES = {
    'elsarticle.cls': 'https://mirrors.ctan.org/macros/latex/contrib/elsarticle/elsarticle.cls',
    'elsarticle-num.bst': 'https://mirrors.ctan.org/macros/latex/contrib/elsarticle/elsarticle-num.bst',
}
FALLBACK = 'https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions'

def main():
    print("Downloading Elsevier LaTeX templates...")
    for filename, url in TEMPLATES.items():
        if os.path.exists(filename):
            size_kb = os.path.getsize(filename) // 1024
            print(f"  ✓ Already present: {filename} ({size_kb} KB)")
            continue
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=15) as r:
                data = r.read()
            if b'<html' in data[:200].lower():
                raise ValueError("Received HTML instead of file")
            with open(filename, 'wb') as f:
                f.write(data)
            print(f"  ✓ Downloaded: {filename} ({len(data)//1024} KB)")
        except Exception as e:
            print(f"  ✗ Failed: {filename} — {e}")
            print(f"    Manual download: {FALLBACK}")
            return 1
    print("\nAll templates ready.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
