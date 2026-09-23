# PM Discovery Lab

A public, vendor-neutral skill package for AI-assisted product discovery. This is the published repository (`PM-Discovery-Repo`) — fork it as the seed for your own PM discovery workspace.

It is intentionally generic. It helps PMs build their own product context, taxonomy, evidence model, opportunity workflow, AI-assistant planning workflow, competitive-analysis workflow, task-card knowledge base, assistant-evaluation workflow, how-to video pipeline, and prototype system — without exposing private company knowledge. Every example in this repo is synthetic.

It also covers what happens after discovery. A delivery loop for TPMs and PMs who own execution takes a committed bet from charter to launch: framing the program, decomposing it across teams, finding the critical path, earning stakeholder commitment, running status and risk, handling tradeoffs, and proving the result against a baseline.

## What's inside

- `skills/` — thirty-eight skills (listed below): the `ai-brain` front door, twenty-three for discovery, and fourteen for delivery, each with a `SKILL.md` and a vendor-neutral `agents/agent.yaml` interface descriptor.
- `templates/` — fill-in templates for source cards, taxonomy, evidence, painpoint validation, opportunity briefs, and prototype contracts, plus program charters, dependency maps, risk registers, stakeholder maps, communication plans, decision logs, status reports, tradeoff briefs, metric trees, launch-readiness checklists, and retrospectives.
- `scripts/` — standard-library Python helpers: critical-path analysis, risk-register scoring, a status-report drafter, and a static validator for the skills themselves.
- `examples/` — a synthetic DemoDesk program to run the scripts against.
- `validation-plan.md` — how to test the skills against synthetic fixtures before you rely on them.
- `publication-manifest.md` — the public-safety policy and the review record for this repo.

## Start here: ask the AI Brain

Not sure where to begin? Use `ai-brain`. Ask it things like *"What can this repo help me do?"*, *"How do I build a product brief?"*, *"We committed to this feature, now what?"*, or *"Is there a template for a risk register?"* It asks at most two questions, recommends the shortest path through the skills, names the template each step fills, and then walks you through the work to a finished deliverable. Its catalog of every skill, template, and script lives in `skills/ai-brain/references/`.

## The 5-stage operating loop

Five skills package a repeatable loop for using AI across the whole product management lifecycle, not just for one-off drafting — **SENSE → LISTEN → GROUND → PROTOTYPE → COMMIT**. Each stage names the specific skill(s) below it that do the detailed work; think of these five as the narrative spine and the rest of the skills as the machinery underneath it.

