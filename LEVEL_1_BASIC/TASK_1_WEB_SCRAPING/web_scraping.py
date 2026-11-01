# ==========================================
# TASK 1: COUNTRY POPULATION WEB SCRAPER
# Codveda Technology - Data Science Internship
# ==========================================

# Import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the target website URL
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

# Set User-Agent to identify the scraping application
headers = {
    "User-Agent": "KaushikDataScienceProject/1.0 (educational web scraping)"
}

# Send an HTTP GET request to the website
# Handle possible connection and HTTP errors
try:
    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )
    response.raise_for_status()
    print("Status Code:", response.status_code)
    print("Wikipedia connection successful!")
except requests.exceptions.Timeout:
    print("Error: Request timed out.")
    response = None
except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to website.")
    response = None
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
    response = None
except requests.exceptions.RequestException as e:
    print("Request Error:", e)
    response = None
if response is None:
    print("Scraping stopped due to connection failure.")
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Display the webpage title
print(soup.title.text)

# Find all Wikipedia tables
tables = soup.find_all("table", class_="wikitable")

# Display the number of tables found
print("Total tables found:", len(tables))

# Check whether a table was found
if not tables:
    print("Error: No Wikipedia table found.")
    exit()

# Select the population table
population_table = tables[0]

print("\nPopulation Table Headers:")
for heading in population_table.find_all("th"):
    print(heading.text.strip())

# Get all rows from the population table
rows = population_table.find_all("tr")

# Create an empty list to store extracted records
all_data = []

# Iterate through the table rows, skipping the header
for row in rows[1:]:

    # Extract all header and data cells
    columns = row.find_all(["th", "td"])

    # Extract clean text from each cell
    data = [
        column.get_text(" ", strip=True)
        for column in columns
    ]

    # Skip rows that do not contain six columns
    if len(data) != 6:
        continue

    # Skip empty country names and the World summary row
    if not data[0] or data[0] == "World":
        continue

    # Add valid records to the dataset
    all_data.append(data)

# Display the total records extracted
print("Total records extracted:", len(all_data))

# Check whether any records were extracted
if not all_data:
    print("Error: No population records extracted.")
    exit()

# Display the first extracted country
print("First country:", all_data[0])

# Define column names for the dataset
headers = [
    "Country",
    "Population",
    "World_Percentage",
    "Date",
    "Source",
    "Notes"
]

# Convert extracted records into a Pandas DataFrame
df = pd.DataFrame(all_data, columns=headers)

# Clean and convert Population into numeric format
df["Population"] = (
    df["Population"]
    .astype("string")
    .str.replace(",", "", regex=False)
)

# Convert population values into numbers
df["Population"] = pd.to_numeric(
    df["Population"],
    errors="coerce"
)

# Clean and convert World Percentage
df["World_Percentage"] = (
    df["World_Percentage"]
    .astype("string")
    .str.replace("%", "", regex=False)
)

# Convert percentage values into numbers
df["World_Percentage"] = pd.to_numeric(
    df["World_Percentage"],
    errors="coerce"
)

# Display the first five records
print("\nDataFrame Preview:")
print(df.head())

# Display dataset dimensions
print("\nDataset Shape:", df.shape)

# Display column data types
print("\nData Types:")
print(df.dtypes)

# ==========================================
# DATA QUALITY CHECKS AND FINAL VALIDATION
# ==========================================

print("\nDATA QUALITY CHECKS")

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate countries
print("\nDuplicate Countries:")
print(df["Country"].duplicated().sum())

# Check dataset dimensions
print("\nDataset Shape:", df.shape)

# Check unique country names
print("Unique Countries:", df["Country"].nunique())

# Display column data types
print("\nData Types:")
print(df.dtypes)

# Display population statistics
print("\nPopulation Summary:")
print(df["Population"].describe())

# Export the final cleaned dataset
df.to_csv("country_population.csv", index=False)

print("\nFinal CSV saved successfully!")