from circle import Circle

class Cylinder(Circle):
    def __init__(self, color='red', filled=True, radius = 1.0, height = 1.0):
        super().__init__(color = color, filled = filled, radius = radius)
        self.height = height
    
    def to_string(self):
        return f'{super().to_string()}, Height = {self.height}'
    
    def get_area(self):
        return super().get_area() * self.height