def longest_word():
    words = input('Enter a list of words separated by spaces: ')
    longest_word = max(words.split(), key=len)
    print(f"'{longest_word}' is the longest word with {len(longest_word)} characters.")

if __name__ == "__main__":
    longest_word()