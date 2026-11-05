
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "country_population.csv"


def main():
    df = pd.read_csv(DATA_FILE)

    print("DATASET PREVIEW")
    print(df.head())

    print("\nDATASET SHAPE")
    print(df.shape)

    print("\nCOLUMN NAMES")
    print(df.columns.tolist())

    print("\nDATA TYPES")
    print(df.dtypes)

    print("\nMISSING VALUES")
    print(df.isnull().sum())

    print("\nDUPLICATE ROWS")
    print(df.duplicated().sum())

    print("\nNUMERICAL SUMMARY")
    print(df.describe())

    print("\nCATEGORICAL SUMMARY")
    print(df.describe(include="all"))


if __name__ == "__main__":
    main()
