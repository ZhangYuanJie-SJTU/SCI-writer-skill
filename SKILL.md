# SCI-writer
## Full-Chain Scientific Review Paper Orchestration System
**Version:** 4.2.0 | **Target:** Q1/CAS-TOP Journals | **Mode:** Self-Contained + Optional Accelerators

### What's New in v4.2 (Changelog)
- **v4.1 → v4.2 major:**
  - **Unified Pedagogical-Rigor Framework [NEW]** — Teaching and peer-review quality are no longer separate goals; the "measurement instrument chain" narrative structure serves both simultaneously
  - **Stage 1.3 Measurement Chain Framework [NEW]** — §1 now includes a technology history timeline (§1.2) and a unifying measurement system framework (§1.3) that readers use as cognitive scaffolding throughout the paper
  - **Stage 2 Search Pattern D/E/F [NEW]** — Foundational & tutorial papers (Pattern D), Chinese literature via CNKI/Wanfang (Pattern E), Commercial & industrial papers (Pattern F)
  - **Stage 4 Sub-stage 4.5 Knowledge Scaffolding [NEW]** — Each section gets prerequisite mapping, concept introduction protocol, worked examples, and decision flowcharts
  - **Stage 5 Pass 2.5 Pedagogical Enhancement [NEW]** — Between content writing (Pass 2) and evidence audit (Pass 3): concept introduction check, analogy check, decision guide check, quantitative table check
  - **Stage 7 R7 New Reader Simulator [NEW]** — 7th reviewer simulates a first-year graduate student; tests understandability without sacrificing rigor
  - **Domain Config: Decision Flowcharts [NEW]** — Material×geometry selection guide and sensing modality selection matrix embedded in outline
  - **Domain Config: Commercial Benchmarks [NEW]** — Dexcom/Abbott/Medtronic/Senseonics product data for clinical validation context
  - **Domain Config: Chinese Research Groups [NEW]** — 10+ CN research teams added for balanced geographic coverage
- **v4.0 → v4.1 patch:**
  - Pipeline State Persistence · BibTeX Key Convention · Gate A Exception Path · Verification Scripts · Table Legend Check · Elsevier URL Fix · Stage 7 Threshold Fix
- **v3.0 → v4.0 upgrades:**
  - Stage 6.5 · R6 Reviewer · Method-Type Consistency · Score Escalation · [AUTO]/[USER] Classification

---

## When to Trigger

Invoke `/SCI-writer` when the user:
- Says "write a review paper", "全流程写综述", "sci综述", "academic review"
- Provides: a paper title + target journal + research domain simultaneously
- Asks to run any named stage: "stage 2", "gate-b", "run literature search"
- Says "start the pipeline", "全自动模式", `/sciw`

**Shorthand:** `/sciw` is an alias for `/SCI-writer`

---

## Skill Availability Map — Honest Fallbacks

Some tasks reference skills that may not be installed. SCI-writer has built-in fallbacks for all of them. **Never halt or error on a missing skill — fall through to the standalone protocol.**

| Skill referenced in task | Installed? | SCI-writer fallback |
|--------------------------|-----------|---------------------|
| `literature-survey-agent` | ✗ not a real skill name | Stage 2 PRISMA protocol + `tavily-search` |
| `sci-paper-writer` | ✗ not installed | Stage 5 four-pass writing protocol |
| `latex-compiler-pro` | ✗ not installed | Stage 9 4-pass bash compilation sequence |
| `file-organizer` | ✗ not installed | Stage 10 manual flat-directory assembly |
| `academic-image-fetcher` | ✗ not installed | Stage 6: Claude generates Python/matplotlib figures |
| `literature-review` | ✓ installed | Use directly at Stage 2 |
| `literature-research` | ✓ installed | Use directly at Stage 1 |
| `deep-research` | ✓ installed | Use at Stage 2 for systematic search |
| `paper-analyze` | ✓ installed | Use at Stage 3 for extraction |
| `academic-paper` | ✓ installed | Use at Stage 5 for writing |
| `academic-paper-reviewer` | ✓ installed | Use at Stage 7 for review simulation |
| `paper-verification` | ✓ installed | Use at Gate B for citation check |
| `latex-document` | ✓ installed | Use at Stage 9 for compilation |
| `scientific-visualization` | ✓ installed | Use at Stage 6 for figure generation |

**Rule:** when a task prompt names a non-existent skill, substitute the corresponding fallback from this table silently. Do not tell the user "this skill doesn't exist" — just execute the fallback.

---

## Architecture: Self-Contained Core + Optional Accelerators

```
┌──────────────────────────────────────────────────────────────┐
│              SCI-writer v4.2.0                               │
│        Full-Chain Review Paper Pipeline                       │
├──────────────────────────────────────────────────────────────┤
│  CORE PIPELINE — fully self-contained, zero dependencies      │
│  ─ All 10-stage logic + 3 quality Gates embedded              │
│  ─ PRISMA search protocol built-in (Stage 2)                  │
│  ─ 4-pass writing quality protocol built-in (Stage 5)         │
│  ─ Figure mount + cross-reference audit built-in (Stage 6.5)  │
│  ─ 6-persona peer review simulation built-in (Stage 7)        │
│  ─ Anti-hallucination + method-type audit built-in (Gate B)   │
│  ─ Works for ANY domain via YAML config                       │
│  ─ Distributable: ONE file install, full capability           │
├──────────────────────────────────────────────────────────────┤
│  ⚡ OPTIONAL ACCELERATORS (companion skills, if present)      │
│  ─ academic-pipeline: parallel multi-agent execution          │
│  ─ academic-paper: 12-agent automated writing                 │
│  ─ deep-research: automated multi-database PRISMA search      │
│  ─ literature-review: structured systematic review            │
│  ─ academic-paper-reviewer: automated 5-persona review        │
│  ─ paper-verification: batch citation integrity check         │
│  ─ start-my-day: daily literature monitoring                  │
│  ─ arxiv-search / tavily-search: fast live search             │
│                                                               │
│  ⚠ Zero accelerators installed = pipeline runs fully.        │
│    Accelerators add speed/automation, NOT new capability.     │
└──────────────────────────────────────────────────────────────┘
```

**At pipeline start:** Silently check which accelerator skills are present. Use them when available. Fall through to the embedded standalone protocol otherwise. Never block or halt on a missing skill.

---

## The 11-Stage Pipeline (v4.0)

```
PHASE I  — FOUNDATION
  Stage 1   │ Domain Intelligence & Gap Mapping
  Stage 2   │ Literature Acquisition (Corpus Building)
  ▓▓▓▓▓▓▓▓▓ GATE A: Corpus Completeness ▓▓▓▓▓▓▓▓▓

PHASE II — CONSTRUCTION
  Stage 3   │ Deep Synthesis & Knowledge Extraction
  Stage 4   │ Narrative Architecture & Outline Design
  Stage 5   │ Section-by-Section Drafting
  Stage 6   │ Figures, Tables & Visual Narrative
  Stage 6.5 │ Figure Mount & Cross-Reference Verification  ← NEW
  ▓▓▓▓▓▓▓▓▓ GATE B: Citation Integrity + Method-Type Audit ▓▓▓▓▓▓▓▓▓

PHASE III — REFINEMENT
  Stage 7   │ Multi-Persona Peer Review Simulation (6 reviewers)
  Stage 8   │ Revision & Rebuttal Engineering
  Stage 9   │ Journal Formatting & LaTeX Compilation
  ▓▓▓▓▓▓▓▓▓ GATE C: Submission Readiness Check ▓▓▓▓▓▓▓▓▓

PHASE IV — DELIVERY
  Stage 10  │ Submission Package Assembly
```

---

## Stage 1 — Domain Intelligence & Gap Mapping

**Goal:** Map the field comprehensively, identify what existing reviews miss, and define the paper's irreplaceable contribution.

**Standalone procedure:**
1. Ask user to provide: research domain, paper title, target journal, key research groups they know
2. Generate a conceptual map covering: core technologies → key applications → open challenges → emerging directions
3. Search for existing reviews in the field (use tavily-search or WebSearch):
   - Query pattern: `"[domain] review [year range]" site:sciencedirect.com OR site:nature.com`
   - Query pattern: `"[domain] comprehensive review" [journal name]`
   - Query pattern: `"[domain] tutorial introduction fundamentals" site:pubmed.ncbi.nlm.nih.gov`
4. For each found review: identify what scope it covers and what it omits
5. Build a **Technology History Timeline** (§1.2 content): map the field's evolution from first demonstration to current state, identifying 8–12 milestone papers with dates. This timeline becomes Fig. 1 in the final paper.
6. Design a **Unifying Framework Diagram** (§1.3 content): define the single cognitive model that organizes the entire paper. For engineering/technology reviews, the "measurement instrument chain" framework (被测量 → 前端感知 → 信号调理 → 数据处理 → 输出) is recommended. This framework must be:
   - Simple enough for a new graduate student to grasp in 30 seconds
   - Precise enough for a domain expert to see the design space
   - Comprehensive enough to accommodate all planned sections
   This framework becomes the paper's central figure and is referenced in every subsequent section.
7. Output a **Gap Statement** document:

```
## Research Gap Analysis
### Existing Reviews Found:
[List with scope summary]

### Identified Gaps:
1. [Gap 1]: [description] — last addressed: [year/author or "never"]
2. [Gap 2]: ...

### Our Paper's Unique Position:
[2-sentence differentiation statement]

### Contribution Claim (for Introduction §1.4):
This review is the FIRST to [specific claim], covering [scope] from [start] to [end].
```

⚡ **Accelerators (optional):** invoke `/scientific-brainstorming` for conceptual mapping, `/literature-research` for gap analysis

**Output:** `gap_analysis.md` saved to project directory

---

## Stage 2 — Literature Acquisition (Corpus Building)

**Goal:** Build a verified corpus of 150–250 papers with full metadata, covering all planned sections.

### Search Strategy (Universal Template)

For each section in the outline, run these search patterns:

**Pattern A — Foundational works:**
```
"[core technology]" AND "[application]" AND ("review" OR "overview")
Filter: highly cited papers (>50 citations), 2015–2022
```

**Pattern B — Recent advances:**
```
"[core technology]" AND "[application]" AND ("novel" OR "advanced" OR "emerging")
Filter: 2022–2026, high-impact journals
```

**Pattern C — Interdisciplinary bridges:**
```
"[technology A]" AND "[technology B]" AND "[target application]"
Filter: any year, look for integration papers
```

**Pattern D — Foundational & tutorial (for pedagogical depth):**
```
"[field]" AND ("tutorial" OR "introduction" OR "fundamentals" OR "primer" OR "basic principles")
Filter: highly cited review articles, textbook chapters, any year
```
Purpose: papers that explain core concepts accessibly. These are cited in §1 and §3.X introductory paragraphs to build reader understanding.

**Pattern E — Chinese literature (for geographic balance):**
```
Search CNKI/Wanfang: "[Chinese keywords]" AND "[field]"
Search PubMed: "[field]" AND ("China" OR "Chinese" in affiliation)
Filter: Q1/Q2 journals or top Chinese journals (化学进展, 分析化学, 传感器技术学报)
```
Purpose: ensure Chinese research groups are represented, especially for SJTU-affiliated authors.

**Pattern F — Commercial & industrial (for real-world context):**
```
"[product name]" AND ("clinical trial" OR "MARD" OR "FDA" OR "CE marking")
"[field]" AND ("patent" OR "commercialization" OR "manufacturing scale-up")
Filter: any year, include white papers and regulatory filings
```
Purpose: bridge the lab-to-market gap. Cited in §7 (Challenges & Commercialization).

**Search Sources (check in order):**
1. `tavily-search` with query + `site:pubmed.ncbi.nlm.nih.gov`
2. `tavily-search` with query + `site:sciencedirect.com`
3. `arxiv-search` if available, else `tavily-search` + `site:arxiv.org`
4. WebSearch with `"[exact title fragment]" filetype:pdf`
5. Grey literature: `tavily-search` + `site:researchgate.net` for preprints

