# Using dictionary comprehension to generate a dictionary of squares
numbers = [1, 2, 3, 4, 5]

# Create a dictionary of squares
squares_dict = {x: x**2 for x in numbers}#key value pair

# Print the result
print("Original numbers:", numbers)
print("Squares Dictionary:", squares_dict)
