# SCI-writer

> **Full-Chain Scientific Review Paper Orchestration System for Claude Code**
> *From research gap to submission-ready LaTeX — a single skill that orchestrates the entire academic review paper pipeline with built-in anti-hallucination, citation integrity gates, and multi-persona peer review simulation.*

[![Version](https://img.shields.io/badge/version-4.2.0-blue)](SKILL.md)
[![Target](https://img.shields.io/badge/target-Q1%20%2F%20CAS--TOP-red)](SKILL.md)
[![Gates](https://img.shields.io/badge/gates-A%20%2F%20B%20%2F%20C-green)](SKILL.md)
[![Anti-Hallucination](https://img.shields.io/badge/anti--hallucination-builtin-orange)](SKILL.md)
[![Pipeline](https://img.shields.io/badge/pipeline-11%20stages-purple)](SKILL.md)
[![Affiliation](https://img.shields.io/badge/Affiliation-SJTU-blue)](https://www.sjtu.edu.cn)

---

## What This Does

SCI-writer is a **Claude Code Skill** that turns your research idea into a submission-ready review paper through a structured 11-stage pipeline with 3 mandatory quality gates.

**Built-in specialization:** Deep configuration for wearable electrochemical sensing / microneedle array research (Biosensors and Bioelectronics, ACS Nano, etc.)

**Key innovation in v4.2:** The **measurement instrument chain** framework — treating the review paper as a unified cognitive model that simultaneously serves newcomers (educational) and domain experts (professional).

---

## What's New in v4.2

| Feature | Description |
|---------|-------------|
| **Unified Pedagogical-Rigor Framework** | Teaching and peer-review quality are no longer separate goals; the framework structure serves both simultaneously |
| **Measurement Chain Framework (§1.3)** | A single cognitive model (target → frontend → signal chain → intelligence → output) organizes the entire paper |
| **Technology History Timeline (§1.2)** | Temporal context for newcomers; milestone-based field evolution |
| **Search Pattern D/E/F** | Foundational & tutorial papers, Chinese literature (CNKI/Wanfang), commercial & industrial papers |
| **Knowledge Scaffolding (Sub-stage 4.5)** | Prerequisite maps, concept introduction protocol, decision flowcharts, benchmark tables |
| **Pedagogical Enhancement (Pass 2.5)** | Concept check, analogy check, decision guide check, quantitative table check |
| **R7 New Reader Simulator** | 7th reviewer: simulates a first-year graduate student; tests understandability without sacrificing rigor |
| **Decision Flowcharts** | Material × geometry selection guide and sensing modality selection matrix |
| **Commercial Benchmarks** | Dexcom G7, FreeStyle Libre 3, Medtronic Guardian 4, Senseonics Eversense 365 |
| **Chinese Research Groups** | 10+ CN research teams for balanced geographic coverage |

---

## Quick Start (3 Steps)

### Step 1 — Install

**Windows:**
```powershell
./install.ps1
```

**Mac/Linux:**
```bash
chmod +x install.sh && ./install.sh
```

**Manual:**
```bash
cp -r skills/SCI-writer ~/.claude/skills/
```

### Step 2 — Start the Pipeline

```
/sciw load microneedle      ← Built-in microneedle/electrochemical sensing config
/sciw init                   ← Interactive configuration for any domain
```

### Step 3 — Run

```
/sciw auto                   ← Full autonomous mode (pauses at each Gate)
/sciw stage 2                ← Jump to specific stage
/sciw resume                 ← Continue from last checkpoint
/sciw status                 ← Check progress
```

---

## The 11-Stage Pipeline

```
PHASE I  — FOUNDATION
  Stage 1   │ Domain Intelligence & Gap Mapping (+ history + framework)
  Stage 2   │ Literature Acquisition (Corpus Building, 8 search patterns)
  ▓▓▓▓▓▓▓▓▓ GATE A: Corpus Completeness ▓▓▓▓▓▓▓▓▓

PHASE II — CONSTRUCTION
  Stage 3   │ Deep Synthesis & Knowledge Extraction
  Stage 4   │ Narrative Architecture & Outline Design (+ Sub-stage 4.5 Knowledge Scaffolding)
  Stage 5   │ Section-by-Section Drafting (+ Pass 2.5 Pedagogical Enhancement)
  Stage 6   │ Figures, Tables & Visual Narrative
  Stage 6.5 │ Figure Mount & Cross-Reference Verification
  ▓▓▓▓▓▓▓▓▓ GATE B: Citation Integrity + Method-Type Audit ▓▓▓▓▓▓▓▓▓

PHASE III — REFINEMENT
  Stage 7   │ Multi-Persona Peer Review Simulation (7 reviewers: R1-R7)
  Stage 8   │ Revision & Rebuttal Engineering
  Stage 9   │ Journal Formatting & LaTeX Compilation
  ▓▓▓▓▓▓▓▓▓ GATE C: Submission Readiness Check ▓▓▓▓▓▓▓▓▓

PHASE IV — DELIVERY
  Stage 10  │ Submission Package Assembly
```

---

## Features

### Anti-Hallucination Gates
Three mandatory stops that cannot be skipped:
- **Gate A** — Corpus completeness (≥150 papers, ≥20/section, ≥40% recent)
- **Gate B** — Citation integrity audit + method-type consistency check
- **Gate C** — Submission readiness (reviewer score ≥80/100, R7 ≥70, zero unresolved citations)

### 7-Reviewer Peer Review Simulation
| Reviewer | Focus |
|----------|-------|
| R1 Domain Expert | Technical accuracy, depth, completeness |
| R2 Neighboring Field Expert | Interdisciplinary context, positioning |
| R3 Methods/Rigor Expert | Systematic coverage, methodology |
| R4 Clinical/Translational Expert | Clinical relevance, regulatory pathways |
| R5 Devil's Advocate | Central thesis challenge |
| R6 Format/Integration Auditor | LaTeX formatting, cross-references |
| R7 New Reader Simulator | Can a first-year grad student understand this? |

### Pipeline State Persistence
`sci_writer_state.md` written after every stage — pipeline survives context compaction and multi-day runs. Use `/sciw resume` to continue.

### Domain Configuration System
Inject domain-specific intelligence via YAML config. Built-in: wearable electrochemical sensing / microneedle arrays.

---

## Command Reference

```
/sciw init                  Configure title, journal, domain
/sciw load microneedle      Load built-in microneedle config
/sciw start                 Begin pipeline from Stage 1
/sciw auto                  Full autonomous run (Gate pauses)
/sciw stage [1-10]          Jump to specific stage
/sciw stage 6.5             Figure mount + cross-reference audit
/sciw gate [a/b/c]          Run quality gate only
/sciw search [query]        Literature search mode
/sciw write [section]       Write specific section
/sciw review                Run peer review simulation
/sciw verify                Citation audit
/sciw resume                Continue from last checkpoint
/sciw status                Show pipeline progress
/sciw export                Generate submission package
```

---

## File Structure

```
SCI-writer/
├── SKILL.md                           ← Main skill (copy to ~/.claude/skills/)
├── README.md                          ← This file
├── templates/
│   ├── microneedle-sensing.yaml       ← Built-in domain config (v2.0)
│   ├── generic-review.yaml            ← Blank template for other domains
│   └── cover-letter-template.md       ← Cover letter template
├── docs/
│   ├── anti-hallucination.md
│   └── companion-skills.md
├── install.ps1                        ← Windows installer
└── install.sh                         ← Mac/Linux installer
```

---

## Companion Skills (Optional)

These skills enhance capabilities but are NOT required:

| Skill | Enhances |
|-------|----------|
| `academic-paper` | Stage 5 writing (12-agent parallel) |
| `academic-paper-reviewer` | Stage 7 review simulation |
| `deep-research` | Stage 2 systematic search |
| `paper-verification` | Gate B citation check |
| `arxiv-search` | Stage 2 arXiv search |
| `scientific-visualization` | Stage 6 figure generation |
| `latex-document` | Stage 9 compilation |

---

## Citation

If you use SCI-writer in your research, please cite:

```bibtex
@software{SCI-writer2026,
  author = {Zhang, Yuanjie and Wang, Kan},
  title  = {SCI-writer: Full-Chain Scientific Review Paper Orchestration System},
  year   = {2026},
  url    = {https://github.com/ZhangYuanJie-SJTU/SCI-writer-skill}
}
```

---

*SCI-writer v4.2.0 — Designed for researchers who want to write papers, not manage tools.*
*SJTU Wang Lab | Zhang Yuanjie + Wang Kan | Updated: 2026-05-29*