### PRISMA-Informed Systematic Search Protocol

**This protocol is built-in — no external skill required. Execute before any search.**

**Step 0 — Define PICOS (document in `02_corpus.md` before searching):**
```
Population (P):   [what system/subject is studied]
Intervention (I): [the core technology being reviewed]
Comparison (C):   [what it compares against or integrates with]
Outcome (O):      [what metrics/results are extracted]
Study type (S):   [original research / prior reviews / in vivo validation]
```
Every inclusion/exclusion decision must trace back to one of these criteria.

**Step 1 — Build master search string per cluster:**
```
Core:     ("[primary keyword]" OR "[synonym]")
          AND ("[application domain]" OR "[variant]")
          AND ("[modifier: sensing/monitoring/detection]")
Date:     2019/01/01–2026/12/31 (keep pre-2019 seminal works if >100 citations)
Exclude:  conference abstracts only, editorials, letters without data
```

**Step 2 — Two-stage screening:**

*Title/abstract include if ANY:*
- Title directly contains primary keywords
- Abstract reports original experimental data OR systematic review
- Published in domain-relevant journal

*Title/abstract exclude if:*
- Conference abstract without corresponding journal paper
- Purely theoretical with no experimental validation
- Outside date range and citation count < 100

*Full-text include only if ALL:*
- Addresses ≥1 planned section topic
- Reports quantitative performance metrics (for technical sections)
- Peer-reviewed, non-predatory journal

**Step 3 — PRISMA flow tracking (record in `02_corpus.md`):**
```
Identified (all databases, pre-dedup): N = ___
After deduplication:                   N = ___
Screened (title/abstract):             N = ___
Eligible (full-text reviewed):         N = ___
Included (final corpus):               N = ___
Excluded at full-text (reasons):
  - Wrong topic:       N = ___
  - No quantitative data: N = ___
  - Quality threshold fail: N = ___
```

### BibTeX Key Naming Convention (mandatory — prevents cross-session key collisions)

All BibTeX keys must follow: **`LastnameYYYYKeyword`**

```
AuthorYYYYKeyword format:
- Lastname: First author's last name, no spaces (CamelCase for compound names)
- YYYY: 4-digit publication year
- Keyword: 2-8 char descriptor of the paper's core topic

Examples:
  Chen2022CNT        ← Chen 2022, carbon nanotube paper
  Fan2026EdgeAI      ← Fan 2026, edge AI paper
  Tehrani2022Wearable ← Tehrani 2022, wearable systems
  Zhang2025Glucose   ← Zhang 2025, glucose sensor

Forbidden:
  chen22, chen_2022, Smith et al 2023, ref001   ← ambiguous, not sortable
  Smith2023          ← missing keyword, will collide with other Smith 2023 papers
```

Enforce this standard when building `references.bib`. At Gate B, scan for keys that violate this pattern.

### Corpus Quality Filter

For each found paper, record in the corpus table:

| Field | Requirement |
|-------|-------------|
| DOI | Must be verifiable via doi.org |
| Year | 2019–2026 (allow exceptions for seminal works) |
| Journal tier | Prefer Q1; no preprints without peer review |
| Relevance | Must directly address one of the planned sections |
| Citation count | >10 for pre-2023; any for 2024+ |
| **Detection method** | **Record the method type (amperometry/EIS/fluorescence/ISE etc.) — required for Gate B method-type check** |

**Corpus Completeness Targets:**
- Total papers: ≥150
- Per major section: ≥20 papers
- Recent (2023–2026): ≥40% of total
- Target journal papers cited: ≥5 (shows scope awareness)

**Standalone procedure:**
1. Create a `corpus.md` file with sections matching the outline
2. For each section: run 3 searches, record 15–30 papers per section
3. Deduplicate (same paper may appear in multiple searches)
4. Verify at least 5 DOIs manually via WebSearch before proceeding to Gate A

⚡ **Accelerators (optional):** invoke `deep-research` in PRISMA mode for systematic search; `literature-review` for structured systematic review; `paper-analyze` for deep reading; `read-arxiv-paper` for arXiv papers; `start-my-day` for automated daily new-paper tracking during extended writing periods

---

## ▓▓▓ GATE A: Corpus Completeness Check ▓▓▓

**MANDATORY STOP.** Do not proceed to Stage 3 without passing all checks.

```
GATE A Checklist:
[ ] Total papers in corpus ≥ 150  (see exception path below if < 150)
[ ] Each planned section has ≥ 20 papers assigned
[ ] Papers from 2023–2026 are ≥ 40% of corpus
[ ] At least 5 DOIs manually verified as real
[ ] Target journal represented with ≥ 5 citations
[ ] No section has > 60% from a single research group (diversity check)
[ ] Detection method recorded for every paper that will be cited in method-specific sections
[ ] All BibTeX keys follow AuthorYYYYKeyword convention

Result: PASS (all ✓) → proceed to Stage 3
        FAIL → return to Stage 2 and fill gaps
```

### Gate A Exception Path — Domain-Limited Corpus

Some research domains have inherently fewer qualifying papers (emerging fields, niche technology intersections). If the corpus is < 150 but ≥ 80 after exhaustive search, use this exception path:

**Conditions for exception (ALL must be true):**
1. At least 3 independent search passes completed across ≥ 4 databases
2. Every planned major section has ≥ 10 papers (not 20) assigned
3. Domain is genuinely niche (< 500 total papers match PICOS criteria)
4. Document in `corpus_notes.md`: exact search queries run, databases searched, total raw hits before filtering

**Compensating controls when using exception:**
- Increase citation density in text: ≥ 2 citations per 3 sentences (vs normal 1 per 3)
- Flag in Introduction §1.4: "A systematic search of [N] peer-reviewed papers from 2019–2026 was conducted"
- Gate B verification rate: 100% of all [N]-tagged citations (vs normal high-risk-only audit)
- Stage 7 R3 (Methods/Rigor reviewer) will specifically probe search completeness — pre-prepare rebuttal

---

## Stage 3 — Deep Synthesis & Knowledge Extraction

**Goal:** Transform the raw corpus into structured knowledge: key findings, quantitative benchmarks, methodological taxonomy.

**Extraction Protocol (for each paper in corpus):**

Extract and store in `synthesis_notes.md`:
```
## [Author Year] — [Short Title]
- Detection method type: [amperometry / DPV / SWV / EIS / potentiometry / fluorescence / FSCV / other]
- Method/approach: [1 sentence]
- Key finding/result: [specific number or claim]
- Performance metrics: [if applicable: sensitivity, LOD, accuracy, etc.]
- Innovation vs prior work: [1 sentence]
- Limitation acknowledged: [1 sentence]
- Assigned section: [Section X.Y]
- Citation key: [Author_Year_Journal]
```

**⚠️ Method type recording is mandatory.** It feeds Gate B's method-type consistency check. A fluorescence paper cited in an EIS paragraph = automatic Gate B failure.

**Cross-paper synthesis tasks:**
1. **Performance comparison table:** extract all quantitative metrics → build comparison matrix
2. **Methodological taxonomy:** group papers by approach → identify 3–5 sub-categories per section
3. **Timeline analysis:** map publication dates → identify research trends and acceleration points
4. **Contradiction detection:** find papers with conflicting claims → note for balanced discussion

### Evidence Quality Grading (GRADE — built-in)

Assign every major extracted finding one of four evidence grades. Note grade in `synthesis_notes.md`. This determines hedging language in the draft.

| Grade | Symbol | Criteria | Writing hedge |
|-------|--------|----------|---------------|
| High | ⊕⊕⊕⊕ | Multiple consistent results, low risk of bias, large reproducible effect | State as established fact: "X achieves Y" |
| Moderate | ⊕⊕⊕○ | Single high-quality study, or multiple with minor limitations | "Studies demonstrate..." / "Evidence suggests..." |
| Low | ⊕⊕○○ | Few studies, methodological concerns, small sample sizes | "Preliminary evidence indicates..." |
| Very Low | ⊕○○○ | Single case report, no controls, highly inconsistent | "One study reported..." (do not generalize) |

**Contradiction resolution:** when two papers report conflicting values for the same metric, present both with exact values and attribute each: "Smith et al. reported X while Jones et al. found Y, likely attributable to [fabrication difference / measurement condition]."

⚡ **Accelerators (optional):** `paper-analyze` automates per-paper extraction; `systematic-review` provides structured PICOTS-aligned synthesis

---

## Stage 4 — Narrative Architecture & Outline Design

**Goal:** Build a logically airtight outline where each section has a clear purpose, the narrative flows from problem to solution, and the paper's unique contribution is unmistakable.

### Universal Outline Template (Adaptable — v4.2 Measurement Instrument Chain)

```
1. Introduction (~2,000–2,500 words)
   1.1 Clinical/societal motivation — establish urgency [why this matters]
   1.2 Technology history — key milestones from first demo to current state [temporal context]
   1.3 [Unifying framework] — the cognitive model for the entire paper ★ [cognitive map]
   1.4 Scope, organization, and unique contribution of this review [claim]

2. [Foundation Layer: Device Fabrication & Materials] (~2,500–3,500 words)
   [Cover the enabling technology/materials/fabrication]
   Sub-sections: organized by category (material/geometry/method/etc.)
   End with: Design decision guide (flowchart) for material × geometry selection

3. [Functional Layer: Sensing Principles & Modalities] (~2,500–3,500 words)
   [Cover the core functional mechanism — how the sensor generates a signal]
   Sub-sections: organized by operating principle or modality
   Begin with: foundational measurement concepts (accessible to newcomers)
   End with: Sensing modality selection matrix (quantitative comparison table)

4. [Application Layer: Target Biomarkers & Clinical Use] (~2,000–2,500 words)
   [Cover specific use cases and target analytes]
   Sub-sections: organized by application category (metabolic / ionic / stress / neural / drug)

5. [Integration Layer: Signal Chain & System Design] (~2,500–3,500 words) ★ KEY SECTION
   [Cover the COMPLETE signal chain from sensor interface to digital output]
   Sub-sections: sensor-skin interface → analog front-end → flexible substrate →
                 wireless communication → power management
   This section treats the entire system as a measurement instrument —
   the unique perspective of instrument science / measurement engineering

6. [Intelligence Layer: Data Processing & Edge AI] (~2,000–2,500 words)
   [Cover signal processing, calibration, edge AI, cloud connectivity]
   Include: 2–3 end-to-end system teardowns from literature (deep case studies)

7. Challenges, Commercialization & Future (~2,000–2,500 words)
   7.1 Open technical challenges [honest assessment]
   7.2 Commercialization landscape — existing products, patents, market
   7.3 Translation barriers (regulatory: FDA/CE/NMPA, cost, manufacturing)
   7.4 Emerging directions and research priorities
   7.5 Open questions list (15–25 items with priority ratings) ★ research guide

8. Conclusion (~500 words)
   [3 key takeaways, not a summary of what was written]
```

**Key differences from v4.1 outline:**
- §1.2 adds technology history timeline → builds temporal context for newcomers
- §1.3 adds unifying framework → the cognitive model referenced throughout the paper
- §2 ends with design decision guide → readers can make their own design choices
- §3 begins with foundational concepts → accessible to newcomers without losing depth
- §3 ends with modality selection matrix → quantitative comparison, not just narrative
- §5 is restructured as "Signal Chain" → the instrument science perspective (end-to-end)
- §6 includes system teardowns → real-world case studies for deeper understanding
- §7 adds commercialization + open questions → bridges lab-to-market gap

**The "measurement instrument chain" framework (§1.3) is the key innovation:**
it makes the paper simultaneously educational (clear cognitive structure) and
professional (design space analysis, quantitative benchmarks, system-level thinking).

### Outline → Figure Mapping (mandatory)

At outline stage, produce a `figure_plan.md` with this structure for EVERY figure:

