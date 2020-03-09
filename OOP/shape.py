class Shape:
    def __init__(self, color = "red", filled = True):
        self.color = color
        self.filled = filled
    
    def to_string(self, a, b):
        return f'Color = {self.color}, Filled = {self.filled}'
    
    def get_area(self):
        pass