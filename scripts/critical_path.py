#!/usr/bin/env python3
"""Compute the critical path of a program from a dependency-map CSV.

Input columns (see templates/dependency-map.csv):
    task_id, task_name, owner_team, duration_days, depends_on, estimate_source, ...
`depends_on` holds task ids separated by semicolons.

Output: the critical path, total duration, slack per task, cross-team edges on
the path, and the tasks whose estimates are inferred rather than team-provided.

Standard library only. Usage:
    python scripts/critical_path.py examples/demodesk-program/dependency-map.csv
    python scripts/critical_path.py plan.csv --json
"""

import argparse
import csv
import json
import sys


class PlanError(Exception):
    pass


def load_tasks(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    tasks = {}
    for i, row in enumerate(rows, start=2):
        tid = (row.get("task_id") or "").strip()
        if not tid:
            raise PlanError(f"row {i}: missing task_id")
        if tid in tasks:
            raise PlanError(f"row {i}: duplicate task_id {tid}")
        raw = (row.get("duration_days") or "").strip()
        try:
            duration = float(raw)
        except ValueError:
            raise PlanError(f"row {i} ({tid}): duration_days '{raw}' is not a number")
        if duration < 0:
            raise PlanError(f"row {i} ({tid}): duration_days cannot be negative")
        deps = [d.strip() for d in (row.get("depends_on") or "").split(";") if d.strip()]
        tasks[tid] = {
            "id": tid,
            "name": (row.get("task_name") or "").strip(),
            "team": (row.get("owner_team") or "").strip(),
            "duration": duration,
            "deps": deps,
            "estimate_source": (row.get("estimate_source") or "").strip(),
            "row": row,
        }
    for t in tasks.values():
        for d in t["deps"]:
            if d not in tasks:
                raise PlanError(f"{t['id']} depends on unknown task {d}")
    return tasks


def topological_order(tasks):
    indegree = {tid: len(t["deps"]) for tid, t in tasks.items()}
    dependents = {tid: [] for tid in tasks}
    for t in tasks.values():
        for d in t["deps"]:
            dependents[d].append(t["id"])
    ready = [tid for tid, n in indegree.items() if n == 0]
    order = []
    while ready:
        tid = ready.pop(0)
        order.append(tid)
        for nxt in dependents[tid]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                ready.append(nxt)
    if len(order) != len(tasks):
        stuck = sorted(tid for tid, n in indegree.items() if n > 0)
        raise PlanError("dependency cycle among: " + ", ".join(stuck))
    return order, dependents


def analyze(tasks):
    order, dependents = topological_order(tasks)
    es, ef = {}, {}
    for tid in order:
        t = tasks[tid]
        es[tid] = max((ef[d] for d in t["deps"]), default=0.0)
        ef[tid] = es[tid] + t["duration"]
    total = max(ef.values(), default=0.0)
    ls, lf = {}, {}
    for tid in reversed(order):
        lf[tid] = min((ls[n] for n in dependents[tid]), default=total)
        ls[tid] = lf[tid] - tasks[tid]["duration"]
    slack = {tid: round(ls[tid] - es[tid], 6) for tid in tasks}

    # Walk one critical chain from a zero-slack start to the zero-slack end.
    path = []
    current = next(
        (tid for tid in order if slack[tid] == 0 and not tasks[tid]["deps"]), None
    )
    while current is not None:
        path.append(current)
        current = next(
            (
                n
                for n in dependents[current]
                if slack[n] == 0 and es[n] == ef[current]
            ),
            None,
        )

    cross_team = [
        (a, b)
        for a, b in zip(path, path[1:])
        if tasks[a]["team"] and tasks[a]["team"] != tasks[b]["team"]
    ]
    inferred = [
        tid for tid in path if tasks[tid]["estimate_source"].lower() != "team-provided"
    ]
    return {
        "total_duration_days": total,
        "critical_path": path,
        "cross_team_edges_on_path": cross_team,
        "inferred_estimates_on_path": inferred,
        "tasks": {
            tid: {
                "name": tasks[tid]["name"],
                "team": tasks[tid]["team"],
                "duration": tasks[tid]["duration"],
                "earliest_start": es[tid],
                "earliest_finish": ef[tid],
                "latest_finish": lf[tid],
                "slack": slack[tid],
                "critical": slack[tid] == 0,
            }
            for tid in order
        },
    }


def fmt(n):
    return str(int(n)) if float(n).is_integer() else f"{n:.1f}"


def render_text(result):
    tasks = result["tasks"]
    lines = [f"Total duration: {fmt(result['total_duration_days'])} days", "", "Critical path:"]
    for tid in result["critical_path"]:
        t = tasks[tid]
        lines.append(f"  {tid}  {t['name']}  [{t['team']}]  {fmt(t['duration'])}d")
    lines.append("")
    if result["cross_team_edges_on_path"]:
        lines.append("Cross-team handoffs on the critical path (agree these contracts early):")
        for a, b in result["cross_team_edges_on_path"]:
            lines.append(f"  {a} [{tasks[a]['team']}] -> {b} [{tasks[b]['team']}]")
        lines.append("")
    if result["inferred_estimates_on_path"]:
        lines.append("Critical-path estimates not yet team-provided (confirm before baselining):")
        lines.append("  " + ", ".join(result["inferred_estimates_on_path"]))
        lines.append("")
    lines.append("Slack by task (days):")
    for tid, t in sorted(tasks.items(), key=lambda kv: (kv[1]["slack"], kv[0])):
        mark = "  CRITICAL" if t["critical"] else ""
        lines.append(f"  {tid}  slack {fmt(t['slack'])}{mark}")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("csv_path", help="dependency-map CSV")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args(argv)
    try:
        result = analyze(load_tasks(args.csv_path))
    except (PlanError, OSError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2) if args.json else render_text(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
