import random

def load_names(filename):
    with open(filename, 'r') as file:
        names = [name.strip() for name in file.readlines()]
    return names

def save_name(filename, name):
    with open(filename, 'a') as file:
        file.write(name + '\n')

def random_name(names):
    selected_name = random.choice(names)
    return selected_name

def display_menu():
    print("\nPlease select an option:")
    print("1. Show the total number of names")
    print("2. Add a new name")
    print("3. Select a random name")
    print("4. Exit")

def main():
    filename = 'names.txt'
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            names = load_names(filename)
            print(f"\nTotal number of names: {len(names)}")
        elif choice == 2:
            new_name = input("Enter the new name to add: ").strip()
            if new_name:
                save_name(filename, new_name)
                print(f"{new_name} has been added to the file.")
            else:
                print("Name cannot be empty.")
        elif choice == 3:
            names = load_names(filename)
            if names:
                selected_name = random_name(names)
                print(f"\nRandomly selected name: {selected_name}")
            else:
                print("The name list is empty. Add names first.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()