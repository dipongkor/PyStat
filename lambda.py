
def add(n):
    return lambda x: x*n
def square(n):
    return n*n

print(square(5))

lambda_square = lambda n: n*n

print(lambda_square(5))

def is_even_number(n):
    return n%2 == 0
lambda_is_even_number = lambda n: n%2 == 0

print(lambda_is_even_number(5))
