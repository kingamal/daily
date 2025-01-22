words = ["love", "peace", "joy", "love", "happiness", "love", "joy"]

def most_frequent_word(word_list):
    word_count = {}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    most_frequent = max(word_count, key=word_count.get)
    
    return [most_frequent, word_count[most_frequent]]

most_frequent = most_frequent_word(words)
print(f"The most frequently occurring word is '{most_frequent[0]}' appearing {most_frequent[1]} times.")

