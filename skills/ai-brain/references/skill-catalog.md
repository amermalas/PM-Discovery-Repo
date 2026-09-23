# Skill, Template, And Script Catalog

Every skill, template, and script in this repo. `scripts/validate_skills.py` fails if a skill folder or template file is missing from this catalog, so keep it current when you add one.

Columns: **Use when** (the trigger), **Needs** (minimum input), **Produces** (the artifact), **Next** (the usual following step).

## Start here

| Skill | Use when | Needs | Produces | Next |
|---|---|---|---|---|
| `ai-brain` | Someone asks what the repo can do, how to build a deliverable, or what to do next | A question | A recommended path, then the deliverable | Any skill below |

## Discovery loop: SENSE -> LISTEN -> GROUND -> PROTOTYPE -> COMMIT

| Skill | Use when | Needs | Produces | Next |
|---|---|---|---|---|
| `pm-sense` | You need a live market or competitor radar, weekly signal digest, or monthly market brief | A product bucket, known competitors, approved public sources | Signal digest, market brief, competitor capability matrix, each claim sourced and dated | `pm-listen` or `competitive-analysis-intelligence` |
| `pm-listen` | You want to know what customers are saying, pull quotes, or build an evidence-backed opportunity brief | Customer calls or notes with account, date, speaker | Traceable evidence rows, interpreted needs kept separate from quotes | `pm-ground` or `painpoint-validation` |
| `pm-ground` | You need to check what the product already does before treating an idea or claim as fact | The claim or idea, docs and tickets | Confirmed facts, conflicts, inferences, "not found" cases | `opportunity-refinement` or `pm-prototype` |
| `pm-prototype` | You want a clickable prototype, a decision log, and the business rules a prototype can't show | A refined opportunity | Prototype brief, decision log, Business Logic Companion | `pm-commit` |
| `pm-commit` | You need requirements, an epic, and stories from a validated prototype | Prototype, decision log, Business Logic Companion | Requirements brief or PRD, epic, testable stories | `tpm-frame` |

## Discovery machinery

| Skill | Use when | Needs | Produces | Next |
|---|---|---|---|---|
| `source-intake` | You are adding new research, interviews, tickets, surveys, or docs | Raw sources | Source cards with sensitivity and allowed uses | `product-taxonomy-builder` or `customer-evidence-normalizer` |
| `product-taxonomy-builder` | You need a map of product areas, capabilities, workflows, personas, glossary | Product docs, walkthroughs, release notes | Product taxonomy | `customer-evidence-normalizer` |
| `customer-evidence-normalizer` | You have messy feedback and need structured evidence | Source cards, feedback | Atomic evidence rows with lineage and painpoint candidates | `painpoint-validation` |
| `painpoint-validation` | You need to know which problems are actually supported | Evidence rows, painpoint candidates | Validation table: supported, under-evidenced, unclear, not supported | `generic-claim-falsification` |
| `opportunity-selection` | You need to turn validated problems into a chosen opportunity | Validated painpoints, strategy criteria | Primary opportunity, follow-on, not-now list, AI posture | `opportunity-refinement` |
| `opportunity-refinement` | You have one opportunity and need a product brief | The selected opportunity and its evidence | Problem, JTBD, MVP behaviors, guardrails, non-goals, risks, review questions | `prototype-planning` or `pm-prototype` |
| `prototype-planning` | You are about to build a prototype and need its question and contract | Refined opportunity | Prototype plan and `PROTOTYPE.md` contract | `disposable-prototype-builder` |
| `disposable-prototype-builder` | You are building the throwaway prototype | Prototype plan, synthetic fixtures | Prototype, verification notes, known limitations | `pm-commit` |
| `ai-assistant-flow-planner` | The opportunity is an assistant, chatbot, or copilot | Assistant idea, workflow context | Workflow families, conversation paths, prompt chips, gates, tool and data map, eval plan | `assistant-golden-evaluator` |

## Rigor gates and finishing passes

