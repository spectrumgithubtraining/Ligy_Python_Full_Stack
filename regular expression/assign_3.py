import re

# Test strings
test_strings = ["123", "456789", "0", "78901", "abc123", ""]

# Regular expression pattern
pattern = re.compile(r'^[0-9]{1,6}$')

# Check if each string matches the pattern using if
for test_string in test_strings:
    if pattern.match(test_string):
        print(f"String: {test_string}, Matches the pattern")
    else:
        print(f"String: {test_string}, Does not match the pattern")
