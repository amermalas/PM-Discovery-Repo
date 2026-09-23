# Public PM Discovery Lab Skill Testing Guide

## Purpose

This guide explains how to test the public PM Discovery Lab skills before publishing, sharing, or using them as a starter repo.

The goal is not to reproduce a private company workflow. The goal is to prove that the skills produce useful, traceable, public-safe product discovery artifacts from synthetic inputs.

## Test Rules

- Use synthetic product names, customer names, people, tickets, and source paths.
- Do not use private company examples, customer evidence, source IDs, screenshots, or local repo paths.
- Keep AI-generated summaries separate from source evidence.
- Mark every example fixture as synthetic.
- Run `public-safety-review` before considering the repo publishable.

## Synthetic Test Fixture

Use one simple fictional product area across tests:

```text
Product: DemoDesk
User group: operations managers
Workflow: daily intake review
Problem seed: managers receive too many incoming requests and cannot quickly tell which need action today.
Sources:
  SRC-001: synthetic interview note
  SRC-002: synthetic support ticket excerpt
  SRC-003: synthetic survey response
  SRC-004: synthetic product walkthrough note
```

Use placeholder paths such as:

```text
sources/synthetic/interview-note-001.md
sources/synthetic/support-ticket-001.md
```

## Static Checks

Run these checks before any workflow simulation:

1. Every skill has `SKILL.md`.
2. Every skill has YAML frontmatter with `name` and `description`.
3. Skill descriptions clearly say when to use the skill.
4. Each skill has an explicit output contract.
5. Hard boundaries are explicit.
6. The repo contains no real customer names, emails, domains, secrets, source IDs, private URLs, local absolute paths, or proprietary UI assets.
7. `python scripts/validate_skills.py` passes (it automates checks 1-5 and part of 6).

## Single-Skill Smoke Tests

### 1. Source Intake

Input: one synthetic interview note.

Expected output:

- source card
- sensitivity classification
- raw-versus-derived status
- allowed and unsafe uses
- extraction recommendations
- recommended downstream skills

Pass criteria:

- does not analyze the full opportunity too early
- does not treat raw feedback as public-safe by default
- produces a usable source card

### 2. Product Taxonomy Builder

Input: synthetic product walkthrough notes for DemoDesk.

Expected output:

- product areas
- capabilities
- workflows
- personas or roles
- glossary terms
- source references
- open taxonomy questions

Pass criteria:

- marks inferred taxonomy items clearly
- separates product structure from customer painpoints
- produces a structured table or YAML-ready output

### 3. Customer Evidence Normalizer

Input: three synthetic feedback snippets plus source cards.

Expected output:

- atomic evidence rows
- source references
- product area and workflow tags
- painpoint candidates
- confidence notes
- public-safe paraphrases

Pass criteria:

- splits distinct issues into separate rows
- does not rank priorities
- preserves source lineage

### 4. Painpoint Validation

Input: normalized evidence rows and two painpoint candidates.

Expected output:

- validation table
- evidence count
- source breadth
- recurrence
- severity
- confidence
- contradictions or caveats
- supported, under-evidenced, unclear, or not-supported status

Pass criteria:

- refuses unsupported claims
- does not hide contradictory evidence
- treats one strong quote as narrow evidence, not broad validation

### 5. Opportunity Selection

Input: validated painpoints and simple strategy criteria.

Expected output:

- candidate opportunities
- primary selected opportunity
- follow-on candidate
- not-now opportunities
- AI posture
- rationale and tradeoffs

Pass criteria:

- links every selected opportunity to validated painpoints
- does not call something an AI opportunity just because AI could be added
- states why secondary candidates were not selected now

### 6. Opportunity Refinement

Input: one selected opportunity.

Expected output:

- problem statement
- jobs to be done
- MVP behaviors
- guardrails
- non-goals
- assumptions
- risks
- design and engineering review questions
- prototype candidates

Pass criteria:

- keeps the first version narrow
- preserves evidence lineage
- separates MVP from later-phase ambition

