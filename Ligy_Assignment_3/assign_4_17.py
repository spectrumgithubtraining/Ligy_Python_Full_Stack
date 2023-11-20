def find_second_smallest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements in the list

    smallest = second_smallest = float('inf')  # Initialize with positive infinity

    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return second_smallest

# Example usage:
my_list = [5, 12, 3, 8, 9, 4, 15, 7]

result = find_second_smallest(my_list)

if result is not None:
    print("List:", my_list)
    print("Second Smallest Element:", result)
else:
    print("Not enough elements in the list.")
