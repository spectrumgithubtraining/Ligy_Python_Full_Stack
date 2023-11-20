def square():
    square_dict = {}
    for number in range(1, 21):
        square_dict[number] = number ** 2
    return square_dict

# Example usage:
result = square()
print(result)
