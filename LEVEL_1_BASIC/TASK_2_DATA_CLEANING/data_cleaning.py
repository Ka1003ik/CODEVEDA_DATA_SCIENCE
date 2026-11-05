from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "country_population.csv"
OUTPUT_FILE = BASE_DIR / "cleaned_country_population.csv"


def main():
    df = pd.read_csv(INPUT_FILE)

    print("Original missing values:")
    print(df.isnull().sum())

    df["Notes"] = df["Notes"].fillna("Not Available")

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())
    print("\nDataset shape:", df.shape)

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    print(f"\nMissing value handling completed! Saved to {OUTPUT_FILE}.")

    for column in ["Population", "World_Percentage"]:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1

        lower_limit = q1 - 1.5 * iqr
        upper_limit = q3 + 1.5 * iqr

        outliers = df[(df[column] < lower_limit) | (df[column] > upper_limit)]

        print(f"\nOutliers in {column}:")
        print(outliers[["Country", column]])
        print("Total outliers:", len(outliers))

    print("\nOutlier detection completed!")


if __name__ == "__main__":
    main()
