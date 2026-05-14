# SCI-writer

> **Full-Chain Scientific Review Paper Orchestration System**  
> *From literature search to submission-ready LaTeX — automated, audited, and reproducible.*

[![Version](https://img.shields.io/badge/version-4.1.0-blue)](SKILL.md)
[![Target](https://img.shields.io/badge/target-Q1%20%2F%20CAS--TOP-red)](SKILL.md)
[![Gate system](https://img.shields.io/badge/gates-A%20%2F%20B%20%2F%20C-green)](SKILL.md)
[![Anti-hallucination](https://img.shields.io/badge/anti--hallucination-built--in-orange)](SKILL.md)
[![Pipeline](https://img.shields.io/badge/pipeline-11%20stages-purple)](SKILL.md)

---

## What is SCI-writer?

SCI-writer is a Claude Code skill that orchestrates the **complete lifecycle of a scientific review paper** — from domain gap analysis through systematic literature search, section drafting, peer review simulation, LaTeX compilation, and submission package assembly.

It was developed and battle-tested at **SJTU Wang Lab** (Shanghai Jiao Tong University, School of Sensing Science and Engineering) for the paper:

> *"Wearable Electrochemical Sensing Systems Based on Microneedle Arrays: A Full-Chain Review from Sensor Fabrication to Intelligent Embedded Terminals"*  
> Target journal: *Biosensors and Bioelectronics* (Q1, CAS TOP)

The skill is **self-contained** — it runs a full pipeline without requiring any companion skills. Optional accelerator skills (deep-research, academic-paper, paper-verification, etc.) can be detected and used automatically to compress wall-clock time when installed.

---

## Key Features

| Capability | Detail |
|------------|--------|
| **11-Stage pipeline** | Foundation → Construction → Refinement → Delivery, with 3 mandatory quality gates |
| **3 Quality Gates** | Gate A (corpus completeness) · Gate B (citation integrity + method-type consistency) · Gate C (submission readiness) |
| **Anti-hallucination protocol** | 4-rule system: citation sourcing, numbers traceability, superlatives rule, method-type rule · [V]/[U]/[N]/[X]/[M] tag taxonomy |
| **6-persona peer review simulation** | Domain expert · Adjacent field expert · Methods/rigor expert · Clinical/translational expert · Devil's advocate · Format/integration auditor (R6) |
| **Figure mount verification** | Stage 6.5 audits commented-out `\includegraphics`, orphan figures (no `\ref{}`), table legend consistency — all via Python scripts |
| **Pipeline state persistence** | `sci_writer_state.md` written after every stage — pipeline survives context compaction and multi-day runs; `/sciw resume` to continue |
| **Domain configuration** | Built-in YAML config for wearable MNA electrochemical sensing; adaptable to any research domain |
| **[AUTO]/[USER] delivery classification** | Clearly separates what Claude completes automatically vs. what requires private information from the user |
| **Tiered citation verification** | Tier 1 (all), Tier 2 ([N]/[U] tagged), Tier 3 (high-risk numbers + superlatives) |
| **Score escalation** | Stage 7 runs up to 3 rounds: R1 avg ≥78 → R2 avg ≥80 (post-P0) → R3 avg ≥82 (post-P1) |

---

## The 11-Stage Pipeline

```
┌─────────────────────────────────────────────────────┐
│                  PHASE I — FOUNDATION                │
├──────────────────────────────────────────────────────┤
│  Stage 1   │ Domain Intelligence & Gap Mapping       │
│  Stage 2   │ Literature Acquisition (PRISMA)         │
│  ▓▓▓▓▓▓▓▓▓ GATE A: Corpus Completeness ▓▓▓▓▓▓▓▓▓   │
├──────────────────────────────────────────────────────┤
│                 PHASE II — CONSTRUCTION              │
├──────────────────────────────────────────────────────┤
│  Stage 3   │ Deep Synthesis & Knowledge Extraction   │
│  Stage 4   │ Narrative Architecture & Outline Design │
│  Stage 5   │ Section-by-Section Drafting (4-pass)    │
│  Stage 6   │ Figures, Tables & Visual Narrative      │
│  Stage 6.5 │ Figure Mount & Cross-Reference Audit ★ │
│  ▓▓▓▓▓▓▓▓▓ GATE B: Citation Integrity Audit ▓▓▓▓▓▓▓ │
├──────────────────────────────────────────────────────┤
│                 PHASE III — REFINEMENT               │
├──────────────────────────────────────────────────────┤
│  Stage 7   │ 6-Persona Peer Review Simulation        │
│  Stage 8   │ Revision & Rebuttal Engineering         │
│  Stage 9   │ Journal Formatting & LaTeX Compilation  │
│  ▓▓▓▓▓▓▓▓▓ GATE C: Submission Readiness Check ▓▓▓▓▓ │
├──────────────────────────────────────────────────────┤
│                  PHASE IV — DELIVERY                 │
├──────────────────────────────────────────────────────┤
│  Stage 10  │ Submission Package Assembly             │
└─────────────────────────────────────────────────────┘
★ Stage 6.5 is new in v4.0 — eliminates the most common LaTeX failure mode
```

---

## Quick Start

### Installation

```bash
# Clone this skill into your Claude Code skills directory
git clone https://github.com/ZhangYuanJie-SJTU/SCI-writer-skill.git ~/.claude/skills/SCI-writer

# Or on Windows:
git clone https://github.com/ZhangYuanJie-SJTU/SCI-writer-skill.git "C:\Users\<you>\.claude\skills\SCI-writer"
```

### Basic Usage (in Claude Code)

```
# Start a new paper from scratch
/SCI-writer

# Load the built-in microneedle/wearable-sensing domain config
/sciw load microneedle

# Full auto mode (stops at each Gate for your approval)
/sciw auto

# Resume an interrupted pipeline (reads sci_writer_state.md)
/sciw resume

# Jump to a specific stage
/sciw stage 7

# Run only the figure mount audit
/sciw mount-check

# Run only Gate B citation audit
/sciw gate b
```

---

## The Gate System

### Gate A — Corpus Completeness

Ensures the literature corpus is large, diverse, and recent enough before writing begins.

- ≥150 papers total (exception path available for niche domains: ≥80 with compensating controls)
- ≥20 papers per major section
- ≥40% from 2023–2026
- ≥5 DOIs manually verified
- Detection method recorded for every paper (feeds Gate B method-type check)
- All BibTeX keys follow `AuthorYYYYKeyword` convention

### Gate B — Citation Integrity + Method-Type Audit

The anti-hallucination firewall. Three-tier verification:

| Tier | Scope | What's checked |
|------|-------|----------------|
| **Tier 1** | All citations | BibTeX key format + DOI field present |
| **Tier 2** | [N] and [U] tagged | Title + author + year + journal confirmed |
| **Tier 3** | High-risk (numbers, "first", 2025–2026, unusual DOIs) | Specific metric confirmed in source paper |

**Method-type consistency check (unique to SCI-writer):** A fluorescence paper cited in an EIS paragraph = automatic `[METHOD_X]` flag. The cited paper's detection modality must match the method described in the citing sentence.

### Gate C — Submission Readiness

Final pre-submission checklist: zero figure mount failures, zero orphan figures, R2 avg ≥ 80/100, word count 8,000–15,000, abstract ≤ 300 words, all highlights ≤ 85 chars. Fully automated verification via Python scripts.

---

## Anti-Hallucination Protocol

Four rules, always active:

1. **Citation Sourcing Rule** — Every claim about a specific study must have a verified source. No source = `[NEEDS_REF]`, not an invented citation.

2. **Numbers Rule** — Every quantitative value (LOD, sensitivity, MARD, p-value) must be traceable to a specific table/figure in a verified paper.

3. **Superlatives Rule** — "first", "highest", "only", "unprecedented" always require a citation. Without one: "among the reported approaches..."

4. **Method-Type Rule** — The cited paper's detection method must match what the citing sentence claims. Optical ≠ electrochemical.

**Verification tag taxonomy:**
```
[V]  Verified — DOI confirmed, method type confirmed
[U]  Unverified — user-provided, not independently checked
[N]  Needs verification — in corpus but not yet audited
[X]  Failed — not found; remove from draft
[M]  Method mismatch — paper exists but method type conflicts
```

---

## The 6-Reviewer Panel (Stage 7)

| Reviewer | Focus | Primary attack vectors |
|----------|-------|----------------------|
| **R1** Domain Expert | Technical accuracy, depth, completeness | Missing key citations; performance benchmarks inconsistent with source papers |
| **R2** Adjacent Field Expert | Interdisciplinary context, positioning | "Done better in [adjacent field]"; overclaims novelty |
| **R3** Methods/Rigor Expert | Systematic coverage, review methodology | No PRISMA compliance; unclear selection criteria |
| **R4** Clinical/Translational Expert | Clinical relevance, regulatory pathway, in vivo evidence | In vitro cited as clinical; no comparison to commercial gold standard |
| **R5** Devil's Advocate | Central thesis coherence | "Is this really unified or just topics stapled together?" |
| **R6** Format/Integration Auditor ★ | LaTeX quality, figure mounting, journal compliance | Commented-out `\includegraphics`; orphan figures; highlights > 85 chars |

★ R6 was added in v4.0 after real-world experience showed that formatting failures consistently evaded the first 5 reviewers.

Score escalation: R1 avg ≥ 78 → R2 avg ≥ 80 → R3 avg ≥ 82

---

## Stage 6.5 — Figure Mount Audit

The single most impactful addition in v4.0. Runs mandatory checks via Python scripts after figure generation:

- **Commented-out `\includegraphics` detection** — Scans for `% \includegraphics` patterns; uncomments automatically
- **Orphan figure detection** — Every `\label{fig:X}` must have ≥1 `\ref{fig:X}` in text
- **Orphan table detection** — Every `\label{tab:X}` must have ≥1 `\ref{tab:X}` in text
- **Caption completeness** — Every figure environment must have a non-empty `\caption{}`
- **Table legend consistency** — Every symbol used in table body must be defined in the caption

**Why this matters:** It is trivially easy for figure files to be generated while their `\includegraphics` commands remain commented out from an earlier draft phase. The resulting PDF shows blank boxes — a silent failure invisible until compilation.

---

## Pipeline State Persistence

A review paper takes 3–10 days. Context compaction happens multiple times. `sci_writer_state.md` is written to disk after every stage, recording:

- Current stage and completed stages
- Gate pass/fail history with dates
- Stage 7 score history (all 3 rounds)
- Corpus status ([V]/[N]/[X]/[M] counts)
- Figure status table
- Outstanding [AUTO] and [USER] items

`/sciw resume` reads this file and continues from the last checkpoint.

---

## Domain Configuration

### Using the Built-in Microneedle/Wearable-Sensing Config

```
/sciw load microneedle
```

Loads pre-configured settings for:
- Target journal: *Biosensors and Bioelectronics*
- 5 search clusters (fabrication, sensing modalities, system integration, embedded intelligence, clinical validation)
- 7 domain-specific performance metrics (glucose LOD, sensitivity, MARD, ion slope, etc.)
- 6 key research groups to ensure representation
- Detection method taxonomy (amperometry, DPV, SWV, EIS, ISE, FSCV, fluorescence, SERS)
- 3 existing reviews to differentiate from

### Custom Domain Config

Create a `domain-config.yaml` file and load with `/sciw config load domain-config.yaml`. The YAML schema supports:
- Paper metadata (title, journal, word target, reference target)
- Search clusters with multi-query patterns
- Performance metrics with units and thresholds
- Detection method taxonomy (for Gate B method-type checks)
- Existing reviews to differentiate from
- Unique contribution claim

---

## Verification Scripts (Gate C Automation)

All scripts are pure Python stdlib — no external tools required.

```python
# Abstract word count (≤300)
/sciw verify abstract

# Highlights character count (≤85 per line)
/sciw verify highlights

# LaTeX body word count (8,000–15,000)
/sciw verify wordcount

# Reference count (≥130)
/sciw verify references

# Figure mount status
/sciw mount-check

# Run all verification
/sciw verify all
```

---

## Changelog

### v4.1.0 (2026-05-14)
- **Pipeline State Persistence** — `sci_writer_state.md` + `/sciw resume` command
- **BibTeX Key Convention** — `AuthorYYYYKeyword` mandatory standard; automated compliance check
- **Gate A Exception Path** — Domain-limited corpus (≥80 papers) with documented compensating controls
- **Gate B Tiered Verification** — Tier 1/2/3 protocol replaces ambiguous "high-risk" heuristic
- **Verification Scripts** — Python snippets for abstract words, highlights chars, LaTeX word count, reference count
- **Stage 6.5: Table Legend Check** — Auto-scan caption symbols vs. table body symbols
- **Elsevier Template URL Fix** — `mirrors.ctan.org` direct download with HTML content validation
- **Stage 7 Threshold Fix** — R1/R2/R3 table now consistent; previous contradiction between Scoring Protocol and Score Escalation Rule resolved

### v4.0.0 (2026-05-14)
- **Stage 6.5** — Figure Mount & Cross-Reference Verification (mandatory new stage)
- **R6 Reviewer** — Format/Integration Auditor added to 5-reviewer panel
- **Gate B Part 2** — Method-Type Consistency Check; `[METHOD_X]` tag
- **Gate C** — Cross-Reference Completeness; `\includegraphics` uncommented check
- **Stage 10** — `[AUTO]`/`[USER]` delivery classification

### v3.0.0
- Initial public release: 10-stage pipeline, Gates A/B/C, PRISMA protocol, 5-reviewer simulation, Built-in microneedle domain config

---

## Electrochemical Sensing Formula Bank

The skill includes a ready-to-use LaTeX formula bank for wearable electrochemical sensing:

| Formula | LaTeX macro |
|---------|------------|
| Cottrell equation (amperometry) | `i(t) = nFAD^{1/2}C / π^{1/2}t^{1/2}` |
| Randles–Ševčík (voltammetry) | `i_p = 0.4463 nFAC(nFvD/RT)^{1/2}` |
| Nernst equation (potentiometry/ISE) | `E = E⁰ + (RT/z_iF) ln a_i` (slope: 59.2/z mV/decade) |
| Butler–Volmer (electrode kinetics) | `i = i₀[exp(α_a Fη/RT) - exp(-α_c Fη/RT)]` |
| Randles cell (EIS) | `Z = R_s + 1/(jωC_dl + 1/(R_ct + Z_W))` |
| LOD (IUPAC) | `LOD = 3σ_b / S` |
| Sensitivity | `S = Δi/ΔC [μA mM⁻¹ cm⁻²]` |

---

## Compatibility

| Tool | Required | Notes |
|------|----------|-------|
| Claude Code | ✅ Required | Tested on Claude Sonnet 4.6+ |
| Python (stdlib only) | ✅ Required | For figure generation and verification scripts |
| matplotlib + numpy | Recommended | For Python figure generation (Stage 6) |
| pdflatex | Optional | For LaTeX compilation; matplotlib fallback available if absent |
| tavily-search skill | Recommended | Stage 2 literature search (Tier 1 search channel) |
| deep-research skill | Optional | PRISMA-mode systematic search accelerator |
| paper-verification skill | Optional | Batch DOI verification accelerator |

---

## File Structure (after complete pipeline run)

```
[project-root]/          ← ALL files flat (Editorial Manager requirement)
├── sci_writer_state.md  ← Pipeline state (resume checkpoint)
├── main.tex             ← LaTeX source (~700–900 lines)
├── references.bib       ← BibTeX database (≥130 entries, AuthorYYYYKeyword keys)
├── generate_figures.py  ← Python figure generation script (matplotlib)
├── fig_01_*.png         ← All figures at ≥300 DPI
├── ...
├── fig_0N_*.png
├── graphical_abstract.png  ← 400×300px
├── elsarticle.cls       ← [AUTO] downloaded from mirrors.ctan.org
├── elsarticle-num.bst   ← [AUTO] downloaded from mirrors.ctan.org
├── highlights.txt       ← 3–5 items, each ≤85 chars
├── cover_letter.md      ← With [USER] placeholders for phone/grant number
├── revision_log.md      ← P0/P1 revision record
├── review_report.md     ← 6-reviewer scores (R1/R2/R3 rounds)
├── gate_c_checklist.md  ← All items ✓
└── submission_package.zip  ← Upload-ready archive
```

---

## About

Developed by **Yuanjie Zhang (张元杰)** and **Prof. Kan Wang (王侃)**  
School of Sensing Science and Engineering, Shanghai Jiao Tong University  
Correspondence: wangkan@sjtu.edu.cn

> *Designed for researchers who want to write papers, not manage tools.*

---

*SCI-writer v4.1.0 · SJTU Wang Lab · 2026-05-14*
