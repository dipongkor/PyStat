from circle import Circle
from cylinder import Cylinder
from shape import Shape
circle = Circle()
shape = Shape()

print("***Circle Testing***")
print(circle.to_string())
print(circle.get_area())

print("\n")

print("***Cylinder Testing***")
cylinder = Cylinder()
print(cylinder.to_string())
print(cylinder.get_area())