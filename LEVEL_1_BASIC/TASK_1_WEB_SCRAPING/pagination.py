
# ==========================================
# TASK 1: PAGINATION HANDLING DEMONSTRATION
# Codveda Technology - Data Science Internship
# ==========================================

from pathlib import Path
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent
BASE_URL = "https://news.ycombinator.com/news"
HEADERS = {
    "User-Agent": "KaushikDataScienceProject/1.0 (educational project)"
}
MAX_PAGES = 3


def main():
    all_data = []
    visited_pages = set()

    for page in range(1, MAX_PAGES + 1):
        print(f"\nScraping Page {page}...")

        if page in visited_pages:
            print("Page already visited. Stopping.")
            break

        visited_pages.add(page)

        try:
            response = requests.get(
                BASE_URL,
                params={"p": page},
                headers=HEADERS,
                timeout=20,
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as exc:
            print("Request failed:", exc)
            break

        soup = BeautifulSoup(response.text, "html.parser")
        stories = soup.find_all("tr", class_="athing")

        if not stories:
            print("No stories found. Stopping pagination.")
            break

        for story in stories:
            title_tag = story.select_one(".titleline > a")
            rank_tag = story.select_one(".rank")

            if title_tag:
                title = title_tag.get_text(strip=True)
                link = title_tag.get("href", "")
                rank = rank_tag.get_text(strip=True) if rank_tag else ""
                all_data.append({
                    "Rank": rank,
                    "Title": title,
                    "URL": link,
                    "Page": page,
                })

        print("Stories extracted:", len(stories))

        if not soup.select_one("a.morelink"):
            print("No next page available.")
            break

        time.sleep(2)

    print("\nTotal stories collected:", len(all_data))

    if not all_data:
        raise SystemExit("No data collected. Check the website structure.")

    df = pd.DataFrame(all_data)
    df = df.drop_duplicates(subset=["URL"]).copy()

    print("\nDataset Preview:")
    print(df.head())
    print("\nDataset Shape:", df.shape)

    df.to_csv(BASE_DIR / "hacker_news_paginated.csv", index=False)
    df.to_json(BASE_DIR / "hacker_news_paginated.json", orient="records", indent=4)

    print("\nCSV and JSON files saved successfully!")
    print("Pagination demonstration completed.")


if __name__ == "__main__":
    main()
