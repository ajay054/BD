def vow_count(str):
    vowels ='aeiouAEIOU'
    count=0
    for char in str:
        if char in vowels:
            count=count+1
    return count

str = input("Enter the input string: ")
print(vow_count(str))