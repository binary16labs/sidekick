import argparse
import json
import os
import re
import sys

# Force UTF-8 output on Windows to prevent UnicodeEncodeError in terminal
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Core design system rules
RULES_DOC = """
# Universal Agentic Project Rules & Guidelines

## 1. Zen Earth-Tone Design System
- **Backgrounds**: Muted, warm charcoal glass (`#0a0e17`, `rgba(16, 17, 13, 0.82)`), soft slate, and warm olive-charcoal.
- **Accents & Primary Text**: Sage green (`rgb(156, 175, 136)` or `#9caf88`), warm Bone (`rgb(236, 230, 216)` or `#ece6d8`), soft moss, warm gold/taupe.
- **Forbidden Colors**: Cool neons (harsh cyan, blue, magenta) or generic solid neons (red, green, blue) unless they are semantic indicators of drift (like coral/orange for error/diff warnings).
- **Reduced Cognitive Load**: Progressive discovery of visual interfaces (cellular nodes, convex hull grouping, collapsible docks). Full bleed views with Zen mode options to strip clutter to the stage.

## 2. Local-First Architectural Contracts
- **Atomic File-System Database**: Keep sessions, logs, and artifacts portable. Save them as distinct, self-describing JSON files (e.g. `Session -> Thought -> Tool Call -> Artifact -> Result` ontology) under `data/entities/<id>.json`.

- **Single Source of Truth**: Center all environment/log folder configurations in a single manifest config file (like `manifest.json` or `config.js`). Use home-relative paths (e.g. `~/.<app_name>/` or `%USERPROFILE%/...`) to avoid environment lock-in.
- **Local CORS**: Secure APIs by restricting CORS strictly to `localhost` to protect local OS and terminal integration.

## 3. Developer and Tool Discipline
- **Tool Specificity**: Never use generic commands where specific tools exist. Use `view_file` over `cat`, `grep_search` over `grep`, and `list_dir` over `ls`.
- **File Output Default**: Large tool results or API responses should be redirected to JSON/text files rather than printed to stdout to protect the context window.
- **Mandatory Brainstorming**: Always perform an interactive design alignment with the operator before writing code modifications or creating skills.

## 4. Windows & Environment Resiliency (Constant Corrections)
- **Console Encoding**: Always force UTF-8 on Windows in Python scripts (`sys.stdout.reconfigure(encoding='utf-8')`) to prevent `UnicodeEncodeError` crashes when outputting emojis or box-drawing characters.
- **Path Escaping Bugs**: Never use raw backslashes in Python string replacements (e.g., `replace('\', '/')` will cause a SyntaxError). Use proper escaping `replace('\\\\', '/')` or rely on `pathlib`.
- **Stuck Git Processes**: Interactive `git` commands (and `git-credential-manager`) frequently get stuck in background tasks on Windows, locking the repository. Use explicit credential configurations or avoid interactive triggers.
- **Anti-Pattern Polling**: Do not use chained terminal commands like `sleep 30 && git branch` to wait for CI/CD actions. Use the agent's native asynchronous task management or the `schedule` tool instead.
- **Absolute Paths**: Stop hardcoding machine-specific paths like `C:/Users/nsdha/...` in source code or scripts. Always resolve paths relative to `__file__`, `os.getcwd()`, or environment variables (`%USERPROFILE%`).

## 5. Everything As Code (Architecture, Compliance, Policy, Lineage)
- **Architecture as Code**: Define environments, layouts, UI canvases, and tool registries in static manifest files (`manifest.json`). UIs should be pure functions of backend state, avoiding implicit GUI configuration.
- **Compliance & Policy as Code**: Enforce sandbox bounds with scope-guard middleware. Write scripts to actively lint and enforce design palettes and tool discipline. Cryptographically hash and verify critical audit logs.
- **Lineage as Code**: Keep a complete, queryable history of `Session -> Thought -> Artifact`. Never overwrite data without leaving an atomic JSON trace of the transformation.
- **Observable by Default**: Build drill-down explainability into the system. Expose LLM reasoning traces so operators can inspect *why* an agent made a decision, and ensure exceptions wrap contextual state.

## 6. DevSecOps & SDLC Management
- **Continuous Integration (Snapshot Builds)**: Every commit to the `main` branch must trigger an automated snapshot build (multi-platform) via CI/CD to ensure the build is never broken.
- **One-Command Release**: Releases should never be manual. Use a dedicated script (e.g., `manage-release.js patch/minor/major`) to automatically bump semantic versions, create commits, and push git tags.
- **Automated Deployments**: Pushing a version tag (`v*`) must automatically trigger the CI/CD pipeline to compile, sign, generate release notes, and deploy binaries to the release hosting platform (e.g., GitHub Releases).
- **Security Scans**: Linting for hardcoded paths and design violations should run as a pre-commit hook or part of the CI pipeline before a PR can be merged. Ensure automated CI/CD security scans are integrated.

## 8. The Cognitive Mesh (Graph RAG & CAG)
- **Tri-Graph CAG Context**: The ecosystem achieves Context-Augmented Generation (CAG) by combining three graphs rather than relying solely on flat vector search. Agents must leverage:
  - **The Knowledge Graph (Graph RAG)**: Ingested documentation and business logic mapped contextually.
  - **The Code Graph**: Tree-Sitter AST representations of the system.
  - **The Memory Graph**: Memo-Ray's portable entity mapping of `Session -> Thought -> Artifact`.
- **Enrichment Before Action**: Before acting on complex tasks, agents should combine memory (what was tried), code (what is built), and knowledge (what is intended).

## 9. Agent Operational Patterns & Anti-Patterns
- **Good: Canonical Tokens**: Consolidate shared resources (like CSS design tokens) into a single canonical source of truth (e.g., `colors.css`) and mirror them via aliases, ensuring disjointed apps never drift visually.
- **Good: Interactive Scoping**: When facing massive rewrites or unifications, agents must present the operator with concrete multi-option choices (e.g., Scope boundaries) *before* touching code.
- **Bad: Skin Overrides**: Avoid writing local module overrides that bypass the root architectural tokens (e.g., hardcoding navy blue surfaces on top of an earth-tone foundation).

## 10. Token Economics & Tax Removal
- **Zero Token Tax Architecture**: Avoid the "token tax" of perpetually dumping massive manifests, ASTs, and logs into the context window.
- **Dynamic Context Retrieval**: Leverage MCP capabilities to pull only atomic, localized entities exactly when needed. Caching, targeted graph queries, and modular memory layers should be used to make multi-agent processes significantly cheaper and faster.

## 11. Agentic Test Harness & Evals
- **Automated Workflow Evals**: All core systems must be verifiable by a dedicated agentic test harness that produces a final evaluation report.
- **The Evaluation Pipeline**: The harness must follow the `Planner -> Fan Out -> Condense -> Publish` pattern:
  1. **Planner**: Analyzes the manifest/contract and formulates a discrete test plan.
  2. **Fan Out**: Deploys parallel sub-agents or processes to concurrently evaluate specific components, domains, or edge cases.
  3. **Condense**: Synthesizes the parallel execution results into a unified understanding of system health.
  4. **Publish**: Emits the final structured evaluation report (often as an Artifact or Markdown document).

## 12. Institutional Data Mesh & Virtualization
- **Manifest-Driven Institutional Mesh**: Treat the ecosystem as a library. Every application, capability, and data asset must be indexed via a manifest, creating a hierarchical map of the organization (similar to an integrated App Directory or Collibra).
- **Data Virtualization (The Denodo Pattern)**: Avoid copying or centralizing data. Instead, build semantic virtualization layers over base views (e.g., `schema.table.column`) so agents and systems query federated sources in place.
- **Dynamic Domain Lenses**: Instead of rigid dashboards, systems should allow operators to define domain rules that instantly create a contextual "lens" or dynamic view of the mesh (akin to Outlook search folders).

## 13. Decentralized Lineage & Ledgers
- **Distributed Chain Lineage**: System logging and lineage must not rely on a monolithic central database. Use a distributed ledger or chained model where artifacts and state changes are cryptographically linked to their precedents, creating an unbroken, decentralized audit trail.

## 14. Up-Front Value & Behavior-Driven Discipline
- **Up-Front Value Assessment**: Progressive discovery demands that before *any* execution begins, the agent must clearly articulate the value of the change. If the ROI does not justify the complexity, the operation is blocked.
- **Strict TDD & BDD**: Test-Driven Development (TDD) and Behavior-Driven Development (BDD) are non-negotiable. Define the expected behaviors and the test harnesses *before* writing the implementation.
"""

