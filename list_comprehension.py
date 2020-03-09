items = [1, 2, 3, 4, 6]
even_numbers = []

for n in items:
    if n%2 == 0:
        even_numbers.append(n)

squared_number = [n for n in items if n%2 == 0]

for number in squared_number:
    print(number)

