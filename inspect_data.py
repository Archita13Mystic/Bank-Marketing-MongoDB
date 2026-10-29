
import pandas as pd
from pathlib import Path

# Dataset location
file_path = Path("data/bank-full.csv")


df = pd.read_csv(file_path, sep=";")

print("=" * 60)
print("BANK MARKETING DATASET OVERVIEW")
print("=" * 60)

print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 records:")
print(df.head())

print("\nDataset information:")
df.info()

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nTarget column distribution:")
print(df["y"].value_counts())

print("\nTarget distribution in percentage:")
print((df["y"].value_counts(normalize=True) * 100).round(2))