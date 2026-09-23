# Program Strategy Checklist

A thinking checklist, not a form. For any program, pick the three to five aspects that dominate it and go deep on those. Filling in every row with the same weight is a sign the plan has not been thought about.

| Aspect | The question to answer | The mistake to avoid |
|---|---|---|
| Goals | What outcome, measured how, from what baseline? Is the reasoning written down for people who were not in the room? | Goal-setting that drags on until the team settles for a weak goal to finish the exercise. |
| Requirements | Are requirements debated with engineering for value and feasibility, prioritized into releases, with acceptance criteria? | Leaving non-functional requirements (latency, throughput, availability, scale, consistency) and security, privacy, compliance, accessibility until late. |
| Customers | Does the whole team share one picture of the target user? Is feedback collection (usability, demos, experiments) set up before launch? | Engineers designing for their own usage pattern; one large customer's request shaping a product meant to generalize. |
| Architecture | Does the design meet the business requirements and scale path? Has reuse been checked? Is there a prototype to de-risk the biggest unknown? | Resolving competing designs by authority instead of by data or clarified requirements. |
| Decision forum | Who influences execution? Who decides, and who is only informed? | Putting everyone who wants updates into the decision group. |
| Risk | Is there a register, reviewed on a cadence, with mitigations that reduce both probability and impact? | Treating risk as a one-time exercise, or letting the team become risk-averse instead of taking calculated risks. |
| Fixed variable | Which of date, scope, resources, quality is fixed, and who agreed it? | Discovering the fixed variable for the first time during a crisis. |
| Staffing | Does headcount and skill match the plan? Are estimates checked against historical data? | Staffing only engineering and forgetting design, analytics, docs, support, on-call. |
| Partner teams | Are dependent internal or external teams bought in at the level of dates and deliverables? Have vendor contracts started? | Telling another team how to do its work; starting procurement late. |
| Cross-functional partners | Are sales, support, marketing, legal, privacy, operations on a regular cadence? | Surprising a partner with a risk you could have shared (sharing risk is itself a mitigation). |
| Timeline | Are milestones aligned across all teams? Is the critical path named? | Spreading buffer evenly instead of on the critical path. |
| Communication | Is there a cadence for the working team, for cross-functional partners, and for executives, plus a status view anyone can check? | Status that only exists in meetings, so people have to ask. |

## Weighting by program shape

| | Short program (weeks) | Long program (years) |
|---|---|---|
| Fixed variable | Date; scope flexes from a pre-agreed cut list | Outcome; scope and plan re-set each quarter |
| Goals | One measurable outcome | Phase goals, re-validated |
| Governance | One decider, daily sync | Steering group, quarterly reviews |
| Architecture | Reuse what exists | Design for evolution; platform choices matter |
| Dominant risk | Execution | Strategic drift, sponsor or staff turnover, technology shifts |
| People | Who is available now | Hiring, retention, knowledge transfer |
