
from pymongo import MongoClient

MONGO_URI = "mongodb://127.0.0.1:27017/"
DATABASE_NAME = "bank_marketing_db"
COLLECTION_NAME = "customers"


def get_database():
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

    # Verify that the MongoDB server is reachable
    client.admin.command("ping")

    db = client[DATABASE_NAME]
    return client, db


if __name__ == "__main__":
    client = None

    try:
        client, db = get_database()
        print("MongoDB connection successful!")
        print("Database:", db.name)
        print("Collection:", COLLECTION_NAME)
    except Exception as error:
        print("MongoDB connection failed:", error)
    finally:
        if client is not None:
            client.close()
