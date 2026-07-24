# PM Discovery Lab

A public, vendor-neutral skill package for AI-assisted product discovery. This is the published repository (`PM-Discovery-Repo`) — fork it as the seed for your own PM discovery workspace.

It is intentionally generic. It helps PMs build their own product context, taxonomy, evidence model, opportunity workflow, AI-assistant planning workflow, competitive-analysis workflow, task-card knowledge base, assistant-evaluation workflow, how-to video pipeline, and prototype system — without exposing private company knowledge. Every example in this repo is synthetic.

## What's inside

- `skills/` — fourteen discovery skills (listed below), each with a `SKILL.md` and a vendor-neutral `agents/agent.yaml` interface descriptor.
- `templates/` — fill-in templates for source cards, taxonomy, evidence, painpoint validation, opportunity briefs, and prototype contracts.
- `validation-plan.md` — how to test the skills against synthetic fixtures before you rely on them.
- `publication-manifest.md` — the public-safety policy and the review record for this repo.

## Skills

Core discovery-to-prototype chain:

- `source-intake`
- `product-taxonomy-builder`
- `customer-evidence-normalizer`
- `painpoint-validation`
- `opportunity-selection`
- `opportunity-refinement`
- `prototype-planning`
- `disposable-prototype-builder`
- `ai-assistant-flow-planner`

Extended workflows — competitive analysis, product knowledge, and assistant/video production:

- `competitive-analysis-intelligence` — evidence-grounded competitor scorecards, dossiers, and opportunities/threats reports for a program or feature.
- `task-card-knowledge-builder` — turn messy product knowledge into verified, agent-safe task cards with a source-to-verification-to-promotion lifecycle.
- `assistant-golden-evaluator` — regression-test any assistant/chatbot against a golden Q/A or scenario set and route defects to the right owner/layer.
- `how-to-video-producer` — turn a verified task card into a scripted, recorded, QA'd how-to video with optional voiceover.

Safety:

- `public-safety-review`

## Choosing a skill

If you're not sure where to start: run discovery first (`source-intake` through `opportunity-refinement`), then branch into whichever extended workflow matches the output you need — a prototype, an AI assistant plan, a competitive study, a verified knowledge base, an assistant regression test, or a how-to video. Each `SKILL.md` names the other skills it expects to run before or after it.

## Evidence discipline

Every skill in this repo that makes a claim about customer pain, priority, or competitive position follows the same evidence rule:

- **First-hand evidence** (account reports, transcripts, survey rows, support records, verified task cards, product/code checks, public competitor docs) is proof.
- **Governed lineage artifacts** (generated evidence tables, quote indices, source-lineage tables that point back to proof files) are usable but should stay traceable to the proof layer.
- **Context-only artifacts** (prior generated narrative studies, strategy memos, old assistant answers without lineage) are useful for framing and prior assumptions, never for validation claims on their own.

Use precise language to keep these separate: "Evidence shows..." only when backed by proof or lineage; "The prior study framed..." when using a generated study as context; "We infer..." when the connection is logical but not directly stated by a customer; "Open question..." when nothing has validated the claim yet. Do not let an AI-generated artifact become the source of truth for itself.

## Use it with any model

Each skill ships a vendor-neutral `agents/agent.yaml` describing its interface. Wire the skills into whichever agent or model you use; nothing here is tied to a specific AI vendor.

## Keep it public-safe

This package contains no customer data, internal taxonomy, company-specific source IDs, private UI assets, secrets, or production code — and it should stay that way. If you fork it and add your own sources, keep private material in a separate, non-public workspace. Run the `public-safety-review` skill before publishing anything derived from your own evidence; `publication-manifest.md` describes the full boundary.

## Contributing

Improvements to the skills and templates are welcome. See `CONTRIBUTING.md` for how to propose changes. To report sensitive content or a security issue, follow `SECURITY.md` — do not open a public issue for those.

## License

MIT — see `LICENSE`.
