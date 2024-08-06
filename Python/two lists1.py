def list_intersection(a,b):
    output = []
    for numbers in a:
        if numbers in b:
            output.append(numbers)

    return output
print(list_intersection(a=[1,2,3,4],b=[3,4,5,6])