```
## Fig. N — [Title]
- LaTeX label: fig:[shortname]     ← will become \label{fig:[shortname]}
- Planned \includegraphics file: fig_0N_[name].png
- Will be referenced in text at: §[X.Y], paragraph [description]
- Required \ref{} sentence: "[proposed sentence that mentions this figure]"
```

This mapping becomes the checklist for Stage 6.5. Figures without a planned `\ref{}` location are **not allowed** — add one before proceeding.

### Sub-stage 4.5 — Knowledge Scaffolding Design (v4.2 — pedagogical architecture)

**Goal:** Ensure every section builds reader understanding progressively, not just presents facts. This is NOT a separate "educational layer" — it is embedded into the section structure itself.

**For each section in the outline, define:**

**A. Prerequisite Map:**
```
§3.2 (Amperometry) prerequisites:
  → §3.1 covers: electrode-electrolyte interface, Faradaic current
  → External: basic circuit theory (Ohm's law, RC circuits)
  → Concept to introduce before first use: "overpotential"
```

**B. Concept Introduction Protocol (applied during Stage 5 Pass 2.5):**
- Every technical term MUST have a one-sentence physical meaning explanation at first occurrence
- At least one analogy per section linking to instrument science / circuits / measurement
- Example: "EIS measures how the electrode interface resists current at different frequencies — analogous to measuring the frequency response of a filter circuit"

**C. Decision Flowchart Specification (becomes a figure):**
For sections covering design choices (materials, sensing modalities, circuit topologies), specify a decision flowchart:
```
Decision chart for §2.5: Material × Geometry selection
Input: target analyte, wear duration, manufacturing capability
Output: recommended material + geometry + fabrication method
```
This flowchart is designed here (Stage 4) and generated in Stage 6.

**D. Quantitative Benchmark Table Specification:**
For each technical section, define the comparison table that will appear at its end:
```
§3 end-of-section table: Sensing modality comparison matrix
Columns: [modality] [analyte] [LOD] [sensitivity] [linear range] [response time] [stability] [power]
```

**E. What-We-Know / What-We-Don't Map:**
For §7, pre-define the list of open questions (15–25 items) with priority ratings. This is both a teaching tool ("here's what we don't know yet") and a research guide ("here's where you can contribute").

### Narrative Flow Validation

Before finalizing outline, verify:
1. **Problem → Solution arc:** Does §1 set up a problem that §2–6 solve?
2. **No orphan sections:** Can each section justify why it belongs in THIS review vs. a different one?
3. **Unique contribution visible:** Is the "first to cover X" claim reflected in the section structure?
4. **Journal scope fit:** Does the outline match the target journal's recent special issues/themes?

⚡ **Accelerators (optional):** invoke `academic-paper` in outline mode; `scientific-critical-thinking` for narrative critique

---

## Stage 5 — Section-by-Section Drafting

**Goal:** Write each section to publication quality, with every claim sourced, every number verified.

### Writing Protocol Per Section

**Pre-writing checklist:**
- [ ] Section has ≥15 papers assigned in corpus
- [ ] Performance comparison table (if applicable) is complete
- [ ] Methodological taxonomy for this section is defined
- [ ] Previous section has been written (maintain narrative continuity)

**Drafting prompt structure:**
```
Write Section [X.Y]: [Title]

Context:
- Target journal: [journal name] — style: [formal/concise/detailed]
- Paper title: [full title]
- This section covers: [scope description]
- Connects to: §[X-1] (preceding) and §[X+1] (following)

Source papers to incorporate:
[list 10–15 most relevant papers with key findings AND their method types]

Performance data to mention:
[list 3–5 specific numbers with sources]

Specific claims to make:
1. [Claim 1] — supported by [Author Year] — method type: [X]
2. [Claim 2] — supported by [Author Year] — method type: [X]

Anti-hallucination constraint:
Every specific number, every "first", every superlative MUST cite a paper
from the provided list above. If you cannot support a claim with the
provided papers, write [NEEDS_REF] as a placeholder instead of inventing.

Method-type constraint:
If this section describes [method type], only cite papers that use [method type].
Do NOT cite fluorescence papers in an electrochemical section.
Do NOT cite in vitro papers as clinical validation evidence.
```

### Electrochemical Domain Formula Bank (Wearable Sensing)

Insert these equations into the appropriate sections. All LaTeX-ready.

**Amperometry — Cottrell equation (current-time response):**
```latex
i(t) = \frac{nFAD^{1/2}C}{\pi^{1/2}t^{1/2}}
```
*n*: electrons transferred; *F*: Faraday constant; *A*: electrode area; *D*: diffusion coefficient; *C*: analyte concentration.

**Voltammetry — Randles–Ševčík (peak current vs scan rate):**
```latex
i_p = 0.4463 \, nFAC\left(\frac{nFvD}{RT}\right)^{1/2}
```
*v*: scan rate; *R*: gas constant; *T*: temperature.

**Potentiometry — Nernst equation (ion-selective electrodes):**
```latex
E = E^0 + \frac{RT}{z_iF}\ln a_i
```
*z_i*: charge of ion *i*; *a_i*: activity of ion *i*. Nernstian slope at 25°C: 59.2/z_i mV/decade.

**Electrode kinetics — Butler–Volmer:**
```latex
i = i_0\left[\exp\!\left(\frac{\alpha_a F \eta}{RT}\right) - \exp\!\left(-\frac{\alpha_c F \eta}{RT}\right)\right]
```
*i_0*: exchange current density; *α*: transfer coefficients; *η*: overpotential.

**EIS — Randles cell impedance:**
```latex
Z = R_s + \frac{1}{j\omega C_{dl} + \frac{1}{R_{ct} + Z_W}}
```
*R_s*: solution resistance; *C_dl*: double-layer capacitance; *R_ct*: charge transfer resistance; *Z_W*: Warburg diffusion impedance.

**Limit of detection (LOD) — IUPAC:**
```latex
\text{LOD} = \frac{3\sigma_b}{S}
```
*σ_b*: standard deviation of blank signal; *S*: sensitivity (slope of calibration curve).

**Linear range sensitivity:**
```latex
S = \frac{\Delta i}{\Delta C} \quad [\mu\text{A}\,\text{mM}^{-1}\,\text{cm}^{-2}]
```

Use these formulas consistently. When citing a sensitivity value like "12 μA mM⁻¹ cm⁻²", always confirm it traces to a specific Table/Figure in a verified corpus paper.

### Four-Pass Writing Quality Protocol (built-in)

Each section must complete all 4 passes before moving to the next section.

**Pass 1 — Structure (5–10 min per section):**
- Write the section heading and 3–5 topic sentences only (one per paragraph)
- Each topic sentence = a single falsifiable claim the paragraph will prove
- List at the end: "§[X] makes these claims: [1], [2], [3]"
- Validate: does the section logically follow from §[X-1]? Does it set up §[X+1]?
- Do NOT write body text yet — skeleton only

**Pass 2 — Content (20–40 min per section):**
- Expand each topic sentence into a full paragraph (150–250 words)
- Assign a source paper from corpus to every technical claim (use `[NEEDS_REF: claim]` if none)
- Cite with exact location: "Smith et al. (Table 2) reported..." or "as shown in Fig. 3 of [ref]"
- End each paragraph with a transition sentence to the next claim

**Pass 2.5 — Pedagogical Enhancement (10 min per section) (NEW in v4.2):**
- **Concept introduction check:** every technical term at first occurrence has a one-sentence physical meaning explanation. If not, add one inline (no separate Box needed — one sentence suffices).
- **Analogy check:** at least one analogy per section linking to instrument science / circuits / measurement. Example: "the charge-transfer resistance Rct in EIS is analogous to the output impedance of a circuit — higher Rct means the electrode 'resists' the electrochemical reaction more."
- **Decision guide check:** if this section covers design choices, verify a decision flowchart or selection matrix is referenced (from Stage 4 Sub-stage 4.5). If missing, add a forward reference to the relevant figure.
- **Quantitative table check:** key performance data is presented in a comparison table (not only in narrative text). Tables serve both quick-reference (expert) and learning (newcomer) purposes.
- **Section-opening motivation check:** the first paragraph answers "why does this section matter?" before diving into technical content. This is NOT "In this section, we will..." — it is a substantive motivation statement.

**Pass 3 — Evidence audit (10–15 min per section):**
- Scan for ALL: numbers, percentages, "first", "highest", "best", "only", "novel", "unprecedented"
- For each: is it in a verified corpus paper? Does the paper actually contain this value?
- **Method-type spot check:** for each citation in a method-specific paragraph, confirm the cited paper actually uses that method. A fluorescence paper cited in an EIS paragraph = flag immediately.
- If yes: tag `[V]` and keep. If no: replace with `[NEEDS_REF]` or rewrite without the superlative
- Check citation density: ≥1 citation per 3 sentences in technical paragraphs

**Pass 4 — Flow and coherence (10 min per section):**
- First sentence: bridge from previous section ("Building on the [X] framework established in §[N]...")
- Last sentence: bridge to next section ("These [X] principles are integrated into system-level circuits, as detailed in §[N+1]...")
- Remove any sentence that repeats a claim already made in another section
- **Figure forward-reference check (STRICT):** for every figure planned in `figure_plan.md` that belongs to this section, verify a `\ref{fig:[shortname]}` command actually appears in the written text. A figure "mentioned in planning" but absent from the text = Pass 4 FAIL. Write the reference sentence if it is missing.

### Style Guidelines (Journal-Agnostic)

- **Paragraph length:** 150–250 words (one focused argument per paragraph)
- **Citation density:** at least 1 citation per 3 sentences in technical sections
- **Tense:** present tense for established facts; past tense for specific studies ("Smith et al. demonstrated...")
- **Quantitative claims:** always include units, error ranges if available
- **Avoidance list:** "novel", "state-of-the-art", "unprecedented" without citation
- **Figure integration:** mention every figure in text with `\ref{fig:X}` BEFORE the figure environment appears

⚡ **Accelerators (optional):** `academic-paper` in section mode runs Passes 2–4 in parallel with multiple agents; `scientific-writing` provides style polish; `paper-writing` handles individual section generation

---

## Stage 6 — Figures, Tables & Visual Narrative

**Goal:** Create figures that carry scientific argument, not just decoration. Generate all figure files and update LaTeX source.

### Required Figure Set (Minimum for Any Review)

| Figure | Purpose | Content |
|--------|---------|---------|
| Graphical Abstract | First impression | Full-chain system overview, 400×300px |
| Fig. 1 | Motivation | Timeline/growth of field + publication trend |
| Fig. 2–3 | Foundation | Technology taxonomy (hierarchical diagram) |
| Fig. 4 | Comparison | Quantitative performance benchmarks (radar/bar) |
| Fig. 5–6 | Applications | Application domains + representative examples |
| Fig. 7 | Integration | System architecture block diagram |
| Fig. 8 | Future | Roadmap / challenge-opportunity matrix |

### Required Table Set

| Table | Purpose |
|-------|---------|
| Table 1 | Materials/methods taxonomy with key references |
| Table 2 | Quantitative performance comparison (comprehensive) |
| Table 3 | Clinical/validation studies summary |

### Figure Generation Procedure (Standalone)

**Preferred approach — Python/matplotlib (avoids pdflatex dependency):**
```python
import matplotlib
matplotlib.use('Agg')  # headless rendering — no display required
import matplotlib.pyplot as plt
# DPI 300 for publication quality
plt.savefig('fig_0N_name.png', dpi=300, bbox_inches='tight', facecolor='white')
```

This approach works regardless of whether pdflatex/TikZ is installed. Always prefer matplotlib over TikZ for standalone figure generation — TikZ requires pdflatex which may not be present.

**For schematic/architecture diagrams:**
- Use `matplotlib.patches.FancyBboxPatch` for boxes, `ax.annotate` with `arrowprops` for arrows
- If TikZ source is also written, generate a matplotlib equivalent as the primary PNG output

