
from pathlib import Path

import pandas as pd
from sklearn.preprocessing import StandardScaler

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "encoded_country_population.csv"
OUTPUT_FILE = BASE_DIR / "preprocessed_country_population.csv"


def main():
    df = pd.read_csv(INPUT_FILE)

    print("Original dataset shape:", df.shape)

    numeric_columns = ["Population", "World_Percentage"]
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[numeric_columns])

    df["Population_Standardized"] = scaled_data[:, 0]
    df["World_Percentage_Standardized"] = scaled_data[:, 1]

    print("\nStandardized Dataset Preview:")
    print(df[[
        "Country",
        "Population",
        "Population_Standardized",
        "World_Percentage",
        "World_Percentage_Standardized",
    ]].head())

    print("\nStandardized Column Means:")
    print(df[["Population_Standardized", "World_Percentage_Standardized"]].mean())

    print("\nFinal Dataset Shape:", df.shape)

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    print(f"\nNumerical standardization completed! Saved to {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()
