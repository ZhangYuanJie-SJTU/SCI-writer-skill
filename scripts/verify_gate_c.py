#!/usr/bin/env python3
"""
SCI-writer Gate C — Submission Readiness Verification
Run from the project directory containing main.tex, references.bib, highlights.txt.

Usage: python verify_gate_c.py
"""
import os, re, sys

def main():
    errors = 0

    if not os.path.exists('main.tex'):
        print("ERROR: main.tex not found.")
        sys.exit(1)

    with open('main.tex', 'r', encoding='utf-8') as f:
        content = f.read()

    # ── Abstract word count ──
    print("=" * 60)
    print("ABSTRACT WORD COUNT (limit: 300)")
    print("=" * 60)
    abstract = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', content, re.DOTALL)
    if abstract:
        text = re.sub(r'\\[a-zA-Z]+\{[^}]*\}|\\[a-zA-Z]+|\{|\}|~', ' ', abstract.group(1))
        words = [w for w in text.split() if w.strip()]
        status = '✓' if len(words) <= 300 else '⚠ EXCEEDS LIMIT'
        print(f"  Abstract word count: {len(words)} / 300 {status}")
        if len(words) > 300:
            errors += 1
    else:
        print("  ⚠ Abstract environment not found")

    # ── Highlights character count ──
    print("\n" + "=" * 60)
    print("HIGHLIGHTS CHARACTER COUNT (each line ≤ 85 chars)")
    print("=" * 60)
    if os.path.exists('highlights.txt'):
        with open('highlights.txt', 'r', encoding='utf-8') as f:
            lines = [l.rstrip('\n') for l in f if l.strip()]
        for i, line in enumerate(lines, 1):
            status = '✓' if len(line) <= 85 else f'⚠ {len(line)} chars — EXCEEDS 85'
            print(f"  Highlight {i} ({len(line)} chars): {status}")
            if len(line) > 85:
                errors += 1
        total_ok = 3 <= len(lines) <= 5
        print(f"\n  Total highlights: {len(lines)} {'✓' if total_ok else '⚠ must be 3-5'}")
        if not total_ok:
            errors += 1
    else:
        print("  ⚠ highlights.txt not found")
        errors += 1

    # ── Body word count ──
    print("\n" + "=" * 60)
    print("BODY WORD COUNT (target: 8,000–15,000)")
    print("=" * 60)
    body = content.split(r'\begin{document}', 1)[-1] if r'\begin{document}' in content else content
    body = re.sub(r'\\begin\{frontmatter\}.*?\\end\{frontmatter\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\begin\{(figure|table)\*?\}.*?\\end\{(figure|table)\*?\}', '', body, flags=re.DOTALL)
    body = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})*', ' ', body)
    body = re.sub(r'[{}$\\]', ' ', body)
    words = [w for w in body.split() if len(w) > 1 and w.isalpha()]
    in_range = 8000 <= len(words) <= 15000
    print(f"  Estimated body word count: {len(words)}")
    print(f"  Status: {'✓ in range' if in_range else '⚠ outside 8,000–15,000 range'}")
    if not in_range:
        errors += 1

    # ── Reference count ──
    print("\n" + "=" * 60)
    print("REFERENCE COUNT (minimum: 130)")
    print("=" * 60)
    if os.path.exists('references.bib'):
        with open('references.bib', 'r', encoding='utf-8') as f:
            bib = f.read()
        count = len(re.findall(r'^@', bib, re.MULTILINE))
        print(f"  References: {count} {'✓' if count >= 130 else '⚠ below 130'}")
        if count < 130:
            errors += 1
    else:
        print("  ⚠ references.bib not found")
        errors += 1

    # ── Post-compile figure mount ──
    print("\n" + "=" * 60)
    print("POST-COMPILE FIGURE MOUNT VERIFICATION")
    print("=" * 60)
    active = re.findall(r'(?<!%)\\includegraphics(?:\[.*?\])?\{([^}]+)\}', content)
    commented = re.findall(r'%.*\\includegraphics(?:\[.*?\])?\{([^}]+)\}', content)

    if active:
        for f in active:
            fname = f if '.' in f else f + '.png'
            if os.path.exists(fname):
                print(f"  ✓ {fname}")
            else:
                print(f"  ✗ MISSING FILE: {fname}")
                errors += 1
    else:
        print("  ⚠ No active \\includegraphics found")

    if commented:
        print(f"\n  ⚠ {len(commented)} commented-out figure(s):")
        for f in commented:
            print(f"    - {f}")

    # ── "In this section" check ──
    print("\n" + "=" * 60)
    print("BAD OPENING PHRASE CHECK")
    print("=" * 60)
    bad_openings = re.findall(r'(?:^|\n)\s*\\section\{[^}]*\}\s*\n\s*In this section[^.]*\.', content, re.IGNORECASE)
    if bad_openings:
        print(f"  ✗ {len(bad_openings)} section(s) start with 'In this section...'")
        errors += 1
    else:
        print("  ✓ No sections start with 'In this section...'")

    # ── Summary ──
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    if errors == 0:
        print("  ✓ ALL CHECKS PASSED — ready for submission")
    else:
        print(f"  ✗ {errors} issue(s) found — fix before submission")
    return errors

if __name__ == '__main__':
    sys.exit(0 if main() == 0 else 1)
