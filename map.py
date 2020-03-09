def square(n):
    return n*n

items = [1, 2, 3, 4, 6]

squared_items = map(square, items)

for item in squared_items:
    print(item)