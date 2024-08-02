# Define a simple decorator function
def greet_decorator(func):
    def wrapper():
        print("Hello!")  # Additional functionality
        func()  # Original function is called
    return wrapper

# Define a normal function
def say_name():
    print("My name is AJ.")

# Apply the decorator
say_name = greet_decorator(say_name)

# Call the decorated function
say_name()
