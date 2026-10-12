# Interview Prep Wiki & Wiki Agent Engine

A structured, interconnected Markdown knowledge base and autonomous Wiki Agent engine tailored for **AI Engineer, LLM Engineer, and Applied AI** technical interview preparation.

The repository serves two distinct purposes:
1. **Ready-to-Use Knowledge Base**: Curated interview guides, 13 core technical topic modules, and 19 runnable from-scratch Python coding challenges.
2. **Re-usable Wiki Agent Engine**: A specification-driven engine ([AGENTS.md](AGENTS.md)) that can ingest heterogeneous documents and web pages to compile, index, and self-heal any technical wiki.

---

## Repository Structure

```
.
├── AGENTS.md                  # Autonomous Wiki Agent specification & persistent config
├── README.md                  # This file
├── Makefile                   # Developer shortcuts (build, serve, test, docker)
├── Dockerfile                 # Multi-stage container build (Quartz builder -> Nginx runtime)
├── docker-compose.yml         # Containerized dev & production preview services
├── input/                     # Source documents & ingested web archives (non-destructive)
│   ├── AI_ML_Engineer_Interview_Preparation.md
│   └── ai_engineer_interview_questions_ombharatiya.md
├── wiki/                      # Generated Markdown knowledge base (Source of truth)
│   ├── index.md               # Global root catalog
│   ├── topics.md              # Normalized taxonomy of canonical terms & aliases
│   ├── lint_report.md         # Structural & hyperlink integrity report
│   ├── groups/                # Category rollup pages
│   │   ├── data-science-core.md
│   │   ├── dsa-and-core-cs.md
│   │   └── interview-scenarios.md
│   └── interview-scenarios/   # Synthesized technical guides
│       ├── ai-ml-engineer-interview-preparation.md
│       └── ai-engineer-interview-questions-curriculum-and-challenges.md
├── quartz/                    # Quartz v5 static site generator engine
│   ├── quartz.config.yaml     # Site metadata, plugins & Obsidian shortest link settings
│   └── package.json           # Quartz dependencies & CLI runners
└── tests/                     # Automated link integrity & 404 validation suite
    └── test_site_integrity.py
```

---

## Part 1: Using This Repository for Interview Preparation (As-Is)

This repository is pre-compiled with high-signal material for entry-level to senior AI/ML and LLM engineering interview loops.

### 1. Navigating the Knowledge Graph
- **Global Catalog ([wiki/index.md](wiki/index.md))**: The central table of contents grouping all guides by entity category.
- **Taxonomy Index ([wiki/topics.md](wiki/topics.md))**: Over 25 normalized canonical concepts (e.g., *Transformer architectures*, *KV caching*, *LoRA*, *RoPE*, *Speculative decoding*, *MCP*, *BPE*) with aliases and cross-references to corresponding wiki guides.
- **Category Rollups ([wiki/groups/](wiki/groups))**: High-level aggregators for:
  - [Data science core](wiki/groups/data-science-core.md): Neural network foundations, LLM mechanics, and from-scratch algorithms.
  - [DSA and core CS](wiki/groups/dsa-and-core-cs.md): Algorithmic pattern recognition, SQL data wrangling, and modular OOP.
  - [Interview scenarios](wiki/groups/interview-scenarios.md): Comprehensive preparation guides, study tracks, and loop strategies.

### 2. Available Guides

#### A. [AI/ML Engineer Interview Preparation](wiki/interview-scenarios/ai-ml-engineer-interview-preparation.md)
Foundational strategy guide covering:
- **Core ML Foundations**: The AI Engineer 75 roadmap, Transformer basics, RAG, KV caching, and scratch implementations.
- **Software Engineering & DSA**: High-frequency patterns via NeetCode 150, advanced SQL (window functions and joins), and modular Python OOP.
- **ML System Design**: Architectural blueprints based on Chip Huyen (*Designing Machine Learning Systems*) and Alex Xu (*Machine Learning System Design Interview*).
- **Behavioral Scenarios**: The STAR method adapted for model failure triage, data drift, bias, and cross-functional technical tradeoffs.

