from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "cleaned_country_population.csv"
OUTPUT_FILE = BASE_DIR / "encoded_country_population.csv"


def main():
    df = pd.read_csv(INPUT_FILE)

    print("Original dataset shape:", df.shape)

    df["Population_Group"] = pd.qcut(
        df["Population"],
        q=4,
        labels=["Low", "Medium-Low", "Medium-High", "High"],
    )

    print("\nPopulation Group Distribution:")
    print(df["Population_Group"].value_counts())

    df = pd.get_dummies(df, columns=["Population_Group"], dtype=int)

    print("\nEncoded Dataset Preview:")
    print(df.head())
    print("\nEncoded Dataset Shape:", df.shape)

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    print(f"\nCategorical encoding completed successfully! Saved to {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()
