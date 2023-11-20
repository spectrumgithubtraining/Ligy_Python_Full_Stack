class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Example usage
circle_instance = Circle(5)
print(f"Area of the circle with radius {circle_instance.radius} is: {circle_instance.area()}")
