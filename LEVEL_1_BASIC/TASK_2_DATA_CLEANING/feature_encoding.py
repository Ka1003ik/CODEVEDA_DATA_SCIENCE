
import pandas as pd

# Load the cleaned dataset from the previous step
df = pd.read_csv("cleaned_country_population.csv")

print("Original dataset shape:", df.shape)

# Create population groups using quartiles
df["Population_Group"] = pd.qcut(
    df["Population"],
    q=4,
    labels=["Low", "Medium-Low", "Medium-High", "High"]
)

# Display group distribution
print("\nPopulation Group Distribution:")
print(df["Population_Group"].value_counts())

# Apply One-Hot Encoding
df = pd.get_dummies(
    df,
    columns=["Population_Group"],
    dtype=int
)

# Display results
print("\nEncoded Dataset Preview:")
print(df.head())

print("\nEncoded Dataset Shape:", df.shape)

# Export encoded dataset
df.to_csv(
    "encoded_country_population.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nCategorical encoding completed successfully!")
