---
name: analog-peer-evidence
description: Use when the target organization's internal evidence is unavailable and the analysis must reason from named peer deployments instead. Defines an analog_peer source family, per-claim transfer-assumption grading, a search order that prefers published reversals over published wins, and the language rules that keep outside-in claims honest.
---

# Analog Peer Evidence

Use this skill when you are analyzing an organization you cannot see inside.

This is the normal condition for pre-hire work, partner evaluation, category analysis, and any study of an organization that is not your own. The tempting move is to substitute category commentary for evidence and hope the reader does not notice the difference. The honest move is to name real peers, state what you are assuming when you carry their result across, and grade that assumption per claim.

An analysis that says **"here is what happened at three named organizations, here is why I think it transfers, and here is where I think it does not"** is stronger than one that asserts inside knowledge it does not have. Readers who work at the target will spot the fake immediately, and will not read the honest version as a weakness.

## Inputs

- the target organization
- the claim set that needs support
- public, first-party peer material: published outcomes, engineering writing, earnings commentary, conference talks, post-mortems
- the target's own public artifacts, for the specificity check

## The analog_peer source family

Add a source family distinct from first-party, named-third-party, and directional. An `analog_peer` source is:

- a **named** organization, not "a large retailer"
- with a **published, attributable** result or decision
- in a **comparable deployment context**, stated explicitly

Anonymous benchmarks and vendor-aggregated averages are not `analog_peer` sources. They are directional at best, and they are the material that makes an analysis read as generic. Prefer one named deployment over ten anonymized data points.

## Search order: reversals before wins

Search in this order. It is deliberately the opposite of what surfaces first.

1. **Reversals.** Organizations that publicly walked back a strategy, revised a target downward, or re-hired for something they had automated. Highest value by a wide margin: nobody publishes these for marketing reasons, so they are underreported, and they encode what actually failed rather than what was claimed.
2. **Self-implicating disclosures.** A vendor's own internal deployment measured on the metric that undercuts its pitch. An organization publishing its own defect rate. These are the hardest facts available in outside-in work, because the source had every incentive to publish something else.
3. **Methodology-transparent wins.** Published outcomes with a stated definition and measurement window.
4. **Methodology-opaque wins.** Published numbers with unpublished method. Usable, but cite the opacity in the same sentence as the number. A number that needs a caveat is still worth more than no number, provided the caveat travels with it.

Never present tier 4 as tier 3 by omitting the caveat.

## Transfer-assumption grading

The transfer assumption is what you are assuming when you carry a peer result to the target. **Grade it per claim, not once for the document.** A blanket disclaimer at the top is not a grading; it is an apology, and it lets weak transfers ride on the credibility of strong ones.

| Grade | Condition |
|---|---|
| `strong` | Same product type, same user population, same constraint structure. The mechanism that produced the peer result is present at the target for reasons independent of the peer. |
| `medium` | Two of the three match. Name the one that does not, and say what it would change. |
| `weak` | One or none match, or the transfer rests on the two organizations sharing an industry. Usable as illustration, never as support for a recommendation. |

Record the grade beside the claim where the reader sees it, not in an appendix.

## Absence as a signal

What a target's own artifacts **do not** say is admissible, and is often the most target-specific material available: a capability that never appears in a scope statement, a metric absent from every public description of a program, a role that is never hired for.

Two rules, both required:

- It is citable. Say exactly what was searched and what was absent.
- It can never be load-bearing. Absence is a **signal, not a finding**, and must be labelled that way in the artifact. Documents are silent for many reasons, most of them boring.

If a red-team pass cannot demote your absence claim to a signal without collapsing the argument, the argument was resting on it and needs different support.

## Language rules for outside-in claims

The failure that costs an outside analyst credibility is not being wrong. It is **sounding certain about decisions they have no way to know**. Three rules:

1. **Never assert current internal state.** Not "they measure X." Write "if X is measured the way the category measures it," or "I have found no public description of X." The conditional costs one clause and removes the only sentence a knowledgeable reader can dismiss you for.
2. **Frame recommendations as hypotheses under test.** Not "buy A, build B." Write "my working hypothesis: commoditize A, differentiate on B." This reads as more senior, not less decisive, because it shows the analyst knows which of their inputs are assumptions.
3. **Attribute knowledge to its owner.** Not "our systems." An outsider writes "the knowledge an organization's own operators hold about its own systems." Possessive pronouns claim standing you do not have.

## Workflow

1. Confirm that first-party access is genuinely unavailable, and record what was attempted. Analog peers are a substitute, not a shortcut.
2. Search in the reversal-first order. Log what was searched, not only what was found.
3. Build peer source cards with the `analog_peer` family, the deployment context, and the publication tier.
4. Attach peers to claims.
5. Grade the transfer assumption per claim.
6. Run the specificity check from `generic-claim-falsification`. Peer evidence alone does not make a claim target-specific; it makes it real. Target-specific material still has to come from the target's own artifacts.
7. Apply the language rules across the draft.
8. State the standing caveat once, in addition to the per-claim grades, never instead of them.

## Output Contract

Return:

- source id and `analog_peer` family tag
- peer organization name
- deployment context: product type, user population, constraint structure
- what was published, and by whom
- publication tier: `reversal`, `self-implicating`, `method-transparent`, `method-opaque`
- claim the peer supports
- transfer assumption, stated as a sentence
- transfer grade: `strong`, `medium`, `weak`
- what would break the transfer
- absence signals, each labelled `signal, not finding`, with what was searched
- search log: sources sought and not found
- standing caveat text

## Hard Boundaries

- Do not use an unnamed peer. "A major carrier" is not evidence.
- Do not carry a `weak` transfer into a recommendation.
- Do not grade transfer once for the whole document.
- Do not let absence become load-bearing.
- Do not write in the first-person plural about an organization you do not work for.
- Do not present peer evidence as if it were knowledge of the target. The reader must always be able to tell which is which.