### 7. Prototype Planning

Input: refined opportunity.

Expected output:

- prototype question
- target reviewer
- workflow stages
- screens and states
- synthetic data plan
- mocked behavior
- verification checklist
- `PROTOTYPE.md` content

Pass criteria:

- defines what the prototype must learn
- uses synthetic data by default
- marks mocked behavior and production non-goals

### 8. Disposable Prototype Builder

Input: prototype plan and synthetic fixtures.

Expected output:

- prototype file or change summary
- implemented screens and states
- synthetic fixture summary
- verification notes
- known limitations
- production non-goals

Pass criteria:

- does not use real data or private assets
- keeps the prototype disposable
- does not claim production readiness

### 9. AI Assistant Flow Planner

Input: a fictional assistant idea:

```text
DemoDesk Intake Assistant helps operations managers review new requests, identify missing information, draft follow-up questions, and prepare a daily review packet.
```

Expected output:

- workflow family
- top-down scope audit
- conversation paths
- interaction stories
- suggested prompt chips
- durable artifacts and gates
- ownership layer map
- tool and data source map
- scenario/evaluation plan
- optional flow-map prompt

Pass criteria:

- defines the workflow before prompt behavior
- separates chat output from durable artifacts
- includes human review gates before approvals, exports, or mutations
- marks missing tools, data, or UI as gaps instead of assuming they exist

### 10. Competitive Analysis Intelligence

Input: a synthetic account-evidence corpus mentioning two fictional competitors (`RivalDesk`, `QueueWorks`) for the DemoDesk intake-review arena.

Expected output:

- competitor-to-arena landscape
- a capability rubric with 1-5 anchors
- DemoDesk's own scorecard, cited to synthetic source rows
- Tier-1 competitor dossiers with confidence levels
- opportunities and threats findings tied to specific evidence rows
- a validation note stating confidence limitations

Pass criteria:

- never produces a single global rank across arenas
- every score cites a source or is explicitly marked uncited/low-confidence
- separates real competitors from shadow-tooling/adjacent-system mentions
- keeps future-feature scoring in a clearly labelled separate delta view

### 11. Task Card Knowledge Builder

Input: three synthetic source rows (a support conversation excerpt, a release note, a UI observation) about the DemoDesk intake-review workflow.

Expected output:

- source disposition for each row
- a shape decision (`standalone_card`, `parent_card`, `step_or_detail`, `gap_only`, or `rejected_not_task_card`) for each candidate
- a verification-ladder classification for each candidate
- a tool-readiness bucket where relevant
- a promotion decision with rationale

Pass criteria:

- does not promote a candidate without a verification outcome
- never marks a card execution-ready without an explicit approval gate
- keeps assistant-internal wording out of user-facing card content

### 12. Assistant Golden Evaluator

Input: a synthetic 5-question golden set for a fictional "DemoDesk Intake Assistant," plus three captured (synthetic) assistant answers.

Expected output:

- normalized golden-set cases
- per-case score across the scoring dimensions
- defect classification by root cause
- a regression report using the report template

Pass criteria:

- does not default every failure to a prompt-tuning fix
- classifies at least one retrieval/source-scope defect distinctly from a prompt defect
- report leads with health status and blocker count

### 13. How-To Video Producer

Input: one verified synthetic task card (`create a DemoDesk intake review`) and a request for a how-to video.

Expected output:

- a video script matching the card's steps
- a quality-gate checklist applied to a (described, not real) recording
- a sync-QA timing map when voiceover is requested
- an output contract listing script, review notes, and QA status

Pass criteria:

- does not invent steps beyond the written card
- flags any placeholder/recorder-tool naming as a quality-gate failure
- keeps assistant-internal phrases out of narration

### 14. Generic Claim Falsification

Input: a short synthetic analysis whose claims are deliberately mixed — some grounded in the fixture product, some true of any company.

Expected output:

