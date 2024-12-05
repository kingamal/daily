def count_word():
    word = input("Enter the word to count: ").strip().lower()
    try:
        with open('book.txt', 'r', encoding='utf-8') as file:
            content = file.read().lower()

        words = content.split()

        count = words.count(word)

        print(f"The word '{word}' appears {count} times in the file 'book.txt'.")
    except FileNotFoundError:
        print("Error: The file 'book.txt' was not found. Please ensure the file exists in the same directory.")

if __name__ == "__main__":
    count_word()