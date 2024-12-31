WORDS = ["apple", "banana", "cherry", "blueberry"]

def longest_word(words):
    longest_word = max(words, key=len)
    print(f"'{longest_word}' is the longest word with {len(longest_word)} characters.")

if __name__ == "__main__":
    longest_word(WORDS)