# def palindrome(word):
#     return word == word[::-1]

# if palindrome('check'):
#     print("Word is palindrome")
# else:
#     print("Word is not a palindrome")

def palindrome(word):

    list1 = list(word)

    list1.reverse()
    reversed_word = "".join(list1)
    
    return word == reversed_word
print(palindrome('mom'))