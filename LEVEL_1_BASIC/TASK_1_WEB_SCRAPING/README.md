# Codveda Technology – Data Science Internship
## Level 1 (Basic): Task 1 – Data Collection and Web Scraping

### Project overview
This project demonstrates web data collection using Python. It contains three separate scraping demonstrations covering a static webpage, paginated content, and JavaScript-rendered content.

### Objectives covered
1. Identify websites and inspect their HTML structure.
2. Retrieve webpage content using `requests` and parse it with BeautifulSoup.
3. Store collected data in structured CSV and JSON files using pandas.
4. Demonstrate pagination and dynamic-content handling.

### Project structure
```text
TASK_1_WEB_SCRAPING/
├── web_scraping.py
├── country_population.csv
├── pagination.py
├── hacker_news_paginated.csv
├── hacker_news_paginated.json
├── dynamic_content.py
├── dynamic_quotes.csv
├── dynamic_quotes.json
└── README.md
```

### 1. Country population scraper
- **Source:** https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population
- **Libraries:** `requests`, `beautifulsoup4`, `pandas`
- **Method:** Sends an HTTP GET request, parses the returned HTML table with BeautifulSoup, converts the extracted records into a pandas DataFrame, performs basic data-quality checks, and exports the result.
- **Output:** `country_population.csv`
- **Recorded result:** 239 records and 6 columns (`Country`, `Population`, `World_Percentage`, `Date`, `Source`, `Notes`).
- **Note:** The values on the source webpage can change. The CSV represents the data captured when the scraper was run.

### 2. Pagination demonstration
- **Source:** https://news.ycombinator.com/news
- **Libraries:** `requests`, `beautifulsoup4`, `pandas`
- **Method:** Requests pages using the page parameter, extracts story ranks, titles and URLs, combines records, removes duplicate URLs, and exports the result.
- **Pages requested:** 3
- **Recorded result:** 90 stories collected before duplicate removal and 89 unique URL records after duplicate removal.
- **Outputs:** `hacker_news_paginated.csv` and `hacker_news_paginated.json`

### 3. Dynamic-content demonstration
- **Source:** https://quotes.toscrape.com/js/
- **Libraries:** `selenium`, `beautifulsoup4`, `pandas`
- **Method:** Selenium opens the page in Chrome and waits for quote elements to appear after JavaScript execution. BeautifulSoup then parses the rendered page source and extracts each quote and author.
- **Recorded result:** 10 quotes and 2 columns (`Quote`, `Author`).
- **Outputs:** `dynamic_quotes.csv` and `dynamic_quotes.json`

### Requirements
- Python 3
- Google Chrome
- Python packages: `requests`, `beautifulsoup4`, `pandas`, `selenium`

Install the packages with:

```bash
python -m pip install requests beautifulsoup4 pandas selenium
```

Selenium 4 includes Selenium Manager, which normally manages the compatible browser driver automatically.

### How to run
Open a terminal in the `TASK_1_WEB_SCRAPING` directory and run each script separately:

```bash
python web_scraping.py
python pagination.py
python dynamic_content.py
```

The scripts save their output files in the current working directory. Run them from the project directory so the CSV and JSON files are saved alongside the scripts.

### Data and responsible-use notes
- Scraped results are snapshots and may change when the source websites update.
- The pagination demonstration is limited to three pages.
- The dynamic-content demonstration extracts the quotes visible on the selected JavaScript page; it does not implement pagination across all quote pages.
- Respect each website's terms, robots instructions, rate limits, and applicable laws. Use reasonable request delays and avoid excessive traffic.
- The population, Hacker News, and quote datasets are separate demonstrations; they are not merged into one dataset.

### Task 1 completion summary
The project demonstrates static-page scraping, structured CSV/JSON export, pagination across multiple pages, and extraction of JavaScript-rendered content. The outputs and record counts above reflect the successful runs recorded during development.
