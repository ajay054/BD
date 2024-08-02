# Define a simple generator function
def even_numbers():
    yield 2
    yield 4
    yield 6

# Create a generator object
numbers = even_numbers()

# Iterate over the generator and print the numbers
for number in numbers:
    print(number)
