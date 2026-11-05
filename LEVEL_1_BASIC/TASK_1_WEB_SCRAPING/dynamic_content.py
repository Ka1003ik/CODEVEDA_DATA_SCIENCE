
# ==========================================
# TASK 1: DYNAMIC CONTENT SCRAPING
# Codveda Technology - Data Science Internship
# ==========================================

from pathlib import Path

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_DIR = Path(__file__).resolve().parent
URL = "https://quotes.toscrape.com/js/"


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver = None
    all_quotes = []

    try:
        driver = webdriver.Chrome(options=options)
        driver.get(URL)
        print("Website opened successfully!")

        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))
        print("Dynamic content loaded successfully!")

        soup = BeautifulSoup(driver.page_source, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            text_tag = quote.find("span", class_="text")
            author_tag = quote.find("small", class_="author")

            if text_tag and author_tag:
                all_quotes.append({
                    "Quote": text_tag.get_text(strip=True),
                    "Author": author_tag.get_text(strip=True),
                })

        print("Total quotes extracted:", len(all_quotes))
    except WebDriverException as exc:
        raise SystemExit(f"Browser error: {exc}") from exc
    except Exception as exc:  # pragma: no cover - general fallback for network/render issues
        raise SystemExit(f"Scraping error: {exc}") from exc
    finally:
        if driver is not None:
            driver.quit()

    if not all_quotes:
        raise SystemExit("No quotes extracted.")

    df = pd.DataFrame(all_quotes)
    print("\nDataset Preview:")
    print(df.head())
    print("\nDataset Shape:", df.shape)

    df.to_csv(BASE_DIR / "dynamic_quotes.csv", index=False, encoding="utf-8-sig")
    df.to_json(
        BASE_DIR / "dynamic_quotes.json",
        orient="records",
        indent=4,
        force_ascii=False,
    )

    print("\nCSV and JSON files saved successfully!")
    print("Dynamic content scraping completed!")


if __name__ == "__main__":
    main()
