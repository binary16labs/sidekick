---
name: make-project-right
description: >-
  Enforce Binary 16 design principles, local-first data conventions, and
  developer discipline using the Memo-Ray memory map.
---

# Make Project Right

## Overview
This skill acts as the institutional quality gate for all Universal Agentic Projects. It codifies established design aesthetics (the Zen earth-tone palette), local-first architectural contracts, multi-agent context alignment, and terminal tool specificity discipline.

## Dependencies
None. (Utilizes the local file-system entity database for context retrieval).

## Quick Start
Check if the styles in your workspace align with Binary 16 principles:
```bash
uv run check_project.py check-style --path .
```

Get a summary of decisions and stats from local project history:
```bash
uv run check_project.py get-context --project <your_project_name>
```

## Utility Scripts
The `check_project.py` utility script provides subcommands for quality enforcement.

### check-style
Analyzes CSS files in a target directory to ensure adherence to the zen earth-tone color system.
```bash
uv run check_project.py check-style --path /path/to/project
```
- Outputs a list of compliant colors and flags any non-compliant cool neons or blues.

### get-context
Fetches session summaries and metadata from the local Memo-Ray files to reconstruct context.
```bash
uv run check_project.py get-context --project <project_name> [--limit <n>]
```
- Directly reads the JSON database at `~/.<app_name>/data/` or relative path.

### show-rules
Outputs the structured design system tokens and architectural constraints.
```bash
uv run check_project.py show-rules
```

## Rules and Guidelines

### 1. Zen Earth-Tone Design System
- **Backgrounds**: Muted, warm charcoal glass (`#0a0e17`, `rgba(16, 17, 13, 0.82)`), soft slate, and warm olive-charcoal.
- **Accents & Primary Text**: Sage green (`rgb(156, 175, 136)` or `#9caf88`), warm Bone (`rgb(236, 230, 216)` or `#ece6d8`), soft moss, warm gold/taupe.
- **Forbidden Colors**: Cool neons (harsh cyan, blue, magenta) or generic solid neons (red, green, blue) unless they are semantic indicators of drift (like coral/orange for error/diff warnings).
- **Reduced Cognitive Load**: Progressive discovery of visual interfaces (cellular nodes, convex hull grouping, collapsible docks). Full bleed views with Zen mode options to strip clutter to the stage.

### 2. Local-First Architectural Contracts
- **Atomic File-System Database**: Keep sessions, logs, and artifacts portable. Save them as distinct, self-describing JSON files (e.g. `Session -> Thought -> Tool Call -> Artifact -> Result` ontology) under `data/entities/<id>.json`.
- **Single Source of Truth**: Center all environment/log folder configurations in a single manifest config file (like `manifest.json` or `config.js`). Use home-relative paths (e.g. `~/.<app_name>/` or `%USERPROFILE%/...`) to avoid environment lock-in.
- **Local CORS**: Secure APIs by restricting CORS strictly to `localhost` to protect local OS and terminal integration.

### 3. Developer and Tool Discipline
- **Tool Specificity**: Never use generic commands where specific tools exist. Use `view_file` over `cat`, `grep_search` over `grep`, and `list_dir` over `ls`.
- **File Output Default**: Large tool results or API responses should be redirected to JSON/text files rather than printed to stdout to protect the context window.
- **Mandatory Brainstorming**: Always perform an interactive design alignment with the operator before writing code modifications or creating skills.

