lines = []
print("Enter lines (type 'exit' to end input):")
while True:
    line = input()
    if line.lower() == 'exit':
        break
    lines.append(line)

# Capitalize each line
capitalized_lines = [line.upper() for line in lines]

# Print the capitalized lines
print("\nCapitalized Lines:")
for line in capitalized_lines:
    print(line)