import pandas as pd

# Load Task 1 output
df = pd.read_csv("country_population.csv")

print("Original missing values:")
print(df.isnull().sum())

# Handle missing values
df["Notes"] = df["Notes"].fillna("Not Available")

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDataset shape:", df.shape)

# Save cleaned dataset
df.to_csv(
    "cleaned_country_population.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nMissing value handling completed!")

# Outlier detection using IQR method

for column in ["Population", "World_Percentage"]:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print(f"\nOutliers in {column}:")
    print(outliers[["Country", column]])

    print("Total outliers:", len(outliers))

print("\nOutlier detection completed!")