- `pm-sense` — Stage 1: build or refresh a live market/competitor radar.
- `pm-listen` — Stage 2: turn customer calls into a searchable, traceable evidence base.
- `pm-ground` — Stage 3: ground a new idea in your product's actual current state before treating it as fact.
- `pm-prototype` — Stage 4: build a disposable prototype, keep a decision log, and capture the Business Logic Companion (the rules a prototype can't show).
- `pm-commit` — Stage 5: convert a validated prototype into requirements, an epic, and testable stories without losing traceability.

Validated insight from COMMIT should feed back into SENSE, LISTEN, and GROUND — it's a loop, not a one-way pipeline.

## The 5-stage delivery loop

Discovery ends with a committed epic. Delivery starts there. Five skills take that bet to launch and back — **FRAME → PLAN → ALIGN → RUN → LAND**. They carry program sense: the judgment about goals, dependencies, stakeholders, risk, and tradeoffs that gets a feature shipped without adding needless process.

- `tpm-frame` — Stage 1: agree the goal, success metric and baseline, program type, fixed variable, execution model, and decider; write the charter.
- `tpm-plan` — Stage 2: decompose the work by team, name the interface contracts between teams, find the critical path, set demo-ending milestones, check staffing, and seed the risk register.
- `tpm-align` — Stage 3: map stakeholders, earn partner-team commitments tied to their own goals, set the decision forum, and write the communication plan.
- `tpm-run` — Stage 4: run status and risk review, cost out change requests, bring tradeoffs to the decider with options, and keep the decision log.
- `tpm-land` — Stage 5: run go/no-go, stage the rollout with a rollback owner, measure against the baseline, and feed lessons back into discovery.

LAND feeds back into SENSE, LISTEN, and GROUND, so the two loops form one cycle from signal to shipped outcome.

## Skills

Core discovery-to-prototype chain:

- `source-intake`
- `product-taxonomy-builder`
- `customer-evidence-normalizer`
- `painpoint-validation`
- `opportunity-selection`
- `opportunity-refinement`
- `prototype-planning`
- `disposable-prototype-builder`
- `ai-assistant-flow-planner`

Rigor gates and finishing passes — run these on the output of the chain above:

- `generic-claim-falsification` — substitute unrelated organizations into every load-bearing claim; anything that stays true is a category description, not a diagnosis. Blocking gate between painpoint validation and opportunity selection.
- `analog-peer-evidence` — reason from named peer deployments when internal access is unavailable, with per-claim transfer grading and a search order that prefers published reversals over published wins.
- `section-role-audit` — finishing pass on a persuasive document: cut sections that only restate the apex, check stance and map consistency, and test the document against a realistic attention budget.

Extended workflows — competitive analysis, product knowledge, and assistant/video production:

- `competitive-analysis-intelligence` — evidence-grounded competitor scorecards, dossiers, and opportunities/threats reports for a program or feature.
- `task-card-knowledge-builder` — turn messy product knowledge into verified, agent-safe task cards with a source-to-verification-to-promotion lifecycle.
- `assistant-golden-evaluator` — regression-test any assistant/chatbot against a golden Q/A or scenario set and route defects to the right owner/layer.
- `how-to-video-producer` — turn a verified task card into a scripted, recorded, QA'd how-to video with optional voiceover.
- `technical-writing-taskcard-bridge` — audit your documentation against verified task cards for drift, or draft a doc page from a verified task-card cluster.

Delivery loop machinery — the detailed work under the five delivery stages:

- `delivery-decomposition` — turn a design into owning teams, interface contracts, a dependency map, the critical path, and phasing.
- `risk-register` — pre-mortem, probability × impact scoring, owners and resolve-by dates, overdue risks converted to issues, and calculated-risk decision records.
- `tradeoff-decision-brief` — when the plan no longer fits, frame what gives across date, scope, resources, and quality, with options and a decider.
- `stakeholder-alignment` — stakeholder map, 1:1 discovery, partner asks tied to their goals, and conflict resolution.
- `program-status-report` — executive, partner-org, and working-team updates with an evidence-based status color.
- `success-metric-tree` — one outcome metric with a baseline, supporting branches, and counter-metrics for anything gameable.
- `launch-readiness-review` — go/no-go with every criterion met, waived by an owner, or blocking, plus AI-specific gates.
- `program-recovery` — diagnose and re-baseline a program that is badly off plan, including the option to stop.
- `program-retrospective` — measure against baseline, review decisions, and route lessons to owners and back into discovery.

Safety:

- `public-safety-review`

## Choosing a skill

If you'd rather be guided, ask `ai-brain`. If you're building the whole loop, start with the 5-stage operating loop above — `pm-sense` through `pm-commit` — and let each stage route you into the detailed skill it needs. If you just need one piece: run discovery first (`source-intake` through `opportunity-refinement`, with `generic-claim-falsification` as a gate before you commit to a direction), then branch into whichever extended workflow matches the output you need — a prototype, an AI assistant plan, a competitive study, a verified knowledge base, an assistant regression test, a how-to video, or a documentation audit. Once a bet is committed, move to the delivery loop — `tpm-frame` through `tpm-land`. If you only need one delivery piece, reach for it directly: `risk-register` for a risk review, `tradeoff-decision-brief` when a plan breaks, `program-recovery` for a troubled program, `launch-readiness-review` before a ship decision. Each `SKILL.md` names the other skills it expects to run before or after it.

## Evidence discipline

Every skill in this repo that makes a claim about customer pain, priority, or competitive position follows the same evidence rule:

- **First-hand evidence** (account reports, transcripts, survey rows, support records, verified task cards, product/code checks, public competitor docs) is proof.
- **Governed lineage artifacts** (generated evidence tables, quote indices, source-lineage tables that point back to proof files) are usable but should stay traceable to the proof layer.
- **Context-only artifacts** (prior generated narrative studies, strategy memos, old assistant answers without lineage) are useful for framing and prior assumptions, never for validation claims on their own.

Two additions cover the case where you are analyzing an organization you cannot see inside:

- **Named peer deployments** (`analog_peer`) are real evidence when the peer is named, the result is published and attributable, and the deployment context is stated. Anonymous benchmarks and vendor-aggregated averages are not; they are the material that makes an analysis read as generic. Grade the transfer assumption per claim, never once for the document.
- **Absence** — what a target's own artifacts do not say — is admissible and is often the most target-specific material available, but it is a **signal, never a finding**. Record the search that established it, and never let it carry a recommendation.

And one test that applies to the whole result: if you swap the target organization for an unrelated one and the analysis still reads as true, you have written a category description. Evidence volume does not fix this; only target-specific grounding does.

Use precise language to keep these separate: "Evidence shows..." only when backed by proof or lineage; "The prior study framed..." when using a generated study as context; "We infer..." when the connection is logical but not directly stated by a customer; "Open question..." when nothing has validated the claim yet. Do not let an AI-generated artifact become the source of truth for itself.

## Use it with any model

Each skill ships a vendor-neutral `agents/agent.yaml` describing its interface. Wire the skills into whichever agent or model you use; nothing here is tied to a specific AI vendor.

The scripts in `scripts/` need only Python 3.8+ and the standard library. They produce drafts from your CSVs; the skills tell the agent (and you) how to judge them.

```text
python scripts/critical_path.py examples/demodesk-program/dependency-map.csv
python scripts/risk_register.py examples/demodesk-program/risk-register.csv --today 2026-03-16
python scripts/status_report.py --plan examples/demodesk-program/dependency-map.csv --risks examples/demodesk-program/risk-register.csv --today 2026-03-16
python scripts/validate_skills.py
```

## Keep it public-safe

This package contains no customer data, internal taxonomy, company-specific source IDs, private UI assets, secrets, or production code — and it should stay that way. If you fork it and add your own sources, keep private material in a separate, non-public workspace. Run the `public-safety-review` skill before publishing anything derived from your own evidence; `publication-manifest.md` describes the full boundary.

## Contributing

Improvements to the skills and templates are welcome. See `CONTRIBUTING.md` for how to propose changes. To report sensitive content or a security issue, follow `SECURITY.md` — do not open a public issue for those.

## License

MIT — see `LICENSE`.
