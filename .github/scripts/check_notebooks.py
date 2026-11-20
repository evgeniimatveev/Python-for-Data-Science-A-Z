"""Static checks for every notebook in the repo (no notebook is executed).

* every .ipynb must be valid nbformat JSON
* if a notebook has metadata.widgets it must contain a "state" key,
  otherwise GitHub refuses to render it ("Invalid Notebook")
* every code cell must be valid Python syntax (magics such as %matplotlib / !pip are ignored);
  this also covers notebooks that cannot be executed in CI because they call input()
* no spaces in tracked file names
"""
import ast
import glob
import os
import subprocess
import sys
import warnings

import nbformat

warnings.filterwarnings("ignore")  # old notebooks lack cell ids; irrelevant here

notebooks = sorted(glob.glob("**/*.ipynb", recursive=True))
rows, failed = [], 0

for path in notebooks:
    problem = ""
    try:
        nb = nbformat.read(path, as_version=4)
        nbformat.validate(nb)
        widgets = nb.metadata.get("widgets")
        if widgets is not None and "state" not in widgets:
            problem = "metadata.widgets has no 'state' key (GitHub cannot render it)"
        if not problem:
            for n, cell in enumerate(nb.cells):
                if cell.cell_type != "code":
                    continue
                lines = [("" if l.lstrip().startswith(("%", "!")) else l) for l in cell.source.splitlines()]
                code = chr(10).join(lines)
                try:
                    ast.parse(code)
                except SyntaxError as err:
                    problem = f"syntax error in code cell {n}: {err.msg} (line {err.lineno})"
                    break
    except Exception as exc:  # noqa: BLE001 - report any failure
        problem = f"{type(exc).__name__}: {str(exc).splitlines()[0][:120]}"
    if problem:
        failed += 1
        print(f"FAIL  {path}: {problem}")
    rows.append((path, problem))

tracked = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout.splitlines()
spaced = [f for f in tracked if " " in os.path.basename(f)]
for f in spaced:
    failed += 1
    print(f"FAIL  file name contains a space: {f}")

print(f"Validated {len(notebooks)} notebooks, {failed} problem(s)")

summary = os.environ.get("GITHUB_STEP_SUMMARY")
if summary:
    ok = len(notebooks) - sum(1 for _, p in rows if p)
    lines = ["## Notebook check", "", f"**{ok} / {len(notebooks)} notebooks valid** · {len(spaced)} file names with spaces", ""]
    bad = [(p, m) for p, m in rows if m]
    if bad:
        lines += ["| Notebook | Problem |", "|---|---|"] + [f"| `{p}` | {m} |" for p, m in bad]
    with open(summary, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

sys.exit(1 if failed else 0)