#### B. [AI Engineer Interview Questions Curriculum & Challenges](wiki/interview-scenarios/ai-engineer-interview-questions-curriculum-and-challenges.md)
Comprehensive curriculum synthesized from Om Bharatiya's open-source interview suite:
- **13 Modular Topic Tracks (596+ Questions)**: Direct links to question banks with worked, collapsible solutions across:
  - `01-ml-and-dl-foundations`
  - `02-llm-fundamentals`
  - `03-prompt-engineering-and-context`
  - `04-rag-and-retrieval`
  - `05-fine-tuning-and-alignment`
  - `06-agents-and-tool-use`
  - `07-evaluation-and-observability`
  - `08-inference-and-production`
  - `09-safety-security-and-responsible-ai`
  - `10-multimodal`
  - `11-ai-system-design` (10 worked case studies)
  - `12-coding-challenges`
  - `13-interview-process-and-behavioral`
- **19 From-Scratch Coding Challenges**: Standalone Python scripts using only NumPy and the standard library, each with embedded test suites:
  - *Attention*, *BPE Tokenizer*, *Sampling Strategies*, *Positional Encodings (RoPE)*, *LayerNorm & Softmax*, *KV Cache*, *Mini-GPT Forward Pass*, *Semantic Search/RAG*, *Text Chunking*, *Agent Loop*, *Rate Limiter & Retry*, *Eval Metrics (pass@k)*, *Streaming Parser*, *LoRA Adapter*, *Beam Search*, *Semantic Cache*, *Hybrid Search & Rerank (BM25 + RRF)*, *Constrained JSON Decoding*, *Speculative Decoding*.

### 3. Verification & Integrity
Inspect [wiki/lint_report.md](wiki/lint_report.md) at any time to verify that there are zero broken wikilinks, zero orphan pages, and consistent heading structures across the knowledge graph.

---

## Part 2: Setting Up the Repository to Create a New LLM Wiki

The Wiki Agent protocol defined in [AGENTS.md](AGENTS.md) allows you to re-purpose this repository to build any custom technical knowledge base.

### 1. Re-configuring the Memory Block
Open [AGENTS.md](AGENTS.md) and reset the embedded `CONFIG` block at the top:

```markdown
<!--
CONFIG_START
wiki_name: Your New Wiki Name
input_folder: input
output_folder: wiki
entity_types: Category A, Category B, Category C
language: English
CONFIG_END
-->
```
*(If `wiki_name` is left blank, the agent automatically executes an interactive 5-question setup wizard before taking action).*

### 2. Loading Your Source Material
Place your source files into the configured `input_folder` (`input/`). Supported file types include:
- Markdown (`.md`) & Text (`.txt`)
- PDF documents (`.pdf`)
- Word documents (`.docx`)
- Spreadsheets (`.xlsx`, `.csv` rendered as pipe-delimited Markdown tables)
- Presentations (`.pptx` extracted slide-by-slide)

### 3. Running the Full Pipeline
Prompt the AI agent:
> *"Run all"* or *"Generate the wiki"*

The agent executes the sequential 8-stage pipeline:
1. **Stage 1 (Read)**: Ingests all documents from `input_folder` non-destructively.
2. **Stage 2 (Generate)**: Executes a 3-pass loop (*Writer* &rarr; *Evaluator* &rarr; *Editor*) to produce structured wiki pages with standardized headings (`Summary`, `Key points`, `Details`, `Related`, `References`).
3. **Stage 3 (Topics)**: Extracts key terminology into a normalized taxonomy (`topics.md`).
4. **Stage 4 (Groups)**: Synthesizes high-level category rollups (`groups/*.md`).
5. **Stage 5 (Index)**: Compiles the global directory in `index.md`.
6. **Stage 6 (Consolidate)**: Flags near-duplicate content (&ge; 70% overlap) and merges pages after human confirmation.
7. **Stage 7 (Lint)**: Audits broken `[[links]]`, orphans, and heading skips into `lint_report.md`.
8. **Stage 8 (Repair)**: Auto-resolves fuzzy link matches and links orphan pages into the graph.

---

## Part 3: Ingesting Web Resources & Online Articles (Incremental Mode)

You can expand the wiki continuously by supplying URLs to online tutorials, GitHub repositories, technical blogs, or documentation.

### How to Request Ingestion
Prompt the agent:
> *"Ingest the URL `<URL>` and focus on `<specific focus areas or sections>`"*

