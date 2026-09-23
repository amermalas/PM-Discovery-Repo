#!/usr/bin/env python3
"""Run the static checks from validation-plan.md across every skill in the repo.

Checks, per skill folder under skills/:
  1. SKILL.md exists
  2. YAML frontmatter has `name` and `description`, and `name` matches the folder
  3. the description says when to use the skill ("use" appears in it)
  4. an output section exists (a heading containing "Output")
  5. hard boundaries exist (a heading containing "Boundar" or "Guardrail")
  6. agents/agent.yaml exists with display_name, short_description, default_prompt

And across the whole repo (text files only):
  7. no email addresses, absolute local paths, or private-looking URLs

Exits non-zero if any check fails. Standard library only. Usage:
    python scripts/validate_skills.py
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXT_EXT = {".md", ".yaml", ".yml", ".csv", ".py", ".txt"}
UNSAFE = [
    ("email address", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
    ("absolute Windows path", re.compile(r"\b[A-Za-z]:\\(?:Users|Documents)\\")),
    ("absolute home path", re.compile(r"(?:/Users/|/home/)[A-Za-z0-9_.-]+/")),
    ("internal-looking URL", re.compile(r"https?://[^\s)]*(?:internal|intranet|corp|\.local)\b", re.I)),
]
ALLOWED_EMAIL = re.compile(r"noreply@", re.I)


def frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fields = {}
    for line in text[3:end].splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def check_skill(folder):
    problems = []
    skill_md = os.path.join(folder, "SKILL.md")
    name = os.path.basename(folder)
    if not os.path.isfile(skill_md):
        return [f"{name}: missing SKILL.md"]
    with open(skill_md, encoding="utf-8") as f:
        text = f.read()
    fm = frontmatter(text)
    if fm is None:
        problems.append(f"{name}: SKILL.md has no YAML frontmatter")
    else:
        if fm.get("name") != name:
            problems.append(f"{name}: frontmatter name '{fm.get('name')}' does not match folder")
        desc = fm.get("description", "")
        if not desc:
            problems.append(f"{name}: frontmatter has no description")
        elif "use" not in desc.lower():
            problems.append(f"{name}: description does not say when to use the skill")
    headings = [h.lower() for h in re.findall(r"^#{2,3}\s+(.+)$", text, re.M)]
    if not any("output" in h for h in headings):
        problems.append(f"{name}: no output section")
    if not any("boundar" in h or "guardrail" in h for h in headings):
        problems.append(f"{name}: no hard boundaries or guardrails section")
    agent = os.path.join(folder, "agents", "agent.yaml")
    if not os.path.isfile(agent):
        problems.append(f"{name}: missing agents/agent.yaml")
    else:
        with open(agent, encoding="utf-8") as f:
            ytext = f.read()
        for key in ("display_name", "short_description", "default_prompt"):
            if f"{key}:" not in ytext:
                problems.append(f"{name}: agent.yaml missing {key}")
    return problems


def scan_repo():
    problems = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in filenames:
            if os.path.splitext(fn)[1].lower() not in TEXT_EXT:
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, ROOT)
            if rel == os.path.join("scripts", "validate_skills.py"):
                continue
            with open(path, encoding="utf-8", errors="replace") as f:
                for lineno, line in enumerate(f, start=1):
                    for label, pattern in UNSAFE:
                        m = pattern.search(line)
                        if m and not (label == "email address" and ALLOWED_EMAIL.search(m.group(0))):
                            problems.append(f"{rel}:{lineno}: possible {label}: {m.group(0)}")
    return problems


def main():
    skills_dir = os.path.join(ROOT, "skills")
    folders = sorted(
        os.path.join(skills_dir, d)
        for d in os.listdir(skills_dir)
        if os.path.isdir(os.path.join(skills_dir, d))
    )
    problems = []
    for folder in folders:
        problems += check_skill(folder)
    problems += scan_repo()
    print(f"Checked {len(folders)} skills.")
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("All static checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
