def get_middle_elements(list_of_lists):
    middle_elements = []
    for sublist in list_of_lists:
        # Find the index of the middle element
        middle_index = len(sublist) // 2
        middle_elements.append(sublist[middle_index])
    return middle_elements

# Example usage:
list_of_lists = [[2, 4, 5], [6, 4, 8], [5, 7, 3]]
result = get_middle_elements(list_of_lists)
print(result)  # Should print [4, 4, 7]
