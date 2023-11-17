prefix = "Hello"

# Sample list of items
items = ["World", "Python", "Programming", "List"]

# Insert the given string at the beginning of each item using list comprehension
modified_items = [prefix + x for x in items]

# Print the result
print("Original list:", items)
print(f"List after inserting '{prefix}':", modified_items)