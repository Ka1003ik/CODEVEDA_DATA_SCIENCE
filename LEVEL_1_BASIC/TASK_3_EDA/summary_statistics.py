
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "preprocessed_country_population.csv"
OUTPUT_FILE = BASE_DIR / "summary_statistics.csv"


def main():
    df = pd.read_csv(DATA_FILE)

    print("DATASET INFORMATION")
    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())

    numeric_columns = ["Population", "World_Percentage"]
    summary = df[numeric_columns].agg([
        "count",
        "mean",
        "median",
        "var",
        "std",
        "min",
        "max",
    ]).T

    print("\nSUMMARY STATISTICS")
    print(summary)

    summary.to_csv(OUTPUT_FILE)
    print(f"\nSummary statistics saved to {OUTPUT_FILE}.")
    print("EDA Step 1 completed!")


if __name__ == "__main__":
    main()