| Skill | Use when | Needs | Produces | Next |
|---|---|---|---|---|
| `generic-claim-falsification` | Before selecting an opportunity, to check the diagnosis is about this organization and not the category | Draft thesis or painpoints, evidence | Graded claims, specificity ratio, whether the recommendation survives | `opportunity-selection` |
| `analog-peer-evidence` | You can't see inside the target organization and must reason from named peers | Claims, public peer material | Peer rows, per-claim transfer grades, absence signals, search log | `painpoint-validation` |
| `section-role-audit` | A persuasive document is finished and needs tightening | The document | Sections kept or cut, stance and map checks, attention test | `public-safety-review` |

## Specialist workflows

| Skill | Use when | Needs | Produces | Next |
|---|---|---|---|---|
| `competitive-analysis-intelligence` | You need a full competitive study for an arena or feature | Account evidence, your feature map, competitor list | Landscape, scorecards, dossiers, opportunities and threats | `opportunity-selection` |
| `task-card-knowledge-builder` | You need verified how-to cards from messy product knowledge | Q/A, docs, code, browser tests | Task cards with verification and promotion decisions | `technical-writing-taskcard-bridge` or `how-to-video-producer` |
| `assistant-golden-evaluator` | You need to regression-test an assistant against a golden set | Golden set, captured answers | Scores, root-cause defect classes, regression report | `launch-readiness-review` |
| `how-to-video-producer` | You need a how-to video from a verified task card | Verified card | Script, QA checklist, sync map, output contract | `technical-writing-taskcard-bridge` |
| `technical-writing-taskcard-bridge` | You need a docs drift audit or a doc page drafted from verified cards | Doc pages, verified cards | Drift review items, doc opportunities, draft pages | `task-card-knowledge-builder` |

## Delivery loop: FRAME -> PLAN -> ALIGN -> RUN -> LAND

| Skill | Use when | Needs | Produces | Next |
|---|---|---|---|---|
| `tpm-frame` | A committed bet needs to become a program | Epic, requirements brief, decision log, a sponsor | Program charter | `tpm-plan` |
| `tpm-plan` | You need workstreams, the critical path, milestones, staffing | Charter, epic and stories | Baselined delivery plan, dependency map, seeded risk register | `tpm-align` |
| `tpm-align` | You need stakeholder buy-in, a kickoff, a decision forum, a comms plan | Charter, plan | Stakeholder map, partner commitments, communication plan | `tpm-run` |
| `tpm-run` | You are running the program week to week, or it is slipping | Plan, risk register, this week's updates | Status, re-scored risks, decision log entries, tradeoff briefs | `tpm-land` or `program-recovery` |
| `tpm-land` | You are ready to ship, or it just shipped | Charter metric, test and eval results, readiness status | Go/no-go, rollout plan, results vs baseline, retro | `pm-sense`, `pm-listen`, `pm-ground` |

## Delivery machinery

| Skill | Use when | Needs | Produces | Next |
|---|---|---|---|---|
| `delivery-decomposition` | A design lists components but not who waits on whom | Epic, component list, teams | Ownership map, interface contracts, dependency map, critical path, phasing | `risk-register` |
| `risk-register` | Starting a plan, weekly review, or shipping with a known risk | Plan, design review notes | Scored, owned risks; overdue risks as issues; calculated-risk records | `program-status-report` |
| `tradeoff-decision-brief` | The plan no longer fits; something has to give | Fixed knob, the change, estimates | Options with consequences, recommendation, decider, decide-by date | `tpm-run` |
| `stakeholder-alignment` | A partner won't commit, priorities conflict, or before kickoff | Plan, teams touched | Stakeholder table, partner asks, conflict resolution plan | `tpm-align` |
| `program-status-report` | You need a status update for leadership, partners, or the team | Plan, risk register, decision log | Three audience-specific updates with an evidence-based color | `tpm-run` |
| `success-metric-tree` | You need to define how success is measured | Goal, instrumentation status | Outcome metric with baseline, metric tree, counter-metrics | `tpm-frame` or `tpm-land` |
| `launch-readiness-review` | Before a go/no-go | Readiness status, test and eval results, risks | Criteria table, rollout and rollback plan, recommendation | `tpm-land` |
| `program-recovery` | The program is badly off plan | Baseline, actuals, change history | Diagnosis, re-baseline, options including stop | `tpm-run` |
| `program-retrospective` | After launch or a milestone | Metrics vs baseline, decision log | Lessons, owned actions, learnings routed to discovery | `pm-listen`, `pm-ground`, `pm-sense` |

