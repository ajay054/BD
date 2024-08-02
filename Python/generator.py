# Defining the generator function
def cube():
    n = 1
    while n <= 10:
        result = n**3  # Calculate cube
        yield result  # Yield the result
        n += 1

# Creating a generator object
x = cube()

# Iterating through the generator object and printing the results
for i in x:
    print(i)
