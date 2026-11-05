# Data-collection-and-Exploration

A collection of beginner-friendly data science projects completed as part of the Codveda Technology Data Science Internship, Level 1 (Basic). The projects cover web data collection, data cleaning and preprocessing, and exploratory data analysis (EDA).

## Projects

| Task | Description | Folder |
| --- | --- | --- |
| Task 1: Web Scraping | Scrapes static, paginated, and JavaScript-rendered webpages; saves results as CSV and JSON. | [TASK_1_WEB_SCRAPING](LEVEL_1_BASIC/TASK_1_WEB_SCRAPING/) |
| Task 2: Data Cleaning | Inspects and cleans country population data, encodes population groups, scales numeric features, and validates the output. | [TASK_2_DATA_CLEANING](LEVEL_1_BASIC/TASK_2_DATA_CLEANING/) |
| Task 3: Exploratory Data Analysis | Summarizes and visualizes population data, reviews outliers, and examines correlations. | [TASK_3_EDA](LEVEL_1_BASIC/TASK_3_EDA/) |

## Repository layout

```text
LEVEL_1_BASIC/
├── TASK_1_WEB_SCRAPING/
├── TASK_2_DATA_CLEANING/
└── TASK_3_EDA/
```

Each task folder includes its relevant scripts, datasets or generated results, and task-level documentation. Read the README in each folder for dependencies, detailed instructions, outputs, and how to run its scripts.

## Getting started

Install Python 3.11 or newer and the project dependencies:

```bash
python -m pip install -r requirements.txt
```

Run scripts from the repository root using the paths in each task README. Scripts resolve input and output files relative to their own folder.

The GitHub Actions workflow compiles all Python files and runs the Task 2 and Task 3 data workflows. The live web-scraping scripts are not run in CI because they depend on external websites and, for the dynamic example, a browser.

## Notes

- Included datasets are snapshots and may differ if data collection scripts are rerun.
- Web scraping examples are for learning; respect source websites’ terms, robots instructions, and rate limits.
