from shape import Shape
import math
class Circle(Shape):
    def __init__(self, color='red', filled=True, radius = 1.0):
        super().__init__(color=color, filled=filled)
        self.radius = radius
    
    def to_string(self):
        return f'{super().to_string()}, Radius = {self.radius}'
    
    def get_area(self):
        return math.pi * self.radius**2