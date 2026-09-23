#!/usr/bin/env python3
"""Score, rank, and check a program risk register CSV.

Input columns (see templates/risk-register.csv):
    risk_id, description, category, probability, impact, owner, trigger,
    response, mitigation, resolve_by, status, ...

Score = probability x impact (each 1-5). Flags:
  - overdue: resolve_by is before --today and status is open or mitigating
    (convert these to issues with a written explanation)
  - missing owner, trigger, mitigation, or resolve_by
  - accepted risks (response = accept), which need a decider and an expiry

Standard library only. Usage:
    python scripts/risk_register.py examples/demodesk-program/risk-register.csv --today 2026-03-16
    python scripts/risk_register.py register.csv --today 2026-03-16 --json
"""

import argparse
import csv
import datetime as dt
import json
import sys

ACTIVE = {"open", "mitigating"}
REQUIRED = ("owner", "trigger", "mitigation", "resolve_by")


class RegisterError(Exception):
    pass


def parse_date(value, label):
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        raise RegisterError(f"{label}: '{value}' is not a YYYY-MM-DD date")


def score_1_to_5(value, label):
    try:
        n = int(value)
    except ValueError:
        raise RegisterError(f"{label}: '{value}' is not an integer 1-5")
    if not 1 <= n <= 5:
        raise RegisterError(f"{label}: {n} is outside 1-5")
    return n


def load_risks(path, today):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    risks = []
    for i, row in enumerate(rows, start=2):
        rid = (row.get("risk_id") or "").strip() or f"row {i}"
        p = score_1_to_5((row.get("probability") or "").strip(), f"{rid} probability")
        im = score_1_to_5((row.get("impact") or "").strip(), f"{rid} impact")
        status = (row.get("status") or "").strip().lower()
        resolve_by_raw = (row.get("resolve_by") or "").strip()
        if resolve_by_raw.upper().startswith("YYYY"):
            resolve_by_raw = ""  # unfilled template placeholder
        resolve_by = parse_date(resolve_by_raw, f"{rid} resolve_by") if resolve_by_raw else None
        missing = [k for k in REQUIRED if not (row.get(k) or "").strip()]
        if not resolve_by_raw and "resolve_by" not in missing:
            missing.append("resolve_by")
        risks.append(
            {
                "risk_id": rid,
                "description": (row.get("description") or "").strip(),
                "category": (row.get("category") or "").strip(),
                "owner": (row.get("owner") or "").strip(),
                "probability": p,
                "impact": im,
                "score": p * im,
                "status": status,
                "response": (row.get("response") or "").strip().lower(),
                "resolve_by": resolve_by.isoformat() if resolve_by else "",
                "overdue": bool(resolve_by and resolve_by < today and status in ACTIVE),
                "missing_fields": missing,
            }
        )
    return risks


def summarize(risks):
    active = [r for r in risks if r["status"] in ACTIVE]
    ranked = sorted(active, key=lambda r: (-r["score"], r["risk_id"]))
    return {
        "active_ranked": ranked,
        "overdue": [r for r in ranked if r["overdue"]],
        "incomplete": [r for r in risks if r["missing_fields"] and r["status"] != "closed"],
        "accepted": [r for r in active if r["response"] == "accept"],
        "issues": [r for r in risks if r["status"] == "issue"],
    }


def render_text(summary, today):
    out = [f"Risk register check as of {today.isoformat()}", ""]
    out.append("Active risks by score (probability x impact):")
    out.append("| Risk | Score | P | I | Owner | Resolve by | Flag |")
    out.append("|---|---|---|---|---|---|---|")
    for r in summary["active_ranked"]:
        flag = "OVERDUE: convert to issue" if r["overdue"] else ""
        out.append(
            f"| {r['risk_id']} {r['description']} | {r['score']} | {r['probability']} | "
            f"{r['impact']} | {r['owner'] or 'MISSING'} | {r['resolve_by'] or 'MISSING'} | {flag} |"
        )
    out.append("")
    if summary["overdue"]:
        out.append("Overdue risks (write an explanation and a new plan for each):")
        out += [f"  {r['risk_id']} (resolve by {r['resolve_by']}, owner {r['owner']})" for r in summary["overdue"]]
        out.append("")
    if summary["incomplete"]:
        out.append("Incomplete entries:")
        out += [f"  {r['risk_id']}: missing {', '.join(r['missing_fields'])}" for r in summary["incomplete"]]
        out.append("")
    if summary["accepted"]:
        out.append("Accepted risks (confirm decider, expiry, and controls in the decision log):")
        out += [f"  {r['risk_id']} (expires {r['resolve_by'] or 'MISSING'})" for r in summary["accepted"]]
        out.append("")
    if summary["issues"]:
        out.append("Already converted to issues: " + ", ".join(r["risk_id"] for r in summary["issues"]))
    return "\n".join(out).rstrip()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("csv_path", help="risk-register CSV")
    parser.add_argument("--today", help="YYYY-MM-DD (default: today)")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args(argv)
    try:
        today = parse_date(args.today, "--today") if args.today else dt.date.today()
        summary = summarize(load_risks(args.csv_path, today))
    except (RegisterError, OSError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    print(json.dumps(summary, indent=2) if args.json else render_text(summary, today))
    return 0


if __name__ == "__main__":
    sys.exit(main())