- claim list, each as a standalone sentence
- substitution targets used
- grade per claim: specific, conditional, generic
- disposition per claim
- specificity ratio
- whether the recommendation survives removal of the generic claims

Pass criteria:

- grades a well-written but category-level claim as generic
- does not accept evidence volume as a defence
- reports honestly when the recommendation collapses without the generic claims

### 15. Analog Peer Evidence

Input: two synthetic claims and a set of public-style peer material, including one unnamed benchmark.

Expected output:

- peer source rows with deployment context and publication tier
- transfer assumption per claim, stated as a sentence
- transfer grade per claim
- absence signals, labelled as signals
- search log

Pass criteria:

- refuses the unnamed benchmark as an analog_peer source
- grades transfer per claim rather than once for the set
- does not carry a weak transfer into a recommendation
- rewrites first-person-plural or state-asserting language about the target

### 16. Section Role Audit

Input: a synthetic two-page brief with a clear apex and two sections that restate it.

Expected output:

- role per section
- unique residue per restating section
- disposition per section
- mode violations
- map-to-body discrepancies
- attention-test result
- words removed

Pass criteria:

- identifies the restating sections
- extracts their unique residue before recommending a cut
- does not cut the concessions or rejected-alternatives section for being short
- adds no new claims

### 18. PM Sense

Input: a fictional product bucket (DemoDesk Intake) with two synthetic competitors (`RivalDesk`, `QueueWorks`) and three synthetic dated public-source snippets.

Expected output:

- a weekly signal digest limited to net-new items since a stated prior run
- each item carrying a factual summary, source, source date, and confidence
- an explicit "no meaningful change" case when no snippet is net-new

Pass criteria:

- never states a competitor claim without a source and date
- separates observed fact from interpretation
- checks for and extends a prior dossier rather than duplicating one

### 19. PM Listen

Input: three synthetic call excerpts (with account, date, speaker, role) about the DemoDesk intake-review workflow, including one contradictory data point.

Expected output:

- evidence rows tagged by product area, persona, workflow, observation type, and strength
- an interpreted-need line kept visibly separate from the verbatim excerpt
- the contradictory excerpt preserved, not smoothed away

Pass criteria:

- never treats a repeated account as multiple independent signals
- routes new/unclassified source material to `source-intake` rather than tagging it directly
- keeps every tag traceable to an account, date, and speaker

### 20. PM Ground

Input: a claim ("DemoDesk cannot export to PDF") plus one synthetic documentation page and one synthetic ticket that partially contradict it.

Expected output:

- a retrieval-based answer that inspects the page/ticket body, not just a title
- confirmed facts, conflicts, and inference listed separately
- an explicit "not found" case when no source addresses the claim

Pass criteria:

- never answers from unstated memory as though it were a current retrieval
- surfaces the page/ticket conflict rather than silently picking one source
- routes an existing-capability question to a task-card/taxonomy check before calling something a gap

### 21. PM Prototype

Input: a refined opportunity (from Opportunity Refinement) for the DemoDesk intake-review workflow.

Expected output:

- a prototype brief (user/job, starting state, happy path, critical states, non-goals, decision)
- a decision log entry format
- a Business Logic Companion with every row labeled Confirmed, PM decision, Inference, or Open question

Pass criteria:

- does not skip the Business Logic Companion when the prototype is described as delivery-track
- never treats an inferred rule as a confirmed one
- hands the actual interactive build off to `disposable-prototype-builder`/`prototype-planning` rather than reimplementing it

### 22. PM Commit

Input: a completed DemoDesk prototype brief, decision log, and Business Logic Companion from PM Prototype.

Expected output:

- an epic and a small set of independently valuable stories
- each story with rationale, linked evidence, acceptance criteria, edge/error states, and open questions
- explicit flags on anything inferred rather than confirmed

Pass criteria:

- does not invent an implementation detail not present in the prototype/decision log
- separates product requirements from implementation suggestions
- states the definition-of-ready checklist result before treating stories as filing-ready

### 23. Technical Writing Task-Card Bridge

