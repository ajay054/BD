# list_of_lists = [[2,4,5], [6,4,8], [5,7,3]]

# def middle_list (newlist):



#     for sublist in newlist:

#         print(sublist[1])


# print(middle_list(list_of_lists))

# list_of_lists = [[2, 4, 5], [6, 4, 8], [5, 7, 3]]
# def get_middle_elements(list_of_lists):
#     middle_elements = []
#     for sublist in list_of_lists:
#         middle_index = len(sublist) // 2
#         middle_elements.append(sublist[middle_index])
#     return middle_elements

# result = get_middle_elements(list_of_lists)
# print(result) 

# list_of_lists = [[2, 4, 5], [6, 4, 8], [5, 7, 3]]
# def get_middle_elements(list_of_lists):
#     return [sublist[len(sublist) // 2] for sublist in list_of_lists]

# result = get_middle_elements(list_of_lists)
# print(result) 

list_of_lists = [[2,4,5], [6,4,8], [5,7,3]]

def middle_list (newlist):

    output = []
 
    for sublist in newlist:
        output.append(sublist[1])

    return output

print(middle_list(list_of_lists))