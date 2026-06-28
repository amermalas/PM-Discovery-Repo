# Contributing

This repo is meant to be forked, used, and improved. Contributions that make the skills and templates clearer, safer, or more useful are welcome.

## The one rule: keep it public-safe

This is a public repository. Everything in it must stay generic and synthetic.

- No customer data, real company or product names, real account names, or personal data.
- No internal source IDs, ticket IDs, private URLs, or local file paths.
- No secrets, tokens, or credentials.
- No proprietary UI assets or brand-specific style tokens.
- All examples must be clearly synthetic (the repo uses a fictional `DemoDesk` product for illustration).

Run the `public-safety-review` skill over your change before you open a pull request. `publication-manifest.md` describes the full boundary policy.

## How to propose a change

1. Fork the repository.
2. Create a branch for your change.
3. Make the change. Keep each skill self-contained: clear `name`/`description` frontmatter, an explicit output contract, and explicit hard boundaries.
4. Confirm your change adds no private or sensitive content (see above).
5. Open a pull request describing what the change improves and why.

## What good looks like

- Skills describe *when to use them*, *what they produce*, and *what they must not do*.
- Templates stay as fill-in structures, not filled-in examples.
- Changes preserve source lineage and the separation between raw evidence and AI-generated summaries.

## Reporting a problem

For a non-sensitive bug or suggestion, open an issue. If your report would itself expose sensitive content, follow `SECURITY.md` instead — do not put sensitive material in a public issue.
