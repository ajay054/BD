def cube():
    n = 1
    cube_values = []  # Initialize an empty list to store cube values
    while n <= 10:
        cube_values.append(n**3)  # Calculate and add cube value to the list
        n += 1
    return cube_values

# Call the function and store the result
result_list = cube()

# Now you have a list of cube values
print(result_list)
