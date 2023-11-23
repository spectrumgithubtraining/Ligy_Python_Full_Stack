import re

test_strings = ["a", "ab", "abb", "aabb", "abc"]

# Regular expression pattern
pattern = re.compile(r'ab*')

# Check if each string matches the pattern using if
for test_string in test_strings:
    if pattern.fullmatch(test_string):
        print(f"String: {test_string}, Matches the pattern")
    else:
        print(f"String: {test_string}, Does not match the pattern")
