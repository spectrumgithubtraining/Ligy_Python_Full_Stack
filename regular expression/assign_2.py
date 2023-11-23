import re

# Test strings
test_strings = ["Hello123", "Python", "12345", "Special@Char"]
allowed_chars = "a-z, A-Z, and 0-9"

# Regular expression pattern
pattern = re.compile(r'^[a-zA-Z0-9]+$')

# Check if each string contains only allowed characters using if
for test_string in test_strings:
    if pattern.match(test_string):
        print(f"String: {test_string}, Contains only {allowed_chars}")
    else:
        print(f"String: {test_string}, Does not contain only {allowed_chars}")
