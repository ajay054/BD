
def anagram_sorting(str1, str2):
    
    print(sorted(str1))
    print(sorted(str2))

    return sorted(str1.lower()) == sorted(str2.lower()) 

   
print(anagram_sorting("listen", "silent"))  
print(anagram_sorting("hello", "world"))
print(anagram_sorting("Like" , "dislike"))
print(anagram_sorting("cat","act"))