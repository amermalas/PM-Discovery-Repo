# Launch Readiness Checklist

For each item, set the state to **met** (with evidence), **waived** (with owner, reason, follow-up date), **blocking** (with owner and what unblocks it), or **n/a** (with reason).

## Product And Quality

| Criterion | State | Evidence / reason | Owner | Follow-up |
|---|---|---|---|---|
| Acceptance criteria pass for in-scope stories | | | | |
| No open blocking defects | | | | |
| Non-functional targets met (latency, availability, scale) | | | | |
| Success metric and guardrails instrumented | | | | |

## Reviews And Sign-Offs

| Criterion | State | Evidence / reason | Owner | Follow-up |
|---|---|---|---|---|
| Security review | | | | |
| Privacy review | | | | |
| Legal / compliance review | | | | |
| Accessibility review | | | | |

## Rollout And Rollback

| Criterion | State | Evidence / reason | Owner | Follow-up |
|---|---|---|---|---|
| Rollout stages defined (internal, cohort, wider) | | | | |
| Promotion criteria between stages | | | | |
| Halt metric defined | | | | |
| Rollback mechanism tested | | | | |
| Rollback owner named | | | | |

## Operations

| Criterion | State | Evidence / reason | Owner | Follow-up |
|---|---|---|---|---|
| Monitoring and alerting live | | | | |
| On-call owner after launch | | | | |
| Runbook published | | | | |
| Launch-day lead and channel | | | | |

## Organizational Readiness

| Criterion | State | Evidence / reason | Owner | Follow-up |
|---|---|---|---|---|
| Support trained, runbook available | | | | |
| Documentation and release notes ready | | | | |
| Customer-facing teams briefed on date and limitations | | | | |

## AI Or Model-Backed Features

| Criterion | State | Evidence / reason | Owner | Follow-up |
|---|---|---|---|---|
| Golden-set evaluation at or above threshold | | | | |
| Prompt, model, and retrieval changes gated like deploys | | | | |
| Actions tiered by reversibility; irreversible actions need human approval | | | | |
| Policy limits enforced in code or configuration, not only in prompts | | | | |
| Mutating actions idempotent | | | | |
| Step, token, time, and spend budgets with defined at-limit behavior | | | | |
| "No relevant information" handled by escalation, not a guess | | | | |
| Escalation triggers and context handoff | | | | |
| Traces retained for replay | | | | |
| Honest success metric instrumented (resolution, not deflection) | | | | |

## Accepted Risks

| Risk ID | Accepted by | Expires | Still acceptable at launch |
|---|---|---|---|
| | | | |

## Decision

Go / go with conditions / no-go:

Conditions:

Decider:

Date:
