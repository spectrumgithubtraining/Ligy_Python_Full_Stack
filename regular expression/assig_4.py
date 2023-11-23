import re

# Test string
test_string = "hello_world python_programming abc_def_ghi"

# Regular expression pattern
pattern = re.compile(r'\b[a-z]+_[a-z]+\b')

# Find all matches in the test string
matches = pattern.findall(test_string)

# Print the matches
print("Matches:", matches)
