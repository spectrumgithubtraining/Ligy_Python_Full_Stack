class Shape:
    def __init__(self):
        pass  # No specific attributes for the base class

    def area(self):
        return 0  # Default area for the base class

class Square(Shape):
    def __init__(self, length):
        super().__init__()  # Call the constructor of the base class (Shape)
        self.length = length

    def area(self):
        return self.length ** 2  # Area of a square is length squared

# Example usage
shape_instance = Shape()
print("Area of generic shape:", shape_instance.area())

square_instance = Square(4)
print("Area of square with length 4:", square_instance.area())