**For performance comparison charts:**
1. Extract all quantitative metrics from `synthesis_notes.md` into a table
2. Identify the 2 most important metrics for this field
3. Generate a comparison plot: scatter (metric A vs B) or bar (ranked by metric)
4. Annotate with author labels for key data points

**For graphical abstract:**
- Generate or crop from Fig. 1 to 400×300 px
- Minimal text overlay — visual only
- Use PIL/Pillow for cropping: `img.crop((x0, y0, x1, y1)).save('graphical_abstract.png')`

### ⚠️ Critical: After generating each figure PNG, immediately update main.tex

For each generated figure, find the corresponding `\begin{figure}` environment in main.tex and:
1. **Uncomment** the `\includegraphics` line if it was commented out
2. **Verify** the filename matches exactly (case-sensitive on Linux)
3. **Verify** a `\label{fig:shortname}` is present

**Do NOT leave `\includegraphics` commented out pending "later review"** — this is the single most common failure mode. If the PNG file exists, the `\includegraphics` must be active.

⚡ **Accelerators (optional):** invoke `scientific-visualization` for chart generation; `extract-paper-images` for reference figure extraction; `scientific-slides` for schematic design

---

## Stage 6.5 — Figure Mount & Cross-Reference Verification ← NEW

**Goal:** Catch all disconnects between generated figure files and their LaTeX integration before Gate B. This stage was introduced in v4.0 after real-world experience showed that generated figures with commented-out `\includegraphics` commands produce blank boxes in the final PDF — a defect invisible until compilation.

**This stage is MANDATORY and cannot be skipped.**

### Step 1 — Figure File Audit

Run these checks in the project directory:

```python
# Figure file existence check
import os, re

fig_files = [f for f in os.listdir('.') if re.match(r'fig_\d+.*\.(png|eps|pdf)$', f)]
print("Figure files present:", sorted(fig_files))
```

For each figure in `figure_plan.md`: confirm the PNG file exists. If missing, generate it now (do not proceed).

### Step 2 — Commented-out \includegraphics Audit

Search main.tex for all commented-out includegraphics commands:

```python
with open('main.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    stripped = line.strip()
    if stripped.startswith('%') and 'includegraphics' in stripped:
        print(f"Line {i}: COMMENTED OUT — {stripped}")
```

**If any are found: uncomment them immediately.** This is a hard stop — do not proceed to Gate B with any commented-out `\includegraphics`.

### Step 3 — Cross-Reference Completeness Audit

Every `\label{fig:}` must have at least one `\ref{fig:}` in the text. Run:

```python
import re

with open('main.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all figure labels
labels = re.findall(r'\\label\{(fig:[^}]+)\}', content)
# Find all figure refs
refs = re.findall(r'\\ref\{(fig:[^}]+)\}', content)

ref_set = set(refs)
for label in labels:
    if label not in ref_set:
        print(f"ORPHAN FIGURE: \\label{{{label}}} has no \\ref in text")
    else:
        print(f"OK: {label}")
```

**For every orphan figure found:** go to the section where this figure belongs (from `figure_plan.md`) and add the planned reference sentence. Do not proceed to Gate B with orphan figures.

### Step 4 — Table Cross-Reference Audit

Apply the same check for tables:

```python
tab_labels = re.findall(r'\\label\{(tab:[^}]+)\}', content)
tab_refs = re.findall(r'\\ref\{(tab:[^}]+)\}', content)
tab_ref_set = set(tab_refs)

for label in tab_labels:
    if label not in tab_ref_set:
        print(f"ORPHAN TABLE: \\label{{{label}}} has no \\ref in text")
```

### Step 5 — Caption Completeness

For each `\begin{figure}` environment: verify it has a `\caption{}` that is non-empty and includes a panel-level description if the figure has sub-panels (a), (b), (c)...

### Step 5 — Table Caption Legend Consistency Check (NEW in v4.1)

For tables using notation symbols in the body (e.g., H/A/B/E or ✓/✗ or superscript letters), verify every symbol in the table body is defined in the caption:

```python
import re

with open('main.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all table environments
table_blocks = re.findall(r'\\begin\{table\}.*?\\end\{table\}', content, re.DOTALL)

for i, block in enumerate(table_blocks):
    caption = re.search(r'\\caption\{(.+?)\}', block, re.DOTALL)
    if not caption:
        print(f"Table {i+1}: MISSING CAPTION")
        continue
    cap_text = caption.group(1)

    # Check for common legend patterns: "X = ..." in caption
    legend_defined = re.findall(r'\b([A-Z])\s*[=~]\s*', cap_text)

    # Check for those same symbols used as standalone entries in the table body
    # (rough heuristic: single uppercase letters surrounded by & or \\ or whitespace)
    symbols_used = re.findall(r'(?:^|&|\\\\\s*)\s*([A-Z])\s*(?:&|\\\\|$)', block, re.MULTILINE)

    undefined = set(symbols_used) - set(legend_defined) - {'H', 'A', 'B', 'C'}  # exclude column headers
    if undefined:
        print(f"Table {i+1}: Symbols used but NOT defined in caption: {undefined}")
    else:
        print(f"Table {i+1}: OK — all symbols accounted for")
```

**Note:** This is a heuristic scan. Always manually review Table captions after the script runs to catch legend entries the regex misses.

### Stage 6.5 Exit Gate

```
Stage 6.5 Checklist:
[ ] All planned figures have PNG files on disk
[ ] Zero commented-out \includegraphics commands in main.tex
[ ] Every \label{fig:X} has ≥1 \ref{fig:X} in text
[ ] Every \label{tab:X} has ≥1 \ref{tab:X} in text
[ ] Every figure environment has a non-empty \caption
[ ] Table legend symbols: every symbol used in table body is defined in its caption

PASS → proceed to Gate B
FAIL → fix issues and re-run Stage 6.5 — do NOT skip
```

---

## ▓▓▓ GATE B: Citation Integrity + Method-Type Audit ▓▓▓

**MANDATORY STOP. This gate prevents academic misconduct AND method-type mismatch errors.**

### Anti-Hallucination Protocol

Every citation in the draft must be classified:

```
[VERIFIED]  — DOI confirmed via WebSearch/doi.org lookup
[NOT_FOUND] — Paper cannot be located; MUST be removed from draft
[MISMATCH]  — Citation details don't match the actual paper; MUST be corrected
[NEEDS_REF] — Claim flagged in Stage 5 as needing citation; MUST be resolved
[METHOD_X]  — Method type mismatch: paper uses X but sentence claims Y; MUST be corrected
```

### Gate B Citation Verification Tiers

Not all citations need equal scrutiny. Use tiered verification to focus effort where hallucination risk is highest:

| Tier | Citations | Verification required |
|------|-----------|----------------------|
| **Tier 1 — All citations** | Every entry in references.bib | Confirm BibTeX key follows AuthorYYYYKeyword; DOI field is present and plausible format |
| **Tier 2 — [N] and [U] tagged** | Unverified + user-provided citations | Full search: title + author + year confirmed via tavily-search or doi.org lookup |
| **Tier 3 — High-risk** | Any citation with: specific numbers, "first", superlatives, 2025–2026 dates, unusual DOI format | DOI live-check + verify the specific metric is in the paper (not just the paper exists) |

**Exception:** If Gate A exception path was used (corpus < 150), ALL citations are Tier 3.

**BibTeX key audit (Tier 1 — automated):**
```python
import re

with open('references.bib', 'r', encoding='utf-8') as f:
    bib_content = f.read()

keys = re.findall(r'@\w+\{([^,]+),', bib_content)
pattern = re.compile(r'^[A-Z][a-z]+\d{4}[A-Z][a-zA-Z]+$')

print(f"Total entries: {len(keys)}")
for key in keys:
    if not pattern.match(key):
        print(f"  NON-STANDARD KEY: {key}")
```

### Gate B Procedure — Part 1: Existence Check

For each citation flagged [N], [U], or as high-risk (Tier 2/3):
1. Search: `"[exact title]" [first author] [year]` via tavily-search
2. If found: verify author names, year, journal, DOI match
3. If NOT found after 2 searches: mark [NOT_FOUND] — do not invent corrections
4. If metrics cited (Tier 3): verify the specific number appears in the source paper

### Gate B Procedure — Part 2: Method-Type Consistency Check (NEW in v4.0)

For every citation in a method-specific section (EIS section, amperometry section, etc.):

1. Look up the paper's recorded method type in `synthesis_notes.md`
2. Compare against the method type claimed in the citing sentence
3. **Flag as `[METHOD_X]` if there is a mismatch:**
   - Fluorescence/optical paper cited in an EIS/electrochemical section → [METHOD_X]
   - In vitro paper cited as "in vivo validated" → [METHOD_X]
   - Non-wearable benchtop paper cited as "wearable demonstration" → [METHOD_X]

**Resolution for [METHOD_X] citations:**
- Option A: Rewrite the sentence to accurately describe what the cited paper actually does
- Option B: Move the citation to a more appropriate section
- Option C: Replace with a paper that genuinely uses the described method

**Example fix (from real case):**
```
BEFORE (wrong): "EIS-based aptasensor platforms have also demonstrated ISF cortisol monitoring
                 with diurnal rhythm tracking [Zhou2025Cortisol]"
REASON: Zhou2025Cortisol uses HCR fluorescence amplification, not EIS

AFTER (correct): "As a complementary optical approach, fluorescence-based aptasensor
                  detection using HCR amplification on swellable hydrogel MNA patches
                  has demonstrated ISF cortisol monitoring [Zhou2025Cortisol] —
                  illustrating that the MNA ISF-sampling platform is transduction-agnostic."
```

⚡ **Accelerators (optional):** invoke `paper-verification` (phd-skills) for batch verification; `academic-paper` in citation-check mode

```
GATE B Checklist:
[ ] Tier 1 audit: all BibTeX keys follow AuthorYYYYKeyword convention
[ ] Tier 1 audit: every entry has a DOI field in plausible format
[ ] Tier 2 audit: all [N] and [U] citations verified (author/year/journal/DOI)
[ ] Tier 3 audit: all high-risk citations — specific numbers confirmed in source
[ ] All [NEEDS_REF] placeholders resolved or acknowledged
[ ] Zero citations marked [NOT_FOUND] remain in draft
[ ] Zero citations marked [MISMATCH] remain in draft
[ ] Zero citations marked [METHOD_X] remain in draft
[ ] Reference count ≥ 130 (verify: grep -c "@" references.bib)
[ ] No section has < 8 references
[ ] Stage 6.5 has been completed (figure mount audit passed)

PASS → proceed to Stage 7
FAIL → return to Stage 5/corpus and fix
```

---

## Stage 7 — Multi-Persona Peer Review Simulation

**Goal:** Identify every weakness the reviewers will find — before submission.

### The 6-Reviewer Panel (v4.0 — added R6)

**R1 — Domain Expert (Field Authority)**
Focus: Technical accuracy, depth, completeness within the field
Attack vectors:
- "You omitted the key work by [prominent group]"
- "Your performance benchmarks are inconsistent with the actual papers"
- "Section X mischaracterizes the mechanism of Y"

**R2 — Neighboring Field Expert (Adjacent Domain)**
Focus: Interdisciplinary context, positioning vs. adjacent fields
Attack vectors:
- "This has been done better in [adjacent field]"
- "You don't compare to [competing technology]"
- "The introduction overclaims novelty"

**R3 — Methods/Rigor Expert (Systematic Review Quality)**
Focus: Systematic coverage, methodology of the review itself
Attack vectors:
- "No search methodology described (not PRISMA-compliant)"
- "Selection criteria for included papers are not clear"
- "Time range not specified or justified"

**R4 — Clinical/Translational Expert**
Focus: Clinical relevance, regulatory pathway, in vivo evidence quality
Attack vectors:
- "In vitro results cited as clinical evidence"
- "No comparison to commercial gold standard (e.g., Dexcom G7 MARD)"
- "Regulatory pathway analysis is superficial"

