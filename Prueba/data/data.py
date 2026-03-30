import csv

# Save CSV
def save_csv(inventory, path):
    if not inventory:
        print("Inventory is empty")
        return

    try:
        with open(path, 'w', newline="", encoding="utf-8") as f:
            fieldnames = ["name", "id", "age", "program", "status"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(inventory)

        print(f"Data saved in: {path}")

    except Exception as e:
        print("Error saving file:", e)

# Load CSV
def load_csv(path):
    inventory = []

    try:
        with open(path, 'r', newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                students= {
                    "name": row["name"],
                    "id": row["id"],
                    "age": int(row["age"]),
                    "program" : row["program"],
                    "status": row["status"],
                }

                inventory.append(students)

        print("Data loaded successfully")
        return inventory

    except FileNotFoundError:
        print("File not found")
        return []

    except Exception as e:
        print("Error:", e)
        return []