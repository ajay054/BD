# def remove_duplicates(lst):
#     return list(set(lst))

# # Example usage
# lst = [5, 3, 4, 4, 2, 6, 3, 4, 5, 2, 5, 6, 8, 1, 3, 2, 0, 6, 4]
# print(remove_duplicates(lst))

lst = [5, 3, 4, 4, 2, 6, 3, 4, 5, 2, 5, 6, 8, 1, 3, 2, 0, 6, 4]

def duplicates(my_list):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
        
    return new_list

print(duplicates(lst))