# ==========================================
# TASK 1: COUNTRY POPULATION WEB SCRAPER
# Codveda Technology - Data Science Internship
# ==========================================

from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = BASE_DIR / "country_population.csv"
URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
HEADERS = {
    "User-Agent": "KaushikDataScienceProject/1.0 (educational web scraping)"
}


def main():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=20)
        response.raise_for_status()
        print("Status Code:", response.status_code)
        print("Wikipedia connection successful!")
    except requests.exceptions.Timeout:
        raise SystemExit("Error: Request timed out.")
    except requests.exceptions.ConnectionError:
        raise SystemExit("Error: Unable to connect to website.")
    except requests.exceptions.HTTPError as exc:
        raise SystemExit(f"HTTP Error: {exc}") from exc
    except requests.exceptions.RequestException as exc:
        raise SystemExit(f"Request Error: {exc}") from exc

    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.title.text)

    tables = soup.find_all("table", class_="wikitable")
    print("Total tables found:", len(tables))

    if not tables:
        raise SystemExit("Error: No Wikipedia table found.")

    population_table = tables[0]
    print("\nPopulation Table Headers:")
    for heading in population_table.find_all("th"):
        print(heading.text.strip())

    rows = population_table.find_all("tr")
    all_data = []

    for row in rows[1:]:
        columns = row.find_all(["th", "td"])
        data = [column.get_text(" ", strip=True) for column in columns]

        if len(data) != 6:
            continue

        if not data[0] or data[0] == "World":
            continue

        all_data.append(data)

    print("Total records extracted:", len(all_data))

    if not all_data:
        raise SystemExit("Error: No population records extracted.")

    print("First country:", all_data[0])

    headers = [
        "Country",
        "Population",
        "World_Percentage",
        "Date",
        "Source",
        "Notes",
    ]

    df = pd.DataFrame(all_data, columns=headers)
    df["Population"] = (
        df["Population"].astype("string").str.replace(",", "", regex=False)
    )
    df["Population"] = pd.to_numeric(df["Population"], errors="coerce")

    df["World_Percentage"] = (
        df["World_Percentage"].astype("string").str.replace("%", "", regex=False)
    )
    df["World_Percentage"] = pd.to_numeric(df["World_Percentage"], errors="coerce")

    print("\nDataFrame Preview:")
    print(df.head())
    print("\nDataset Shape:", df.shape)
    print("\nData Types:")
    print(df.dtypes)

    print("\nDATA QUALITY CHECKS")
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicate Countries:")
    print(df["Country"].duplicated().sum())
    print("\nDataset Shape:", df.shape)
    print("Unique Countries:", df["Country"].nunique())
    print("\nData Types:")
    print(df.dtypes)
    print("\nPopulation Summary:")
    print(df["Population"].describe())

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\nFinal CSV saved successfully to {OUTPUT_PATH}!")


if __name__ == "__main__":
    main()