# Codveda Technology – Data Science Internship
## Level 1 (Basic): Task 2 – Data Cleaning and Preprocessing

## Project overview

This project cleans and preprocesses the country-population dataset produced in Level 1, Task 1.

- Input: `country_population.csv` (239 rows × 6 columns)
- Final output: `preprocessed_country_population.csv` (239 rows × 12 columns)
- The original Task 1 CSV is kept unchanged.

## Objectives and workflow

### 1. Data inspection — `data_inspection.py`

The script reports the dataset preview, dimensions, column names, data types, missing values, duplicate rows, and summary statistics.

Recorded results:
- 239 rows and 6 columns
- 206 missing values in `Notes`
- No missing values in the other five columns
- 0 duplicate rows

### 2. Missing values and outlier detection — `data_cleaning.py`

**Missing values:** The 206 missing entries in `Notes` were filled with `Not Available`. No rows were deleted. The output `cleaned_country_population.csv` contains 239 rows × 6 columns and no missing values.

**Outlier detection:** The Interquartile Range (IQR) method was applied separately to `Population` and `World_Percentage`. It identified 25 and 24 outliers, respectively.

**Outlier treatment decision:** These values correspond to real countries with comparatively large populations and world-population shares. They were retained to avoid deleting valid country records. Therefore, this project detects and reviews outliers but does **not** remove these valid observations. Do not describe this step as outlier removal.

### 3. Categorical encoding — `feature_encoding.py`

A derived `Population_Group` feature was created from `Population` using `pandas.qcut` with four quantile-based groups: `Low`, `Medium-Low`, `Medium-High`, and `High`.

One-Hot Encoding created:
- `Population_Group_Low`
- `Population_Group_Medium-Low`
- `Population_Group_Medium-High`
- `Population_Group_High`

Recorded group counts: 60, 60, 59, and 60. The original columns are preserved. Output: `encoded_country_population.csv` (239 rows × 10 columns).

These are relative groups based on this dataset's quartiles, not official demographic classifications.

### 4. Numerical standardization — `feature_scaling.py`

Scikit-learn's `StandardScaler` was applied to `Population` and `World_Percentage`. The original measurements were preserved, and two columns were added:
- `Population_Standardized`
- `World_Percentage_Standardized`

One-Hot encoded indicator columns were not scaled. Output: `preprocessed_country_population.csv` (239 rows × 12 columns).

### 5. Final validation — `final_validation.py`

The final validation checks dimensions, missing values, duplicate rows, standardized means and population standard deviations (`ddof=0`), column names, and a data preview.

Recorded results:
- Shape: 239 rows × 12 columns
- Missing values: 0 in every column
- Duplicate rows: 0
- Standardized means: approximately 0
- Standardized population standard deviations: 1.0 for both features

## Project structure

```text
TASK_2_DATA_CLEANING/
├── country_population.csv
├── data_inspection.py
├── data_cleaning.py
├── feature_encoding.py
├── feature_scaling.py
├── final_validation.py
├── cleaned_country_population.csv
├── encoded_country_population.csv
├── preprocessed_country_population.csv
└── README.md
```

## Requirements

- Python 3
- pandas
- scikit-learn

Install dependencies:

```bash
python -m pip install pandas scikit-learn
```

## How to run

Run the scripts in order from the repository root:

```bash
python LEVEL_1_BASIC/TASK_2_DATA_CLEANING/data_inspection.py
python LEVEL_1_BASIC/TASK_2_DATA_CLEANING/data_cleaning.py
python LEVEL_1_BASIC/TASK_2_DATA_CLEANING/feature_encoding.py
python LEVEL_1_BASIC/TASK_2_DATA_CLEANING/feature_scaling.py
python LEVEL_1_BASIC/TASK_2_DATA_CLEANING/final_validation.py
```

The scripts resolve their CSV inputs and outputs relative to their own folder, so they work reliably from any working directory. Each processing stage reads the output created by the preceding stage; `data_inspection.py` reads the original input.

## Output files

| File | Purpose |
|---|---|
| `cleaned_country_population.csv` | Missing `Notes` values handled |
| `encoded_country_population.csv` | Population groups one-hot encoded |
| `preprocessed_country_population.csv` | Final dataset with standardized numerical features |

## Notes and limitations

- The scraped source data is a snapshot and can change if Task 1 is rerun.
- Population-group boundaries depend on the dataset's quartiles and may change with different input data.
- StandardScaler was fitted on the full dataset for this preprocessing exercise. In a predictive modelling workflow, fit preprocessing transformations on training data only and apply them to validation/test data.
- IQR outliers were identified but retained for the domain-based reason above. If an evaluator strictly requires outlier removal, discuss this exception or create a separate outlier-filtered analysis copy; do not silently delete valid countries from the main cleaned dataset.
