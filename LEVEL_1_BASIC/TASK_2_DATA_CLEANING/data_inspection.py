
import pandas as pd

# Load Task 1 output
df = pd.read_csv("country_population.csv")

print("DATASET PREVIEW")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nDATA TYPES")
print(df.dtypes)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

print("\nNUMERICAL SUMMARY")
print(df.describe())

print("\nCATEGORICAL SUMMARY")
print(df.describe(include="str"))