**R5 — Devil's Advocate (Central Thesis Challenger)**
Focus: The central thesis — is the "full-chain" or "integrated" narrative actually justified?
Attack vectors:
- "Is this really a unified review or just N adjacent topics stapled together?"
- "The connection between Section X and Section Y is unclear"
- "Your 'unique contribution' claim is undermined by [existing paper]"

**R6 — Format/Integration Auditor (NEW in v4.0)**
Focus: LaTeX formatting, figure mounting, cross-references, journal compliance
Attack vectors:
- "Figure X is referenced in the text but not shown — missing `\includegraphics`?"
- "Table 1 has a legend entry 'E' not defined in the caption"
- "Figure Y appears in the paper but is never mentioned in the text"
- "Line numbers are disabled — journal requires `\linenumbers`"
- "Abstract word count exceeds 300 words"
- "Highlights.txt entry exceeds 85 characters"
- "Cover letter is missing recommended reviewers section"

**R6 detailed checklist (run for every submission):**
```
R6 Checks:
[ ] Every \includegraphics file exists on disk (not commented out)
[ ] Every \label{fig:X} has ≥1 \ref{fig:X} in text
[ ] Every \label{tab:X} has ≥1 \ref{tab:X} in text
[ ] Abstract: ≤300 words, 0 citations, 0 undefined abbreviations
[ ] Highlights: 3–5 items, each ≤85 chars including spaces
[ ] \linenumbers is active (required for B&B review)
[ ] Table captions: all legend symbols defined (no undefined entries)
[ ] Author block: ORCID present, affiliations complete
[ ] CRediT authorship statement: included
[ ] Declaration of competing interests: included
[ ] Data availability statement: included
[ ] Grant numbers in acknowledgments (or explicit "No funding" statement)
```

**R7 — New Reader Simulator (NEW in v4.2)**
Focus: Can a first-year graduate student in the author's field read this paper and emerge with a working understanding of the entire domain?
Test scenario: "You are a first-year Master's student in [instrument science / biomedical engineering / chemistry]. You've taken basic courses but have never worked in this specific field."

Evaluation questions (answerable after reading):
1. After §1: Can you draw the complete system block diagram from memory?
2. After §2: Do you know "if I were to build a [X] sensor, what material and geometry should I choose?"
3. After §3: Can you explain the fundamental difference between [modality A] and [modality B] in physical terms?
4. After §5: Can you identify the noise sources at each stage of the signal chain?
5. After §7: Do you know what problems in this field remain unsolved?

Scoring (25 pts × 4 dimensions):
- **Understandability** (25): Are concepts introduced progressively? Are analogies appropriate?
- **Actionability** (25): After reading, could the reader independently design a basic experiment?
- **Completeness** (25): Are there knowledge gaps that would block the reader?
- **Depth** (25): Does the paper go beyond textbook-level understanding?

R7 < 70 = add pedagogical scaffolding (concept introductions, analogies, decision guides)
     but do NOT reduce technical depth — add clarity, not simplification.
R7 is scored in addition to R1–R6; it does not replace any existing reviewer.

### Scoring Protocol

For each reviewer, score 0–100 on:
- Technical rigor (25 pts)
- Completeness of coverage (25 pts)
- Clarity and organization (25 pts)
- Novelty and positioning (25 pts)

### Score Escalation Rule — Three Rounds (v4.1 fix: resolves threshold contradiction)

Stage 7 runs up to 3 times across the pipeline. Each round has its own threshold:

| Round | When | Pass threshold | Min single reviewer (R1–R6) | R7 minimum |
|-------|------|---------------|---------------------------|------------|
| **R1** — Initial Stage 7 (pre-Stage 8) | After Stage 6.5 | avg ≥ 78 | ≥ 70 | ≥ 65 |
| **R2** — After Stage 8 P0 fixes | Mandatory re-score after P0 revisions | avg ≥ 80 | ≥ 75 | ≥ 70 |
| **R3** — After Stage 8 P1 fixes | Optional re-score after P1 revisions | avg ≥ 82 | ≥ 78 | ≥ 75 |

**Additional constraints (all rounds):**
- R6 (Format Auditor) score < 70 in any round → fix formatting before re-scoring R6
- R7 (New Reader Simulator) score < 65 in R1 → add pedagogical scaffolding and re-score
- If avg score (R1–R6) decreases from R1→R2 after revisions: the revisions were cosmetic — return to Stage 5 for substantive rewriting
- **Final delivery standard: R2 avg (R1–R6) ≥ 80 AND R7 ≥ 70** (R3 is best-effort, not blocking)

**Gate C uses R2 avg score (R1–R6)** as the primary quality metric, plus **R7 ≥ 70** as the pedagogical quality metric. Record all round scores in `review_report.md`.

⚡ **Accelerators (optional):** invoke `academic-paper-reviewer` in full-review mode; `reviewer-defense` for pre-building rebuttals; `peer-review` for additional perspectives

---

## Stage 8 — Revision & Rebuttal Engineering

**Goal:** Address every identified weakness systematically, strengthen the paper, and pre-build the point-by-point rebuttal.

### Revision Priority Matrix

| Priority | Issue Type | Action |
|----------|-----------|--------|
| P0 — Critical | Missing key citations, factual errors, method-type mismatches, figure mount failures | Fix before anything else; re-run Stage 6.5 after fix |
| P1 — Major | Weak arguments, unclear connections, insufficient depth, cross-reference gaps | Fix in this stage |
| P2 — Minor | Language polish, formatting, figure captions, caption legend completeness | Fix in Stage 9 |

### After P0 Fix: Mandatory Re-Run

After fixing any P0 issue that touches LaTeX structure:
1. **Re-run Stage 6.5** (figure mount audit) — P0 fixes often involve adding/uncomment `\includegraphics`
2. **Re-score Stage 7** with Round 2 threshold (avg ≥ 80)
3. Confirm the specific reviewer concern that triggered P0 is addressed

### Rebuttal Template

For each reviewer concern:
```
## Reviewer [N], Comment [M]

**Concern:** [exact quote or paraphrase]
**Classification:** [Valid / Partially valid / Misunderstanding]

**Our Response:**
[For valid concerns:]
We agree with the reviewer. We have [specific action taken] in [Section X, Lines Y-Z].
The revised text now reads: "[specific new text]"

[For misunderstandings:]
We respectfully clarify that [explanation]. This is supported by [citation].
We have added [clarifying sentence] to Section X to prevent this misunderstanding.

**Evidence of change:** [Section + line reference in revised manuscript]
```

⚡ **Accelerators (optional):** invoke `academic-paper` in revision-coach mode; `reviewer-defense` for rebuttal strategy; `scientific-writing` for prose improvement

---

## Stage 9 — Journal Formatting & LaTeX Compilation

**Goal:** Produce submission-ready files that pass editorial desk review instantly.

### Biosensors and Bioelectronics (B&B) — Specific Requirements

**⚠️ Critical constraints — deviating from these causes desk rejection:**
- **All files in project root — NO subdirectories.** `main.tex`, `references.bib`, all `fig_*.eps/png` must be in the same flat directory. Elsevier's Editorial Manager compilation system does not support subdirectories.
- **Reference style:** `\bibliographystyle{elsarticle-num}` (numbered, author-year NOT accepted)
- **Document class:** `\documentclass[review,1p]{elsarticle}` for submission (double-spaced, single column — this is what B&B reviewers receive); use `5p` option only for local two-column preview
- **Abstract:** ≤300 words, no citations, no non-standard abbreviations
- **Highlights:** exactly 3–5 bullet points, each ≤85 characters (including spaces), plain text file `highlights.txt`
- **Word count:** 8,000–15,000 words for review articles (B&B guideline)

### B&B LaTeX Template (submission mode)

```latex
\documentclass[review,1p]{elsarticle}
% For local two-column preview: \documentclass[5p,times,twocolumn]{elsarticle}

\usepackage{lineno, hyperref, booktabs, graphicx, amsmath, amssymb}
\usepackage[utf8]{inputenc}
\modulolinenumbers[5]

\journal{Biosensors and Bioelectronics}

\bibliographystyle{elsarticle-num}  % ← B&B REQUIRED — do not change

\begin{document}

\begin{frontmatter}
\title{[Full Paper Title]}

\author[inst1]{[Author 1]\corref{cor1}\fnref{orcid1}}
\ead{email@institution.edu}
\cortext[cor1]{Corresponding author}
\fntext[orcid1]{ORCID: [0000-0000-0000-0000]}
\author[inst1]{[Author 2]}
\address[inst1]{[Department, Institution, City, Country]}

\begin{abstract}
[250–300 words: motivation, gap, scope, key contributions, significance.
No citations. No undefined abbreviations.]
\end{abstract}

\begin{keyword}
keyword1 \sep keyword2 \sep keyword3 \sep keyword4 \sep keyword5
\end{keyword}
\end{frontmatter}

\linenumbers  % B&B requires line numbers for review

\section{Introduction}
% ...

\section*{CRediT authorship contribution statement}
[Author 1]: Conceptualization, Writing – original draft.
[Author 2]: Supervision, Funding acquisition, Writing – review \& editing.

\section*{Declaration of competing interests}
The authors declare no competing financial interests.

\section*{Data availability}
No data was used for the research described in the article.

\section*{Acknowledgements}
[Funding sources, grant numbers]

\bibliography{references}  % ← references.bib in same directory
\end{document}
```

### LaTeX Compilation Sequence (run in order, from project root)

```bash
pdflatex main.tex        # Pass 1: generates .aux
bibtex main              # Process bibliography
pdflatex main.tex        # Pass 2: resolves citations
pdflatex main.tex        # Pass 3: resolves cross-references
```

After each run: check `.log` file for `!` (fatal errors) and `Warning` (overfull boxes, undefined refs).

**Common errors and fixes:**
- `! Undefined control sequence`: missing `\usepackage` or typo in command
- `Citation undefined`: BibTeX key in `.tex` doesn't match `.bib` entry
- `Overfull \hbox`: reduce text or use `\sloppy` in the offending paragraph
- `Missing figure file`: figure filename in `\includegraphics` doesn't match actual file (case-sensitive)
- **`Commented-out \includegraphics` (NEW):** figure environment renders as blank — search for `% \includegraphics` in main.tex and uncomment every occurrence where the PNG file exists
- `Undefined label`: `\ref{fig:X}` used but `\label{fig:X}` is missing or in a commented environment
- `Package hyperref Warning: Token not allowed in a PDF string`: special characters in section titles — wrap with `\texorpdfstring{formula}{text}`

### Verification Scripts (v4.1 — automated Gate C compliance checks)

Run these before Gate C. No external tools required — pure Python stdlib.

**Abstract word count (must be ≤ 300):**
```python
import re

with open('main.tex', 'r', encoding='utf-8') as f:
    content = f.read()

abstract = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', content, re.DOTALL)
if abstract:
    text = re.sub(r'\\[a-zA-Z]+\{[^}]*\}|\\[a-zA-Z]+|\{|\}|~', ' ', abstract.group(1))
    words = [w for w in text.split() if w.strip()]
    print(f"Abstract word count: {len(words)} / 300 {'✓' if len(words) <= 300 else '⚠ EXCEEDS LIMIT'}")
```

**Highlights character count (each line must be ≤ 85 chars):**
```python
with open('highlights.txt', 'r', encoding='utf-8') as f:
    lines = [l.rstrip('\n') for l in f if l.strip()]

for i, line in enumerate(lines, 1):
    status = '✓' if len(line) <= 85 else f'⚠ {len(line)} chars — EXCEEDS 85'
    print(f"Highlight {i} ({len(line)} chars): {status}")
    print(f"  {line}")

print(f"\nTotal highlights: {len(lines)} {'✓' if 3 <= len(lines) <= 5 else '⚠ must be 3-5'}")
```

