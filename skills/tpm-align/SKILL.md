---
name: tpm-align
description: Use for Stage 3 (ALIGN) of the 5-stage delivery loop, getting the people who can make or break the program committed to it. Maps stakeholders, runs 1:1 discovery to learn each one's goals and objections, holds a kickoff, sets the decision forum, and writes a communication plan for the working team, partner orgs, and executives. Trigger on "stakeholder map", "get buy-in for X", "kickoff meeting", "comms plan", "who needs to know", or "this team won't prioritize our dependency". Requires a plan from tpm-plan.
---

# TPM Align: Stage 3, earn commitment before execution

Part of a 5-stage delivery loop (FRAME -> PLAN -> ALIGN -> RUN -> LAND). A TPM leads by influence, not authority. This stage turns a plan into commitments from people who do not report to you.

Programs that stall in execution are usually stalled by priority, not by technical difficulty: a partner team with its own roadmap, a function that was never asked. This stage is where you find those blockers while they are still cheap.

## Objective

Every stakeholder who can block the program knows what is being asked of them, why it helps their own goals, and where decisions get made.

## Required inputs

- The charter (`tpm-frame`) and the baselined plan with its dependencies (`tpm-plan`).
- The list of teams and functions the plan touches, including partner teams and cross-functional partners (sales, support, marketing, legal, privacy, security, operations, finance).
- Any known history: prior conflicts, competing launches, teams already over capacity.

## What to do

1. **Build the stakeholder map.** Route to `stakeholder-alignment`. Group stakeholders as sponsors, partners (teams you depend on), performers (the working teams), and beneficiaries (users and teams who gain). For each, record influence, interest, and whether they **decide** or are **informed**.
2. **Hold 1:1s before any group meeting.** Learn each stakeholder's goals, their dislikes, their current commitments, and what "success" means to them. Different stakeholders turn different knobs: one cares about customer retention, another about revenue, another about operational load.
3. **Tie the ask to their goals.** For each partner team, write the ask at the level of dates, deliverables, and interface contracts, and state how it helps their own objectives. Do not tell another team how to do its work.
4. **Run a kickoff for motivation, not requirements.** Explain the goal, the metric, and the plan. Send questions in advance. Ask each stakeholder to come back with what they will contribute.
5. **Stand up the decision forum.** Name it, its members (deciders only), its cadence, and what it decides (scope changes, date changes, risk acceptance). Keep informed-only stakeholders out of it; give them the broadcast channel instead.
6. **Write the communication plan** with `templates/communication-plan.md`. Three streams:
   - **Upward** (executives): short, status color plus business impact, options when off track.
   - **Sideways** (partner orgs and the wider company): periodic updates so others can plan.
   - **Downward** (the working team): standups, working syncs, and a decision log so any decision can be traced.
   Plus a status view anyone can check without asking.
7. **Name the unresolved blockers.** If a partner will not commit, do not paper over it. Record it as a risk with an owner and take it to the decision forum with the cost of the delay quantified. Escalation is a last resort, and it lands better with numbers.

## Outputs

- Stakeholder map with decide/informed status and each stakeholder's stated goals.
- Written commitments from each partner team (dates, deliverables, contracts).
- Decision forum charter.
- Communication plan with owners and cadence per stream.
- Unresolved alignment blockers, logged as risks.

## Review gate

Every team on the critical path has committed in writing to its milestones and interfaces. If one has not, the program's date is an assumption, and the charter's sponsor must be told so.

## Copy-ready prompt

> Using the charter and the delivery plan, build a stakeholder map grouped as sponsors, partners, performers, and beneficiaries. For each, record influence, interest, decide or informed, and a 1:1 question list to learn their goals and objections. For each partner team on the critical path, draft the ask as dates, deliverables, and interface contracts, and state how it serves that team's own goals. Then draft a three-stream communication plan (executives, partner orgs, working team) with cadence, format, and owner. Mark every stakeholder goal as stated by them or inferred.

## Related repo resources

- Before: `tpm-plan`.
- Detail: `stakeholder-alignment`, `templates/stakeholder-map.csv`, `templates/communication-plan.md`.
- Next: `tpm-run`.

## Guardrails

- Do not record a stakeholder's goal as fact unless they stated it. Label inferred goals as inference.
- Do not use persuasion techniques to hide a real cost. Buy-in built on a hidden tradeoff breaks at the first slip.
- Do not escalate before trying peer resolution, and do not avoid escalation when a critical-path commitment is missing.
