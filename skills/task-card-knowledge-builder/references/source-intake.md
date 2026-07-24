# Source Intake And Disposition

Use this reference when harvesting source material or deciding whether a source row should become task-card work.

## Source Families

Accept source rows from:

- internal Q/A, chat, support, implementation, and product-owner conversations
- internal walkthroughs, video scripts, how-to guides, release notes, and wiki/help-center pages
- customer/account evidence when it reveals recurring user jobs or blocked workflows
- product code, route maps, UI components, backend services, action registries, permissions, and audit paths
- browser observations from an approved environment
- tool inventories and resource bindings for whatever assistant platform you use
- existing task cards, runtime exports, eval failures, and assistant regression results

Treat each source as evidence, not final text. Directional answers can seed questions and candidate cards, but they require stronger verification before becoming trusted guidance.

## Minimum Source Row

Capture:

- `source_id`
- `source_type`
- `source_path_or_channel`
- `title_or_question`
- `program_area`
- `product_area`
- `user_job_hypothesis`
- `source_summary`
- `evidence_strength`
- `sensitivity`
- `verification_needed`
- `candidate_disposition`

Use stable IDs so the same source row can be traced through candidate cards, verification artifacts, runtime cards, eval prompts, and future audits.

## Source Disposition

Classify each source row:

| Disposition | Meaning |
|---|---|
| `new_card_candidate` | Source describes a reusable user job not already covered. |
| `merge_into_existing_card` | Source strengthens or clarifies an existing card. |
| `verification_only_source` | Source helps verify labels, steps, caveats, or boundaries but does not create new user guidance. |
| `step_or_detail_source` | Source belongs inside another card as a step, caveat, prerequisite, or example. |
| `execution_gap_only` | Source reveals future tool/API/wrapper work but no new user-facing how-to. |
| `owner_review_needed` | Source involves sensitive wording, legal/security/package/roadmap claims, or unsupported workflow ambiguity. |
| `do_not_cardize` | Source is stale, duplicate, internal-only, unsupported, not a user job, or too weak. |

## Harvest Rules

- Preserve source lineage and evidence strength.
- Separate source text from normalized task-card wording.
- Prefer user jobs over feature labels.
- Keep source rows restricted unless separately reviewed.
- Do not broaden source scope just to fill a card.
- Do not use a weak source to override stronger code/browser/product-owner evidence.