Input: two synthetic documentation pages and three synthetic verified task cards for the DemoDesk intake-review workflow, with one intentional drift (a page describing a removed field).

Expected output:

- a drift audit with suggested review items, not declarative "this is wrong" statements
- doc-only candidates classified into a disposition bucket
- verified-card clusters with no doc equivalent flagged as a doc opportunity

Pass criteria:

- phrases every finding as a suggested check, never an assertion of error, unless the input explicitly supplies proof
- routes actual card promotion/verification back to `task-card-knowledge-builder` rather than doing it inline
- keeps reviewer/source notes separate from the user-facing draft body

### 24. Public Safety Review

Input: the full public repo folder.

Expected output:

- risk rating
- findings by severity
- required redactions
- synthetic replacements
- go/no-go recommendation

Pass criteria:

- flags any real customer data, local absolute path, email, domain, private URL, source ID, private ticket ID, or proprietary asset
- recommends no-go when sensitive material remains

## Delivery Loop Smoke Tests

Use the synthetic program in `examples/demodesk-program/` as the fixture: the DemoDesk Intake Assistant, answer-only mode first and acting mode second, with quality fixed in the charter.

### 25. TPM Frame

Input: a synthetic committed epic and decision log for the DemoDesk Intake Assistant, with no baseline measured and no named decider.

Expected output:

- a draft charter with problem, goal, metric, program type, fixed variable, execution model, scope in and out
- the missing baseline and missing decider flagged as blocking open questions
- long-lead reviews (security, privacy, legal) listed to start this week

Pass criteria:

- does not invent a baseline, sponsor, date, or budget
- names which of date, scope, resources, quality is fixed and what flexes first
- does not start detailed planning while the goal, metric, fixed variable, or decider is missing

### 26. TPM Plan

Input: the charter plus a synthetic component list for the assistant.

Expected output:

- workstreams with owning teams and interface contracts between them
- dependency rows with estimate sources
- critical path, milestones ending in demos, staffing check, seeded risk register

Pass criteria:

- decomposes by owning team, not only by component
- names the critical path explicitly
- marks inferred estimates as inferred
- includes non-engineering roles (docs, support, analytics) in the staffing check

### 27. TPM Align

Input: the plan plus a synthetic list of six teams, one of which has not committed to its critical-path task.

Expected output:

- stakeholder map grouped as sponsors, partners, performers, beneficiaries, with decides or informed
- partner asks written as dates, deliverables, and contracts tied to each team's goals
- three-stream communication plan
- the uncommitted team logged as a risk

Pass criteria:

- labels inferred stakeholder goals as inference
- keeps informed-only stakeholders out of the decision forum
- does not treat the program date as firm while a critical-path team is uncommitted

### 28. TPM Run

Input: the example dependency map and risk register, `--today 2026-03-16`, plus a synthetic executive request to add a new report to the first release.

Expected output:

- weekly status with a color, business impact, options, and decisions needed
- `R-01` converted to an issue
- the new request priced as a cost of yes with a cheaper alternative

Pass criteria:

- does not mark the program green
- does not say yes or no to the new request without the decider
- records decisions in the decision log format

### 29. Delivery Decomposition

Input: a synthetic design for the assistant: retrieval, orchestrator, chat surface, policy layer, action tools.

Expected output: ownership table, interface contracts, decision dependencies, dependency rows, critical path, phasing.

Pass criteria:

- treats the policy-threshold agreement as a decision dependency with an owner and decide-by date
- proposes an answer-only walking skeleton before the acting phase
- flags any component with no owner

### 30. Risk Register

Input: `examples/demodesk-program/risk-register.csv` and `--today 2026-03-16`.

Expected output: ranked risks, `R-01` flagged overdue, `R-05` listed as accepted with its expiry.

Pass criteria:

- every risk has a named person as owner
- the accepted risk has a decider, controls, and an expiry
- does not score risks to make status look green

### 31. Tradeoff Decision Brief

Input: `T-07` blocked, quality fixed, date requested to hold.

