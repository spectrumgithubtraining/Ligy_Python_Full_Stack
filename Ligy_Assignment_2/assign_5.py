# Initialize a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Display the original dictionary
print("Original Dictionary:")
print(my_dict)

# Demonstrate dictionary methods

# 1. get()
print("\n1. Using get('name'): ", my_dict.get('name'))

# 2. keys()
print("\n2. Dictionary Keys:", my_dict.keys())

# 3. values()
print("\n3. Dictionary Values:", my_dict.values())

# 4. items()
print("\n4. Dictionary Items:", my_dict.items())

# 5. pop()
removed_value = my_dict.pop('age')
print("\n5. Dictionary after pop('age'):", my_dict)
print("   Removed Value:", removed_value)

# 6. popitem()
removed_item = my_dict.popitem()
print("\n6. Dictionary after popitem():", my_dict)
print("   Removed Item:", removed_item)

# 7. update()
my_dict.update({'gender': 'Male'})
print("\n7. Dictionary after update({'gender': 'Male'}):", my_dict)

# 8. clear()
my_dict.clear()
print("\n8. Dictionary after clear():", my_dict)
