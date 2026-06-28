# AI Assistant Flow Map Guide

Use this guide when the user asks for a flowchart, mind map, FigJam, Figma board, or interaction diagram for an AI assistant plan.

Start from the requirements plan. Do not diagram directly from vague chatbot prose.

## Recommended Views

### PM-Facing Workflow Flowchart

Use when the assistant supports a multi-step workflow with review gates, artifacts, exports, or handoffs.

Show:

- workflow stages in business language
- user prompt chips or suggested actions
- assistant-produced draft artifacts
- human or stakeholder review gates
- approval invalidation points when upstream artifacts change
- validation before handoff or execution
- final handoff boundary

### Executive Mind Map

Center node:

```text
[Assistant feature name]
```

Branches:

- user workflows
- conversation paths
- data and tools
- outputs and UI
- guardrails
- artifacts and gates
- gaps and decisions

### Conversation Path Swimlane

Suggested lanes:

- user
- assistant runtime
- agent configuration
- product tools and services
- product UI / output surface
- review, approval, and artifacts

Default sequence:

```text
trigger -> resolve scope -> clarify if needed -> retrieve evidence -> add context -> synthesize -> render output -> follow up -> handoff or exit artifact
```

Operational sequence:

```text
trigger -> resolve scope -> profile inputs -> review state -> draft artifact -> human review -> stakeholder gate -> generate output -> validate -> handoff
```

### Requirement Ownership Map

Use when deciding which team or layer owns each requirement.

Columns:

- assistant runtime
- agent configuration
- product backend/tools
- product UI
- output contract
- evaluation
- governance

### State And Gate Map

Show states:

- not started
- in progress
- needs clarification
- evidence retrieved
- draft generated
- needs review
- approved
- invalidated
- exported or handed off
- blocked

Use decision points for:

- ambiguous request
- insufficient evidence
- approval required
- upstream artifact changed
- export or mutation requested

## Visual Grammar

| Meaning | Treatment |
|---|---|
| User prompt or action chip | Rounded rectangle |
| Assistant step | Rounded rectangle with assistant label |
| Tool or data retrieval | Rectangle with source/tool label |
| Decision or gate | Diamond |
| Output artifact | Document/card shape |
| UI rendering surface | Framed panel |
| Gap or open decision | Dashed border |

Keep labels concise and readable. Do not let color carry meaning alone.

## Diagram Prompt Template

```text
Create a planning diagram titled "[feature name] AI assistant flow map".

Audience: PMs, designers, and engineers.
Purpose: align on conversation paths, data/tool dependencies, output surfaces, review gates, durable artifacts, and ownership layers.

Create these sections:
1. PM-facing workflow flowchart showing stages, user prompt chips, assistant artifacts, gates, validation, and handoff boundaries.
2. Executive mind map with branches for workflows, conversation paths, data/tools, outputs/UI, artifacts/gates, guardrails, and open decisions.
3. Conversation path swimlane using lanes: User, Assistant runtime, Agent configuration, Product tools/services, Product UI/output, Review and artifacts.
4. Requirement ownership map with columns: Assistant runtime, Agent configuration, Product backend/tools, Product UI, Output contract, Evaluation, Governance.
5. Legend explaining node types and status labels: verified, planned, gap, decision needed, draft, reviewed, approved, invalidated.

Use compact product-planning styling: white or light-gray canvas, subtle borders, clear connectors, readable labels, restrained color coding, and no decorative art.

Use these workflow paths:
[paste paths]

Use these prompt chips:
[paste prompt chips]

Use these requirements and ownership notes:
[paste layer map]

Use these guardrails:
[paste guardrails]

Use these open decisions:
[paste decisions]
```

