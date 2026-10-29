import csv
import json
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "data" / "bank-full.csv"
JSON_FILE = BASE_DIR / "data" / "bank-full.json"

def convert_csv_to_json():
    if not CSV_FILE.exists():
        print(f"ERROR: CSV file not found: {CSV_FILE}")
        return

    records = []

    with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            record = {}

            for key, value in row.items():
                value = value.strip()

                # Convert integer-valued fields to integers
                if key in {
                    "age", "balance", "day", "duration",
                    "campaign", "pdays", "previous"
                }:
                    record[key] = int(value)
                else:
                    record[key] = value

            records.append(record)

    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)

    # Verify the generated JSON file
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        verified_records = json.load(file)

    print("CSV to JSON conversion successful!")
    print(f"Records converted: {len(verified_records)}")
    print(f"Fields per record: {len(verified_records[0])}")
    print(f"JSON saved to: {JSON_FILE}")
    print("\nFirst record:")
    print(json.dumps(verified_records[0], indent=2))

    assert len(verified_records) == len(records)
    assert len(verified_records[0]) == 17

if __name__ == "__main__":
    convert_csv_to_json()