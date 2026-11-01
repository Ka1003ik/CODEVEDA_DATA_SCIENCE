
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the encoded dataset
df = pd.read_csv("encoded_country_population.csv")

print("Original dataset shape:", df.shape)

# Select numerical features
numeric_columns = ["Population", "World_Percentage"]

# Apply StandardScaler
scaler = StandardScaler()

scaled_data = scaler.fit_transform(df[numeric_columns])

# Add standardized columns
df["Population_Standardized"] = scaled_data[:, 0]
df["World_Percentage_Standardized"] = scaled_data[:, 1]

# Display results
print("\nStandardized Dataset Preview:")
print(df[[
    "Country",
    "Population",
    "Population_Standardized",
    "World_Percentage",
    "World_Percentage_Standardized"
]].head())

# Verify standardization
print("\nStandardized Column Means:")
print(df[[
    "Population_Standardized",
    "World_Percentage_Standardized"
]].mean())

print("\nFinal Dataset Shape:", df.shape)

# Save final dataset
df.to_csv(
    "preprocessed_country_population.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nNumerical standardization completed!")
print("Final dataset saved successfully!")
