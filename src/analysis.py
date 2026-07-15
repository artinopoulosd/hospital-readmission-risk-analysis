import pandas as pd

# Load dataset
df = pd.read_csv("data/diabetic_data.csv")

print("=" * 60)
print("Hospital Readmission Dataset")
print("=" * 60)

# Number of rows and columns
print("\nDataset shape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Basic information
print("\nDataset information:")
print(df.info())