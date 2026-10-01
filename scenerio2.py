import csv
import sys
from pathlib import Path


def read_grocery(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        return list(csv.DictReader(csvfile))


def display_all_items(items):
    print("\nALL GROCERY ITEMS")
    print("-" * 90)
    if not items:
        print("No grocery items found.")
        return

    for item in items:
        print(
            f"Item ID: {item.get('Item ID', '')} | "
            f"Name: {item.get('Name', '')} | "
            f"Category: {item.get('Category', '')} | "
            f"Quantity: {item.get('Quantity', '')} | "
            f"Price: ₹{item.get('Price', '')}"
        )
    print("-" * 90)


def search_by_item_id(items, item_id):
    target = str(item_id).strip().lower()
    for item in items:
        if str(item.get('Item ID', '')).strip().lower() == target:
            return item
    return None


def main():
    if len(sys.argv) > 1:
        file_path = Path(sys.argv[1])
    else:
        file_path = Path(__file__).with_name("grocery.csv")

    items = read_grocery(file_path)
    display_all_items(items)

    search_id = input("\nEnter the Item ID to search: ").strip()
    item = search_by_item_id(items, search_id)

    if item is None:
        print(f"\nNo item found with Item ID: {search_id}")
        return

    print("\nMatching grocery item:")
    print(
        f"Item ID: {item.get('Item ID', '')} | "
        f"Name: {item.get('Name', '')} | "
        f"Category: {item.get('Category', '')} | "
        f"Quantity: {item.get('Quantity', '')} | "
        f"Price: ₹{item.get('Price', '')}"
    )


if __name__ == "__main__":
    main()
