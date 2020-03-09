def is_even_number(n):
    return n%2 == 0

numbers = [1,2,3,4,5,6]

even_numbers = filter(is_even_number, numbers)

for number in even_numbers:
    print(number)