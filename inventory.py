def display_menu():
    print("\nWelcome to the Inventory Management System!")
    print("1. Add new item")
    print("2. Update stock")
    print("3. View inventory")
    print("4. Search for an item")
    print("5. Exit")

def main():
    inventory = []
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            name = input("Enter item name: ")
            qty = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            product = {"name": name, "qty": qty, "price": price}
            inventory.append(product)
            print("Item added successfully!")
        elif choice == 2:
            name = input("Enter item name to update: ")
            for el in inventory:
                for val in el.values():
                    if val == name:
                        qty = int(input("Enter new quantity: "))
                        el["qty"] = qty
                        print("Stock updated successfully!")
        elif choice == 3:
            i = 0
            print("\nInventory:")
            for el in inventory:
                i += 1
                print(f"{i}. {el["name"]} - Quantity: {el["qty"]}, Price: ${el["price"]}")
        elif choice == 4:
            name = input("Enter item name to search: ")
            for el in inventory:
                for val in el.values():
                    if val == name:
                        print(f"Found: {el["name"]} - Quantity: {el["qty"]}, Price: ${el["price"]}")
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()