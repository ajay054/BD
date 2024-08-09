# Challenge: Write a function that accepts an integer and which checks to see if the integer is a prime number

# def prime_number(num):
#     if num % 2 == 0:
        
#         return True
    
#     else:
        
#         return False

# //

# def prime_number(num):
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for i in range(3, int(num**0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True

# # Example usage
# print(prime_number(3)) 


def is_prime(num):
   
    for X in range(2,num):
        if num % X == 0:
            return False
    return True

print(is_prime(3)) 

