def display_menu():
    print("\nWelcome to the Inventory Management System!")
    print("1. Add new item")
    print("2. Update stock")
    print("3. View inventory")
    print("4. Search for an item")
    print("5. Exit")

def add_item(inventory):
    name = input("Enter item name: ")
    try:
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        product = {"name": name, "qty": qty, "price": price}
        inventory.append(product)
        print("Item added successfully!")
    except ValueError:
        print("Invalid input. Quantity must be an integer and price must be a number.")

def update_stock(inventory):
    name = input("Enter item name to update: ")
    for item in inventory:
        if item["name"].lower() == name.lower():
            try:
                qty = int(input("Enter new quantity: "))
                item["qty"] = qty
                print("Stock updated successfully!")
                return
            except ValueError:
                print("Invalid input. Quantity must be an integer.")
                return
    print("Item not found in inventory.")

def view_inventory(inventory):
    if not inventory:
        print("\nInventory is empty.")
    else:
        print("\nInventory:")
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item['name']} - Quantity: {item['qty']}, Price: ${item['price']:.2f}")

def search_item(inventory):
    name = input("Enter item name to search: ")
    for item in inventory:
        if item["name"].lower() == name.lower():
            print(f"Found: {item['name']} - Quantity: {item['qty']}, Price: ${item['price']:.2f}")
            return
    print("Item not found in inventory.")

def main():
    inventory = []
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            add_item(inventory)
        elif choice == 2:
            update_stock(inventory)
        elif choice == 3:
            view_inventory(inventory)
        elif choice == 4:
            search_item(inventory)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
