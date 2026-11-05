
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "preprocessed_country_population.csv"
STANDARDIZED_COLUMNS = [
    "Population_Standardized",
    "World_Percentage_Standardized",
]
ONE_HOT_COLUMNS = [
    "Population_Group_Low",
    "Population_Group_Medium-Low",
    "Population_Group_Medium-High",
    "Population_Group_High",
]


def main():
    df = pd.read_csv(DATA_FILE)
    required_columns = [
        "Country",
        "Population",
        "World_Percentage",
        *STANDARDIZED_COLUMNS,
        *ONE_HOT_COLUMNS,
    ]
    missing_columns = [column for column in required_columns if column not in df]
    if missing_columns:
        raise ValueError(f"Dataset is missing required columns: {missing_columns}")

    if df.empty:
        raise ValueError("Dataset is empty.")
    if df.isna().any().any():
        raise ValueError("Dataset contains missing values.")
    if df.duplicated().any():
        raise ValueError("Dataset contains duplicate rows.")

    one_hot_totals = df[ONE_HOT_COLUMNS].sum(axis=1)
    if not one_hot_totals.eq(1).all():
        raise ValueError("Each row must belong to exactly one population group.")

    standardized = df[STANDARDIZED_COLUMNS]
    means = standardized.mean()
    standard_deviations = standardized.std(ddof=0)
    if not means.abs().lt(1e-10).all():
        raise ValueError("Standardized feature means are not approximately zero.")
    if not (standard_deviations.sub(1).abs() < 1e-10).all():
        raise ValueError("Standardized feature population standard deviations are not approximately one.")

    print("FINAL DATASET VALIDATION")
    print("\nDataset Shape:", df.shape)
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicate Rows:", df.duplicated().sum())

    print("\nStandardized Feature Means:")
    print(df[STANDARDIZED_COLUMNS].mean())

    print("\nStandardized Feature Standard Deviations:")
    print(df[STANDARDIZED_COLUMNS].std(ddof=0))

    print("\nFinal Columns:")
    print(df.columns.tolist())

    print("\nFinal Dataset Preview:")
    print(df.head())

    print("\nFINAL VALIDATION PASSED!")


if __name__ == "__main__":
    main()
