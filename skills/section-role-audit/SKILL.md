---
name: section-role-audit
description: Use on a finished persuasive document before it ships. For each section, forces a one-sentence statement of what it uniquely adds beyond the apex claim, and cuts anything that only restates. Also checks stance consistency (point of view versus proposal), and that the document's promised contents match what it actually contains.
---

# Section Role Audit

Use this skill on a document that is finished and too long, which is most finished documents.

A pyramid-principle document states its conclusion at the top and supports it below. The natural failure mode of that structure is that **expansion produces restatement**: each supporting section re-tells the apex at greater length before adding anything, because re-telling is how a writer warms up. The reader who read the top meets the same argument two or three more times and concludes the document is padded, which it is.

This audit finds that. It typically removes 15 to 25 percent of length with no information loss.

## Inputs

- a complete draft with a stated apex claim
- the intended reader and the realistic attention budget in seconds
- the document's mode: point of view, proposal, decision memo, or status
- optional: a stated contents or map line near the top

## Part 1 — The role test

For every section below the apex, answer in one sentence: **what does this add that the apex does not?**

Valid answers:

- **new evidence** — attribution, named sources, numbers not stated above
- **new argument** — a step of reasoning the apex asserts but does not justify
- **new mechanism** — how the thing works, where the apex only says that it works
- **new concession** — what was considered and rejected, what is not known, what would falsify this

Invalid answer: *"it explains the apex in more detail."* Detail is not a role. That section is restatement.

**Disposition rule.** A section with an invalid answer is cut down to its unique residue. Usually the residue exists and is small: one fact, one citation, one sentence. Extract it, attach it where it belongs, delete the rest.

Watch specifically for the pattern where a section's *heading* carries a valid role but its *body* restates before delivering it. The fix is to delete the body's lead and let the evidence carry the section, which also improves the visual hierarchy: heading states the claim, block beneath it substantiates.

## Part 2 — The mode test

Documents fail when they mix stances. Declare the mode, then check every sentence obeys it.

| Mode | Grammar it uses | Grammar that breaks it |
|---|---|---|
| **Point of view** | This is what I think is true, and why. No asks. | "The ask is...", "we should fund...", "one team, one quarter" |
| **Proposal** | A named party asks a named party for a named resource. | Diagnosis with no request attached |
| **Decision memo** | Options, criteria, recommendation, decision owner. | Advocacy for one option before the criteria are stated |

A point of view that contains an ask reads as a proposal written by someone who does not have standing to make it, which is worse than either document alone. The tell is a sentence where the reader cannot answer **who is asking whom for what.**

## Part 3 — The map test

If the document promises its own contents near the top, check the promise against the body:

- every promised item exists, in the promised order
- every substantial section is promised, or is deliberately a discovery
- the promise uses the same words the headings use, so a scanning reader can find them

A map line that has drifted from the body is worse than no map line, because it is a broken index.

## Part 4 — The attention test

Read only what fits the stated attention budget, starting at the top. Then answer, using nothing below the cut:

- what is the problem
- what is missing
- what is being claimed
- what would change if the claim is right

If any answer is unavailable, the apex is too slow or too long, and the fix is at the top, not below it. Compress the apex until all four are answerable, then re-run this test.

Track apex length across revisions. It grows every time the document is edited, because new material is easiest to insert where the writer is most confident. Cut it back each pass.

## Workflow

1. Confirm the apex claim, the reader, the attention budget, and the mode.
2. Run the role test on every section; record the disposition.
3. Extract the unique residue from every restating section before deleting anything.
4. Run the mode test; rewrite stance violations.
5. Run the map test; reconcile promise and body.
6. Run the attention test; compress the apex if it fails.
7. Re-check that the visual hierarchy still matches the new structure. Content promoted out of a subordinate block may now be carrying the section and should not still be styled as a footnote.
8. Report words removed and what was preserved.

## Output Contract

Return:

- apex claim, as restated by the auditor
- section id or heading
- role: `new evidence`, `new argument`, `new mechanism`, `new concession`, or `restatement`
- unique residue, if any
- disposition: `keep`, `compress to residue`, `merge into <section>`, `cut`
- mode violations, with the offending sentence
- map-to-body discrepancies
- attention-test result, with the four answers or the ones that failed
- apex length before and after
- total words removed
- anything deliberately kept despite being restatement, and the reason

## Hard Boundaries

- Do not cut a section because it is short, quiet, or unglamorous. Concessions and rejected alternatives are load-bearing to a senior reader and are usually the first thing an editor removes.
- Do not delete a restating section before extracting its unique residue.
- Do not use this skill to sand off voice. It removes duplicated argument, not personality.
- Do not add material. This is a subtractive pass; new claims have not been through validation.
- Do not run it on a draft that is still changing structurally. It is a finishing pass.
