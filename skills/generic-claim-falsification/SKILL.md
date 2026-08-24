---
name: generic-claim-falsification
description: Use as a blocking gate between painpoint validation and opportunity selection. Tests whether a diagnosis is actually about the target organization or is a category description that would be equally true of any company. Substitutes unrelated organizations into every load-bearing claim and forces each survivor to be re-grounded, demoted, or cut.
---

# Generic Claim Falsification

Use this skill to find out whether you have a diagnosis or a genre.

Discovery work drifts toward category description. The failure is quiet: every claim is defensible, every claim is sourced, and the whole set would read as true of an organization you have never studied. That document tells a reader nothing they could not have written themselves, and it is the most common way a well-researched analysis fails.

The useful question is not "is this claim true?" It is **"is this claim about them?"**

## Inputs

- a draft thesis, painpoint set, or opportunity rationale
- the evidence rows supporting each claim
- the name of the target organization
- optional: the target's own public artifacts (job postings, filings, engineering blogs, product docs)

## The substitution test

For each load-bearing claim, replace the target organization with **three unrelated organizations from different industries and different sizes**. At least one should be an organization you know little about, so you cannot unconsciously supply supporting knowledge.

Then read the claim again and grade it:

| Grade | Condition | Required action |
|---|---|---|
| `specific` | Claim becomes false or unverifiable under substitution | Keep. This is your diagnosis. |
| `conditional` | Claim stays plausible under substitution, but the *evidence* attached to it is target-specific | Keep, and move the target-specific evidence into the claim itself so the specificity is visible to the reader. |
| `generic` | Claim stays true and interesting under substitution | Cut, or demote to background framing that is explicitly labelled as category context. |

A document composed entirely of `generic` claims has no diagnosis in it, whatever its evidence count.

## Workflow

1. Extract every load-bearing claim as a standalone sentence. A claim is load-bearing if removing it would change the recommendation.
2. Pick three substitution targets: different industry, different size, one unfamiliar.
3. Grade every claim `specific`, `conditional`, or `generic`.
4. For each `generic` claim, attempt re-grounding **once**: look for target-specific evidence that would move it to `specific` or `conditional`. Say where you looked.
5. Cut or demote every `generic` claim that re-grounding did not rescue.
6. Recompute the recommendation against the surviving claim set. If the recommendation does not change when the `generic` claims are removed, the recommendation was never resting on them and the document was longer than it needed to be. If it collapses, the analysis is not ready.
7. Report the ratio.

## Where target-specific evidence usually is

When first-party access is unavailable, these are the sources that most often move a claim from `generic` to `specific`. They are public and they are about the target specifically:

- the target's own hiring documents, especially scope statements and success criteria
- the target's public engineering or product writing
- the target's regulatory filings and investor commentary
- the target's published architecture, API surface, or developer docs
- what the target's own artifacts **do not** mention, treated as a low-graded signal only (see `customer-evidence-normalizer`)

If none of these were consulted before the analysis reached a recommendation, that is the finding.

## Output Contract

Return:

- claim id
- claim, as a standalone sentence
- substitution targets used
- grade: `specific`, `conditional`, or `generic`
- supporting evidence ids
- re-grounding attempted: yes or no
- where re-grounding was searched
- disposition: `kept`, `re-grounded`, `demoted to context`, `cut`
- specificity ratio: `specific` + `conditional` over total load-bearing claims
- does the recommendation survive removal of all `generic` claims: yes or no
- claims that could not be graded, and why

## Hard Boundaries

- Do not run this as a writing-quality review. A vividly written generic claim is still generic.
- Do not accept evidence volume as a defence. A hundred rows about the category grade `generic` together.
- Do not let a `generic` claim survive because it is true. Truth is not the test; attribution is.
- Do not silently rescue a claim by narrowing it until it is trivial.
- Do not run this after a direction is committed. It is a gate, not a retrospective. Re-opening research is cheap here and expensive later.

## Sequencing

Run after `painpoint-validation` and before `opportunity-selection`. If the specificity ratio is low, return to `source-intake` and `analog-peer-evidence` rather than proceeding.
