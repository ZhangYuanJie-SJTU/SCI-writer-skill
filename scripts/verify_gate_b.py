#!/usr/bin/env python3
"""
SCI-writer Gate B — Citation Integrity & BibTeX Audit
Run from the project directory containing references.bib and main.tex.

Usage: python verify_gate_b.py
"""
import os, re, sys

def main():
    errors = 0

    # ── BibTeX key audit ──
    print("=" * 60)
    print("BIBTEX KEY AUDIT (AuthorYYYYKeyword convention)")
    print("=" * 60)

    if not os.path.exists('references.bib'):
        print("ERROR: references.bib not found.")
        sys.exit(1)

    with open('references.bib', 'r', encoding='utf-8') as f:
        bib_content = f.read()

    keys = re.findall(r'@\w+\{([^,]+),', bib_content)
    pattern = re.compile(r'^[A-Z][a-z]+\d{4}[A-Z][a-zA-Z]+$')

    print(f"  Total entries: {len(keys)}")
    violations = []
    for key in keys:
        if not pattern.match(key):
            violations.append(key)
            print(f"  ✗ NON-STANDARD KEY: {key}")
            errors += 1
    if not violations:
        print("  ✓ All keys follow AuthorYYYYKeyword convention")

    # ── DOI field check ──
    print("\n" + "=" * 60)
    print("DOI FIELD CHECK")
    print("=" * 60)
    entries = re.findall(r'@\w+\{([^,]+),.*?\n\}', bib_content, re.DOTALL)
    doi_pattern = re.compile(r'doi\s*=\s*\{(.+?)\}', re.IGNORECASE)
    no_doi = []
    for entry in entries:
        if not doi_pattern.search(entry):
            key = entry.split(',')[0].strip()
            no_doi.append(key)
    if no_doi:
        print(f"  ⚠ {len(no_doi)} entries missing DOI field:")
        for k in no_doi[:10]:
            print(f"    - {k}")
        if len(no_doi) > 10:
            print(f"    ... and {len(no_doi)-10} more")
    else:
        print(f"  ✓ All {len(keys)} entries have DOI fields")

    # ── Reference count ──
    print("\n" + "=" * 60)
    print("REFERENCE COUNT")
    print("=" * 60)
    count = len(re.findall(r'^@', bib_content, re.MULTILINE))
    status = '✓' if count >= 130 else '⚠ below 130'
    print(f"  References: {count} {status}")
    if count < 130:
        errors += 1

    # ── [NEEDS_REF] check in main.tex ──
    print("\n" + "=" * 60)
    print("[NEEDS_REF] PLACEHOLDER CHECK")
    print("=" * 60)
    if os.path.exists('main.tex'):
        with open('main.tex', 'r', encoding='utf-8') as f:
            tex = f.read()
        needs_ref = re.findall(r'\[NEEDS_REF[^\]]*\]', tex)
        if needs_ref:
            print(f"  ✗ {len(needs_ref)} [NEEDS_REF] placeholders remain:")
            for nr in needs_ref[:5]:
                print(f"    - {nr[:80]}")
            if len(needs_ref) > 5:
                print(f"    ... and {len(needs_ref)-5} more")
            errors += 1
        else:
            print("  ✓ No [NEEDS_REF] placeholders in main.tex")
    else:
        print("  ⚠ main.tex not found, skipping NEEDS_REF check")

    # ── Summary ──
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    if errors == 0:
        print("  ✓ ALL CHECKS PASSED — proceed to Stage 7")
    else:
        print(f"  ✗ {errors} issue(s) found — fix before proceeding")
    return errors

if __name__ == '__main__':
    sys.exit(0 if main() == 0 else 1)
