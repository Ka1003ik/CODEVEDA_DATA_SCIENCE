from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "preprocessed_country_population.csv"


def main():
    df = pd.read_csv(DATA_FILE)
    numeric_columns = ["Population", "World_Percentage"]
    correlation_matrix = df[numeric_columns].corr(method="pearson")

    print("CORRELATION MATRIX")
    print(correlation_matrix)

    correlation_matrix.to_csv(BASE_DIR / "correlation_matrix.csv")

    plt.figure(figsize=(8, 6))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".3f",
        linewidths=0.5,
        vmin=-1,
        vmax=1,
    )
    plt.title("Correlation Matrix of Population Features")
    plt.tight_layout()
    plt.savefig(BASE_DIR / "correlation_heatmap.png", dpi=300)
    plt.close()

    print("\nCorrelation analysis completed!")
    print("Correlation matrix saved successfully!")
    print("Heatmap saved successfully!")


if __name__ == "__main__":
    main()
