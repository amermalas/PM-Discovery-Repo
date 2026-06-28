# PM Discovery Lab

A public, vendor-neutral skill package for AI-assisted product discovery. This is the published repository (`PM-Discovery-Repo`) — fork it as the seed for your own PM discovery workspace.

It is intentionally generic. It helps PMs build their own product context, taxonomy, evidence model, opportunity workflow, AI-assistant planning workflow, and prototype system — without exposing private company knowledge. Every example in this repo is synthetic.

## What's inside

- `skills/` — ten discovery skills (listed below), each with a `SKILL.md` and a vendor-neutral `agents/agent.yaml` interface descriptor.
- `templates/` — fill-in templates for source cards, taxonomy, evidence, painpoint validation, opportunity briefs, and prototype contracts.
- `validation-plan.md` — how to test the skills against synthetic fixtures before you rely on them.
- `publication-manifest.md` — the public-safety policy and the review record for this repo.

## Skills

- `source-intake`
- `product-taxonomy-builder`
- `customer-evidence-normalizer`
- `painpoint-validation`
- `opportunity-selection`
- `opportunity-refinement`
- `prototype-planning`
- `disposable-prototype-builder`
- `ai-assistant-flow-planner`
- `public-safety-review`

## Use it with any model

Each skill ships a vendor-neutral `agents/agent.yaml` describing its interface. Wire the skills into whichever agent or model you use; nothing here is tied to a specific AI vendor.

## Keep it public-safe

This package contains no customer data, internal taxonomy, company-specific source IDs, private UI assets, secrets, or production code — and it should stay that way. If you fork it and add your own sources, keep private material in a separate, non-public workspace. Run the `public-safety-review` skill before publishing anything derived from your own evidence; `publication-manifest.md` describes the full boundary.

## Contributing

Improvements to the skills and templates are welcome. See `CONTRIBUTING.md` for how to propose changes. To report sensitive content or a security issue, follow `SECURITY.md` — do not open a public issue for those.

## License

MIT — see `LICENSE`.