### 4. Windows & Environment Resiliency (Constant Corrections)
- **Console Encoding**: Always force UTF-8 on Windows in Python scripts (`sys.stdout.reconfigure(encoding='utf-8')`) to prevent `UnicodeEncodeError` crashes when outputting emojis or box-drawing characters.
- **Path Escaping Bugs**: Never use raw backslashes in Python string replacements (e.g., `replace('\', '/')` will cause a SyntaxError). Use proper escaping `replace('\\\\', '/')` or rely on `pathlib`.
- **Stuck Git Processes**: Interactive `git` commands (and `git-credential-manager`) frequently get stuck in background tasks on Windows, locking the repository. Use explicit credential configurations or avoid interactive triggers.
- **Anti-Pattern Polling**: Do not use chained terminal commands like `sleep 30 && git branch` to wait for CI/CD actions. Use the agent's native asynchronous task management or the `schedule` tool instead.
- **Absolute Paths**: Stop hardcoding machine-specific paths like `C:/Users/nsdha/...` in source code or scripts. Always resolve paths relative to `__file__`, `os.getcwd()`, or environment variables (`%USERPROFILE%`).

### 5. Everything As Code (Architecture, Compliance, Policy, Lineage)
- **Architecture as Code**: Define environments, layouts, UI canvases, and tool registries in static manifest files (`manifest.json`). UIs should be pure functions of backend state, avoiding implicit GUI configuration.
- **Compliance & Policy as Code**: Enforce sandbox bounds with scope-guard middleware. Write scripts to actively lint and enforce design palettes and tool discipline. Cryptographically hash and verify critical audit logs.
- **Lineage as Code**: Keep a complete, queryable history of `Session -> Thought -> Artifact`. Never overwrite data without leaving an atomic JSON trace of the transformation.
- **Observable by Default**: Build drill-down explainability into the system. Expose LLM reasoning traces so operators can inspect *why* an agent made a decision, and ensure exceptions wrap contextual state.

### 6. DevSecOps & SDLC Management
- **Continuous Integration (Snapshot Builds)**: Every commit to the `main` branch must trigger an automated snapshot build (multi-platform) via CI/CD to ensure the build is never broken.
- **One-Command Release**: Releases should never be manual. Use a dedicated script (e.g., `manage-release.js patch/minor/major`) to automatically bump semantic versions, create commits, and push git tags.
- **Automated Deployments**: Pushing a version tag (`v*`) must automatically trigger the CI/CD pipeline to compile, sign, generate release notes, and deploy binaries to the release hosting platform (e.g., GitHub Releases).
- **Security Scans**: Linting for hardcoded paths and design violations should run as a pre-commit hook or part of the CI pipeline before a PR can be merged. Ensure automated CI/CD security scans are integrated.

### 7. Advanced Architecture & Domain Modeling (Benny/Pypes Standards)
- **Decoupled Stateless Services**: All system capabilities must be built as service-oriented, strictly stateless executors managed entirely by code manifests.
- **Withdrawn Objects**: Core domain logic must be encapsulated in "withdrawn objects"—isolated constructs that strictly define boundaries for User Input, Process execution, and Output.
- **Tri-Level Data Modeling**: Data architecture must follow a strict progression: Conceptual ➔ Logical ➔ Physical. Database connections and structures must be governed by formal standard design patterns (Entity Relation diagrams, UML, BPMN).
- **The Strangler Fig Pattern**: Do not reinvent the wheel. When dealing with existing systems or external capabilities, wrap them using the Strangler Fig pattern to progressively migrate or integrate functionality.
- **Feature Toggles by Design**: Build feature toggles natively into the architecture to allow safe, decoupled deployments and runtime behavioral switches.
- **Strict Contract Enforcement**: The system manifest is the absolute contract. Zero scope creep is permitted outside of what is explicitly defined in the manifest.

### 8. The Cognitive Mesh (Graph RAG & CAG)
- **Tri-Graph CAG Context**: The ecosystem achieves Context-Augmented Generation (CAG) by combining three graphs rather than relying solely on flat vector search. Agents must leverage:
  - **The Knowledge Graph (Graph RAG)**: Ingested documentation and business logic mapped contextually.
  - **The Code Graph**: Tree-Sitter AST representations of the system.
  - **The Memory Graph**: Memo-Ray's portable entity mapping of `Session -> Thought -> Artifact`.
