![Python for Data Science A-Z Banner](assets/banner.svg)

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white"/></a>
  <a href="https://jupyter.org/"><img src="https://img.shields.io/badge/Jupyter-notebooks-F37626?style=flat-square&logo=jupyter&logoColor=white"/></a>
  <a href="https://numpy.org/"><img src="https://img.shields.io/badge/NumPy-arrays-013243?style=flat-square&logo=numpy&logoColor=white"/></a>
  <a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/pandas-DataFrames-150458?style=flat-square&logo=pandas&logoColor=white"/></a>
  <a href="https://matplotlib.org/"><img src="https://img.shields.io/badge/Matplotlib-charts-11557c?style=flat-square"/></a>
  <a href="https://seaborn.pydata.org/"><img src="https://img.shields.io/badge/Seaborn-statistical_plots-4c9aa8?style=flat-square"/></a>
  <a href=".github/workflows/notebooks-check.yml"><img src="https://img.shields.io/badge/GitHub_Actions-notebook_check-2088FF?style=flat-square&logo=githubactions&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/notebooks-34-2ea44f?style=flat-square"/>
  <img src="https://img.shields.io/badge/sections-6-orange?style=flat-square"/>
</p>

A hands-on Python course for data work in **34 Jupyter notebooks**: from your first variable and `for` loop, through NumPy matrices and pandas DataFrames, to Seaborn charts on three real datasets (basketball statistics, world demographics, movie ratings). Each notebook is a lesson with commented code and a small mini project.

> *"Learn the tools by using them: 34 notebooks, 3,471 lines of annotated Python, three real datasets."*

---

## Course map

| # | Section | Notebooks | What you work on |
|:-:|---------|:---------:|------------------|
| 00 | [Quickstart](00-quickstart/) 🎯 | 1 + script | Course overview script, intro notebook |
| 01 | [Python Basics](01-python-basics/) 🧩 | 7 | Types, booleans, `if`, loops, indentation |
| 02 | [Python Fundamentals](02-python-fundamentals/) 🚀 | 7 | Tuples, functions, packages, slicing, NumPy arrays |
| 03 | [Matrices & Advanced Operations](03-matrices-and-advanced-operations/) 🧮 | 6 | Matrices, dictionaries, basketball data, Matplotlib |
| 04 | [DataFrames with pandas](04-dataframes-with-pandas/) 📊 | 8 | Import, filter, explore, rename, Seaborn intro |
| 05 | [Data Visualization](05-data-visualization/) 📈 | 6 | Joint plots, KDE, histograms on movie ratings |
| 06 | [Real-World Projects](06-real-world-projects/) 🛠️ | – | Basketball, demographics and movies, linked from sections 3–5 |

---

## Learning path

```
 Python Basics ──► Fundamentals ──► Matrices ──► DataFrames ──► Visualization ──► Projects
   types             tuples          NumPy        pandas         Seaborn          basketball
   if / loops        functions       matrices     filter         joint plots      demographics
   indentation       slicing         dicts        explore        KDE              movie ratings
                     packages        Matplotlib   rename         histograms
```

Each section builds on the previous one: the lists and loops from Section 1 feed the slicing and arrays of Section 2, arrays become the matrices of Section 3, matrices turn into DataFrames in Section 4, and DataFrames are what the Seaborn charts of Section 5 plot.

---

## Notebook tour

<details>
<summary>🧩 <b>Section 1 — Python Basics</b> (7 notebooks)</summary>

| Notebook | Topic |
|---|---|
| [`01-types-of-variables.ipynb`](01-python-basics/01-types-of-variables.ipynb) | Understanding the types of variables |
| [`02-boolean-variables-and-operators.ipynb`](01-python-basics/02-boolean-variables-and-operators.ipynb) | Boolean variables and logical operators, with a grade-checking mini project |
| [`03-the-if-statement.ipynb`](01-python-basics/03-the-if-statement.ipynb) | `if`, `elif`, `else`, with a random-number mini project |
| [`04-for-loop.ipynb`](01-python-basics/04-for-loop.ipynb) | `for` loops, with a word-counter mini project |
| [`05-while-loop.ipynb`](01-python-basics/05-while-loop.ipynb) | `while` loops, with a password-checker mini project |
| [`06-using-variables.ipynb`](01-python-basics/06-using-variables.ipynb) | Using variables in practice |
| [`07-code-indentation.ipynb`](01-python-basics/07-code-indentation.ipynb) | Code indentation in Python |

</details>

<details>
<summary>🚀 <b>Section 2 — Python Fundamentals</b> (7 notebooks)</summary>

