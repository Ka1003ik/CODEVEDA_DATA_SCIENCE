
# ==========================================
# TASK 1: PAGINATION HANDLING DEMONSTRATION
# Codveda Technology - Data Science Internship
# ==========================================

# Import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Website URL
base_url = "https://news.ycombinator.com/news"

# User-Agent header
headers = {
    "User-Agent": "KaushikDataScienceProject/1.0 (educational project)"
}

# Maximum number of pages to scrape
max_pages = 3

# Store all extracted records
all_data = []

# Track visited pages
visited_pages = set()

# Start pagination
for page in range(1, max_pages + 1):

    print(f"\nScraping Page {page}...")

    # Stop if the page has already been visited
    if page in visited_pages:
        print("Page already visited. Stopping.")
        break

    visited_pages.add(page)

    # Send request to the website
    try:
        response = requests.get(
            base_url,
            params={"p": page},
            headers=headers,
            timeout=20
        )

        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        break

    # Parse webpage HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all news story rows
    stories = soup.find_all("tr", class_="athing")

    if not stories:
        print("No stories found. Stopping pagination.")
        break

    # Extract story information
    for story in stories:

        title_tag = story.select_one(".titleline > a")
        rank_tag = story.select_one(".rank")

        if title_tag:

            title = title_tag.get_text(strip=True)
            link = title_tag.get("href", "")

            rank = (
                rank_tag.get_text(strip=True)
                if rank_tag else ""
            )

            all_data.append({
                "Rank": rank,
                "Title": title,
                "URL": link,
                "Page": page
            })

    print("Stories extracted:", len(stories))

    # Check whether a next-page link exists
    next_page = soup.select_one("a.morelink")

    if not next_page:
        print("No next page available.")
        break

    # Respect the website by waiting briefly
    time.sleep(2)

# ==========================================
# CREATE DATAFRAME
# ==========================================

print("\nTotal stories collected:", len(all_data))

if not all_data:
    raise SystemExit("No data collected. Check the website structure.")

df = pd.DataFrame(all_data)

# Remove duplicate story URLs
df = df.drop_duplicates(subset=["URL"]).copy()

# Display first five records
print("\nDataset Preview:")
print(df.head())

# Display dataset dimensions
print("\nDataset Shape:", df.shape)

# ==========================================
# EXPORT DATA
# ==========================================

df.to_csv("hacker_news_paginated.csv", index=False)

df.to_json(
    "hacker_news_paginated.json",
    orient="records",
    indent=4
)

print("\nCSV and JSON files saved successfully!")
print("Pagination demonstration completed.")
