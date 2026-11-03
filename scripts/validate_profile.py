"""Offline checks for profile navigation, SVG assets and contribution snapshots."""

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []

for path in [*ROOT.glob("*.md"), *(ROOT / "docs").glob("*.md")]:
    body = path.read_text(encoding="utf-8")
    links = re.findall(r"!?\[[^\]\n]*\]\(\s*([^\s)]+)", body)
    links += re.findall(r"\b(?:src|srcset)=[\"']([^\"']+)[\"']", body)
    for link in links:
        target = urlsplit(link)
        if not target.scheme and not target.netloc and target.path:
            if not (path.parent / unquote(target.path)).exists():
                errors.append(f"{path.name}: missing link {link}")
    if any(marker in body for marker in (
        "membrane-engineering-knowledge-agent", "工程资料智能审查", "Engineering document review",
    )):
        errors.append(f"{path.name}: private resume project should not appear on the public profile")

for path in (ROOT / "assets").glob("*.svg"):
    root = ET.parse(path).getroot()
    if root.tag != "{http://www.w3.org/2000/svg}svg":
        errors.append(f"{path.name}: not an SVG")
    for node in root.iter():
        if node.tag.rsplit("}", 1)[-1] in {"script", "foreignObject", "image"}:
            errors.append(f"{path.name}: unexpected active or remote content")

record = json.loads((ROOT / "docs/contributions.json").read_text(encoding="utf-8"))
pulls = record["pull_requests"]
if len(pulls) != record["count"]:
    errors.append("contribution count differs from snapshot")
if len({(row["repository"], row["number"]) for row in pulls}) != len(pulls):
    errors.append("duplicate contribution")
for row in pulls:
    if (row["repository"].lower().startswith("xbzz1018/") or not row["merged_at"]
            or not re.fullmatch(r"[0-9a-f]{40}", row["merge_commit_sha"])):
        errors.append(f"invalid merged contribution: {row['number']}")
    if row["url"] != f"https://github.com/{row['repository']}/pull/{row['number']}":
        errors.append(f"invalid contribution URL: {row['number']}")

print(f"contributions={len(pulls)}; offline checks do not refresh upstream merge status")
if errors:
    raise SystemExit("\n".join(errors))
print("profile-validation-ok")
