# Example: DemoDesk Intake Assistant Program (synthetic)

Everything in this folder is synthetic. `DemoDesk` is the fictional product used throughout this repo. There are no real teams, people, dates, or customers here.

This fixture shows the delivery loop (FRAME -> PLAN -> ALIGN -> RUN -> LAND) picking up a bet that the discovery loop committed: an intake assistant that helps operations managers triage new requests. It gives the three scripts in `scripts/` something to run against.

## The program in one paragraph

Discovery committed an epic for a DemoDesk Intake Assistant with two modes: **answer-only** (answers questions about a request, escalates to a human when unsure) and **acting** (takes a limited set of actions, such as re-routing a request, within policy limits). The charter fixes **quality**: nothing ships below the golden-set threshold. Scope and date flex. Phasing ships answer-only first, because it retires the retrieval-quality unknown without waiting on the harder policy decision.

## Files

- `dependency-map.csv`: 12 tasks across six teams, with owners, estimates, dependencies, and planned vs forecast dates.
- `risk-register.csv`: five risks, including one past its resolve-by date and one deliberately accepted risk with an expiry.

## Try it

```text
python scripts/critical_path.py examples/demodesk-program/dependency-map.csv
python scripts/risk_register.py examples/demodesk-program/risk-register.csv --today 2026-03-16
python scripts/status_report.py --plan examples/demodesk-program/dependency-map.csv --risks examples/demodesk-program/risk-register.csv --today 2026-03-16
```

## What the fixture is built to show

1. **The critical path runs through a negotiation, not through engineering.** `T-07`, agreeing the auto-action policy thresholds between legal and support operations, sits on the critical path ahead of the backend policy layer. The retrieval pipeline, which looks like the hard part, has slack.
2. **An inferred estimate on the critical path.** `T-07` is marked `inferred`, so `critical_path.py` asks for it to be confirmed before baselining.
3. **Cross-team handoffs on the path** (Program -> Security & Compliance -> Backend) are where interface contracts and dates need agreeing early.
4. **A red status with a clear cause.** On 2026-03-16 `T-07` is blocked and the acting-mode milestone is forecast two weeks late. `status_report.py` suggests red and says why. The TPM still writes the business impact and the options.
5. **An overdue risk that should become an issue.** `R-01` passed its resolve-by date without resolution.
6. **An accepted risk with an expiry.** `R-05` launches answer-only mode without non-English support, with detection and human escalation as controls and a date when the acceptance must be revisited.

## A worked tradeoff (for the tradeoff-decision-brief smoke test)

With `T-07` blocked, the TPM brings options to the decider:

- **Option 1:** hold the whole launch until thresholds are agreed. Keeps one launch; delays answer-only value by about two weeks for no quality gain.
- **Option 2:** launch answer-only on its own date; acting mode follows once thresholds are agreed. Delivers value sooner; two launches to support.
- **Option 3:** ship acting mode with conservative interim thresholds that require human approval for every action. Keeps the date, but it is effectively answer-only plus a queue, and it adds support load.

Recommendation: Option 2, because quality is the fixed knob and answer-only does not depend on the blocked decision. Decider and decide-by date go in the decision log.
