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

# Save summary to a text file
with open("outputs/summary.txt", "w") as file:
    file.write("Hospital Readmission Dataset Summary\n")
    file.write("=" * 40 + "\n\n")

    file.write(f"Rows: {df.shape[0]}\n")
    file.write(f"Columns: {df.shape[1]}\n")