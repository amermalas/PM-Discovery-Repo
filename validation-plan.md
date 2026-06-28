# Public PM Discovery Lab Skill Testing Guide

## Purpose

This guide explains how to test the public PM Discovery Lab skills before publishing, sharing, or using them as a starter repo.

The goal is not to reproduce a private company workflow. The goal is to prove that the skills produce useful, traceable, public-safe product discovery artifacts from synthetic inputs.

## Test Rules

- Use synthetic product names, customer names, people, tickets, and source paths.
- Do not use private company examples, customer evidence, source IDs, screenshots, or local repo paths.
- Keep AI-generated summaries separate from source evidence.
- Mark every example fixture as synthetic.
- Run `public-safety-review` before considering the repo publishable.

## Synthetic Test Fixture

Use one simple fictional product area across tests:

```text
Product: DemoDesk
User group: operations managers
Workflow: daily intake review
Problem seed: managers receive too many incoming requests and cannot quickly tell which need action today.
Sources:
  SRC-001: synthetic interview note
  SRC-002: synthetic support ticket excerpt
  SRC-003: synthetic survey response
  SRC-004: synthetic product walkthrough note
```

Use placeholder paths such as:

```text
sources/synthetic/interview-note-001.md
sources/synthetic/support-ticket-001.md
```

## Static Checks

Run these checks before any workflow simulation:

1. Every skill has `SKILL.md`.
2. Every skill has YAML frontmatter with `name` and `description`.
3. Skill descriptions clearly say when to use the skill.
4. Each skill has an explicit output contract.
5. Hard boundaries are explicit.
6. The repo contains no real customer names, emails, domains, secrets, source IDs, private URLs, local absolute paths, or proprietary UI assets.

## Single-Skill Smoke Tests

### 1. Source Intake

Input: one synthetic interview note.

Expected output:

- source card
- sensitivity classification
- raw-versus-derived status
- allowed and unsafe uses
- extraction recommendations
- recommended downstream skills

Pass criteria:

- does not analyze the full opportunity too early
- does not treat raw feedback as public-safe by default
- produces a usable source card

### 2. Product Taxonomy Builder

Input: synthetic product walkthrough notes for DemoDesk.

Expected output:

- product areas
- capabilities
- workflows
- personas or roles
- glossary terms
- source references
- open taxonomy questions

Pass criteria:

- marks inferred taxonomy items clearly
- separates product structure from customer painpoints
- produces a structured table or YAML-ready output

### 3. Customer Evidence Normalizer

Input: three synthetic feedback snippets plus source cards.

Expected output:

- atomic evidence rows
- source references
- product area and workflow tags
- painpoint candidates
- confidence notes
- public-safe paraphrases

Pass criteria:

- splits distinct issues into separate rows
- does not rank priorities
- preserves source lineage

### 4. Painpoint Validation

Input: normalized evidence rows and two painpoint candidates.

Expected output:

- validation table
- evidence count
- source breadth
- recurrence
- severity
- confidence
- contradictions or caveats
- supported, under-evidenced, unclear, or not-supported status

Pass criteria:

- refuses unsupported claims
- does not hide contradictory evidence
- treats one strong quote as narrow evidence, not broad validation

### 5. Opportunity Selection

Input: validated painpoints and simple strategy criteria.

Expected output:

- candidate opportunities
- primary selected opportunity
- follow-on candidate
- not-now opportunities
- AI posture
- rationale and tradeoffs

Pass criteria:

- links every selected opportunity to validated painpoints
- does not call something an AI opportunity just because AI could be added
- states why secondary candidates were not selected now

### 6. Opportunity Refinement

Input: one selected opportunity.

Expected output:

- problem statement
- jobs to be done
- MVP behaviors
- guardrails
- non-goals
- assumptions
- risks
- design and engineering review questions
- prototype candidates

Pass criteria:

- keeps the first version narrow
- preserves evidence lineage
- separates MVP from later-phase ambition

### 7. Prototype Planning

Input: refined opportunity.

Expected output:

- prototype question
- target reviewer
- workflow stages
- screens and states
- synthetic data plan
- mocked behavior
- verification checklist
- `PROTOTYPE.md` content

Pass criteria:

- defines what the prototype must learn
- uses synthetic data by default
- marks mocked behavior and production non-goals

### 8. Disposable Prototype Builder

Input: prototype plan and synthetic fixtures.

Expected output:

- prototype file or change summary
- implemented screens and states
- synthetic fixture summary
- verification notes
- known limitations
- production non-goals

Pass criteria:

- does not use real data or private assets
- keeps the prototype disposable
- does not claim production readiness

### 9. AI Assistant Flow Planner

Input: a fictional assistant idea:

```text
DemoDesk Intake Assistant helps operations managers review new requests, identify missing information, draft follow-up questions, and prepare a daily review packet.
```

Expected output:

- workflow family
- top-down scope audit
- conversation paths
- interaction stories
- suggested prompt chips
- durable artifacts and gates
- ownership layer map
- tool and data source map
- scenario/evaluation plan
- optional flow-map prompt

Pass criteria:

- defines the workflow before prompt behavior
- separates chat output from durable artifacts
- includes human review gates before approvals, exports, or mutations
- marks missing tools, data, or UI as gaps instead of assuming they exist

### 10. Public Safety Review

Input: the full public repo folder.

Expected output:

- risk rating
- findings by severity
- required redactions
- synthetic replacements
- go/no-go recommendation

Pass criteria:

- flags any real customer data, local absolute path, email, domain, private URL, source ID, private ticket ID, or proprietary asset
- recommends no-go when sensitive material remains

## Chain Tests

### Chain A: Discovery To Opportunity

Run:

```text
source-intake -> product-taxonomy-builder -> customer-evidence-normalizer -> painpoint-validation -> opportunity-selection -> opportunity-refinement
```

Pass criteria:

- source lineage survives the chain
- unsupported painpoints do not become opportunities
- final opportunity is narrow enough for review

### Chain B: Opportunity To Prototype

Run:

```text
opportunity-refinement -> prototype-planning -> disposable-prototype-builder -> public-safety-review
```

Pass criteria:

- prototype question is explicit
- fixtures are synthetic
- mocked behavior is visible
- prototype is not presented as production code

### Chain C: AI Assistant Planning

Run:

```text
opportunity-refinement -> ai-assistant-flow-planner -> public-safety-review
```

Pass criteria:

- assistant requirements are workflow-based, not generic chatbot prose
- prompt chips are treated as user-facing affordances
- durable artifacts and gates are named
- missing data, tools, or UI are surfaced as gaps
- public-safety review finds no private platform names, ticket IDs, or internal paths

## Scoring

Use a 0-3 score for each dimension.

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Output shape | Missing | Partial | Usable with gaps | Matches expected structure |
| Source discipline | No lineage | Weak lineage | Mostly traceable | Clearly traceable |
| Safety | Unsafe | Needs major rewrite | Minor cleanup | Public-safe |
| PM usefulness | Not actionable | Heavy rewrite needed | Useful with review | Strong working artifact |
| Judgment checkpoints | None | Implied | Present but thin | Clear decision points |

Publish threshold:

- average score at least 2.4
- no safety score below 3 for the public repo itself
- no source discipline score below 2 for workflow outputs
- no private examples, paths, URLs, or customer names