**LaTeX body word count (texcount-free estimate):**
```python
import re

with open('main.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove preamble (before \begin{document})
body = content.split(r'\begin{document}', 1)[-1] if r'\begin{document}' in content else content
# Remove frontmatter (abstract, keywords)
body = re.sub(r'\\begin\{frontmatter\}.*?\\end\{frontmatter\}', '', body, flags=re.DOTALL)
# Remove figure/table environments (captions inflate count)
body = re.sub(r'\\begin\{(figure|table)\*?\}.*?\\end\{(figure|table)\*?\}', '', body, flags=re.DOTALL)
# Remove LaTeX commands and braces
body = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})*', ' ', body)
body = re.sub(r'[{}$\\]', ' ', body)
words = [w for w in body.split() if len(w) > 1 and w.isalpha()]
print(f"Estimated body word count: {len(words)} (target: 8,000–15,000)")
print(f"Status: {'✓' if 8000 <= len(words) <= 15000 else '⚠ outside range — verify manually'}")
```

**Reference count:**
```python
import re

with open('references.bib', 'r', encoding='utf-8') as f:
    bib = f.read()
count = len(re.findall(r'^@', bib, re.MULTILINE))
print(f"References: {count} {'✓' if count >= 130 else '⚠ below 130'}")
```

### Post-Compile Figure Mount Verification

After pdflatex runs successfully, run this sanity check:

```python
import re, os

with open('main.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all active (non-commented) includegraphics
active = re.findall(r'(?<!%)\\includegraphics(?:\[.*?\])?\{([^}]+)\}', content)
# Find all commented-out includegraphics
commented = re.findall(r'%.*\\includegraphics(?:\[.*?\])?\{([^}]+)\}', content)

print("Active figures:", active)
for f in active:
    fname = f if '.' in f else f + '.png'
    if not os.path.exists(fname):
        print(f"  MISSING FILE: {fname}")
    else:
        print(f"  OK: {fname}")

if commented:
    print("\nWARNING — Commented-out figures (will NOT appear in PDF):")
    for f in commented:
        print(f"  {f}")
```

### Submission Checklist (B&B-specific)

```
[ ] All files in project root directory (NO subfolders)
[ ] \bibliographystyle{elsarticle-num} in main.tex
[ ] main.tex compiles to PDF without errors (4-pass sequence)
[ ] Post-compile figure mount verification passed (0 missing files, 0 commented-out)
[ ] Word count: 8,000–15,000 words
[ ] Abstract: ≤300 words, no citations
[ ] Keywords: 5–8, relevant to Biosensors and Bioelectronics scope
[ ] Highlights: highlights.txt — 3–5 items, each ≤85 characters
[ ] Graphical abstract: graphical_abstract.png — 400×300px, minimal text
[ ] Figures: ≥300 DPI, EPS preferred, TIFF/PNG acceptable
[ ] Line numbers enabled (\linenumbers)
[ ] CRediT author contributions: included in main.tex
[ ] Declaration of competing interests: included
[ ] Data availability statement: included
[ ] Funding acknowledgments: with grant numbers (or explicit no-funding statement)
[ ] Cover letter: written and personalized to B&B editorial board
[ ] ORCID: at least corresponding author ORCID in frontmatter
```

⚡ **Accelerators (optional):** `latex-document` runs the 4-pass compilation; `latex-setup` configures the environment; `research-publishing` handles Editorial Manager upload workflow

---

## ▓▓▓ GATE C: Submission Readiness Check ▓▓▓

**Final quality gate. Paper does not leave your desk until this passes.**

```
GATE C Checklist:
[ ] Stage 6.5 passed: zero commented-out \includegraphics, zero orphan figures
[ ] Gate B passed: 0 [NOT_FOUND], 0 [MISMATCH], 0 [METHOD_X] flags anywhere
[ ] Peer review simulation: average score (R1–R6) ≥ 80/100, all 6 reviewers ≥ 65
[ ] R6 (Format Auditor) score ≥ 70
[ ] R7 (New Reader Simulator) score ≥ 70 — pedagogical quality confirmed
[ ] All P0 and P1 revision items resolved and verified
[ ] Word count: within ±10% of journal guideline
[ ] All figures: ≥300 DPI, files on disk, \includegraphics active and correct filename
[ ] Every \label{fig:X} has ≥1 \ref{fig:X} in text
[ ] Every \label{tab:X} has ≥1 \ref{tab:X} in text
[ ] LaTeX compiles without errors (pdflatex 4-pass sequence, or equivalent)
[ ] Abstract: ≤300 words, no citations
[ ] No section starts with "In this section, we..."
[ ] Cover letter written and personalized to journal
[ ] All author information complete and in correct order
[ ] Table captions: all legend symbols defined
[ ] §1 contains technology history timeline and unifying framework diagram reference
[ ] Each technical section has ≥1 concept introduction (first-occurrence term explained)
[ ] Decision flowcharts/selection matrices present for design-choice sections

PASS → Stage 10
FAIL → identify failed items, loop back to Stage 5/6.5/7/9 as appropriate
```

---

## Stage 10 — Submission Package Assembly

**Goal:** Produce a complete, flat-directory package ready for Editorial Manager upload.

### Delivery Classification (NEW in v4.0)

Before listing the submission checklist, classify every outstanding item as:

| Type | Description | Who acts |
|------|-------------|----------|
| **[AUTO]** | Claude can complete this immediately without user input | Claude does it now |
| **[USER]** | Requires private/personal information only the user has | User fills in before submission |

**[AUTO] items (Claude completes proactively):**
- Download `elsarticle.cls` and `elsarticle-num.bst` from Elsevier (urllib/WebFetch)
- Generate all figures via Python/matplotlib
- Generate graphical abstract (crop from Fig. 1)
- Create `submission_package.zip` with the correct file list
- Verify character counts of highlights.txt
- Write cover letter (with placeholder for private info)

**[USER] items (only private info, cannot be automated):**
- Corresponding author real phone number (`+86-XX-XXXX-XXXX`)
- Grant/funding project number (NSFC grant number, etc.)
- Any co-author ORCID IDs not yet provided

**Never mix [AUTO] and [USER] items in the same checklist without clear labels.** The user should only need to provide information that genuinely cannot be obtained or generated automatically.

### B&B Submission File Structure (ALL files in project root — no subfolders)

```
[project-root]/          ← ALL files here, flat, no subdirectories
├── main.tex             ← LaTeX source
├── references.bib       ← BibTeX database
├── manuscript_final.pdf ← Compiled PDF (4-pass compilation)
├── manuscript_draft.pdf ← Draft before final revision (keep for record)
├── fig_01_architecture.png     ← Fig. 1 (≥300 DPI)
├── fig_02_fabrication.png      ← Fig. 2
├── fig_03_sensing.png          ← Fig. 3
├── fig_04_biomarkers.png       ← Fig. 4
├── fig_05_circuits.png         ← Fig. 5
├── fig_06_intelligence.png     ← Fig. 6
├── graphical_abstract.png      ← 400×300px, no text overlay
├── highlights.txt              ← 3–5 lines, each ≤85 chars
├── cover_letter.md             ← Personalized to B&B editorial board
├── elsarticle.cls              ← Downloaded from Elsevier [AUTO]
├── elsarticle-num.bst          ← Downloaded from Elsevier [AUTO]
├── revision_log.md             ← From Stage 8
└── submission_checklist.md     ← Gate C checklist, all ✓

submission_package.zip   ← Contains only the files Editorial Manager needs:
                           main.tex, references.bib, all fig_*.png,
                           elsarticle.cls, elsarticle-num.bst,
                           graphical_abstract.png, highlights.txt, cover_letter.md
```

### ZIP Package Creation

Create `submission_package.zip` containing ONLY the files for upload:
```python
# Python (cross-platform, no shell dependency)
import zipfile, os, re

submission_files = ['main.tex', 'references.bib', 'highlights.txt',
                    'cover_letter.md', 'graphical_abstract.png',
                    'elsarticle.cls', 'elsarticle-num.bst']
# Add all fig_*.png
submission_files += [f for f in os.listdir('.') if re.match(r'fig_\d+.*\.png$', f)]

with zipfile.ZipFile('submission_package.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    for fname in submission_files:
        if os.path.exists(fname):
            zf.write(fname)
            print(f"  Added: {fname}")
        else:
            print(f"  MISSING: {fname} — fix before submission")
```

### CRediT Authorship Contribution Template

Paste this into `main.tex` under `\section*{CRediT authorship contribution statement}`:

```
[First Author]: Conceptualization, Methodology, Investigation, Writing – original draft, Visualization.
[Co-Author 1]: Resources, Data curation, Writing – review & editing.
[Corresponding Author]: Conceptualization, Supervision, Funding acquisition, Writing – review & editing, Project administration.
```

Available CRediT roles: Conceptualization · Data curation · Formal analysis · Funding acquisition · Investigation · Methodology · Project administration · Resources · Software · Supervision · Validation · Visualization · Writing – original draft · Writing – review & editing

### Highlights Template (highlights.txt)

```
• [Key finding 1 about the technology — ≤85 chars including spaces]
• [Key finding 2 about the system integration — ≤85 chars]
• [Key finding 3 about clinical/in-vivo validation — ≤85 chars]
• [Forward-looking statement about the field — ≤85 chars]
• [Unique contribution of this review — ≤85 chars]
```

Verify character counts: each line including "• " prefix must be ≤85 characters.

### Elsevier Template Auto-Download (Python)

```python
import urllib.request, os

# mirrors.ctan.org provides direct binary downloads (v4.1 fix: ctan.org/tex-archive is a browse page, not a download URL)
templates = {
    'elsarticle.cls': 'https://mirrors.ctan.org/macros/latex/contrib/elsarticle/elsarticle.cls',
    'elsarticle-num.bst': 'https://mirrors.ctan.org/macros/latex/contrib/elsarticle/elsarticle-num.bst',
}
fallback_url = 'https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions'

for filename, url in templates.items():
    if not os.path.exists(filename):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=15) as r:
                data = r.read()
            # Sanity check: cls/bst files should be text, not HTML
            if b'<html' in data[:200].lower():
                raise ValueError("Received HTML instead of file — URL may have redirected")
            with open(filename, 'wb') as f:
                f.write(data)
            print(f"Downloaded: {filename} ({len(data)//1024} KB)")
        except Exception as e:
            print(f"Download failed for {filename}: {e}")
            print(f"  → Manual download: {fallback_url}")
    else:
        print(f"Already present: {filename} ({os.path.getsize(filename)//1024} KB)")
```

⚡ **Accelerators (optional):** `docx` for cover letter Word generation; `pdf` for final PDF compilation; `research-publishing` for Editorial Manager upload workflow

---

## Domain Configuration System

The skill adapts to any research domain via configuration. At pipeline start, if a domain config is provided, inject domain-specific parameters at each stage.

### Config Structure

```yaml
# domain-config.yaml
paper:
  title: "Your Paper Title Here"
  journal: "Target Journal Name"
  type: "review"  # review | systematic_review | meta_analysis
  word_target: 12000
  reference_target: 180

domain:
  field: "your research field"
  keywords:
    primary: ["keyword1", "keyword2", "keyword3"]
    secondary: ["keyword4", "keyword5"]

  key_researchers:  # Names to ensure representation in corpus
    - "Researcher Name (Institution)"

  performance_metrics:  # Domain-specific benchmarks
    - name: "Metric 1"
      unit: "unit"
      good_threshold: "value"

  detection_method_taxonomy:  # For Gate B method-type consistency check
    electrochemical:
      - amperometry
      - DPV
      - SWV
      - EIS
      - potentiometry (ISE)
      - FSCV
    optical:
      - fluorescence
      - SERS
      - colorimetric
      - SPR
    mechanical:
      - QCM
      - cantilever

  search_clusters:  # Paper search topic clusters
    - name: "Cluster A: [topic]"
      queries:
        - "search query 1"
        - "search query 2"

  journals_to_monitor:  # For corpus building
    - "Journal Name 1"
    - "Journal Name 2"

review:
  existing_reviews_to_beat:  # Known reviews in this space
    - "Author Year — scope description"

  unique_contribution:  # Your paper's differentiation
    "This review is the first to cover [X] from [A] to [B]."
```

