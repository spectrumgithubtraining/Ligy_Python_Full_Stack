# Using lambda function and map to display powers of 2
numbers = range(0, 10)  # You can adjust the range as needed
powers = map(lambda x: 3 ** x, numbers)

# Displaying the result
print("Powers of 3:")
for index, result in enumerate(powers):
    print(f"2^{index} = {result}")
