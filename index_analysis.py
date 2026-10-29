
from config import get_database, COLLECTION_NAME


def analyze_indexes():
    client = None

    try:
        client, db = get_database()
        collection = db[COLLECTION_NAME]

        print("=" * 55)
        print("MONGODB INDEX ANALYSIS")
        print("=" * 55)

        # 1. Display existing indexes
        print("\n1. EXISTING INDEXES")

        for index in collection.list_indexes():
            print(index)

        # 2. Explain a query without a hint
        query = {"age": {"$gt": 50}}

        print("\n2. QUERY PLAN - AGE GREATER THAN 50")

        plan = collection.find(query).explain()
        winning_plan = plan["queryPlanner"]["winningPlan"]
        print(winning_plan)

        # 3. Create an index on age
        print("\n3. CREATE AGE INDEX")

        index_name = collection.create_index(
            [("age", 1)],
            name="age_ascending_idx"
        )

        print("Created index:", index_name)

        # 4. Explain the same query again
        print("\n4. QUERY PLAN AFTER INDEX CREATION")

        plan_after = collection.find(query).explain()
        winning_plan_after = plan_after["queryPlanner"]["winningPlan"]
        print(winning_plan_after)

        
        # 5. Execution statistics using MongoDB explain command
        print("\n5. EXECUTION STATISTICS")

        stats = db.command(
            "explain",
            {
                "find": COLLECTION_NAME,
                "filter": query
            },
            verbosity="executionStats"
        )

        execution = stats["executionStats"]

        print("Execution time (ms):", execution["executionTimeMillis"])
        print("Documents returned:", execution["nReturned"])
        print("Documents examined:", execution["totalDocsExamined"])
        print("Index keys examined:", execution["totalKeysExamined"])


    except Exception as error:
        print("Index analysis failed:", error)

    finally:
        if client is not None:
            client.close()


if __name__ == "__main__":
    analyze_indexes()