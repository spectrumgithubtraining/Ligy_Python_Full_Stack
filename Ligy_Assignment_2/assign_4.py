# Read values for the first dictionary
print("Enter values for the first dictionary:")
dict1 = {}
while True:
    key = input("Enter key (type 'exit' to stop): ")
    if key.lower() == 'exit':
        break
    value = input(f"Enter value for {key}: ")
    dict1[key] = value

# Read values for the second dictionary
print("\nEnter values for the second dictionary:")
dict2 = {}
while True:
    key = input("Enter key (type 'exit' to stop): ")
    if key.lower() == 'exit':
        break
    value = input(f"Enter value for {key}: ")
    dict2[key] = value

# Merge dictionaries
merged_dict = {**dict1, **dict2}

# Print the merged dictionary
print("\nMerged Dictionary:")
print(merged_dict)