- **Enrichment Before Action**: Before acting on complex tasks, agents should combine memory (what was tried), code (what is built), and knowledge (what is intended).

### 9. Agent Operational Patterns & Anti-Patterns
- **Good: Canonical Tokens**: Consolidate shared resources (like CSS design tokens) into a single canonical source of truth (e.g., `colors.css`) and mirror them via aliases, ensuring disjointed apps never drift visually.
- **Good: Interactive Scoping**: When facing massive rewrites or unifications, agents must present the operator with concrete multi-option choices (e.g., Scope boundaries) *before* touching code.
- **Bad: Skin Overrides**: Avoid writing local module overrides that bypass the root architectural tokens (e.g., hardcoding navy blue surfaces on top of an earth-tone foundation).

### 10. Token Economics & Tax Removal
- **Zero Token Tax Architecture**: Avoid the "token tax" of perpetually dumping massive manifests, ASTs, and logs into the context window.
- **Dynamic Context Retrieval**: Leverage MCP capabilities to pull only atomic, localized entities exactly when needed. Caching, targeted graph queries, and modular memory layers should be used to make multi-agent processes significantly cheaper and faster.

### 11. Agentic Test Harness & Evals
- **Automated Workflow Evals**: All core systems must be verifiable by a dedicated agentic test harness that produces a final evaluation report.
- **The Evaluation Pipeline**: The harness must follow the `Planner -> Fan Out -> Condense -> Publish` pattern:
  1. **Planner**: Analyzes the manifest/contract and formulates a discrete test plan.
  2. **Fan Out**: Deploys parallel sub-agents or processes to concurrently evaluate specific components, domains, or edge cases.
  3. **Condense**: Synthesizes the parallel execution results into a unified understanding of system health.
  4. **Publish**: Emits the final structured evaluation report (often as an Artifact or Markdown document).

### 12. Institutional Data Mesh & Virtualization
- **Manifest-Driven Institutional Mesh**: Treat the ecosystem as a library. Every application, capability, and data asset must be indexed via a manifest, creating a hierarchical map of the organization (similar to an integrated App Directory or Collibra).
- **Data Virtualization (The Denodo Pattern)**: Avoid copying or centralizing data. Instead, build semantic virtualization layers over base views (e.g., `schema.table.column`) so agents and systems query federated sources in place.
- **Dynamic Domain Lenses**: Instead of rigid dashboards, systems should allow operators to define domain rules that instantly create a contextual "lens" or dynamic view of the mesh (akin to Outlook search folders).

### 13. Decentralized Lineage & Ledgers
- **Distributed Chain Lineage**: System logging and lineage must not rely on a monolithic central database. Use a distributed ledger or chained model where artifacts and state changes are cryptographically linked to their precedents, creating an unbroken, decentralized audit trail.

### 14. Up-Front Value & Behavior-Driven Discipline
- **Up-Front Value Assessment**: Progressive discovery demands that before *any* execution begins, the agent must clearly articulate the value of the change. If the ROI does not justify the complexity, the operation is blocked.
- **Strict TDD & BDD**: Test-Driven Development (TDD) and Behavior-Driven Development (BDD) are non-negotiable. Define the expected behaviors and the test harnesses *before* writing the implementation.

## Common Mistakes
- **Applying Stark Neons**: Adding neon cyan, bright blue, or generic red/blue elements to user interfaces, violating the zen earth-tone calming aesthetics.
- **Hardcoding System Paths**: Hardcoding machine-specific paths (e.g., `C:\Users\username\...`) instead of using dynamic path constructors like `os.homedir()` or environment variables.
- **Neglecting Tool Specificity**: Resorting to running `cat` or `ls` in the terminal when custom file reading or directory listing tools are available.
- **Terminal Polling**: Writing `sleep N` loops in the terminal instead of relying on the native task notification system.
- **Unescaped Path Slashes**: Using raw backslashes inside Python strings intended for replacement or regex, leading to `SyntaxError`.
