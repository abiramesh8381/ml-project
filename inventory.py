import json

# New book to add
new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}


def read_inventory(path):
    """Task 1: Read inventory.json and return the list."""
    with open(path, "r", encoding="utf-8") as f:
        inventory = json.load(f)
    return inventory


def save_inventory(path, inventory):
    """Task 2: Save updated inventory back to inventory.json with indentation."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=4)


def display_inventory(inventory):
    """Task 3: Print each book in the required format."""
    for book in inventory:
        print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']:.2f}")


if __name__ == "__main__":
    file_path = "inventory.json"

    # --- Task 1: Read the inventory ---
    inventory = read_inventory(file_path)
    print(f"Total books currently in file: {len(inventory)}")

    # --- Task 2: Update and save ---
    inventory.append(new_book)
    save_inventory(file_path, inventory)

    # --- Task 3: Read updated file and display ---
    updated_inventory = read_inventory(file_path)
    display_inventory(updated_inventory)