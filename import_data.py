
import pandas as pd
from pymongo import ASCENDING
from config import get_database, COLLECTION_NAME

DATASET_PATH = "data/bank-full.csv"


def import_data():
    client = None

    try:
        client, db = get_database()
        collection = db[COLLECTION_NAME]

        # Read the semicolon-separated CSV
        df = pd.read_csv(DATASET_PATH, sep=";")

        # Convert the DataFrame to MongoDB-compatible dictionaries
        records = df.to_dict(orient="records")

        # Avoid duplicate records when rerunning the import
        collection.create_index(
            [("age", ASCENDING), ("balance", ASCENDING),
             ("job", ASCENDING), ("y", ASCENDING)],
            name="customer_import_lookup"
        )

        # Clear this project's collection before a fresh full import
        collection.delete_many({})

        # Insert records in batches
        batch_size = 1000

        for start in range(0, len(records), batch_size):
            batch = records[start:start + batch_size]
            collection.insert_many(batch)

        print("Dataset imported successfully!")
        print("Database:", db.name)
        print("Collection:", COLLECTION_NAME)
        print("Records in CSV:", len(records))
        print("Records in MongoDB:", collection.count_documents({}))

        print("\nSample document:")
        print(collection.find_one({}, {"_id": 0}))

    except Exception as error:
        print("Import failed:", error)

    finally:
        if client is not None:
            client.close()


if __name__ == "__main__":
    import_data()