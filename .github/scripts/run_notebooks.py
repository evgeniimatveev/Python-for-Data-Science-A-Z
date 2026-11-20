"""Execute every course notebook top to bottom and report pass/fail.

* a notebook that calls input() needs a human, so it is skipped
* each notebook runs with its own folder as working directory (like Jupyter),
  so relative paths such as ../data/... resolve
* plots use a non-interactive backend
"""
import glob
import os
import re
import sys
import time
import warnings

import nbformat
from nbclient import NotebookClient

warnings.filterwarnings("ignore")
os.environ["MPLBACKEND"] = "Agg"

TIMEOUT = 600
INPUT_CALL = re.compile(r"(?<![\w.])input\(")


def needs_input(nb):
    for cell in nb.cells:
        if cell.cell_type == "code":
            for line in cell.source.splitlines():
                if INPUT_CALL.search(line) and not line.lstrip().startswith("#"):
                    return True
    return False


rows = []
for path in sorted(glob.glob("0*/*.ipynb")):
    nb = nbformat.read(path, as_version=4)
    if needs_input(nb):
        print(f"SKIPPED {path} (asks for input)", flush=True)
        rows.append((path, "skipped", 0.0, ""))
        continue
    started = time.time()
    client = NotebookClient(nb, timeout=TIMEOUT, kernel_name="python3",
                            resources={"metadata": {"path": os.path.dirname(path)}})
    error = ""
    try:
        client.execute()
        status = "passed"
    except Exception as exc:  # noqa: BLE001 - report any failure
        status = "FAILED"
        lines = [l for l in str(exc).splitlines() if l.strip()]
        error = lines[-1][:300] if lines else type(exc).__name__
    secs = time.time() - started
    print(f"{status.upper():7s} {path} ({secs:.0f}s)" + (f"\n        {error}" if error else ""), flush=True)
    rows.append((path, status, secs, error))

n_pass = sum(1 for r in rows if r[1] == "passed")
n_fail = sum(1 for r in rows if r[1] == "FAILED")
n_skip = sum(1 for r in rows if r[1] == "skipped")
print(f"\nSummary: {n_pass} passed, {n_fail} failed, {n_skip} skipped, {len(rows)} total")

summary = os.environ.get("GITHUB_STEP_SUMMARY")
if summary:
    icon = {"passed": "✅", "FAILED": "❌", "skipped": "⏭️"}
    md = ["## Notebook run", "", f"**{n_pass} passed · {n_fail} failed · {n_skip} skipped** (of {len(rows)} notebooks)", "",
          "| Notebook | Result | Seconds |", "|---|:-:|--:|"]
    md += [f"| `{p}` | {icon[s]} {s} | {t:.0f} |" for p, s, t, _ in rows]
    errs = [(p, e) for p, s, _, e in rows if e]
    if errs:
        md += ["", "### Errors", ""] + [f"- `{p}`: {e}" for p, e in errs]
    with open(summary, "w", encoding="utf-8") as fh:
        fh.write("\n".join(md) + "\n")

sys.exit(1 if n_fail else 0)
