# SCI-writer Installer for Windows
# Usage: .\install.ps1
# Requires: Claude Code CLI installed

$ErrorActionPreference = "Stop"
$SkillDir = "$env:USERPROFILE\.claude\skills\SCI-writer"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "╔══════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   SCI-writer v5.0.0 Installer                ║" -ForegroundColor Cyan
Write-Host "║   SJTU Wang Lab | Zhang Yuanjie + Wang Kan   ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Step 1: Create skill directory
Write-Host "[1/5] Creating skill directory..." -ForegroundColor Yellow
if (Test-Path $SkillDir) {
    Write-Host "  Directory exists: $SkillDir" -ForegroundColor Gray
    Write-Host "  Updating files..." -ForegroundColor Gray
} else {
    New-Item -ItemType Directory -Path $SkillDir -Force | Out-Null
    Write-Host "  Created: $SkillDir" -ForegroundColor Green
}

# Step 2: Copy core files
Write-Host "[2/5] Copying core files..." -ForegroundColor Yellow
Copy-Item "$ScriptDir\SKILL.md" "$SkillDir\SKILL.md" -Force
Copy-Item "$ScriptDir\README.md" "$SkillDir\README.md" -Force
Write-Host "  SKILL.md ($([math]::Round((Get-Item "$ScriptDir\SKILL.md").Length/1KB)) KB)" -ForegroundColor Green
Write-Host "  README.md" -ForegroundColor Green

# Step 3: Copy templates
Write-Host "[3/5] Copying templates..." -ForegroundColor Yellow
if (-not (Test-Path "$SkillDir\templates")) {
    New-Item -ItemType Directory -Path "$SkillDir\templates" -Force | Out-Null
}
Copy-Item "$ScriptDir\templates\*" "$SkillDir\templates\" -Force
Get-ChildItem "$SkillDir\templates" | ForEach-Object {
    Write-Host "  $($_.Name) ($([math]::Round($_.Length/1KB)) KB)" -ForegroundColor Green
}

# Step 4: Copy scripts
Write-Host "[4/5] Copying verification scripts..." -ForegroundColor Yellow
if (-not (Test-Path "$SkillDir\scripts")) {
    New-Item -ItemType Directory -Path "$SkillDir\scripts" -Force | Out-Null
}
Copy-Item "$ScriptDir\scripts\*" "$SkillDir\scripts\" -Force
Get-ChildItem "$SkillDir\scripts\*.py" | ForEach-Object {
    Write-Host "  $($_.Name)" -ForegroundColor Green
}

# Step 5: Verify installation
Write-Host "[5/5] Verifying installation..." -ForegroundColor Yellow
$RequiredFiles = @(
    "$SkillDir\SKILL.md",
    "$SkillDir\README.md",
    "$SkillDir\templates\microneedle-sensing.yaml",
    "$SkillDir\templates\generic-review.yaml",
    "$SkillDir\templates\cover-letter-template.md",
    "$SkillDir\scripts\verify_stage65.py",
    "$SkillDir\scripts\verify_gate_b.py",
    "$SkillDir\scripts\verify_gate_c.py",
    "$SkillDir\scripts\download_templates.py"
)

$AllPresent = $true
foreach ($f in $RequiredFiles) {
    if (Test-Path $f) {
        Write-Host "  ✓ $(Split-Path $f -Leaf)" -ForegroundColor Green
    } else {
        Write-Host "  ✗ $(Split-Path $f -Leaf) MISSING" -ForegroundColor Red
        $AllPresent = $false
    }
}

Write-Host ""
if ($AllPresent) {
    Write-Host "╔══════════════════════════════════════════════╗" -ForegroundColor Green
    Write-Host "║   ✓ Installation complete!                    ║" -ForegroundColor Green
    Write-Host "║                                               ║" -ForegroundColor Green
    Write-Host "║   Next steps:                                 ║" -ForegroundColor Green
    Write-Host "║   1. Open Claude Code                         ║" -ForegroundColor Green
    Write-Host "║   2. Run: /sciw load microneedle              ║" -ForegroundColor Green
    Write-Host "║   3. Or:  /sciw init (for custom domain)      ║" -ForegroundColor Green
    Write-Host "╚══════════════════════════════════════════════╝" -ForegroundColor Green
} else {
    Write-Host "⚠ Some files are missing. Check the output above." -ForegroundColor Yellow
}
