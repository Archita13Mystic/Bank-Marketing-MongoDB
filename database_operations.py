
from config import get_database, COLLECTION_NAME


def run_crud_operations():
    client = None

    try:
        client, db = get_database()
        collection = db[COLLECTION_NAME]

        print("=" * 50)
        print("MONGODB CRUD OPERATIONS")
        print("=" * 50)

        # READ: Count the original dataset
        print("\n1. READ - Total customer records")
        print("Total:", collection.count_documents({}))

        # CREATE: Insert a test customer
        print("\n2. CREATE - Insert test customer")

        test_customer = {
            "customer_id": "CA2_TEST_001",
            "age": 30,
            "job": "technician",
            "marital": "single",
            "balance": 1500,
            "y": "no",
            "is_test_record": True
        }

        # Remove any previous copy of this test record
        collection.delete_many({
            "customer_id": "CA2_TEST_001"
        })

        result = collection.insert_one(test_customer)
        print("Inserted ID:", result.inserted_id)

        # READ: Find the test customer
        print("\n3. READ - Find test customer")

        customer = collection.find_one(
            {"customer_id": "CA2_TEST_001"},
            {"_id": 0}
        )
        print(customer)

        # UPDATE: Change the test customer's balance
        print("\n4. UPDATE - Change balance")

        result = collection.update_one(
            {"customer_id": "CA2_TEST_001"},
            {"$set": {"balance": 2500}}
        )
        print("Documents updated:", result.modified_count)

        updated_customer = collection.find_one(
            {"customer_id": "CA2_TEST_001"},
            {"_id": 0}
        )
        print("Updated customer:", updated_customer)

        # DELETE: Remove the test customer
        print("\n5. DELETE - Remove test customer")

        result = collection.delete_one({
            "customer_id": "CA2_TEST_001"
        })
        print("Documents deleted:", result.deleted_count)

        # Verify that the original dataset remains intact
        print("\n6. FINAL VERIFICATION")
        print("Total records:", collection.count_documents({}))

    except Exception as error:
        print("CRUD operation failed:", error)

    finally:
        if client is not None:
            client.close()


if __name__ == "__main__":
    run_crud_operations()
