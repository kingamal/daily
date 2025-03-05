def save_note():
    note = input("Write a note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!")

def read_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if notes:
                print("Your notes:")
                for note in notes:
                    print(f"- {note.strip()}")
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found.")

def main():
    while True:
        print("1. Save a note")
        print("2. Read notes")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            save_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()