def show_rules(args):
    print(RULES_DOC.strip())
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(RULES_DOC.strip())
        print(f"\nSuccess! Rules written to: {args.output}")

def check_style(args):
    target_path = os.path.abspath(args.path)
    if not os.path.exists(target_path):
        print(f"Error: Path does not exist: {target_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Auditing CSS files in: {target_path}")
    css_files = []
    if os.path.isfile(target_path) and target_path.endswith('.css'):
        css_files.append(target_path)
    else:
        for root, _, files in os.walk(target_path):
            if 'node_modules' in root or '.git' in root:
                continue
            for file in files:
                if file.endswith('.css'):
                    css_files.append(os.path.join(root, file))

    if not css_files:
        print("No CSS files found to audit.")
        return

    # Non-compliant colors (neon/harsh blue/cyan/etc.)
    # We identify harsh colors (like pure blues, bright purples, standard saturated neon lines)
    # Simple regex to catch common hex/rgb values
    NEON_PATTERNS = [
        (re.compile(r'#00ffff\b|#00ffcc\b|#0000ff\b|#ff00ff\b|#ff0000\b|#00ff00\b', re.IGNORECASE), "Saturated Hex Neon"),
        (re.compile(r'rgba?\(\s*0\s*,\s*255\s*,\s*(255|204)\s*.*?\)', re.IGNORECASE), "Harsh Cyan/Teal RGB"),
        (re.compile(r'rgba?\(\s*0\s*,\s*0\s*,\s*255\s*.*?\)', re.IGNORECASE), "Pure Blue RGB"),
        (re.compile(r'rgba?\(\s*255\s*,\s*0\s*,\s*255\s*.*?\)', re.IGNORECASE), "Harsh Magenta RGB"),
    ]
    
    COMPLIANT_KEYWORDS = ['sage', 'moss', 'bone', 'charcoal', 'slate', 'taupe', 'olive', 'gold', 'earth']

    violations = []
    compliant_count = 0
    total_colors = 0

    for filepath in css_files:
        rel_path = os.path.relpath(filepath, target_path)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for line_idx, line in enumerate(lines, 1):
                # Search for hex colors
                hex_colors = re.findall(r'#[0-9a-fA-F]{3,8}\b', line)
                rgb_colors = re.findall(r'rgba?\(.*?\)', line)
                
                for color in hex_colors + rgb_colors:
                    total_colors += 1
                    is_neon = False
                    for pattern, label in NEON_PATTERNS:
                        if pattern.search(color):
                            violations.append({
                                'file': rel_path,
                                'line': line_idx,
                                'color': color,
                                'reason': f"Flags {label} token (potential clash with Zen Earth-Tone aesthetics)",
                                'content': line.strip()
                            })
                            is_neon = True
                            break
                    
                    if not is_neon:
                        # Check if line indicates standard variable naming
                        if any(kw in line.lower() for kw in COMPLIANT_KEYWORDS):
                            compliant_count += 1
        except Exception as e:
            print(f"Warning: Failed to read {filepath}: {e}", file=sys.stderr)

    report = {
        'files_audited': len(css_files),
        'total_colors_detected': total_colors,
        'compliant_references': compliant_count,
        'violations_count': len(violations),
        'violations': violations
    }

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        print(f"Audit complete. Report written to: {args.output}")
    else:
        print("\n--- STYLES AUDIT REPORT ---")
        print(f"Files Audited: {len(css_files)}")
        print(f"Total Colors Evaluated: {total_colors}")
        print(f"Compliant Token References: {compliant_count}")
        print(f"Violations Found: {len(violations)}\n")
        
        if violations:
            print("WARNING: Found non-compliant harsh accent colors:")
            for v in violations:
                print(f"  [{v['file']}:{v['line']}] {v['color']} - {v['reason']}")
                print(f"    Line: {v['content']}")
        else:
            print("SUCCESS: All evaluated colors adhere to Zen / Earth-Tone design tokens!")

