# Specify the file name
file_name = "new_file.txt"

# Data to be written to the file
data_to_write = "Hello, this is some data that we want to write to the file."

# Open the file in write mode ('w')
# If the file doesn't exist, it will be created; if it exists, its content will be overwritten
with open(file_name, 'w') as file:
    # Write the data to the file
    file.write(data_to_write)

print(f"Data has been written to {file_name} successfully.")