## Safety

| Skill | Use when | Needs | Produces | Next |
|---|---|---|---|---|
| `public-safety-review` | Before publishing anything outside the organization | The artifact or repo | Risk rating, findings, redactions, go/no-go | Publish |

## Templates

All templates live in `templates/`. Copy one, fill it in, and keep the filled copy in your own workspace, not in this public repo.

| Template | What it is for | Filled by | Deliverable it produces |
|---|---|---|---|
| `source-card.md` | Recording one source with its sensitivity and allowed uses | `source-intake` | Source card |
| `product-taxonomy.yaml` | Product areas, capabilities, workflows, personas, glossary | `product-taxonomy-builder` | Product taxonomy |
| `evidence-items.csv` | One row per atomic piece of customer evidence | `customer-evidence-normalizer`, `pm-listen` | Evidence base |
| `painpoint-validation.md` | Scoring whether each painpoint is supported | `painpoint-validation` | Validated painpoint list |
| `opportunity-brief.md` | Problem, JTBD, MVP behaviors, guardrails, non-goals, risks, review questions | `opportunity-refinement`, `pm-listen` | Product brief / opportunity brief |
| `prototype.md` | The prototype's question, reviewer, states, data plan, and non-goals | `prototype-planning`, `pm-prototype` | Prototype contract |
| `public-release-checklist.md` | Final checks before anything is published | `public-safety-review` | Release sign-off |
| `program-charter.md` | Goal, metric and baseline, fixed variable, scope, decider, long-lead reviews | `tpm-frame` | Program charter |
| `success-metric-tree.md` | Outcome metric, branches, counter-metrics, baselines | `success-metric-tree` | Success metrics / OKR draft |
| `dependency-map.csv` | Tasks with owning team, estimate, dependencies, planned and forecast dates | `tpm-plan`, `delivery-decomposition` | Delivery plan and critical path |
| `risk-register.csv` | Risks with score, owner, trigger, response, resolve-by date | `risk-register` | Risk register |
| `stakeholder-map.csv` | Stakeholders with group, influence, decide or informed, goals, asks | `stakeholder-alignment`, `tpm-align` | Stakeholder map |
| `communication-plan.md` | Executive, partner-org, and working-team streams, decision forum, artifact locations | `tpm-align` | Communication plan |
| `decision-log.md` | One entry per material decision, with decider and options | `tpm-run`, `tradeoff-decision-brief` | Decision log |
| `tradeoff-decision-brief.md` | Options across date, scope, resources, quality, with a recommendation | `tradeoff-decision-brief` | Tradeoff / decision memo |
| `weekly-status.md` | Executive, partner, and team updates plus a consistency check | `program-status-report`, `tpm-run` | Weekly status report |
| `launch-readiness-checklist.md` | Every launch criterion as met, waived, or blocking, plus AI-specific gates | `launch-readiness-review`, `tpm-land` | Go/no-go checklist and rollout plan |
| `program-retrospective.md` | Results vs baseline, decisions reviewed, lessons, owned actions | `program-retrospective` | Retrospective / post-launch review |

## Scripts

Standard-library Python, run from the repo root. They draft; the skills judge.

| Script | What it does | Used by |
|---|---|---|
| `scripts/critical_path.py` | Critical path, total duration, slack, cross-team handoffs, inferred estimates on the path | `tpm-plan`, `delivery-decomposition` |
| `scripts/risk_register.py` | Scores and ranks risks, flags overdue and incomplete entries, lists accepted risks | `risk-register`, `tpm-run` |
| `scripts/status_report.py` | Drafts a status report with a suggested color from the plan and risk register | `program-status-report`, `tpm-run` |
| `scripts/validate_skills.py` | Static checks on every skill, plus checks that this catalog lists every skill and template | Contributors |

A synthetic example program to practice on lives in `examples/demodesk-program/`.
