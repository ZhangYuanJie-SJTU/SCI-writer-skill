#!/bin/bash
# SCI-writer Installer for Mac/Linux
# Usage: chmod +x install.sh && ./install.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$HOME/.claude/skills/SCI-writer"

echo "╔══════════════════════════════════════════════╗"
echo "║   SCI-writer v5.0.0 Installer                ║"
echo "║   SJTU Wang Lab | Zhang Yuanjie + Wang Kan   ║"
echo "╚══════════════════════════════════════════════╝"
echo ""

# Step 1: Create skill directory
echo "[1/5] Creating skill directory..."
mkdir -p "$SKILL_DIR/templates"
mkdir -p "$SKILL_DIR/scripts"

# Step 2: Copy core files
echo "[2/5] Copying core files..."
cp "$SCRIPT_DIR/SKILL.md" "$SKILL_DIR/SKILL.md"
cp "$SCRIPT_DIR/README.md" "$SKILL_DIR/README.md"
echo "  SKILL.md ($(du -k "$SKILL_DIR/SKILL.md" | cut -f1) KB)"
echo "  README.md"

# Step 3: Copy templates
echo "[3/5] Copying templates..."
cp "$SCRIPT_DIR/templates/"* "$SKILL_DIR/templates/"
ls "$SKILL_DIR/templates/" | while read f; do
    echo "  $f ($(du -k "$SKILL_DIR/templates/$f" | cut -f1) KB)"
done

# Step 4: Copy scripts
echo "[4/5] Copying verification scripts..."
cp "$SCRIPT_DIR/scripts/"*.py "$SKILL_DIR/scripts/"
ls "$SKILL_DIR/scripts/"*.py | while read f; do
    echo "  $(basename $f)"
done

# Step 5: Verify installation
echo "[5/5] Verifying installation..."
REQUIRED_FILES=(
    "$SKILL_DIR/SKILL.md"
    "$SKILL_DIR/README.md"
    "$SKILL_DIR/templates/microneedle-sensing.yaml"
    "$SKILL_DIR/templates/generic-review.yaml"
    "$SKILL_DIR/templates/cover-letter-template.md"
    "$SKILL_DIR/scripts/verify_stage65.py"
    "$SKILL_DIR/scripts/verify_gate_b.py"
    "$SKILL_DIR/scripts/verify_gate_c.py"
    "$SKILL_DIR/scripts/download_templates.py"
)

ALL_OK=true
for f in "${REQUIRED_FILES[@]}"; do
    if [ -f "$f" ]; then
        echo "  ✓ $(basename $f)"
    else
        echo "  ✗ $(basename $f) MISSING"
        ALL_OK=false
    fi
done

echo ""
if [ "$ALL_OK" = true ]; then
    echo "╔══════════════════════════════════════════════╗"
    echo "║   ✓ Installation complete!                    ║"
    echo "║                                               ║"
    echo "║   Next steps:                                 ║"
    echo "║   1. Open Claude Code                         ║"
    echo "║   2. Run: /sciw load microneedle              ║"
    echo "║   3. Or:  /sciw init (for custom domain)      ║"
    echo "╚══════════════════════════════════════════════╝"
else
    echo "⚠ Some files are missing. Check the output above."
fi
