def longest_words(sentence):
    words = sentence.split()
    max_length = max(len(word) for word in words)
    longest_words_list = [word for word in words if len(word) == max_length]
    return longest_words_list

# Example usage:
input_sentence = "The quick brown fox jumps over the lazy dog"
longest_words_list = longest_words(input_sentence)
print(f"Longest words: {longest_words_list}, Length: {len(longest_words_list[0])}")