Expected output: the gap quantified, leverage checked, two or three options with consequences, a recommendation, a decider, and a decide-by date.

Pass criteria:

- never offers "work harder" as an option
- does not flex quality without the decider
- presents more than one option

### 32. Stakeholder Alignment

Input: a synthetic conflict: support operations wants strict action limits, sales wants broad automation.

Expected output: both positions, the shared goal underneath, a proposed resolution, and an escalation path.

Pass criteria:

- states each side's goal as stated or inferred
- proposes a system fix if the conflict is recurring
- does not go around a stakeholder before talking to them

### 33. Program Status Report

Input: the output of `scripts/status_report.py` on the example fixture.

Expected output: executive, partner-org, and working-team updates.

Pass criteria:

- the executive update leads with color and business impact, and offers options
- the color agrees with the risk register
- no customer names or individual performance details

### 34. Success Metric Tree

Input: the assistant's goal: operations managers spend less time triaging intake.

Expected output: one outcome metric with a baseline plan, four branches, counter-metric pairs.

Pass criteria:

- pairs deflection or throughput with a counter-metric
- does not set a target without a baseline, or labels it provisional
- does not use output measures as outcome metrics

### 35. Launch Readiness Review

Input: synthetic readiness status for answer-only mode with one missing rollback test and golden-set results just above threshold.

Expected output: criteria table, rollout plan, AI-specific checks, recommendation.

Pass criteria:

- the missing rollback test is blocking unless explicitly waived by the decider
- AI-specific checks include action tiering, idempotency, and budgets
- does not treat a passing golden set as proof of production behavior

### 36. Program Recovery

Input: a synthetic program at 30 percent of scope with 70 percent of budget spent and a long change history.

Expected output: variance summary, diagnosis by cause, options including stop, reset controls, early win.

Pass criteria:

- does not add people as the first move
- re-baselines with team estimates
- keeps stopping the program as a legitimate option

### 37. Program Retrospective

Input: synthetic post-launch metrics against the charter baseline and the example decision log.

Expected output: metrics table, decisions reviewed, lessons by process, people, technical, owned actions, routed learnings.

Pass criteria:

- does not move the target after seeing the result
- every lesson has an owner and a destination
- routes at least one learning back to `pm-listen`, `pm-ground`, or `pm-sense`

### 38. TPM Land

Input: the answer-only launch-readiness output and synthetic post-launch metrics.

Expected output: go/no-go decision with decider, staged rollout with rollback owner, results against baseline, expand/iterate/stop recommendation.

Pass criteria:

- no launch without a way to turn it off
- compares against the charter baseline, not a number chosen after the fact

## Script Tests

Run from the repo root:

```text
python scripts/validate_skills.py
python scripts/critical_path.py examples/demodesk-program/dependency-map.csv
python scripts/risk_register.py examples/demodesk-program/risk-register.csv --today 2026-03-16
python scripts/status_report.py --plan examples/demodesk-program/dependency-map.csv --risks examples/demodesk-program/risk-register.csv --today 2026-03-16
```

Pass criteria:

- the validator reports all static checks passed
- the critical path is `T-01 -> T-07 -> T-08 -> T-12`, 52 days, with `T-07` flagged as an inferred estimate
- `R-01` is flagged overdue and `R-05` is listed as accepted
- the status draft suggests red and names `T-07` as blocked on the critical path
- a dependency cycle, an unknown dependency, or a non-numeric duration produces a clear error and a non-zero exit

## Chain Tests

### Chain A: Discovery To Opportunity

Run:

```text
source-intake -> product-taxonomy-builder -> customer-evidence-normalizer -> painpoint-validation -> generic-claim-falsification -> opportunity-selection -> opportunity-refinement
```

Pass criteria:

- source lineage survives the chain
- unsupported painpoints do not become opportunities
- generic painpoints are stopped at the gate rather than becoming opportunities
- final opportunity is narrow enough for review

### Chain E: Outside-In Analysis

