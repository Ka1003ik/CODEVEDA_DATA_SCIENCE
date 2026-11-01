
import pandas as pd

# Load Task 2 output dataset
df = pd.read_csv("preprocessed_country_population.csv")

print("DATASET INFORMATION")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

# Select original numerical columns
numeric_columns = ["Population", "World_Percentage"]

# Calculate summary statistics
summary = df[numeric_columns].agg(
    ["count", "mean", "median", "var", "std", "min", "max"]
).T

print("\nSUMMARY STATISTICS")
print(summary)

# Save summary statistics
summary.to_csv("summary_statistics.csv")

print("\nSummary statistics saved successfully!")
print("EDA Step 1 completed!")
