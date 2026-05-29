# SCI-writer v5.0.0 — Bootstrap Loader
# Claude Code: read this file first, then load SKILL.md sections as needed.

## Quick Commands

| Command | Action | What to load from SKILL.md |
|---------|--------|---------------------------|
| `/sciw load microneedle` | Load microneedle config + start Stage 1 | §Stage 1 + templates/microneedle-sensing.yaml |
| `/sciw init` | Interactive config for any domain | §Domain Configuration System |
| `/sciw start` | Begin from Stage 1 | §Stage 1 |
| `/sciw auto` | Full auto mode | All stages sequentially |
| `/sciw resume` | Continue from checkpoint | Read sci_writer_state.md first |
| `/sciw stage N` | Jump to stage N | §Stage N only |
| `/sciw review` | Run peer review | §Stage 7 |
| `/sciw verify` | Citation audit | §Gate B |
| `/sciw export` | Generate submission package | §Stage 10 |

## Stage → SKILL.md Section Map

| Stage | SKILL.md Section | Lines (approx) | Verification Script |
|-------|-----------------|----------------|-------------------|
| Stage 1 | `## Stage 1 — Domain Intelligence` | ~40 lines | — |
| Stage 2 | `## Stage 2 — Literature Acquisition` | ~150 lines | — |
| Gate A | `## ▓▓▓ GATE A` | ~30 lines | — |
| Stage 3 | `## Stage 3 — Deep Synthesis` | ~40 lines | — |
| Stage 4 | `## Stage 4 — Narrative Architecture` | ~120 lines | — |
| Stage 5 | `## Stage 5 — Iterative Section Drafting` | ~150 lines | — |
| Stage 6 | `## Stage 6 — Figures, Tables` | ~60 lines | — |
| Stage 6.5 | `## Stage 6.5 — Figure Mount` | ~80 lines | `scripts/verify_stage65.py` |
| Gate B | `## ▓▓▓ GATE B` | ~80 lines | `scripts/verify_gate_b.py` |
| Stage 7 | `## Stage 7 — Multi-Persona Peer Review` | ~120 lines | — |
| Stage 8 | `## Stage 8 — Revision & Rebuttal` | ~40 lines | — |
| Stage 9 | `## Stage 9 — Journal Formatting` | ~100 lines | `scripts/verify_gate_c.py` |
| Gate C | `## ▓▓▓ GATE C` | ~30 lines | `scripts/verify_gate_c.py` |
| Stage 10 | `## Stage 10 — Submission Package` | ~80 lines | `scripts/download_templates.py` |

## v5.0 Quality Architecture (new sections in SKILL.md)

| Section | Purpose | When to read |
|---------|---------|-------------|
| `## Thinking-First Protocol` | Force explicit reasoning before writing | Before Stage 3, 4, 5 |
| `## Model Adaptation Layer` | Auto-detect model tier, adjust scaffolding | At pipeline start |
| `## Writing Quality Bank` | Exemplary sentence patterns | During Stage 5 |
| `## Narrative Flow Engine` | Transition management + argument arc | During Stage 4, 5 |
| `## Argumentation Templates` | AREI pattern for sections | During Stage 4, 5 |
| `## Multi-Scale Quality System` | Paragraph/section/paper level checks | During Stage 5, Gate C |
| `## Self-Correction Protocol` | Uncertainty detection + re-verification | During Stage 5 |

## Companion Skills (auto-detected)

At pipeline start, silently check which are installed. Use when available, fall through to built-in fallback otherwise.

| Skill | Fallback if missing |
|-------|-------------------|
| `deep-research` | Built-in PRISMA + tavily-search |
| `literature-review` | Built-in systematic review protocol |
| `paper-analyze` | Built-in Stage 3 extraction |
| `academic-paper` | Built-in Stage 5 iterative loop |
| `academic-paper-reviewer` | Built-in Stage 7 8-reviewer panel |
| `paper-verification` | Built-in Gate B audit |
| `latex-document` | Built-in Stage 9 compilation |
| `scientific-visualization` | Built-in Python/matplotlib generation |

## Verification Scripts

| Script | Purpose | When to run |
|--------|---------|------------|
| `scripts/verify_stage65.py` | Figure mount + cross-reference audit | After Stage 6, before Gate B |
| `scripts/verify_gate_b.py` | BibTeX key audit + DOI check + NEEDS_REF | At Gate B |
| `scripts/verify_gate_c.py` | Abstract/highlights/word count + figure mount | At Gate C |
| `scripts/download_templates.py` | Download elsarticle.cls + .bst | At Stage 10 |

All scripts: `python scripts/<name>.py` from project directory. Pure stdlib, no dependencies.
