"""Build assets/languages.svg from the language stats of my public, non-fork repos."""
import json
import os
import urllib.request
from pathlib import Path

USER = "HelenArams"
SKIP = {"HTML", "CSS", "JavaScript", "Makefile", "Dockerfile", "Shell", "Jupyter Notebook"}
COLORS = {
    "Java": "#b07219", "Go": "#00ADD8", "Python": "#3572A5", "TypeScript": "#3178c6",
    "Kotlin": "#A97BFF", "Rust": "#dea584", "SQL": "#e38c00", "HCL": "#844FBA",
}
TOP = 6


def get(url: str):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req) as r:
        return json.load(r)


repos = get(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner")
totals: dict[str, int] = {}
for repo in repos:
    if repo["fork"] or repo["private"]:
        continue
    for lang, size in get(repo["languages_url"]).items():
        if lang not in SKIP:
            totals[lang] = totals.get(lang, 0) + size

ranked = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)[:TOP]
total = sum(v for _, v in ranked) or 1

W, BAR_Y, BAR_H = 420, 46, 10
rows = []
x = 20.0
segments = []
for lang, size in ranked:
    w = (W - 40) * size / total
    segments.append(f'<rect x="{x:.2f}" y="{BAR_Y}" width="{w:.2f}" height="{BAR_H}" fill="{COLORS.get(lang, "#8b949e")}"/>')
    x += w
for i, (lang, size) in enumerate(ranked):
    cx = 20 + (i % 2) * 200
    cy = 82 + (i // 2) * 24
    pct = 100 * size / total
    rows.append(
        f'<circle cx="{cx + 5}" cy="{cy - 4}" r="5" fill="{COLORS.get(lang, "#8b949e")}"/>'
        f'<text x="{cx + 16}" y="{cy}" class="t">{lang} <tspan class="p">{pct:.1f}%</tspan></text>'
    )
height = 82 + ((len(ranked) + 1) // 2) * 24
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" viewBox="0 0 {W} {height}" role="img" aria-label="Most used languages">
<style>
.h{{font:600 15px -apple-system,Segoe UI,Helvetica,Arial,sans-serif;fill:#2f80ed}}
.t{{font:400 12px -apple-system,Segoe UI,Helvetica,Arial,sans-serif;fill:#434d58}}
.p{{fill:#6e7781}}
@media (prefers-color-scheme: dark){{.t{{fill:#c9d1d9}}.p{{fill:#8b949e}}.h{{fill:#58a6ff}}}}
</style>
<text x="20" y="28" class="h">Most used languages</text>
<clipPath id="r"><rect x="20" y="{BAR_Y}" width="{W - 40}" height="{BAR_H}" rx="5"/></clipPath>
<g clip-path="url(#r)">{"".join(segments)}</g>
{"".join(rows)}
</svg>
'''
out = Path(__file__).resolve().parents[2] / "assets" / "languages.svg"
out.write_text(svg)
print(", ".join(f"{l} {100 * s / total:.1f}%" for l, s in ranked))
