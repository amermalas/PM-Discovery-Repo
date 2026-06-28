---
name: ai-assistant-flow-planner
description: Use when a PM wants to turn an AI assistant, chatbot, copilot, or conversational workflow idea into a buildable product plan. Produces workflow families, conversation paths, interaction stories, prompt chips, durable artifacts and gates, ownership layers, tool/data needs, evaluation scenarios, and optional flow-map guidance without relying on private platform names or company-specific examples.
---

# AI Assistant Flow Planner

Use this skill to turn an AI assistant idea into a product plan that a PM, designer, and engineering team can review.

The goal is not to write a clever prompt. The goal is to define the workflow the assistant supports, the evidence it can safely use, the outputs it produces, and the human gates required before anything becomes durable or actionable.

## Inputs

- product brief, opportunity brief, research notes, or PM idea
- target user or workflow owner
- known source systems or data surfaces
- existing UI or prototype notes, if any
- known constraints, risks, or non-goals
- optional request for a Figma, FigJam, flowchart, or mind map

## Workflow

1. Name the workflow family.
   - Avoid using "chatbot" as the feature boundary.
   - Name the user job: review intake, prepare a briefing, triage an issue, map fields, draft a packet, compare records, or another concrete workflow.

2. Audit the top-down scope.
   - Business outcome.
   - User workflow outcome.
   - Assistant mission.
   - MVP boundary.
   - Out-of-scope boundary.
   - Workflow stages, tasks, deliverables, and review gates.

3. Break the workflow into conversation paths and interactions.
   - Use the default path shape: resolve scope, retrieve evidence, add context, synthesize, render evidence, support follow-ups.
   - For operational assistants, use: resolve scope, profile inputs, review state, draft artifact, human review, stakeholder gate, generate output, validate, hand off.
   - For each interaction, define entry point, required state, required inputs, clarifying questions, assistant action, output, durable artifact, gate behavior, fallback behavior, and exit state.

4. Capture PM-authored prompt chips.
   - Treat suggested prompts as user-facing affordances, similar to buttons in a conventional UI.
   - Do not treat prompt chips as system prompts.

5. Define durable artifacts and gates.
   - Chat history is not workflow state.
   - Name the artifact, owner, state, required evidence, review gate, approval effect, and invalidation rule.
   - AI-generated artifacts remain drafts until reviewed or approved.

6. Map ownership layers.
   - Assistant runtime: conversation, history, tool calls, traces, and session behavior.
   - Agent configuration: instructions, model, tool bindings, starter prompts, deployment, and evaluations.
   - Product backend: source retrieval, deterministic services, permissions, persistence, and mutations.
   - Product UI: chat surface, cards, tables, drawers, maps, timelines, review controls, exports, or handoffs.
   - Output contract: markdown, structured sections, typed artifacts, citations, explicit unknowns.
   - Evaluation and governance: scenario tests, approval rules, audit, access, and safety language.

7. Identify gaps.
   - Mark gaps as runtime, agent configuration, backend, UI, output contract, evaluation, governance, or PM decision.
   - Do not assume a tool, API, data surface, export, or UI exists unless the input says it exists.

8. Create a validation plan.
   - Include happy path, no-data, partial evidence, ambiguous prompt, malformed prompt, broad/high-cost prompt, follow-up question, source-grounding check, and output-quality check.

9. Add a visual plan when requested.
   - Read `references/flow-map-guide.md` for flowchart and FigJam/Figma guidance.
   - Build the diagram from the structured plan, not from vague assistant prose.

## Output Contract

Return:

- one-line feature framing
- workflow family
- primary user and workflow moment
- business and workflow outcomes
- top-down scope audit
- conversation paths
- interaction stories
- suggested prompt chips
- durable artifact and gate model
- ownership layer map
- tool and data source map
- output and rendering contract
- allowed and disallowed recommendations/actions
- scenario and evaluation plan
- open PM decisions
- optional flow-map prompt or diagram outline

For a full reusable skeleton, read `references/assistant-requirements-template.md`.

For visual planning, read `references/flow-map-guide.md`.

## Hard Boundaries

- Do not invent product behavior because the feature says "AI".
- Do not define prompt behavior before the workflow and evidence path are clear.
- Do not imply the assistant checked a source unless a tool or retrieval path exists.
- Do not collapse human review, approval, export, or mutation into a generic chat response.
- Do not treat AI-generated drafts as source truth.
- Do not include private company names, ticket IDs, internal platform names, customer names, local file paths, or proprietary examples in public outputs.

