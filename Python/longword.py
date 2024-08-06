# def longest_word(sentence):
#     words = sentence.split()
#     max_length = len(max(words, key=len))
#     longest_words = [word for word in words if len(word) == max_length]
#     return longest_words, max_length

# # Example usage
# sentence = "The quick brown fox jumps over the lazy dog"
# longest_words, length = longest_word(sentence)
# print(f"The longest word(s): {longest_words}")
# print(f"Number of characters: {length}")

def longest_word(sentence):
    words = sentence.split()
    max_length = len(max(words, key=len))
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words, max_length

# Get user input
sentence = input("Enter a sentence: ")
longest_words, length = longest_word(sentence)
print(f"The longest word(s): {longest_words}")
print(f"Number of characters: {length}")
