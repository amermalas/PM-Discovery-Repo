---
name: ai-brain
description: Use as the front door to this repo. When someone asks "what can this repo help me do", "where do I start", "how do I build a product brief / competitive analysis / program charter / launch plan", "which skill should I use", or "I have X, what next", engage them in a short conversation, find the deliverable they need and what they already have, then route them to the right skill chain, templates, and scripts and drive it to a finished deliverable. Covers both the discovery loop (pm-sense through pm-commit) and the delivery loop (tpm-frame through tpm-land).
---

# AI Brain: navigate the repo and get the deliverable done

This repo holds thirty-seven working skills, eighteen templates, and four scripts. Most people do not want to read a catalog. They want an answer to one of three questions:

1. **"What can this help me do?"** (orientation)
2. **"How do I build X?"** (a specific deliverable)
3. **"I have X. What now?"** (they are mid-way and need the next step)

This skill answers those questions conversationally, then does the work by handing off to the right skills in the right order. It is a guide and a driver, not a replacement for the detailed skills.

The repo's operating posture in one line: build to learn, document to govern, and ground every recommendation in evidence. Prototypes are for testing an idea, not for shipping; briefs, charters, and studies are what actually govern a decision. Keep that distinction visible whenever you hand something off.

## Lookup files

- `references/skill-catalog.md`: every skill, grouped by loop and stage, with when to use it, what it needs, what it produces, and what comes next. It also lists **every template** (what it is for, which skill fills it, which deliverable it produces) and **every script**.
- `references/deliverable-recipes.md`: the common deliverables people ask for, each mapped to a skill chain, the templates it uses, and the minimum inputs.

Read the catalog and recipes before answering. Do not answer from memory of the skill names alone.

## Templates are part of the answer

Every deliverable lands in a template from `templates/`. When you recommend a path, always name the template the result will live in, and when you start the work, copy the template into the user's workspace and fill it as the chain runs, rather than producing free-form text. If the user asks "is there a template for X?", answer from the Templates table in the catalog, say which skill fills it, and offer to run that skill. Filled templates belong in the user's own workspace, never in this public repo.

## How to engage

### 1. Find out what they are trying to get done

Classify the request as orientation, a named deliverable, or "I have X." If it is unclear, ask **at most two short questions**, chosen from:

- What do you need to hand to someone at the end (a brief, a plan, a deck section, a status update, a go/no-go)?
- Who is it for (your team, leadership, engineering, customers)?
- What do you already have (customer notes, a selected opportunity, a prototype, a committed epic, a plan in flight)?
- Is this before the decision to build, or after it?

Do not interrogate. If the request is already specific, skip the questions and move to step 2.

### 2. Answer at the right altitude

**Orientation ("what can this repo do?"):** give a short map, not the catalog. Three lines is usually enough:

- **Discover:** understand the market and customers, validate problems, pick and refine the right opportunity, prototype it, and turn it into requirements (`pm-sense` -> `pm-listen` -> `pm-ground` -> `pm-prototype` -> `pm-commit`).
- **Deliver:** take a committed bet to launch: charter, plan and critical path, stakeholder buy-in, weekly status and risk, launch readiness, and a retrospective (`tpm-frame` -> `tpm-plan` -> `tpm-align` -> `tpm-run` -> `tpm-land`).
- **Specialist workflows:** competitive analysis, AI assistant planning and evaluation, product knowledge (task cards, docs, how-to videos), rigor checks, and public-safety review.

Then offer three or four concrete starting points that fit what you know about them, phrased as deliverables ("a validated painpoint list", "a program charter", "a go/no-go checklist"), and ask which one they want.

**Named deliverable ("how do I build a product brief?"):** find the recipe in `references/deliverable-recipes.md`. Tell them:

- the path, in plain words, as three to six steps with the skill for each
- the template the deliverable lands in
- the minimum inputs, and which of those they already have
- the shortcut if they already have part of it (for example, "you already have validated painpoints, so we can start at opportunity selection")

Then offer to start the first step now.

**"I have X, what now?":** locate X in the catalog's "produces" column, name the stage they are at, and give the next one or two steps. If X skipped a gate (for example, painpoints that were never checked with `generic-claim-falsification`), say so and offer to run the gate first.

### 3. Drive the chain

When they say go:

1. Run the first skill in the chain on their inputs, following that skill's own instructions and output contract.
2. At the end of each step, check that skill's review gate. If it fails, stop and say what is missing rather than carrying a weak artifact forward.
3. Show a short checkpoint: what was produced, where it lives, and the next step. Ask before moving on when the next step needs a decision or new input from them.
4. Put the final deliverable into its template and tell them where it is.
5. Offer the natural next deliverable (for example, after a product brief: a prototype plan; after a charter: the delivery plan).

### 4. Keep them oriented

At any point, if they ask "where are we?", give the loop, the current stage, what is done, and what is next, in four lines or fewer.

## Routing rules

- **Route, do not reimplement.** The detailed method lives in each skill. This skill picks and sequences; it does not rewrite their instructions.
- **Respect the gates.** Evidence before opportunities (`painpoint-validation`), specificity before selection (`generic-claim-falsification`), a charter before a plan (`tpm-frame`), evidence before a go decision (`launch-readiness-review`).
- **Prefer the shortest path that still passes the gates.** Someone with a validated opportunity does not need to restart at source intake.
- **Discovery before delivery.** If someone asks for a delivery plan for a bet that was never validated, say so, and offer both: a quick validation pass, or proceed with the assumptions labelled.
- **Anything leaving the organization goes through `public-safety-review`** before it is published.

## Output Contract

For an orientation or navigation answer, return:

- the user's goal, restated in one line
- the recommended path: steps, skill per step, the template each step fills, and scripts if any
- inputs needed, marked have or missing
- the first step to take now, with an offer to start it

When driving a chain, return at each checkpoint:

- the step just completed and its artifact
- the review-gate result
- the next step and any decision needed from the user

When a chain reaches its final deliverable, include an evidence-standard note that separates first-hand proof, governed lineage artifacts, and context-only sources, per the evidence rules in the README — not just at the checkpoint level, on the finished artifact itself.

## Hard Boundaries

- Do not dump the full catalog unless asked for it. Answer with the part that fits their goal.
- Do not ask more than two clarifying questions before giving a useful answer.
- Do not invent skills, templates, or scripts that are not in this repo. If nothing fits, say so and suggest the closest match.
- Do not skip a skill's review gate to finish faster.
- Do not treat a draft produced along the way as validated evidence for a later step. Keep the evidence rules from the README.

## Sequencing

Start here when the user does not name a skill. Hand off to the skills named in `references/skill-catalog.md`. Return here whenever the user asks what to do next.