### Built-in Domain: Wearable Electrochemical Sensing (Microneedle Arrays)

```yaml
paper:
  title: "Microneedle-Based Wearable Electrochemical Sensing: A Full-Chain Engineering Review from Material Design to Intelligent Terminals"
  short_title: "Microneedle Electrochemical Sensing: Full-Chain Review"
  journal: "Biosensors and Bioelectronics"
  type: "review"
  word_target: 16000
  reference_target: 200
  figures_target: 10
  tables_target: 5

domain:
  field: "wearable electrochemical biosensing via microneedle arrays"
  unifying_framework: "measurement_instrument_chain"
  framework_description: >
    The microneedle sensing system is modeled as a complete measurement instrument:
    Target analyte → Needle-skin interface (sampling) → Electrochemical transduction
    → Analog front-end (signal conditioning) → Digital processing (MCU/AI) → Clinical output.
    Each section of the paper maps to one stage of this chain.
  keywords:
    primary: ["microneedle array", "electrochemical sensing", "wearable biosensor", "minimally invasive", "continuous monitoring"]
    secondary: ["sweat analysis", "interstitial fluid", "transdermal", "embedded system", "IoT health", "point-of-care"]

  key_researchers:
    # International groups
    - "Joseph Wang (UCSD) — flexible wearable electrochemical patches, glucose/lactate"
    - "Ali Javey (UC Berkeley) — multiplexed wearable sensor arrays, FPCB integration"
    - "Wei Gao (Caltech) — fully integrated wearable systems, machine learning integration"
    - "Hyunjae Lee (POSTECH) — painless hollow microneedle glucose, clinical validation"
    - "Rodrigo Martinez-Duarte (Clemson) — carbon microneedle arrays"
    - "Martin Pumera (VSB-TUO) — 3D printed microneedle electrodes"
    - "Mark Prausnitz (Georgia Tech) — dissolvable microneedle delivery/sensing"
    - "Devansh Bhansali (FIU) — microneedle cortisol, ISF sampling"
    - "Liangbing Hu (UMD) — flexible electronics, nanostructured electrodes"
    - "Nae-Eung Lee (Sungkyunkwan) — stretchable electronics, skin-interfaced"
    # Chinese groups (essential for balanced coverage)
    - "Lingqian Chang (PKU) — microneedle transcutaneous biosensing"
    - "Zhuo Li (HUST) — flexible electronics + microneedle integration"
    - "Yong Zhu (PKU) — 3D printed microneedle arrays"
    - "Fei Liu (CAS Suzhou Institute) — microneedle continuous glucose monitoring"
    - "Jianfeng Ping (ZJU) — wearable electrochemical sensors"
    - "Zhong Lin Wang (TJU/BIT) — nanogenerator + self-powered sensing"
    - "Yuehe Lin (WSU) — nanomaterial-enhanced electrochemical biosensors"

  detection_method_taxonomy:
    electrochemical:
      - amperometry        # glucose/lactate GOx/LOx
      - DPV                # uric acid on carbon
      - SWV                # multiplexed detection
      - EIS                # aptasensor, immunosensor
      - potentiometry ISE  # Na+, K+, pH via IrOx/monensin/valinomycin
      - FSCV               # dopamine on carbon-fiber MNA
    optical:
      - fluorescence       # HCR amplification, quantum dot
      - SERS               # surface-enhanced Raman on Au-MNA
      - colorimetric       # paper-based, smartphone readout
    mechanical:
      - piezoresistive     # pressure/strain on microneedle tip
      - piezoelectric      # dynamic pressure measurement
    thermal:
      - thermistor         # temperature at needle tip
      - IR                 # non-contact thermal mapping

  performance_metrics:
    - {name: "Glucose LOD", unit: "μM", good_threshold: "< 1", excellent: "< 0.1"}
    - {name: "Glucose sensitivity", unit: "μA mM⁻¹ cm⁻²", good_threshold: "> 10", excellent: "> 50"}
    - {name: "Glucose linear range", unit: "mM", good_threshold: "0.1–20", clinical: "2.8–22.2"}
    - {name: "Lactate LOD", unit: "μM", good_threshold: "< 10", excellent: "< 5"}
    - {name: "Uric acid LOD (DPV)", unit: "μM", good_threshold: "< 1"}
    - {name: "Cortisol LOD (EIS/aptasensor)", unit: "ng/mL", good_threshold: "< 1"}
    - {name: "Na⁺ slope", unit: "mV/decade", good_threshold: "55–62 (Nernstian 59.2)"}
    - {name: "K⁺ slope", unit: "mV/decade", good_threshold: "55–62"}
    - {name: "Ion selectivity coefficient (ISE)", unit: "log k", good_threshold: "< -2"}
    - {name: "Mechanical fracture force", unit: "N/needle", good_threshold: "> 0.1"}
    - {name: "Skin insertion depth", unit: "μm", good_threshold: "200–800 (epidermis)"}
    - {name: "CGM MARD", unit: "%", good_threshold: "< 10", commercial: "8.2–9.7"}
    - {name: "Wireless range (BLE)", unit: "m", good_threshold: "> 5"}
    - {name: "Power consumption", unit: "mW", good_threshold: "< 10 for continuous"}

  commercial_benchmarks:
    - {product: "Dexcom G7", MARD: "8.2%", wear_time: "10d", analyte: "glucose", sensor: "enzyme electrode"}
    - {product: "Abbott FreeStyle Libre 3", MARD: "7.9%", wear_time: "14d", analyte: "glucose", sensor: "enzyme electrode"}
    - {product: "Medtronic Guardian 4", MARD: "8.7%", wear_time: "7d", analyte: "glucose", sensor: "enzyme electrode"}
    - {product: "Senseonics Eversense 365", MARD: "8.5%", wear_time: "365d", analyte: "glucose", sensor: "flourescence"}

  search_clusters:
    - name: "Cluster A: Microneedle Fabrication & Materials"
      queries:
        - "microneedle array electrochemical sensor fabrication silicon"
        - "hollow microneedle electrodeposition PEDOT glucose amperometric"
        - "polymer PDMS SU-8 microneedle electrochemical sensor"
        - "metal microneedle array gold platinum electrode"
        - "3D printed microneedle electrode biosensor"
        - "hydrogel microneedle swelling interstitial fluid"
        - "carbon nanotube graphene microneedle electrode"
        - "microneedle tip modification enzyme immobilization"
    - name: "Cluster B: Electrochemical Sensing Modalities"
      queries:
        - "microneedle amperometric glucose oxidase continuous monitoring"
        - "wearable differential pulse voltammetry DPV microneedle"
        - "square wave voltammetry SWV uric acid wearable"
        - "impedance spectroscopy EIS microneedle aptasensor cortisol"
        - "ion selective electrode potentiometric wearable skin"
        - "FSCV fast scan cyclic voltammetry dopamine wearable"
        - "multiplexed electrochemical array wearable simultaneous"
    - name: "Cluster C: Wearable System Integration"
      queries:
        - "flexible substrate wearable electrochemical patch skin"
        - "wireless Bluetooth NFC electrochemical sensor wearable"
        - "analog front end potentiostat wearable biosensor ASIC"
        - "power management wearable biosensor energy harvesting"
        - "stretchable electronics biosensor skin-interfaced"
    - name: "Cluster D: Embedded Intelligence & Terminals"
      queries:
        - "edge computing machine learning wearable biosensor calibration"
        - "embedded MCU microcontroller electrochemical sensing IoT"
        - "closed loop insulin delivery glucose sensor wearable"
        - "smartphone interface electrochemical wearable health data"
        - "signal processing algorithm drift correction wearable sensor"
    - name: "Cluster E: Clinical & In Vivo Validation"
      queries:
        - "microneedle in vivo glucose monitoring human clinical"
        - "wearable lactate continuous monitoring exercise validation"
        - "transdermal cortisol monitoring human study"
        - "interstitial fluid microneedle glucose accuracy Clarke"
    - name: "Cluster F: Foundational & Tutorial"  # NEW in v4.2
      queries:
        - "microneedle review tutorial introduction"
        - "electrochemical biosensor fundamentals review"
        - "wearable sensor design principles review"
        - "microfabrication microneedle protocol method"
    - name: "Cluster G: Chinese Literature"  # NEW in v4.2
      queries:
        - "microneedle electrochemical sensor review"
        - "microneedle continuous monitoring fabrication"
        - "wearable biosensor microneedle signal processing"
      databases: ["CNKI", "Wanfang", "PubMed (Chinese affiliation filter)"]
    - name: "Cluster H: Commercial & Industrial"  # NEW in v4.2
      queries:
        - "CGM commercial Dexcom Abbott Medtronic comparison MARD"
        - "microneedle patent landscape commercialization"
        - "microneedle FDA 510k CE marking regulatory pathway"

  journals_to_monitor:
    - "Biosensors and Bioelectronics"
    - "ACS Nano"
    - "Advanced Materials"
    - "Advanced Functional Materials"
    - "Analytical Chemistry"
    - "Lab on a Chip"
    - "Nature Electronics"
    - "npj Digital Medicine"
    - "Theranostics"
    - "Small"
    - "Nano Energy"
    - "ACS Applied Materials & Interfaces"
    - "Chemical Reviews"
    - "Chemical Society Reviews"

  technology_milestones:  # For §1.2 history timeline
    - {year: 2000, event: "Prausnitz: microneedle transdermal drug delivery concept", ref: "Prausnitz2004NatRevDrugDiscov"}
    - {year: 2005, event: "First electrochemical microneedle glucose sensor", ref: "first_mn_glucose"}
    - {year: 2010, event: "Hollow microneedle + ISF sampling demonstrated", ref: "hollow_mn_isf"}
    - {year: 2015, event: "Wearable electrochemical patch era begins (Wang, Javey)", ref: "wearable_patch_era"}
    - {year: 2018, event: "FreeStyle Libre commercial CGM success", ref: "freestyle_libre"}
    - {year: 2020, event: "Multiplexed microneedle arrays + wireless integration", ref: "multiplexed_mn"}
    - {year: 2022, event: "Edge AI + closed-loop insulin delivery concept", ref: "edge_ai_closed_loop"}
    - {year: 2024, event: "7-day continuous monitoring + ML calibration", ref: "7day_ml_calibration"}
    - {year: 2026, event: "Current state: full-chain integration from needle to cloud", ref: "current_state"}

review:
  existing_reviews_to_beat:
    - "Sekar 2023 Adv Mater — fabrication focus, minimal embedded systems/AI"
    - "Yang 2022 Chem Soc Rev — electrochemistry fundamentals, not wearable integration"
    - "Teymourian 2021 ACS Nano — strong wearable patch coverage, weak on microneedle specifics"
    - "Zhao 2023 Biosens Bioelectron — microneedle diabetes focus, narrow scope"
    - "Li 2024 Adv Sci — wearable biosensor review, limited microneedle+terminal integration"
    - "Kim 2023 ACS Nano — microneedle drug delivery/sensing dual function"
    - "Zhang 2024 Chem Eng J — 3D printed microneedle, no system integration"

  unique_contribution: >
    This is the FIRST comprehensive review to adopt a measurement instrument chain
    framework, treating wearable microneedle-based electrochemical sensing as a
    complete engineering system — from material design and electrochemical transduction
    through signal conditioning circuits to embedded intelligent terminals — and
    providing systematic decision guides (material × geometry × sensing modality)
    that enable readers to independently design and evaluate microneedle sensing systems.
```

---

## Anti-Hallucination Master Protocol

**Always active. Cannot be disabled.**

### The Four Rules (v4.0 — added Rule 4)

**Rule 1 — The Citation Sourcing Rule:**
Every factual claim about a specific study MUST be preceded by verification that the study exists. Before writing "Smith et al. demonstrated X [1]", you must have either:
(a) Found the paper via search in this session, OR
(b) Had the user provide the paper reference explicitly

