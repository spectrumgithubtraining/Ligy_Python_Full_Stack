import re

# Test passwords
example_passwords = [
    "Pass123$",
    "SecurePwd123",
    "WeakPwd",
    "Short$1",
    "VeryLongPasswordWithSpecialCharacters123$#@"
]

# Define the regular expression pattern
pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$')

# Check validity for each password
for password in example_passwords:
    if pattern.match(password):
        print(f"Password: {password}, Valid: True")
    else:
        print(f"Password: {password}, Valid: False")