| Notebook | Topic |
|---|---|
| [`01-tuples.ipynb`](02-python-fundamentals/01-tuples.ipynb) | Tuples and immutability |
| [`02-functions.ipynb`](02-python-fundamentals/02-functions.ipynb) | Defining and calling functions |
| [`03-packages.ipynb`](02-python-fundamentals/03-packages.ipynb) | Importing and installing packages (`numpy`, `math`, `requests`, `scrapy`) |
| [`04-slicing.ipynb`](02-python-fundamentals/04-slicing.ipynb) | Slicing sequences, with a message encoder/decoder mini project |
| [`05-square-brackets.ipynb`](02-python-fundamentals/05-square-brackets.ipynb) | Using `[]`, with a list-manager mini project |
| [`06-array-slicing.ipynb`](02-python-fundamentals/06-array-slicing.ipynb) | Slicing NumPy arrays |
| [`07-numpy-and-arrays.ipynb`](02-python-fundamentals/07-numpy-and-arrays.ipynb) | NumPy and arrays: creation, reshaping, broadcasting, matrix addition and multiplication |

</details>

<details>
<summary>🧮 <b>Section 3 — Matrices & Advanced Operations</b> (6 notebooks)</summary>

| Notebook | Topic |
|---|---|
| [`01-building-your-first-matrix.ipynb`](03-matrices-and-advanced-operations/01-building-your-first-matrix.ipynb) | Building your first matrix with NumPy |
| [`02-matrix-operations-with-numpy.ipynb`](03-matrices-and-advanced-operations/02-matrix-operations-with-numpy.ipynb) | Matrix operations with NumPy |
| [`03-understanding-dictionaries.ipynb`](03-matrices-and-advanced-operations/03-understanding-dictionaries.ipynb) | Dictionaries, with a student-grade management mini project |
| [`04-basketball-dataset.ipynb`](03-matrices-and-advanced-operations/04-basketball-dataset.ipynb) | Course project: basketball statistics as matrices |
| [`05-intro-to-matplotlib.ipynb`](03-matrices-and-advanced-operations/05-intro-to-matplotlib.ipynb) | Introduction to Matplotlib, with a performance-vs-salary mini project |
| [`06-advanced-matplotlib.ipynb`](03-matrices-and-advanced-operations/06-advanced-matplotlib.ipynb) | Advanced Matplotlib techniques |

</details>

<details>
<summary>📊 <b>Section 4 — DataFrames with pandas</b> (8 notebooks)</summary>

| Notebook | Topic |
|---|---|
| [`01-importing-data.ipynb`](04-dataframes-with-pandas/01-importing-data.ipynb) | Importing a CSV into a DataFrame |
| [`02-basic-dataframe-operations.ipynb`](04-dataframes-with-pandas/02-basic-dataframe-operations.ipynb) | Selecting columns and basic DataFrame operations |
| [`03-filtering-a-dataframe.ipynb`](04-dataframes-with-pandas/03-filtering-a-dataframe.ipynb) | Filtering rows with conditions |
| [`04-exploring-your-dataset.ipynb`](04-dataframes-with-pandas/04-exploring-your-dataset.ipynb) | Exploring a dataset: dimensions, summaries, patterns |
| [`05-renaming-columns.ipynb`](04-dataframes-with-pandas/05-renaming-columns.ipynb) | Renaming columns |
| [`06-at-and-iat.ipynb`](04-dataframes-with-pandas/06-at-and-iat.ipynb) | Accessing single elements with `.at()` and `.iat()` |
| [`07-intro-to-seaborn.ipynb`](04-dataframes-with-pandas/07-intro-to-seaborn.ipynb) | Introduction to Seaborn |
| [`08-advanced-seaborn.ipynb`](04-dataframes-with-pandas/08-advanced-seaborn.ipynb) | Advanced Seaborn: regression plots and beyond |

</details>

<details>
<summary>📈 <b>Section 5 — Data Visualization</b> (6 notebooks)</summary>

| Notebook | Topic |
|---|---|
| [`01-building-dashboards.ipynb`](05-data-visualization/01-building-dashboards.ipynb) | Finishing touches: assembling a dashboard of charts |
| [`02-intro-to-category-data.ipynb`](05-data-visualization/02-intro-to-category-data.ipynb) | The `category` data type |
| [`03-jointplot.ipynb`](05-data-visualization/03-jointplot.ipynb) | Joint plots: relationships and distributions |
| [`04-kdeplot.ipynb`](05-data-visualization/04-kdeplot.ipynb) | Kernel density estimation (KDE) plots |
| [`05-histograms.ipynb`](05-data-visualization/05-histograms.ipynb) | Histograms in Seaborn: visualizing distributions and layering them for comparison |
| [`06-stacked-histograms.ipynb`](05-data-visualization/06-stacked-histograms.ipynb) | Stacked histograms across categories |

