from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "preprocessed_country_population.csv"


def main():
    df = pd.read_csv(DATA_FILE)
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 5))
    sns.histplot(x=np.log10(df["Population"]), bins=30, kde=True)
    plt.title("Population Distribution (Log10 Scale)")
    plt.xlabel("Log10 of Population")
    plt.ylabel("Number of Countries")
    plt.tight_layout()
    plt.savefig(BASE_DIR / "population_histogram.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="World_Percentage", bins=30, kde=True)
    plt.title("World Population Percentage Distribution")
    plt.xlabel("World Percentage (%)")
    plt.ylabel("Number of Countries")
    plt.tight_layout()
    plt.savefig(BASE_DIR / "world_percentage_histogram.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.boxplot(y=df["Population"])
    plt.yscale("log")
    plt.title("Population Box Plot (Log Scale)")
    plt.ylabel("Population (Log Scale)")
    plt.tight_layout()
    plt.savefig(BASE_DIR / "population_boxplot.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.boxplot(y=df["World_Percentage"])
    plt.title("World Population Percentage Box Plot")
    plt.ylabel("World Percentage (%)")
    plt.tight_layout()
    plt.savefig(BASE_DIR / "world_percentage_boxplot.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="Population", y="World_Percentage")
    plt.xscale("log")
    plt.title("Population vs World Population Percentage")
    plt.xlabel("Population (Log Scale)")
    plt.ylabel("World Percentage (%)")
    plt.tight_layout()
    plt.savefig(BASE_DIR / "population_vs_percentage_scatter.png")
    plt.close()

    print("All visualizations generated successfully!")
    print("\nGenerated files:")
    print("1. population_histogram.png")
    print("2. world_percentage_histogram.png")
    print("3. population_boxplot.png")
    print("4. world_percentage_boxplot.png")
    print("5. population_vs_percentage_scatter.png")


if __name__ == "__main__":
    main()
