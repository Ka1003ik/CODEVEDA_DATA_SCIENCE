# Codveda Technology – Data Science Internship
## Level 1 (Basic): Task 3 – Exploratory Data Analysis

### Project overview
This task explores the cleaned country-population dataset from Task 2. It calculates summary statistics, creates visualisations, checks correlations, and generates a final EDA report.

### Project structure
```text
TASK_3_EDA/
├── summary_statistics.py
├── data_visualization.py
├── correlation_analysis.py
├── generate_eda_report.py
├── preprocessed_country_population.csv
├── summary_statistics.csv
├── correlation_matrix.csv
├── correlation_heatmap.png
├── population_histogram.png
├── world_percentage_histogram.png
├── population_boxplot.png
├── world_percentage_boxplot.png
├── population_vs_percentage_scatter.png
├── EDA_Report.md
└── README.md
```

### How to run
From the repository root, run:

```bash
python LEVEL_1_BASIC/TASK_3_EDA/summary_statistics.py
python LEVEL_1_BASIC/TASK_3_EDA/data_visualization.py
python LEVEL_1_BASIC/TASK_3_EDA/correlation_analysis.py
python LEVEL_1_BASIC/TASK_3_EDA/generate_eda_report.py
```

The scripts resolve their file paths relative to their own folder. That keeps the generated reports and chart files in the same directory as the source code.

### Key outputs
- `summary_statistics.csv`: descriptive statistics for population and world-percentage columns
- PNG chart files: distribution and box-plot visualisations
- `correlation_matrix.csv` and `correlation_heatmap.png`: correlation analysis outputs
- `EDA_Report.md`: final narrative report with findings and summary tables
