
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "preprocessed_country_population.csv"


def main():
    df = pd.read_csv(DATA_FILE)

    print("FINAL DATASET VALIDATION")
    print("\nDataset Shape:", df.shape)
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicate Rows:", df.duplicated().sum())

    print("\nStandardized Feature Means:")
    print(df[["Population_Standardized", "World_Percentage_Standardized"]].mean())

    print("\nStandardized Feature Standard Deviations:")
    print(df[["Population_Standardized", "World_Percentage_Standardized"]].std(ddof=0))

    print("\nFinal Columns:")
    print(df.columns.tolist())

    print("\nFinal Dataset Preview:")
    print(df.head())

    print("\nFINAL VALIDATION COMPLETED!")


if __name__ == "__main__":
    main()