### What the Agent Executes
1. **Fetch & Archive**:
   - The agent reads the web page and extracts its content as clean Markdown.
   - The raw markdown is saved to `input/<resource_slug>.md` to maintain an immutable, reproducible local source archive.
2. **3-Pass Synthesis (Stage 2)**:
   - Evaluates the content against the target entity type.
   - Emits a structured guide under `wiki/{entity_type}/{slugified-title}.md` containing an executive summary, key takeaways, deep technical analysis, external links to the source sections, and bidirectional `[[Double Bracket]]` links.
3. **Graph Integration (Stages 3, 4, 5)**:
   - Registers new terminology in [wiki/topics.md](wiki/topics.md).
   - Adds the new page to its corresponding [wiki/groups/](wiki/groups) category file.
   - Re-indexes [wiki/index.md](wiki/index.md) and updates existing related pages.
4. **Validation (Stages 7 & 8)**:
   - Re-runs link analysis to ensure zero broken links and zero orphan pages, logging the result to [wiki/lint_report.md](wiki/lint_report.md).

---

## Part 4: Browsing and Publishing as Static HTML (Quartz)

The wiki can be rendered into a fully interactive, browsable static website using **Quartz v5**. This enables:
- **Native Obsidian `[[wikilinks]]`**: Shortest-path link resolution across nested entity folders without altering source files.
- **Interactive Knowledge Graph**: Force-directed network graph showing connections across AI/ML topics, DSA patterns, and system design case studies.
- **Page Hover Previews**: Instant popover previews when hovering over any concept link.
- **Fast Full-Text Search**: Client-side instant search (`Ctrl+K`).
- **Dark & Light Mode**: Theme toggle with syntax highlighting and reader mode.

---

### Option A: Local Host Development (Native)

**Prerequisites:** Node.js &ge; 22 and npm.

1. **Initialize Submodule & Install Dependencies**:
   ```bash
   # If cloning fresh:
   # git clone --recurse-submodules <repo-url>

   # In this repository:
   make install
   ```
   `make install` automatically initializes the `quartz` Git submodule (`git submodule update --init --recursive`), syncs `quartz.config.yaml`, and installs npm packages.

2. **Start Development Server (Live Reload)**:
   ```bash
   make serve
   # or: cd quartz && npm run serve
   ```
   Open `http://localhost:8080` in your browser. Any edits made in `wiki/` will automatically hot-reload in the browser.

3. **Build Static Bundle**:
   ```bash
   make build
   # or: cd quartz && npm run build
   ```
   The compiled HTML, CSS, JavaScript, and search indexes are output to `quartz/public/`.

4. **Run Automated Integrity Tests**:
   ```bash
   make test
   ```
   Executes `tests/test_site_integrity.py` (zero external Python dependencies) to verify:
   - All core entrypoints (`index.html`, `topics.html`, `404.html`, `contentIndex.json`) exist.
   - Zero raw unparsed `[[...]]` wikilinks leak into the rendered HTML text.
   - Every internal link resolves to a valid HTML destination (zero 404s).
   - Search index and metadata are complete.

---

### Option B: Docker-First Workflow

If you prefer to run Quartz entirely inside containers without managing Node.js dependencies on the host:

1. **Development Server with Hot Reload**:
   ```bash
   make docker-dev
   # or: docker compose up --build wiki-dev
   ```
   Mounts `./wiki` as read-only and `./quartz` with hot reloading at `http://localhost:8080`.

2. **Production Preview via Nginx**:
   ```bash
   make docker-preview
   # or: docker compose up --build wiki-preview
   ```
   Runs a multi-stage build that compiles static HTML via Quartz and serves it through a lightweight, optimized Nginx container at `http://localhost:8081`.

3. **Stop Docker Services**:
   ```bash
   make docker-down
   # or: docker compose down
   ```

---

## Conventions & System Guardrails

- **Wikilinks**: All internal cross-references strictly use `[[Page Title]]` syntax matching the target document's primary H1 title.
- **File Naming**: Lowercase and hyphenated (`kebab-case`, e.g., `ai-engineer-interview-questions.md`).
- **Headings**: Sentence case throughout (e.g., `## Key points`, `### Data structures and algorithms`).
- **Non-Destructive Ingestion**: Files placed in `input/` are never deleted, renamed, or modified by the agent.
- **Deletion Safety**: No generated wiki page is deleted without explicit human confirmation.
