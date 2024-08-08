str1 = "Silent"
str2 = "listen"
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
print(f"Are '{str1}' and '{str2}' anagrams? {are_anagrams(str1, str2)}")

# def are_anagrams(str1, str2):
#     # Remove any whitespace and convert to lowercase to ensure the comparison is case-insensitive
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
    
#     # Compare sorted versions of the strings
#     return sorted(str1) == sorted(str2)

# # Function to take input and check if the strings are anagrams
# def check_anagrams():
#     str1 = input("Enter the first string: ")
#     str2 = input("Enter the second string: ")
#     if are_anagrams(str1, str2):
#         print(f"'{str1}' and '{str2}' are anagrams.")
#     else:
#         print(f"'{str1}' and '{str2}' are not anagrams.")

# # Run the check
# check_anagrams()
