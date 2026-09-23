# Deliverable Recipes

Match what the user asks for to a recipe. Each recipe gives the path, the template the result lands in, the minimum inputs, and the shortcut when they already have part of it. Phrase the path back in plain words; the skill names are for you.

If a request matches no recipe, find the closest one in `skill-catalog.md` by its "Produces" column, and say that it is the closest match.

---

## Discovery deliverables

### Product brief (opportunity brief)
Asked as: "product brief", "opportunity brief", "one-pager for this idea", "what should we build for X".
- **Path:** `source-intake` -> `customer-evidence-normalizer` -> `painpoint-validation` -> `generic-claim-falsification` -> `opportunity-selection` -> `opportunity-refinement`
- **Template:** `templates/opportunity-brief.md` (supporting: `source-card.md`, `evidence-items.csv`, `painpoint-validation.md`)
- **Minimum inputs:** customer evidence (interviews, tickets, surveys, call notes) about one product area.
- **Shortcuts:** already have call data -> start with `pm-listen`. Already have validated painpoints -> start at `generic-claim-falsification`. Already picked the opportunity -> go straight to `opportunity-refinement`.
- **Next deliverable:** prototype plan.

### Validated painpoint list
Asked as: "what are the real problems", "validate these pain points", "is this problem real".
- **Path:** `source-intake` -> `customer-evidence-normalizer` -> `painpoint-validation` -> `generic-claim-falsification`
- **Template:** `templates/painpoint-validation.md`, `templates/evidence-items.csv`
- **Minimum inputs:** raw feedback and a list of suspected problems.
- **Shortcut:** evidence already in rows -> start at `painpoint-validation`.

### Customer evidence summary
Asked as: "what are customers saying about X", "pull quotes", "voice of customer".
- **Path:** `pm-listen` (routes new sources through `source-intake` and `customer-evidence-normalizer`)
- **Template:** `templates/evidence-items.csv`
- **Minimum inputs:** calls or notes with account, date, speaker.

### Market or competitive brief
Asked as: "competitive analysis", "competitor scan", "what changed in the market", "how do we compare".
- **Quick scan:** `pm-sense` (weekly digest or monthly brief).
- **Full study:** `competitive-analysis-intelligence` (scorecards, dossiers, opportunities and threats).
- **Minimum inputs:** product bucket, competitor list, approved public sources; for the full study, your own feature map and account evidence.
- **Next deliverable:** feed findings into `opportunity-selection`.

### Outside-in analysis of an organization you can't see inside
Asked as: "analyze company X", "where could X use AI", "diagnose X from the outside".
- **Path:** `source-intake` -> `analog-peer-evidence` -> `painpoint-validation` -> `generic-claim-falsification` -> `opportunity-selection` -> `section-role-audit`
- **Minimum inputs:** the target's public artifacts; named peer deployments.

### Is this already built? / current-state check
Asked as: "does the product already do X", "ground this", "check current behavior".
- **Path:** `pm-ground` (uses `product-taxonomy-builder` and `task-card-knowledge-builder` outputs if they exist)
- **Minimum inputs:** the claim, plus access to docs and tickets.

### Prototype
Asked as: "clickable prototype", "demo", "mock this up".
- **Path:** `pm-prototype` -> `prototype-planning` -> `disposable-prototype-builder`
- **Template:** `templates/prototype.md`
- **Minimum inputs:** a refined opportunity (a product brief).
- **Shortcut:** no brief yet -> run the product brief recipe first, or proceed with assumptions labelled.

### PRD, epic, and stories
Asked as: "write the PRD", "requirements", "epic breakdown", "delivery tickets".
- **Path:** `pm-commit`
- **Minimum inputs:** prototype, decision log, Business Logic Companion.
- **Shortcut:** no prototype -> `opportunity-refinement` output can seed it, with open questions marked.
- **Next deliverable:** program charter.

### AI assistant or copilot plan
Asked as: "plan a chatbot", "design an assistant", "copilot requirements".
- **Path:** `opportunity-refinement` -> `ai-assistant-flow-planner` -> `assistant-golden-evaluator` (for the eval plan)
- **Minimum inputs:** the assistant idea and the workflow it supports.

---

## Delivery deliverables

### Program charter
Asked as: "kick off this program", "charter", "we committed, now what", "how do we get this shipped".
- **Path:** `tpm-frame` (+ `success-metric-tree` for the metric)
- **Template:** `templates/program-charter.md`, `templates/success-metric-tree.md`
- **Minimum inputs:** committed epic or product brief, a sponsor, known constraints.
- **Next deliverable:** delivery plan.

