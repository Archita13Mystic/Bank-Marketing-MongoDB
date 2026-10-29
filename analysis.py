
from config import get_database, COLLECTION_NAME


def run_analysis():
    client = None

    try:
        client, db = get_database()
        collection = db[COLLECTION_NAME]

        print("=" * 55)
        print("BANK MARKETING - MONGODB AGGREGATION")
        print("=" * 55)

        # Analysis 1: Count customers by subscription outcome
        print("\n1. SUBSCRIPTION DISTRIBUTION")

        pipeline = [
            {
                "$group": {
                    "_id": "$y",
                    "total_customers": {"$sum": 1}
                }
            },
            {
                "$sort": {"total_customers": -1}
            }
        ]

        for result in collection.aggregate(pipeline):
            print(result)

        # Analysis 2: Subscription outcome by job
        print("\n2. SUBSCRIPTION OUTCOME BY JOB")

        pipeline = [
            {
                "$group": {
                    "_id": {
                        "job": "$job",
                        "subscription": "$y"
                    },
                    "count": {"$sum": 1}
                }
            },
            {
                "$sort": {
                    "_id.job": 1,
                    "_id.subscription": 1
                }
            }
        ]

        for result in collection.aggregate(pipeline):
            print(result)

        # Analysis 3: Subscription rate by housing loan status
        print("\n3. SUBSCRIPTION RATE BY HOUSING LOAN STATUS")

        pipeline = [
            {
                "$group": {
                    "_id": "$housing",
                    "total_customers": {"$sum": 1},
                    "subscribed": {
                        "$sum": {
                            "$cond": [
                                {"$eq": ["$y", "yes"]},
                                1,
                                0
                            ]
                        }
                    }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "housing_loan": "$_id",
                    "total_customers": 1,
                    "subscribed": 1,
                    "subscription_rate_percent": {
                        "$round": [
                            {
                                "$multiply": [
                                    {
                                        "$divide": [
                                            "$subscribed",
                                            "$total_customers"
                                        ]
                                    },
                                    100
                                ]
                            },
                            2
                        ]
                    }
                }
            },
            {
                "$sort": {"subscription_rate_percent": -1}
            }
        ]

        for result in collection.aggregate(pipeline):
            print(result)

    except Exception as error:
        print("Analysis failed:", error)

    finally:
        if client is not None:
            client.close()


if __name__ == "__main__":
    run_analysis()