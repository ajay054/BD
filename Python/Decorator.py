# Defining the decorator function
def dec_func(func):
    def addon():
        func()  # Call the original function
        print("feature-2")
        print("feature-3")
    return addon

# Defining the normal function
def norm_func():
    print("feature-1")

# Applying the decorator
norm_func = dec_func(norm_func)

# Calling the decorated function
norm_func()
