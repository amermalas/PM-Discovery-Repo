# Public PM Discovery Lab Publication Manifest

## Status

Draft public-copy manifest. Run `public-safety-review` again before copying files to any public repository or linking from a public article.

## Public-Copy Candidate

These files are intended to be safe candidates for a future public repo after final review:

- `README.md`
- `publication-manifest.md`
- `validation-plan.md`
- `skills/`
- `templates/`

## Internal-Only Artifacts

Do not copy these workspace artifacts to a public repo as-is:

- validation plans that reference historical replay work
- simulation outputs and scorecards from private sources
- internal style kits or brand-specific prototype assets
- internal product taxonomy, customer evidence, or company knowledge exports
- generated prototypes that have not passed a public-safety review
- agent plans that include private platform names, private ticket IDs, local source paths, or customer-specific examples

## Required Before Public Copy

- Keep validation examples synthetic only.
- Keep source evidence out of runtime prototype fixtures.
- Keep prototype code clearly marked as disposable and non-production.
- Re-run public-safety review on the outgoing repo contents.
- Complete any approval path required for company-name usage, screenshots, or article links.

## Publication Decision Rule

If a file includes customer evidence, private source paths, internal taxonomy, historical replay references, internal validation notes, private platform architecture, or private tickets, it stays internal unless rewritten into a synthetic public example and reviewed again.

