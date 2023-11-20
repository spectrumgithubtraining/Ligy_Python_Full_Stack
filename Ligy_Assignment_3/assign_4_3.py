def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result_string = ''.join(char for char in input_string if char not in vowels)
    return result_string

# Example usage:
user_input = input("Enter a string: ")
result = remove_vowels(user_input)
print(f"String with vowels removed: {result}")
