#!/usr/bin/env python3
"""Draft the factual core of a weekly program status from the plan and risk register.

Reads a dependency-map CSV (templates/dependency-map.csv) and a risk-register CSV
(templates/risk-register.csv) and prints a Markdown draft with:
  - a SUGGESTED status color and the reasons behind it
  - milestones (planned vs forecast)
  - critical-path slips and blocked tasks
  - tasks past their planned finish
  - top active risks and overdue risks

The color is a suggestion from rules, not a judgment. The TPM owns the call and
writes the business impact, options, and decisions needed (see the
program-status-report skill).

Rules:
  red    - a critical-path task is blocked or forecast to finish after its planned finish
  yellow - any other task is blocked or slipping, a risk is past its resolve-by date,
           or an active risk scores 15 or more
  green  - none of the above

Standard library only. Usage:
    python scripts/status_report.py --plan examples/demodesk-program/dependency-map.csv \\
        --risks examples/demodesk-program/risk-register.csv --today 2026-03-16
"""

import argparse
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from critical_path import PlanError, analyze, load_tasks  # noqa: E402
from risk_register import RegisterError, load_risks, parse_date, summarize  # noqa: E402

HIGH_RISK_SCORE = 15


def optional_date(value):
    value = (value or "").strip()
    if not value or value.upper().startswith("YYYY"):
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        return None


def build(plan_path, risks_path, today):
    tasks = load_tasks(plan_path)
    cp = analyze(tasks)
    critical = set(cp["critical_path"])

    rows = []
    for tid, t in tasks.items():
        r = t["row"]
        planned = optional_date(r.get("planned_finish"))
        forecast = optional_date(r.get("forecast_finish")) or planned
        status = (r.get("status") or "").strip().lower()
        slip = (forecast - planned).days if planned and forecast else 0
        rows.append(
            {
                "id": tid,
                "name": t["name"],
                "team": t["team"],
                "status": status,
                "milestone": (r.get("is_milestone") or "").strip().lower() in ("yes", "y", "true"),
                "planned": planned,
                "forecast": forecast,
                "slip": slip if status != "done" else 0,
                "critical": tid in critical,
                "past_due": bool(planned and planned < today and status != "done"),
            }
        )

    risk_summary = summarize(load_risks(risks_path, today)) if risks_path else None

    reasons_red, reasons_yellow = [], []
    for row in rows:
        label = f"{row['id']} {row['name']} [{row['team']}]"
        if row["status"] == "blocked":
            (reasons_red if row["critical"] else reasons_yellow).append(f"{label} is blocked")
        if row["slip"] > 0:
            where = "critical path" if row["critical"] else "off critical path"
            (reasons_red if row["critical"] else reasons_yellow).append(
                f"{label} forecast {row['slip']} days late ({where})"
            )
    if risk_summary:
        for r in risk_summary["overdue"]:
            reasons_yellow.append(f"risk {r['risk_id']} is past its resolve-by date ({r['resolve_by']})")
        for r in risk_summary["active_ranked"]:
            if r["score"] >= HIGH_RISK_SCORE:
                reasons_yellow.append(f"risk {r['risk_id']} scores {r['score']}")

    color = "red" if reasons_red else "yellow" if reasons_yellow else "green"
    return {
        "color": color,
        "reasons": reasons_red + reasons_yellow,
        "rows": rows,
        "critical_path": cp,
        "risks": risk_summary,
    }


def d(value):
    return value.isoformat() if value else "not set"


def render(report, today):
    out = [f"# Program Status Draft: {today.isoformat()}", ""]
    out.append(f"**Suggested status: {report['color'].upper()}** (rule-based; the TPM owns the call)")
    out.append("")
    if report["reasons"]:
        out.append("Why:")
        out += [f"- {r}" for r in report["reasons"]]
    else:
        out.append("Why: no blocked or slipping tasks, no overdue or high-scoring risks.")
    out.append("")
    out.append("To write before sending: headline, business impact (if yellow or red), options with a recommendation, decisions needed with decide-by dates.")
    out.append("")

    milestones = [r for r in report["rows"] if r["milestone"]]
    if milestones:
        out += ["## Milestones", "", "| Milestone | Owner team | Planned | Forecast | Status |", "|---|---|---|---|---|"]
        for m in milestones:
            out.append(f"| {m['id']} {m['name']} | {m['team']} | {d(m['planned'])} | {d(m['forecast'])} | {m['status'] or 'not set'} |")
        out.append("")

    cp = report["critical_path"]
    out += ["## Critical Path", "", f"Planned duration: {cp['total_duration_days']:g} working days", ""]
    out.append(" -> ".join(cp["critical_path"]))
    out.append("")

    past_due = [r for r in report["rows"] if r["past_due"]]
    if past_due:
        out += ["## Past Planned Finish", ""]
        out += [f"- {r['id']} {r['name']} [{r['team']}], planned {d(r['planned'])}, status {r['status']}" for r in past_due]
        out.append("")

    risks = report["risks"]
    if risks:
        out += ["## Top Active Risks", "", "| Risk | Score | Owner | Resolve by |", "|---|---|---|---|"]
        for r in risks["active_ranked"][:5]:
            out.append(f"| {r['risk_id']} {r['description']} | {r['score']} | {r['owner'] or 'MISSING'} | {r['resolve_by'] or 'MISSING'} |")
        out.append("")
        if risks["overdue"]:
            out += ["Overdue risks to convert to issues: " + ", ".join(r["risk_id"] for r in risks["overdue"]), ""]
    return "\n".join(out).rstrip()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--plan", required=True, help="dependency-map CSV")
    parser.add_argument("--risks", help="risk-register CSV")
    parser.add_argument("--today", help="YYYY-MM-DD (default: today)")
    args = parser.parse_args(argv)
    try:
        today = parse_date(args.today, "--today") if args.today else dt.date.today()
        report = build(args.plan, args.risks, today)
    except (PlanError, RegisterError, OSError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    print(render(report, today))
    return 0


if __name__ == "__main__":
    sys.exit(main())
