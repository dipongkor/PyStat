numbers = [1,2,3,4,5,6]
even_numbers = filter(lambda n: n%2 == 0, numbers)
for number in even_numbers:
    print(number)