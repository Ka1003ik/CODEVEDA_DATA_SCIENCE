
# ==========================================
# TASK 1: DYNAMIC CONTENT SCRAPING
# Codveda Technology - Data Science Internship
# ==========================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Target website
url = "https://quotes.toscrape.com/js/"

# Configure Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

all_quotes = []

try:
    # Open website
    driver.get(url)
    print("Website opened successfully!")

    # Wait for JavaScript content
    wait = WebDriverWait(driver, 20)
    wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "quote")
        )
    )

    print("Dynamic content loaded successfully!")

    # Retrieve rendered HTML
    html = driver.page_source

    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")

    # Find all quotes
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text_tag = quote.find("span", class_="text")
        author_tag = quote.find("small", class_="author")

        if text_tag and author_tag:
            all_quotes.append({
                "Quote": text_tag.get_text(strip=True),
                "Author": author_tag.get_text(strip=True)
            })

    print("Total quotes extracted:", len(all_quotes))

except Exception as e:
    print("Scraping error:", e)

finally:
    driver.quit()

# Create DataFrame
if not all_quotes:
    raise SystemExit("No quotes extracted.")

df = pd.DataFrame(all_quotes)

# Display dataset
print("\nDataset Preview:")
print(df.head())

print("\nDataset Shape:", df.shape)

# Export CSV
df.to_csv(
    "dynamic_quotes.csv",
    index=False,
    encoding="utf-8-sig"
)

# Export JSON
df.to_json(
    "dynamic_quotes.json",
    orient="records",
    indent=4,
    force_ascii=False
)

print("\nCSV and JSON files saved successfully!")
print("Dynamic content scraping completed!")
