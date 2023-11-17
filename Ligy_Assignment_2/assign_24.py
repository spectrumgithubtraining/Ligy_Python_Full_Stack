def generate_square_dict(n):
    square_dict = {i: i**2 for i in range(1, n+1)}
    return square_dict

# Example usage:
x=int(input("Enter the Number"))
result_dict = generate_square_dict(x)
print(result_dict)