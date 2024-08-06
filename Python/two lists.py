def find_common_elements(list1, list2):
    # Convert lists to sets and find the intersection
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    
    # Convert the set back to a list
    return list(common_elements)

# Example usage
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(find_common_elements(a, b))  # Output: [3, 4]
