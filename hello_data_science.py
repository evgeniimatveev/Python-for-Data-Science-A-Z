"""
Quick overview script for the Python-for-Data-Science-A-Z repository.

It prints the main sections of the course and the key topics for each.
"""

sections = [
    ("Section 1 – Python Basics", "Variables, loops, conditionals, core syntax"),
    ("Section 2 – Python Fundamentals", "Lists, tuples, slicing, packages"),
    ("Section 3 – Matrices & Advanced Operations", "NumPy arrays, matrices, ops"),
    ("Section 4 – DataFrames with Pandas", "Import, clean, filter, explore data"),
    ("Section 5 – Data Visualization", "Matplotlib, Seaborn, histograms, KDE"),
    ("Section 6 – Real-World Projects", "Basketball stats, demographics, movies"),
]


def print_course_overview():
    print("\n📊 Python for Data Science A-Z – course overview\n")
    print(f"{'Section':<45} | Topics")
    print("-" * 90)
    for name, topics in sections:
        print(f"{name:<45} | {topics}")
    print(
        "\nTip: open the corresponding Jupyter notebooks in each section "
        "to practice on real datasets.\n"
    )


if __name__ == "__main__":
    print_course_overview()
