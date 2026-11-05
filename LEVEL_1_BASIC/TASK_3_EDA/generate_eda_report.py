from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "preprocessed_country_population.csv"
OUTPUT_FILE = BASE_DIR / "EDA_Report.md"
CHARTS = [
    (
        "Population Box Plot (Log Scale)",
        "population_boxplot.png",
        "Shows the median, interquartile range, whiskers and high-population outliers. The logarithmic y-axis makes the wide range of country populations easier to view.",
    ),
    (
        "Population Distribution Histogram (Log10 Scale)",
        "population_histogram.png",
        "Shows the frequency distribution of log10-transformed population values.",
    ),
    (
        "Population vs World Population Percentage",
        "population_vs_percentage_scatter.png",
        "Shows the positive association between population and world-population share. The population axis is logarithmic.",
    ),
    (
        "World Population Percentage Box Plot",
        "world_percentage_boxplot.png",
        "Shows that most countries have small world-population shares, while a small number of countries have much larger shares.",
    ),
    (
        "World Population Percentage Distribution",
        "world_percentage_histogram.png",
        "Shows a strongly right-skewed distribution, with most observations near zero and a small number of much larger percentages.",
    ),
    (
        "Correlation Heatmap",
        "correlation_heatmap.png",
        "Visualizes the Pearson correlation between Population and World_Percentage.",
    ),
]


def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Cannot find {DATA_FILE}. Run this script from the TASK_3_EDA folder or provide an absolute path."
        )

    df = pd.read_csv(DATA_FILE)
    required = ["Country", "Population", "World_Percentage"]
    missing_columns = [col for col in required if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {missing_columns}")

    numeric = df[["Population", "World_Percentage"]]
    stats = numeric.agg(["count", "mean", "median", "var", "std", "min", "max"]).T
    corr = numeric.corr(method="pearson")
    r = corr.loc["Population", "World_Percentage"]

    outlier_counts = {}
    for col in ["Population", "World_Percentage"]:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outlier_counts[col] = int(((df[col] < lower) | (df[col] > upper)).sum())

    def fmt(value):
        return f"{value:,.4f}"

    lines = [
        "# Exploratory Data Analysis (EDA) Report",
        "",
        "**Codveda Technology – Data Science Internship**  ",
        "**Level 1 (Basic), Task 3 – Exploratory Data Analysis**",
        "",
        "## 1. Project overview",
        "",
        "This report explores the country-population dataset produced by Task 1 and preprocessed in Task 2. "
        "The analysis uses the original `Population` and `World_Percentage` measurements from the Task 2 output. "
        "Standardized versions are not used for the descriptive statistics or Pearson correlation.",
        "",
        f"- Records analysed: **{len(df):,}**",
        f"- Columns in the input file: **{df.shape[1]}**",
        f"- Input file: `{DATA_FILE.name}`",
        "- Numerical variables analysed: `Population`, `World_Percentage`",
        "",
        "## 2. Summary statistics",
        "",
        "| Variable | Count | Mean | Median | Variance | Std. deviation | Minimum | Maximum |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for col, row in stats.iterrows():
        lines.append(
            f"| {col} | {int(row['count'])} | {fmt(row['mean'])} | "
            f"{fmt(row['median'])} | {fmt(row['var'])} | {fmt(row['std'])} | "
            f"{fmt(row['min'])} | {fmt(row['max'])} |"
        )

    lines += [
        "",
        "### Interpretation",
        "",
        f"The mean population is **{df['Population'].mean():,.2f}**, while the median is "
        f"**{df['Population'].median():,.0f}**. The mean being substantially higher than the median "
        "indicates a right-skewed population distribution: a relatively small number of highly populated "
        "countries raise the average.",
        "",
        f"The mean world-population share is **{df['World_Percentage'].mean():.4f}%**, and the median is "
        f"**{df['World_Percentage'].median():.4f}%**. This also indicates that most countries account for "
        "a small share, while a few account for much larger shares.",
        "",
        "## 3. Visual analysis",
        "",
    ]

    for title, filename, description in CHARTS:
        lines += [f"### {title}", ""]
        chart_path = BASE_DIR / filename
        if chart_path.exists():
            lines += [f"![{title}]({filename})", ""]
        else:
            lines += [f"> Chart file not found at report-generation time: `{filename}`", ""]
        lines += [description, ""]

    lines += [
        "## 4. Correlation analysis",
        "",
        "| Variable | Population | World_Percentage |",
        "|---|---:|---:|",
        f"| Population | {corr.loc['Population', 'Population']:.6f} | {r:.6f} |",
        f"| World_Percentage | {r:.6f} | {corr.loc['World_Percentage', 'World_Percentage']:.6f} |",
        "",
        f"The Pearson correlation coefficient between Population and World_Percentage is **{r:.6f}**, "
        "which indicates an extremely strong positive linear association in this dataset. This is expected "
        "because a country's world-population percentage is calculated from its population relative to the "
        "world total. The correlation is therefore not evidence that one variable causes the other.",
        "",
        "## 5. IQR outlier review",
        "",
        "| Variable | Number of IQR outliers |",
        "|---|---:|",
        f"| Population | {outlier_counts['Population']} |",
        f"| World_Percentage | {outlier_counts['World_Percentage']} |",
        "",
        "The IQR method flags observations outside 1.5 × IQR from the first and third quartiles. "
        "These flags identify statistically unusual values, not automatically incorrect records. "
        "The high values correspond to real countries with large populations and population shares, "
        "so they are retained in this descriptive analysis.",
        "",
        "## 6. Key findings",
        "",
        f"1. Country populations vary substantially across the {len(df):,} records.",
        "2. Population and world-population share distributions are right-skewed.",
        "3. The box plots identify a number of high-value IQR outliers; these are treated as valid observations.",
        "4. The scatter plot and correlation matrix show an extremely strong positive association between population and world-population share.",
        "5. Logarithmic population axes make the wide range of country population values easier to examine.",
        "",
        "## 7. Conclusion",
        "",
        "The EDA shows that population is unevenly distributed across countries: most countries have comparatively "
        "small populations and world-population shares, while a small number have very large values. Population "
        "and world-population share move together closely because the percentage is derived from population. "
        "The visualizations and statistics provide a clear descriptive overview of the dataset.",
        "",
        "## 8. Reproducibility",
        "",
        "Run the following scripts from the repository root:",
        "",
        "```bash",
        "python LEVEL_1_BASIC/TASK_3_EDA/summary_statistics.py",
        "python LEVEL_1_BASIC/TASK_3_EDA/data_visualization.py",
        "python LEVEL_1_BASIC/TASK_3_EDA/correlation_analysis.py",
        "python LEVEL_1_BASIC/TASK_3_EDA/generate_eda_report.py",
        "```",
        "",
        "The report uses the chart PNG files generated by `data_visualization.py` and `correlation_analysis.py`. "
        "Keep the report and chart images in the same directory so the embedded figures display correctly.",
        "",
    ]

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"EDA report created: {OUTPUT_FILE.resolve()}")
    print(f"Rows analysed: {len(df)}")
    print(f"Pearson correlation: {r:.6f}")
    print(f"IQR outliers - Population: {outlier_counts['Population']}")
    print(f"IQR outliers - World_Percentage: {outlier_counts['World_Percentage']}")


if __name__ == "__main__":
    main()
