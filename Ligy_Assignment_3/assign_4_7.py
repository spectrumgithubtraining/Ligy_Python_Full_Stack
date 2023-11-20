# Example usage:
keys_list = input("Enter a list of keys (comma-separated): ").split(',')
values_list = input("Enter a list of values (comma-separated): ").split(',')

# Convert input lists to integers (you can modify this based on the data type of your lists)
keys_list = [int(key) for key in keys_list]
values_list = [int(value) for value in values_list]

result_dict = dict(zip(keys_list, values_list))
print("Resulting Dictionary:", result_dict)