def get_context(args):
    # Try to locate Entity database
    db_paths = []
    if args.db_path:
        db_paths.append(args.db_path)
    
    # Try standard relative paths
    db_paths.append(os.path.join(os.getcwd(), 'data'))
    if args.project:
        db_paths.append(os.path.join(os.path.expanduser('~'), f'.{args.project}', 'data'))
    
    selected_db = None
    for path in db_paths:
        if path and os.path.exists(os.path.join(path, 'index.json')):
            selected_db = path
            break
            
    if not selected_db:
        # Fallback to scanning parent directories
        current = os.getcwd()
        while True:
            candidate = os.path.join(current, 'agent-os-dashboard', 'server', 'data')
            if os.path.exists(os.path.join(candidate, 'index.json')):
                selected_db = candidate
                break
            parent = os.path.dirname(current)
            if parent == current:
                break
            current = parent

    if not selected_db:
        print("Error: Could not locate entity database index.json.", file=sys.stderr)
        print("Please provide the path using --db-path.", file=sys.stderr)
        sys.exit(1)

    print(f"Using entity database at: {selected_db}")
    
    try:
        with open(os.path.join(selected_db, 'index.json'), 'r', encoding='utf-8') as f:
            index = json.load(f)
            
        sessions = index.get('sessions', [])
        loaded_sessions = []
        
        entities_dir = os.path.join(selected_db, 'entities')
        for sid in sessions:
            entity_path = os.path.join(entities_dir, f"{sid}.json")
            if os.path.exists(entity_path):
                with open(entity_path, 'r', encoding='utf-8') as f:
                    session = json.load(f)
                    
                    # Filter by project if specified
                    if args.project:
                        meta = session.get('metadata', {})
                        proj = meta.get('project', '') or meta.get('cwd', '') or meta.get('projectPath', '')
                        if args.project.lower() not in str(proj).lower():
                            continue
                            
                    loaded_sessions.append(session)
                    
        # Sort by timestamp descending
        loaded_sessions.sort(key=lambda s: s.get('timestamp', 0), reverse=True)
        results = loaded_sessions[:args.limit]
        
        # Load children timeline for the very latest session to give deep context
        timeline_events = []
        if results:
            latest_sid = results[0]['id']
            timeline_events.append(results[0])
            queue = list(results[0].get('children_ids', []))
            
            while queue:
                child_id = queue.pop(0)
                child_path = os.path.join(entities_dir, f"{child_id}.json")
                if os.path.exists(child_path):
                    with open(child_path, 'r', encoding='utf-8') as f:
                        child = json.load(f)
                        timeline_events.append(child)
                        queue.extend(child.get('children_ids', []))
                        
            timeline_events.sort(key=lambda x: x.get('timestamp', 0))

        report = {
            'sessions_count': len(results),
            'latest_session_id': results[0]['id'] if results else None,
            'sessions': results,
            'latest_session_timeline': timeline_events
        }

        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2)
            print(f"Context written to: {args.output}")
        else:
            print(f"\nFound {len(results)} matching sessions.")
            for idx, s in enumerate(results, 1):
                meta = s.get('metadata', {})
                proj = meta.get('project', 'N/A')
                agent = s.get('agent', 'System')
                time_str = str(s.get('timestamp', 0))
                print(f"[{idx}] ID: {s['id']} | Agent: {agent} | Project: {proj}")
                print(f"    Content: {s.get('content', '')[:100]}...")
            
            if timeline_events:
                print(f"\n--- TIMELINE DETAIL FOR LATEST SESSION ({results[0]['id']}) ---")
                for event in timeline_events:
                    print(f"[{event.get('type', 'EVENT').upper()}] ({event.get('agent', 'System')})")
                    print(f"  {event.get('content', '').strip()[:200]}")
                    print("-" * 50)
    except Exception as e:
        print(f"Error querying database: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Enforce Binary 16 design principles and coding rules")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # show-rules
    p_rules = subparsers.add_parser('show-rules', help='Output the core project rules')
    p_rules.add_argument('--output', help='Optional path to write markdown rules file')

    # check-style
    p_style = subparsers.add_parser('check-style', help='Audit CSS color tokens for Earth-Tone compliance')
    p_style.add_argument('--path', required=True, help='Directory or CSS file path to check')
    p_style.add_argument('--output', help='Optional path to save JSON report')

    # get-context
    p_context = subparsers.add_parser('get-context', help='Extract past context from Memo-Ray session DB')
    p_context.add_argument('--project', help='Filter sessions by project name')
    p_context.add_argument('--limit', type=int, default=5, help='Limit number of sessions returned')
    p_context.add_argument('--db-path', help='Explicit path to Memo-Ray data directory containing index.json')
    p_context.add_argument('--output', help='Optional path to save JSON context report')

    args = parser.parse_args()

    if args.command == 'show-rules':
        show_rules(args)
    elif args.command == 'check-style':
        check_style(args)
    elif args.command == 'get-context':
        get_context(args)

if __name__ == '__main__':
    main()
