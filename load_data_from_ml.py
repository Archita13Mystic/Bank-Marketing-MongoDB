
from pymongo import MongoClient
import pandas as pd

MONGO_URI = "mongodb://127.0.0.1:27017/"
DATABASE_NAME = "bank_marketing_db"
COLLECTION_NAME = "customers"

client = MongoClient(MONGO_URI)

try:
    collection = client[DATABASE_NAME][COLLECTION_NAME]

    # Read customer records without MongoDB's internal _id field.
    records = list(collection.find({}, {"_id": 0}))

    # Convert records into a pandas DataFrame.
    df = pd.DataFrame(records)

    print("DATA LOADED SUCCESSFULLY")
    print("-" * 40)

    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nFirst 5 records:")
    print(df.head())

    print("\nTarget distribution:")
    print(df["y"].value_counts())

    print("\nTarget distribution (%):")
    print((df["y"].value_counts(normalize=True) * 100).round(2))

    print("\nMissing values per column:")
    print(df.isnull().sum())

finally:
    client.close()