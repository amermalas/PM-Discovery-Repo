---
name: success-metric-tree
description: Use to define how a program's success will be measured before it launches. Builds a metric tree from one outcome metric down to adoption, quality and guardrail, system health, and delivery health metrics, marks leading and lagging indicators, sets baselines, and pairs gameable metrics with counter-metrics. Trigger on "how will we measure success", "define the success metric", "OKRs for this program", or "what should the dashboard show".
---

# Success Metric Tree

A program without a baseline cannot prove it worked. A program with one metric can be gamed. This skill builds a small tree: one outcome at the top, supporting metrics beneath it, and guardrails that catch the ways the outcome could be hit badly.

## Inputs

- the charter's goal and the discovery evidence behind it
- the users and workflows affected
- what is instrumented today

## Workflow

1. **Pick one outcome metric.** The business or user result the program exists for. If it cannot be measured yet, instrumenting it is a milestone.
2. **Measure the baseline now,** before launch. Record the value, the date, and how it was measured.
3. **Build the branches:**
   - **Adoption:** reach, activation, repeat use, feature adoption through to the outcome.
   - **Quality and guardrails:** what must not get worse (error rate, accuracy, complaints, trust or safety signals, cost per task).
   - **System health:** latency, traffic, errors, saturation; for AI features, evaluation scores against a golden set.
   - **Delivery health:** milestones on time, scope delivered, change-request count, team health pulse.
4. **Mark leading and lagging.** Leading indicators tell you early whether the outcome is likely; lagging ones confirm it.
5. **Pair gameable metrics.** Any metric that can be moved without improving the outcome gets a counter-metric. Examples: throughput paired with post-release defects; deflection paired with resolution verified by follow-up contact; engagement paired with task completion.
6. **Set targets and a review date.** Targets that are ambitious but realistic, with the reasoning written down for people who were not in the room.
7. **Choose the honest metric.** When two metrics could represent success, prefer the one that is harder to move without real improvement, and say why.

## Output Contract

Return:

- outcome metric, definition, baseline value, baseline date, measurement method
- tree: branch, metric, definition, leading or lagging, target, data source, owner
- counter-metric pairs, with the gaming behavior each prevents
- metrics not yet instrumented, as milestones
- review date and who reviews

## Hard Boundaries

- Do not set a target without a baseline, or label the target provisional.
- Do not change a metric's definition after launch without recording the change and the reason.
- Do not use output measures (lines of code, ticket counts, meetings held) as outcome metrics.

## Sequencing

Run in `tpm-frame` to set the charter's metric. Reuse in `tpm-land` and `program-retrospective` to measure results against the baseline. Use `templates/success-metric-tree.md`.