Run:

```text
source-intake -> analog-peer-evidence -> painpoint-validation -> generic-claim-falsification -> opportunity-selection -> section-role-audit
```

Pass criteria:

- peer sources are named, with deployment context and publication tier
- transfer grades are per claim and survive to the final artifact
- absence signals never become load-bearing
- the final document contains no assertion about the target's current internal state
- the finished brief passes the attention test at its stated budget

### Chain B: Opportunity To Prototype

Run:

```text
opportunity-refinement -> prototype-planning -> disposable-prototype-builder -> public-safety-review
```

Pass criteria:

- prototype question is explicit
- fixtures are synthetic
- mocked behavior is visible
- prototype is not presented as production code

### Chain C: AI Assistant Planning

Run:

```text
opportunity-refinement -> ai-assistant-flow-planner -> public-safety-review
```

Pass criteria:

- assistant requirements are workflow-based, not generic chatbot prose
- prompt chips are treated as user-facing affordances
- durable artifacts and gates are named
- missing data, tools, or UI are surfaced as gaps
- public-safety review finds no private platform names, ticket IDs, or internal paths

### Chain D: Knowledge To Assistant Regression

Run:

```text
task-card-knowledge-builder -> how-to-video-producer -> assistant-golden-evaluator -> public-safety-review
```

Pass criteria:

- the video script traces back to a verified (synthetic) task card, not invented steps
- tool-readiness and execution-allowed status stay explicit through the chain
- the golden-set evaluation classifies defects by root cause rather than defaulting to prompt tuning
- public-safety review finds no private platform names, ticket IDs, or internal paths

### Chain F: The Operating Loop

Run:

```text
pm-sense -> pm-listen -> pm-ground -> opportunity-refinement -> pm-prototype -> pm-commit -> public-safety-review
```

Pass criteria:

- the market signal (PM Sense) and the customer evidence (PM Listen) both stay traceable to a source and date
- the grounding step (PM Ground) confirms or contradicts the concept against synthetic documentation/tickets before it proceeds, and distinguishes a genuine gap from an existing-but-undiscovered capability
- the prototype's Business Logic Companion labels every row Confirmed, PM decision, Inference, or Open question
- the final epic/stories trace back through the decision log to the original customer evidence and market signal, not to an intermediate assumption
- public-safety review finds no private platform names, ticket IDs, or internal paths

### Chain G: The Delivery Loop

Run:

```text
tpm-frame -> tpm-plan -> tpm-align -> tpm-run -> tpm-land -> public-safety-review
```

Pass criteria:

- the charter's success metric and baseline are the ones measured in LAND
- the fixed variable in the charter is respected in every tradeoff, or changed only by the decider with a decision log entry
- every critical-path team has a written commitment before RUN starts
- every material change in RUN has a decision log entry
- LAND routes at least one learning back into the discovery loop

### Chain H: Discovery To Delivery

Run:

```text
pm-commit -> tpm-frame -> delivery-decomposition -> risk-register -> launch-readiness-review -> program-retrospective
```

Pass criteria:

- the charter's problem statement traces back to the discovery evidence and decision log, not to a new assumption
- the retrospective's routed learnings reach `pm-listen`, `pm-ground`, or `pm-sense`
- public-safety review finds no real team names, people, dates tied to real work, or internal paths

## Scoring

Use a 0-3 score for each dimension.

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Output shape | Missing | Partial | Usable with gaps | Matches expected structure |
| Source discipline | No lineage | Weak lineage | Mostly traceable | Clearly traceable |
| Safety | Unsafe | Needs major rewrite | Minor cleanup | Public-safe |
| PM usefulness | Not actionable | Heavy rewrite needed | Useful with review | Strong working artifact |
| Judgment checkpoints | None | Implied | Present but thin | Clear decision points |

Publish threshold:

- average score at least 2.4
- no safety score below 3 for the public repo itself
- no source discipline score below 2 for workflow outputs
- no private examples, paths, URLs, or customer names

