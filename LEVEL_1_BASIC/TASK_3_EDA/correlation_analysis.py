import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Task 2 preprocessed dataset
df = pd.read_csv("preprocessed_country_population.csv")

# Select original numerical features
numeric_columns = ["Population", "World_Percentage"]

# Calculate correlation matrix
correlation_matrix = df[numeric_columns].corr(method="pearson")

print("CORRELATION MATRIX")
print(correlation_matrix)

# Save correlation matrix
correlation_matrix.to_csv("correlation_matrix.csv")

# Create correlation heatmap
plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".3f",
    linewidths=0.5,
    vmin=-1,
    vmax=1
)

plt.title("Correlation Matrix of Population Features")
plt.tight_layout()

# Save heatmap
plt.savefig("correlation_heatmap.png", dpi=300)
plt.close()

print("\nCorrelation analysis completed!")
print("Correlation matrix saved successfully!")
print("Heatmap saved successfully!")
