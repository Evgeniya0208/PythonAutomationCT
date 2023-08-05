# 11) Create a function with one parameter as integer that returns True is if the given number is prime number or False otherwise.
def is_prime(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


print(is_prime(4))
