
import pandas as pd

# Load final preprocessed dataset
df = pd.read_csv("preprocessed_country_population.csv")

print("FINAL DATASET VALIDATION")

print("\nDataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nStandardized Feature Means:")
print(df[[
    "Population_Standardized",
    "World_Percentage_Standardized"
]].mean())

print("\nStandardized Feature Standard Deviations:")
print(df[[
    "Population_Standardized",
    "World_Percentage_Standardized"
]].std(ddof=0))

print("\nFinal Columns:")
print(df.columns.tolist())

print("\nFinal Dataset Preview:")
print(df.head())

print("\nFINAL VALIDATION COMPLETED!")
