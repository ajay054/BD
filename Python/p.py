def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_s = s.replace(" ", "").lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_s == cleaned_s[::-1]

# Example usage:
user_input = input("Enter a word or phrase: ")
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")
