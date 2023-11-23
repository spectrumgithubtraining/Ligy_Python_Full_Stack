import re

# Test strings
test_strings = ["abc", "a123b", "axb", "a567b", "ab", "bcd"]

# Regular expression pattern
pattern = re.compile(r'a.*b$')

# Check if each string matches the pattern using if
for test_string in test_strings:
    if pattern.match(test_string):
        print(f"String: {test_string}, Matches the pattern")
    else:
        print(f"String: {test_string}, Does not match the pattern")