If you cannot do (a) or (b): write the claim as `[NEEDS_REF: describe claim]` and proceed. Never invent a paper to fill the gap.

**Rule 2 — The Numbers Rule:**
Every quantitative value (LOD, sensitivity, accuracy, specificity, p-value, n=) MUST be traceable to a specific table, figure, or result statement in a verified paper. If you cite "LOD of 0.5 μM", you must know which paper's Table 2 or Figure 3 contains that number.

**Rule 3 — The Superlatives Rule:**
Words like "first", "highest", "best", "only", "unprecedented", "novel" always require a citation. Without a citation, replace with neutral language: "among the reported approaches..." or "a promising approach..."

**Rule 4 — The Method-Type Rule (NEW in v4.0):**
Every citation in a method-specific paragraph must use the same detection modality as described in the surrounding text. Before citing a paper in §3.X (EIS section), confirm: does this paper actually use EIS? Optical/fluorescence papers cited in electrochemical sections, or in vitro papers cited as clinical evidence, are Rule 4 violations — fix them regardless of whether the paper exists.

### Verification Taxonomy

Label all citations in draft with one of:
- `[V]` — Verified: found via search this session, details confirmed, method type confirmed
- `[U]` — Unverified: user-provided reference, not independently checked
- `[N]` — Needs verification: in corpus but not yet checked
- `[X]` — Failed: not found, remove from draft
- `[M]` — Method mismatch: paper exists but method type conflicts with citing context

Gate B clears all `[N]`, `[X]`, and `[M]` before submission.

---

## Pipeline Control Commands

### Starting the Pipeline
```
/sciw init                     → Configure: title, journal, domain config
/sciw start                    → Begin from Stage 1 (interactive)
/sciw auto                     → Full auto mode (halt at each Gate for approval)
/sciw load microneedle         → Load built-in microneedle config and start
/sciw resume                   → Read sci_writer_state.md and continue from last checkpoint
```

### Stage Control
```
/sciw stage [1-10]             → Jump to specific stage
/sciw stage 6.5                → Run figure mount + cross-reference audit only
/sciw stage [1-10] [context]   → Jump with additional context
/sciw gate [a/b/c]             → Run specific quality gate only
/sciw status                   → Show current pipeline position and completion
```

### Utility Commands
```
/sciw search [query]           → Run literature search (Stage 2 mode)
/sciw write [section]          → Write specific section (Stage 5 mode)
/sciw review                   → Run peer review simulation (Stage 7 mode)
/sciw verify                   → Run citation audit (Gate B mode)
/sciw mount-check              → Run Stage 6.5 figure mount audit only
/sciw export                   → Generate submission package
```

### Configuration
```
/sciw config show              → Display current domain config
/sciw config set [key] [value] → Update config value
/sciw config load [file]       → Load config from YAML file
```

---

## ⚡ Optional Accelerator Map

**All capabilities below are fully available in the standalone core. Accelerator skills, when present, provide faster execution or additional parallelism — they do NOT unlock capabilities that are otherwise unavailable.**

| Capability | Standalone Core (always works) | ⚡ Accelerator skill (optional) |
|------------|-------------------------------|--------------------------------|
| Full pipeline orchestration | Built-in 11-stage logic + 3 Gates | `academic-pipeline` (ARS v3.7, parallel agents) |
| Systematic literature search | PRISMA protocol embedded in Stage 2 | `deep-research` + `literature-review` + `arxiv-search` |
| Daily new-paper monitoring | Manual periodic search | `start-my-day` (evil-read-arxiv) |
| Paper deep reading | Claude extraction with Stage 3 protocol | `paper-analyze` |
| Conference paper tracking | Manual search + `tavily-search` | `conf-papers` |
| Section writing | 4-pass protocol embedded in Stage 5 | `academic-paper` (12-agent parallel) |
| Style polish | Stage 5 style guidelines | `scientific-writing` + `paper-writing` |
| Citation integrity check | Gate B audit protocol built-in | `paper-verification` (batch DOI check) |
| Method-type consistency | Gate B Part 2 built-in | N/A (unique to SCI-writer) |
| Figure mount audit | Stage 6.5 built-in Python scripts | N/A (unique to SCI-writer) |
| Cross-reference audit | Stage 6.5 built-in regex scan | N/A (unique to SCI-writer) |
| Peer review simulation | 6-reviewer panel built-in in Stage 7 | `academic-paper-reviewer` |
| Rebuttal engineering | Stage 8 rebuttal template built-in | `reviewer-defense` |
| LaTeX compilation | Claude generates .tex with embedded template | `latex-document` + `latex-setup` |
| Figures | Python/matplotlib generation (Stage 6) | `scientific-visualization` + `scientific-slides` |
| Journal submission | Stage 10 checklist + cover letter template | `research-publishing` |

**Principle:** installing zero accelerators → full pipeline runs, same 3 Gates + Stage 6.5, same quality standard.

---

## Output File Convention

**All files saved flat in the working directory (no subdirectories).** This aligns with B&B Editorial Manager requirements and the standard task deliverable names.

```
[working-directory]/          ← everything here, flat
│
│  ── Phase 1 outputs ──
├── review_gap_analysis.md    (Stage 1: gap analysis + existing reviews)
├── literature_matrix.xlsx    (Stage 2: full corpus table)
├── corpus_notes.md           (Stage 3: per-paper synthesis extractions with method types)
├── paper_outline.md          (Stage 4: section outline + figure-label mapping)
├── figure_plan.md            (Stage 6: figure specs with planned \ref{} sentences)
├── references.bib            (Stage 2–9: cumulative BibTeX database)
│
│  ── Phase 2 outputs ──
├── main.tex                  (Stage 9: LaTeX source)
├── generate_figures.py       (Stage 6: Python script for all figures)
├── fig_01_[description].png  (Stage 6: figures, named fig_NN_*)
├── fig_02_[description].png
├── ...
├── graphical_abstract.png    (Stage 6: 400×300px)
├── elsarticle.cls            (Stage 9: downloaded [AUTO])
├── elsarticle-num.bst        (Stage 9: downloaded [AUTO])
│
│  ── Phase 3 outputs ──
├── review_report.md          (Stage 7: 6-reviewer simulation results + scores)
├── revision_log.md           (Stage 8: revision matrix with change evidence)
├── gate_c_checklist.md       (Gate C: all items ✓)
├── highlights.txt            (Stage 10)
├── cover_letter.md           (Stage 10)
└── submission_package.zip    (Stage 10: upload-ready archive)
```

### Stage Checkpointing

At the end of each major phase, output:
```
[✓ Phase I完成] 输出物：review_gap_analysis.md (N gaps), corpus_notes.md (N papers, method types recorded),
paper_outline.md (N sections), figure_plan.md (N figures with \ref locations), references.bib (N entries)

[✓ Phase II完成] 输出物：main.tex (N words), generate_figures.py, fig_01–fig_0N.png,
graphical_abstract.png, Stage 6.5 audit PASSED (0 orphan figures, 0 commented-out)

[✓ Phase III完成] 输出物：review_report.md (avg score X/100, all 6 reviewers ≥65),
revision_log.md (N revisions), gate_c_checklist.md (all ✓)

[✓ Phase IV完成] 输出物：submission_package.zip (N files: main.tex + bib + N figs + templates)
[USER] 仍需填写: 通讯作者电话, 基金项目编号
```

---

## Pipeline State Persistence (NEW in v4.1)

**Problem this solves:** A review paper takes 3–10 days. Context compaction happens multiple times. Without explicit state persistence, the pipeline position, score history, and pending tasks are lost between sessions.

**Solution:** Write `sci_writer_state.md` to disk after every stage. This file is the single source of truth for pipeline position across sessions.

### sci_writer_state.md Format

```markdown
# SCI-writer Pipeline State
**Last updated:** [ISO datetime]
**Paper:** [Short title]
**Target journal:** [Journal name]
**Working directory:** [Absolute path]

## Pipeline Position
**Current stage:** [Stage N.N — Stage Name]
**Completed stages:** [1, 2, Gate-A, 3, 4, 5, 6, 6.5, Gate-B, ...]
**Next action:** [One sentence: what to do when resuming]

## Gate Results
| Gate | Status | Date | Notes |
|------|--------|------|-------|
| Gate A | ✅ PASS / ⚠ EXCEPTION / ❌ FAIL | [date] | [corpus size, exception reason if used] |
| Gate B | ✅ PASS / ❌ FAIL | [date] | [N verified, N [METHOD_X] found/fixed] |
| Gate C | ✅ PASS / ❌ FAIL | [date] | [final score, word count] |

## Stage 7 Score History
| Round | Date | Avg | R1 | R2 | R3 | R4 | R5 | R6 | P0 issues | P1 issues |
|-------|------|-----|----|----|----|----|----|----|-----------|-----------|
| R1 | [date] | [score] | ... | ... | ... | ... | ... | ... | [list] | [list] |
| R2 | [date] | [score] | ... | | | | | | | |
| R3 | [date] | [score] | ... | | | | | | | |

## Corpus Status
- Total papers: [N]
- Verified [V]: [N]
- Unverified [N]: [N]
- Failed [X]: [N]
- Method-type flags [M]: [N]
- BibTeX key violations: [list or "none"]

## Figures Status
| File | Generated | \includegraphics active | \ref{} in text |
|------|-----------|------------------------|----------------|
| fig_01_*.png | ✅/❌ | ✅/❌ | ✅/❌ |

## Outstanding Items
- [ ] [Item 1] — [USER/AUTO] — [priority]
- [ ] [Item 2]

## Session Log
- [datetime] Stage N completed — [one-line summary]
- [datetime] Stage N+1 started
```

### Resume Protocol

When starting a new session on an existing project:

1. **First action:** Read `sci_writer_state.md` — this tells you exactly where you are
2. **Verify state:** Run Stage 6.5 figure mount check if figures were recently generated; grep for any `[NEEDS_REF]` remaining in main.tex
3. **Announce position:** Tell the user "Resuming at Stage X — [next action]" before proceeding
4. **Update state file:** After each completed stage, update `sci_writer_state.md` immediately

### `/sciw resume` Command

```
/sciw resume     → Read sci_writer_state.md and announce current position
                   Run quick sanity check (figure files present, BibTeX intact)
                   Continue from the stage listed in "Next action"
```

**Write `sci_writer_state.md` after completing each of these pipeline events:**
- Each stage completion
- Each Gate pass/fail decision
- Each Stage 7 scoring round
- Each Stage 8 revision batch (P0, P1)
- Each major file generation (figures, templates)

---

## Integration with Global CLAUDE.md Rules

If the user has a global CLAUDE.md, this skill respects those rules:
- Web searches: use `tavily-search` (Tier 1) → `WebSearch` (Tier 2)
- Git commits: use `git-commit` skill
- Debug failures: use `systematic-debugging`
- PUA rules if present: maintain owner consciousness, verify before claiming completion
- Bypass permissions: execute autonomously for all [AUTO] items; no confirmation needed for generating figures, downloading templates, running Python scripts

---

*SCI-writer v4.2.0 — Designed for researchers who want to write papers, not manage tools.*
*v4.2 major: Unified pedagogical-rigor framework · Technology history + measurement chain framework (§1.2–1.3) · Search Pattern D/E/F (foundational/Chinese/commercial) · Knowledge scaffolding sub-stage (4.5) · Pass 2.5 pedagogical enhancement · R7 new reader simulator · Decision flowcharts · Commercial benchmarks · Chinese research groups*
*v4.1 patch: Pipeline state persistence · BibTeX key convention · Gate A exception path · Verification scripts · Table legend check · Elsevier URL fix · Stage 7 threshold fix*
*v4.0 major: Stage 6.5 · R6 reviewer · Method-type consistency · Score escalation · [AUTO]/[USER] classification*
*SJTU Wang Lab | 张元杰 + 王侃 | Updated: 2026-05-29*
