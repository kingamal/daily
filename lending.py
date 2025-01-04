class BookLendingSystem:
    def __init__(self):
        self.available_books = {
            1: "The Great Gatsby",
            2: "To Kill a Mockingbird",
            3: "1984",
            4: "Pride and Prejudice"
        }
        self.borrowed_books = {}

    def display_menu(self):
        print("\nWelcome to the Book Lending System!")
        print("1. View available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. View Borrowed Books")
        print("5. Exit")


    def view_available_books(self):
        print("\n--- Available Books ---")
        if not self.available_books:
            print("No books are currently available for borrowing.")
        else:
            for key, book in self.available_books.items():
                print(f"{key}. {book}")

    def borrow_book(self):
        if not self.available_books:
            print("\nNo books are currently available for borrowing.")
            return

        try:
            book_number = int(input("\nEnter the book number to borrow: ").strip())
            if book_number not in self.available_books:
                print("Invalid book number. Please try again.")
                return

            name = input("Enter your name: ").strip()
            self.borrowed_books[book_number] = name
            print(f"\nYou have borrowed '{self.available_books[book_number]}'. Please return it on time.")
            del self.available_books[book_number]

        except ValueError:
            print("Invalid input. Please enter a valid book number.")

    def return_book(self):
        if not self.borrowed_books:
            pass

    def view_borrowed_books(self):
        if not self.borrowed_books:
            pass

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nChoose an option: ").strip()
            if choice == "1":
                self.view_available_books()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.view_borrowed_books()
            elif choice == "5":
                print("\nThank you for using the Book Lending System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                

system = BookLendingSystem()
system.run()