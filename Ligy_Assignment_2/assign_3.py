# Sample list
my_list = [1, 2, 3, 4, 5]

# Append an element to the list
my_list.append(6)
print("After append(6):", my_list)

# Extend the list with another list
my_list.extend([7, 8, 9])
print("After extend([7, 8, 9]):", my_list)

# Insert an element at a specific index
my_list.insert(2, 10)
print("After insert(2, 10):", my_list)

# Remove the first occurrence of a value
my_list.remove(3)
print("After remove(3):", my_list)

# Pop an element by index
popped_element = my_list.pop(4)
print(f"Popped element at index 4: {popped_element}")
print("After pop(4):", my_list)

# Index of the first occurrence of a value
index_of_4 = my_list.index(4)
print(f"Index of the first occurrence of 4: {index_of_4}")

# Count occurrences of a value
count_of_5 = my_list.count(5)
print(f"Count of occurrences of 5: {count_of_5}")

# Reverse the list in-place
my_list.reverse()
print("After reverse():", my_list)

# Sort the list in ascending order in-place
my_list.sort()
print("After sort():", my_list)

# Clear all elements from the list
my_list.clear()
print("After clear():", my_list)
