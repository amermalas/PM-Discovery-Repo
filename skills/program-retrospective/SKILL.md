---
name: program-retrospective
description: Use after a launch or milestone to measure results against the charter's baseline and turn lessons into owned changes. Compares outcome, adoption, quality, system, and delivery metrics to baseline, reviews the decision log for decisions that aged well or badly, groups lessons as process, people, and technical, and routes each lesson to where it will change something, including back into the discovery loop. Trigger on "retro", "post-launch review", "postmortem", "what did we learn", or "should we expand this".
---

# Program Retrospective

A retrospective is useful only if something changes because of it. This skill measures what happened, finds why, and sends each lesson to an owner and a place where it will be used: the next plan, a team process, a template in this repo, or the discovery loop.

## Inputs

- the charter, success metric tree, and baseline
- post-launch metrics for the agreed interval
- the plan, change history, risk register, and decision log
- input from the working teams and key stakeholders, collected before the meeting

## Workflow

1. **Measure against the baseline.** For each metric in the tree: baseline, target, actual, and whether the gap is explained. Report adoption, quality and guardrails, system health, and delivery health separately.
2. **Review the decision log.** Which decisions aged well, which did not, and what information would have changed them. Look especially at waivers, accepted risks, and scope cuts.
3. **Review the plan against actuals.** Where estimates were off, and whether the critical path was where the plan said.
4. **Collect lessons blamelessly,** grouped as:
   - **Process:** planning, cadence, change control, handoffs, tooling
   - **People:** ownership, communication, alignment, staffing
   - **Technical:** architecture, non-functional requirements, testing, evaluation, operations
5. **For each lesson, name what you would do differently,** in concrete terms, and why the thing that worked actually worked.
6. **Turn lessons into owned actions,** each with an owner, a date, and where it lands.
7. **Route learning back into discovery:**
   - user and customer insight to `pm-listen`
   - changed product behavior to `pm-ground` and `task-card-knowledge-builder`
   - market or competitive learning to `pm-sense`
   - a follow-on opportunity to `opportunity-selection`
8. **Recommend expand, iterate, or stop,** with the evidence.

## Output Contract

Return:

- metrics table: metric, baseline, target, actual, explained (yes or no)
- decisions reviewed: decision, outcome, what would have changed it
- estimate and critical-path accuracy
- lessons: category, what happened, why, what to do differently
- actions: owner, date, destination
- learnings routed to the discovery loop
- recommendation: expand, iterate, or stop, with evidence

## Hard Boundaries

- Do not assign individual blame.
- Do not move the target after seeing the actual. If the target was wrong, say so and set a new one for next time.
- Do not end with lessons that have no owner.
- Do not skip the retrospective because the launch went well; wins need explaining too.

## Sequencing

Run inside `tpm-land`, after the measurement interval agreed in the charter. Use `templates/program-retrospective.md`.
