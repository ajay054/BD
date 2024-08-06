def count_vowels(string):
    vowels = "aeiouAEIOU"
    return len([char for char in string if char in vowels])

# Example usage:
input_string = "Hello World"
result = count_vowels(input_string)
print(f"Number of vowels in '{input_string}': {result}")
