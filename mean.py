from functools import reduce

marks = [12, 13, 15, 20, 19, 15.5]
n = len(marks)

arithmetic_mean = sum(marks) / n
print(f"Arithmetic mean: {arithmetic_mean}")

marks_inverse = [1/mark for mark in marks]
harmonic_mean = n / sum(marks_inverse)
print(f"Harmonic mean: {harmonic_mean}")

geometric_mean = reduce(lambda x,y: x*y, marks) ** (1/n)
print(f"Geometric mean: {geometric_mean}")