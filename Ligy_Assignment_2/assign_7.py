
n = int(input("Enter a positive integer value for n: "))    
if n < 1:
    raise ValueError("Please enter a positive integer.")
square_dict = {}
for i in range(1, n + 1):
    square_dict[i] = i * i
print(f"Generated dictionary: {square_dict}")
