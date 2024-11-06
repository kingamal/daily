def count_words_in_sentence():
    sentence = input('Enter a sentence: ')
    number_of_words = len(sentence.split())
    the_longest_word = max(sentence.split(), key=len)
    number_of_words_sentence = f"The number of words in the sentence is: {number_of_words}"
    the_longest_word_sentence = f"The longest word in the sentence is: '{the_longest_word}'"
    return number_of_words_sentence + '\n' + the_longest_word_sentence

print(count_words_in_sentence())