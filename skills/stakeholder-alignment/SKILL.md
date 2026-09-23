---
name: stakeholder-alignment
description: Use to map a program's stakeholders and plan how to earn each one's commitment. Groups stakeholders as sponsors, partners, performers, and beneficiaries; records influence, interest, and decide-or-informed status; prepares 1:1 discovery questions; writes each partner's ask in terms of their own goals; and plans how to resolve blockers and conflicts. Use when a partner team won't prioritize a dependency, when priorities conflict, or before a kickoff.
---

# Stakeholder Alignment

Most cross-functional conflict is organizational, not personal. It comes from incentives: one team is measured on launches, another on reliability, another on revenue. Under most conflicts there is a shared goal that is not actually in conflict. This skill finds it and builds the ask around it.

## Inputs

- the charter and delivery plan, including cross-team dependencies
- the list of teams and functions touched
- known history: prior conflicts, competing commitments, capacity limits

## Workflow

1. **List stakeholders and group them:**
   - **Sponsors:** fund and own the outcome
   - **Partners:** teams you depend on but do not direct
   - **Performers:** the working teams
   - **Beneficiaries:** users and teams who gain
2. **Rate each on influence and interest,** and mark **decides** or **informed**. Only deciders go in the decision forum.
3. **Prepare 1:1 discovery questions** for each key stakeholder:
   - What are you measured on this half?
   - What would make this program a success for you? What would make it a problem?
   - What else is competing for your team's time?
   - What have past programs like this gotten wrong?
   - Who else should I talk to?
4. **Record their stated goals and objections,** labelled as stated or inferred.
5. **Write the ask for each partner** as dates, deliverables, and interface contracts, and state how it serves their goals. Different stakeholders respond to different reasons: customer pain, revenue, reduced operational load, a deprecation deadline, a regulatory requirement.
6. **Choose influence moves deliberately:**
   - give before asking (help with their priorities)
   - give a reason with every request, including a deadline and why
   - get small early commitments that build toward the full ask
   - bring data, especially customer or operational data, rather than opinion
   - show existing support from peers or leadership
   - tell a concrete before-and-after story with a real user when data alone does not land
7. **Plan conflict resolution.** Restate each side's actual goal. Look for the shared goal underneath. If you contributed to the conflict, say so and fix it. Resolve with peers first; escalate with quantified cost only when a critical-path commitment is still missing.
8. **Turn recurring conflicts into system fixes,** for example capacity-aware planning, a clearer ownership model, or an agreed intake process.
9. **Plan to scale yourself.** Set up rhythms, templates, and self-serve status so the program does not depend on the TPM being in every conversation.

## Output Contract

Return:

- stakeholder table: name or role, group, influence, interest, decides or informed, stated goals, objections, source (stated or inferred)
- 1:1 question list per key stakeholder
- partner asks: dates, deliverables, contracts, how it serves their goals
- influence plan per resistant stakeholder
- open conflicts: the two positions, the shared goal, proposed resolution, escalation path if unresolved
- system fixes proposed for recurring conflicts

## Hard Boundaries

- Do not record a stakeholder's goal or motive as fact without it being stated. Label inference.
- Do not use persuasion to conceal a cost or risk.
- Do not go around a stakeholder to their team or manager before talking to them directly.
- Do not put informed-only stakeholders into the decision forum.

## Sequencing

Run inside `tpm-align`. Revisit in `tpm-run` when a partner's commitment slips. Use `templates/stakeholder-map.csv` and `templates/communication-plan.md`.