</details>

---

## Featured: real datasets

| Dataset | Size | Used in |
|---------|------|---------|
| [`data/demographic-data.csv`](data/demographic-data.csv) | 195 countries × 5 columns: birth rate, internet users, income group | Section 4: importing, exploring |
| [`data/movie-ratings.csv`](data/movie-ratings.csv) | 559 films, 7 genres, 2007–2011: critic and audience ratings, budget | Section 5: joint plots, histograms |
| [`data/basketball-dataset.docx`](data/basketball-dataset.docx) | documentation of the basketball project | Section 3: matrices |

<details>
<summary>📈 Sample from <code>05-data-visualization/05-histograms.ipynb</code></summary>

```python
# 5️⃣ Layering Histograms for Comparison
# ------------------------------
# Compare 'CriticRating' and 'AudienceRating' on the same plot
sns.histplot(
    data=movies,
    x='CriticRating',
    bins=15,
    color="blue",
    kde=True,
    label="Critic Rating"     # Add a legend label
)
sns.histplot(
    data=movies,
    x='AudienceRating',
    bins=15,
    color="orange",
    kde=True,
    label="Audience Rating"   # Add a legend label
)
plt.title("Comparison of Critic and Audience Ratings 🆚")
plt.xlabel("Ratings")
plt.ylabel("Frequency")
plt.legend()  # Display the legend
plt.show()
```

</details>

---

## Repository layout

```
Python-for-Data-Science-A-Z/
├── 00-quickstart/                         # overview script + intro notebook
├── 01-python-basics/                      # one folder per course section,
├── 02-python-fundamentals/                #   each with its own README
├── 03-matrices-and-advanced-operations/
├── 04-dataframes-with-pandas/
├── 05-data-visualization/
├── 06-real-world-projects/                # guide to the three projects
├── data/                                  # datasets shared by the notebooks
├── assets/                                # README banner
├── .github/                               # CI
└── requirements.txt
```

**Why a single `main`?** This repo used to keep every section on its own branch. Everything now lives on `main`, and the original branch history is preserved in the commit graph.

---

## Quick start

```bash
git clone https://github.com/evgeniimatveev/Python-for-Data-Science-A-Z.git
cd Python-for-Data-Science-A-Z
uv venv && uv pip install -r requirements.txt   # or: python -m venv .venv && pip install -r requirements.txt
jupyter lab
```

Open a notebook from its own folder: the notebooks that need data read it from `../data/`, which is where Jupyter's working directory points by default.

---

## Continuous integration

Every push and pull request runs [`notebooks-check.yml`](.github/workflows/notebooks-check.yml):

| Check | What it catches |
|-------|-----------------|
| **Validate every `.ipynb`** | Broken or corrupted notebook files |
| **Code-cell syntax** | Syntax errors, including in notebooks that CI cannot run |
| **Widget metadata** | Notebooks GitHub would show as "Invalid Notebook" |
| **File-name hygiene** | Spaces in file names |
| **Quickstart script + datasets** | `hello_data_science.py` still runs and the data files exist |

Notebooks are teaching material, so they are **not** executed on every push. A second workflow, [`notebooks-run.yml`](.github/workflows/notebooks-run.yml), is **manual**: Actions → *Notebook run (manual)* → *Run workflow*. It runs every notebook top to bottom (27 of 35; the 8 that call `input()` are skipped) and writes a pass/fail table to the Job Summary.

---

## Known limitations

- 8 notebooks call `input()` and wait for you to type. They are marked with ⌨️ in the section READMEs and skipped by the manual run.
- `02-python-fundamentals/03-packages` makes a live request to the GitHub API and imports `scrapy`, so it needs internet and `requirements.txt` installed.
- Saved outputs come from the original runs, so they may show absolute paths of the original machine (for example the working directory printed in `04 / 01-importing-data`).
- In Google Colab, clone the repo first and open the notebook from the cloned folder so `../data/...` resolves.

---

## Credits

The basketball, demographic and movie-ratings datasets and parts of the exercises come from Super Data Science course material. The notebooks are my annotated working copies, extended with mini projects.

---

## Tech stack

`Python` · `Jupyter` · `NumPy` · `pandas` · `Matplotlib` · `Seaborn` · `GitHub Actions`

---

*Built by [Evgenii Matveev](https://github.com/evgeniimatveev) · Data Analyst / Analytics & MLOps Engineer*
