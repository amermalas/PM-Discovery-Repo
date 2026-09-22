---
name: pm-ground
description: Use for Stage 3 (GROUND) of the 5-stage AI-enabled product management loop — grounding a new idea or fast answer in your product's actual current state via your documentation/ticketing systems and this repo's taxonomy/task-card knowledge before treating it as fact. Trigger on "ground this in the product", "what does the product already do for X", "check current behavior/state of X", or "is this already built". Distinguishes confirmed documentation from inference.
---

# PM Ground — Stage 3: Ground product work in existing product knowledge

Part of a 5-stage operating loop (SENSE -> LISTEN -> GROUND -> PROTOTYPE -> COMMIT) for using AI across the product management lifecycle, not just for one-off drafting. This stage uses your documentation and ticketing systems, plus this repo's own governed knowledge, as live source systems so new ideas account for existing behavior, decisions, dependencies, bugs, and active work — instead of being invented from memory.

## Objective

Before treating a concept as novel or a claim as fact, confirm what the product already does, has decided, or has in flight.

## Required inputs

- A working documentation/ticketing connector (external to this repo) when live page/ticket status is needed.
- This repo's own governed knowledge: product/program taxonomy, verified task cards, and prior product briefs — often faster and more precise than a fresh documentation search for "does this capability exist."

## What to do

1. Treat "ground this" as a retrieval instruction, not a memory lookup — memory alone is not evidence and may be stale.
2. Search documentation first for product behavior and process questions; search your ticketing system first for active work, bugs, blockers, ownership, and status.
3. Open and inspect the actual page or issue — do not rely on search snippets.
4. Before claiming something is a build gap, check this repo's taxonomy and task-card knowledge:
   - Route to `product-taxonomy-builder` when the product/program/feature boundary, alias, or workflow ownership is unclear.
   - Route to `task-card-knowledge-builder` when checking whether a capability is already documented. A documented existing capability usually means an enablement/discoverability gap, not a build gap.
5. Report page titles/links or ticket keys, last-updated context, confirmed facts, ambiguity, and inference — separately.

## Suggested memory instruction (for the connected AI assistant, not this repo)

> When I say "Ground this," search connected sources before answering. For product behavior or process, inspect relevant documentation pages. For bugs, ownership, status, blockers, or active work, inspect tickets and recent comments. Cite page titles/links and ticket keys. Separate confirmed facts, conflicting evidence, inference, and open questions. If no relevant source is found, say so.

## Outputs

- Faster orientation to an unfamiliar product area.
- An idea brief that identifies existing capabilities, constraints, dependencies, and prior decisions.
- An answer that clearly distinguishes confirmed documentation from synthesis or inference.

## Quick grounding checklist

- [ ] Did the assistant retrieve current sources in this session (not just recall)?
- [ ] Did it inspect the source body / issue details and recent comments, not just a snippet?
- [ ] Are claims linked to a page, issue, or call?
- [ ] Are conflicts, staleness, and uncertainty visible?
- [ ] Is the PM's interpretation clearly separate from source facts?

## Review gate

Claims cite current pages, issues, calls, or approved evidence — not memory.

## Related repo resources

- `product-taxonomy-builder`, `task-card-knowledge-builder`.
- Your own theme-to-task-card crosswalk, if you maintain one, for existing-capability disposition.

## Guardrails

Do not let a visually convincing brief imply capabilities, reliability, or behavior the platform doesn't yet support. Flag every unconfirmed claim as inference or open question, not fact.