### Success metrics / OKRs
Asked as: "how will we measure success", "define the KPIs", "OKRs".
- **Path:** `success-metric-tree`
- **Template:** `templates/success-metric-tree.md`
- **Minimum inputs:** the goal and what is instrumented today.

### Delivery plan and critical path
Asked as: "program plan", "who builds what", "critical path", "4-month plan", "roadmap with dependencies".
- **Path:** `tpm-plan` -> `delivery-decomposition` -> `risk-register`
- **Templates:** `templates/dependency-map.csv`, `templates/risk-register.csv`
- **Script:** `python scripts/critical_path.py <dependency-map.csv>`
- **Minimum inputs:** charter, epic and stories, the teams available.
- **Shortcut:** no charter -> write one first with `tpm-frame`, or label the fixed variable and decider as assumptions.

### Stakeholder map and communication plan
Asked as: "stakeholder map", "get buy-in", "kickoff", "comms plan", "a team won't prioritize our work".
- **Path:** `tpm-align` -> `stakeholder-alignment`
- **Templates:** `templates/stakeholder-map.csv`, `templates/communication-plan.md`
- **Minimum inputs:** charter and plan, list of teams touched.

### Risk register
Asked as: "risk assessment", "what could go wrong", "pre-mortem", "we want to ship with a known issue".
- **Path:** `risk-register`
- **Template:** `templates/risk-register.csv`
- **Script:** `python scripts/risk_register.py <risk-register.csv> --today YYYY-MM-DD`
- **Minimum inputs:** the plan and dependency map.

### Weekly status / exec update
Asked as: "status report", "exec update", "what do I tell leadership".
- **Path:** `tpm-run` -> `program-status-report`
- **Template:** `templates/weekly-status.md`, with decisions in `templates/decision-log.md`
- **Script:** `python scripts/status_report.py --plan <dependency-map.csv> --risks <risk-register.csv> --today YYYY-MM-DD`
- **Minimum inputs:** baselined plan, risk register, this week's updates.

### Tradeoff or decision memo
Asked as: "we have half the time", "a team pulled out", "leadership added a must-have", "new requirement vs bugs".
- **Path:** `tradeoff-decision-brief` (then log it in the decision log)
- **Templates:** `templates/tradeoff-decision-brief.md`, `templates/decision-log.md`
- **Minimum inputs:** what changed, the fixed knob from the charter, estimates.

### Recovery plan for a troubled program
Asked as: "we're way behind", "most of the budget is gone", "take over this program", "restructure".
- **Path:** `program-recovery` -> `tradeoff-decision-brief` -> `tpm-plan` (re-baseline)
- **Minimum inputs:** original baseline if any, actuals, change history.

### Go/no-go and rollout plan
Asked as: "are we ready to ship", "launch checklist", "go/no-go", "rollout plan".
- **Path:** `tpm-land` -> `launch-readiness-review` (+ `assistant-golden-evaluator` for AI features)
- **Template:** `templates/launch-readiness-checklist.md`
- **Minimum inputs:** test results, readiness status from support/docs/ops/security/privacy, open risks.

### Retrospective / post-launch review
Asked as: "retro", "postmortem", "did it work", "should we expand this".
- **Path:** `program-retrospective`
- **Template:** `templates/program-retrospective.md`
- **Minimum inputs:** metrics against the charter baseline, the decision log.
- **Next:** route learnings to `pm-listen`, `pm-ground`, `pm-sense`.

---

## Knowledge and assistant deliverables

### Verified task cards / how-to knowledge base
- **Path:** `task-card-knowledge-builder`
- **Minimum inputs:** product Q/A, docs, or observed workflows.

### Documentation drift audit or doc page
- **Path:** `task-card-knowledge-builder` -> `technical-writing-taskcard-bridge`
- **Minimum inputs:** current doc pages, verified task cards.

### How-to video
- **Path:** `task-card-knowledge-builder` -> `how-to-video-producer`
- **Minimum inputs:** one verified task card.

### Assistant evaluation report
- **Path:** `assistant-golden-evaluator`
- **Minimum inputs:** golden Q/A or scenario set, captured assistant answers.

---

## Cross-cutting

### Tighten a document before it goes out
- **Path:** `section-role-audit` -> `public-safety-review` (if external)

### Publish anything outside the organization
- **Path:** `public-safety-review`
- **Template:** `templates/public-release-checklist.md`

### End to end: idea to launch
Asked as: "walk me through the whole thing", "from idea to shipped".
- **Path:** `pm-sense` -> `pm-listen` -> `pm-ground` -> `pm-prototype` -> `pm-commit` -> `tpm-frame` -> `tpm-plan` -> `tpm-align` -> `tpm-run` -> `tpm-land`
- **Approach:** find where the user already is, start there, and checkpoint at every stage's review gate.
