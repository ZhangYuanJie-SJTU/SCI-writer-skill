#!/usr/bin/env python3
"""
SCI-writer Stage 6.5 — Figure Mount & Cross-Reference Verification
Run from the project directory containing main.tex and figure files.

Usage: python verify_stage65.py
"""
import os, re, sys

def main():
    if not os.path.exists('main.tex'):
        print("ERROR: main.tex not found. Run this script from the project directory.")
        sys.exit(1)

    with open('main.tex', 'r', encoding='utf-8') as f:
        content = f.read()
    with open('main.tex', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    errors = 0

    # ── Step 1: Figure file existence ──
    print("=" * 60)
    print("STEP 1: Figure File Audit")
    print("=" * 60)
    fig_files = sorted([f for f in os.listdir('.') if re.match(r'fig_\d+.*\.(png|eps|pdf)$', f)])
    if fig_files:
        for f in fig_files:
            size_kb = os.path.getsize(f) // 1024
            print(f"  ✓ {f} ({size_kb} KB)")
    else:
        print("  ⚠ No figure files found (fig_NN_*.png)")

    # ── Step 2: Commented-out \includegraphics ──
    print("\n" + "=" * 60)
    print("STEP 2: Commented-out \\includegraphics Audit")
    print("=" * 60)
    commented_out = []
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith('%') and 'includegraphics' in stripped:
            commented_out.append((i, stripped))
            print(f"  ✗ Line {i}: COMMENTED OUT — {stripped}")
            errors += 1
    if not commented_out:
        print("  ✓ No commented-out \\includegraphics found")

    # ── Step 3: Figure cross-reference audit ──
    print("\n" + "=" * 60)
    print("STEP 3: Figure Cross-Reference Audit")
    print("=" * 60)
    fig_labels = re.findall(r'\\label\{(fig:[^}]+)\}', content)
    fig_refs = set(re.findall(r'\\ref\{(fig:[^}]+)\}', content))
    for label in fig_labels:
        if label not in fig_refs:
            print(f"  ✗ ORPHAN: \\label{{{label}}} has no \\ref in text")
            errors += 1
        else:
            print(f"  ✓ {label}")

    # ── Step 4: Table cross-reference audit ──
    print("\n" + "=" * 60)
    print("STEP 4: Table Cross-Reference Audit")
    print("=" * 60)
    tab_labels = re.findall(r'\\label\{(tab:[^}]+)\}', content)
    tab_refs = set(re.findall(r'\\ref\{(tab:[^}]+)\}', content))
    for label in tab_labels:
        if label not in tab_refs:
            print(f"  ✗ ORPHAN: \\label{{{label}}} has no \\ref in text")
            errors += 1
        else:
            print(f"  ✓ {label}")

    # ── Step 5: Caption completeness ──
    print("\n" + "=" * 60)
    print("STEP 5: Caption Completeness")
    print("=" * 60)
    fig_envs = re.findall(r'\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}', content, re.DOTALL)
    for i, env in enumerate(fig_envs, 1):
        caption = re.search(r'\\caption\{(.+?)\}', env, re.DOTALL)
        if not caption:
            print(f"  ✗ Figure {i}: MISSING CAPTION")
            errors += 1
        elif len(caption.group(1).strip()) < 10:
            print(f"  ⚠ Figure {i}: caption very short ({len(caption.group(1).strip())} chars)")
        else:
            print(f"  ✓ Figure {i}: caption present")

    # ── Step 6: Table legend consistency ──
    print("\n" + "=" * 60)
    print("STEP 6: Table Legend Consistency")
    print("=" * 60)
    table_blocks = re.findall(r'\\begin\{table\*?\}(.*?)\\end\{table\*?\}', content, re.DOTALL)
    for i, block in enumerate(table_blocks, 1):
        caption = re.search(r'\\caption\{(.+?)\}', block, re.DOTALL)
        if not caption:
            print(f"  ✗ Table {i}: MISSING CAPTION")
            errors += 1
            continue
        cap_text = caption.group(1)
        legend_defined = set(re.findall(r'\b([A-Z])\s*[=~]\s*', cap_text))
        symbols_used = set(re.findall(r'(?:^|&|\\\\\s*)\s*([A-Z])\s*(?:&|\\\\|$)', block, re.MULTILINE))
        undefined = symbols_used - legend_defined - {'H', 'A', 'B', 'C'}
        if undefined:
            print(f"  ⚠ Table {i}: symbols used but not defined in caption: {undefined}")
        else:
            print(f"  ✓ Table {i}: all symbols accounted for")

    # ── Summary ──
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    if errors == 0:
        print("  ✓ ALL CHECKS PASSED — proceed to Gate B")
    else:
        print(f"  ✗ {errors} issue(s) found — fix before proceeding to Gate B")
    return errors

if __name__ == '__main__':
    sys.exit(0 if main() == 0 else 1)
