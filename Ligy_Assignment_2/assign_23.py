def count_letters_and_digits(sentence):
    result = {'letter_count': 0, 'digit_count': 0}

    for char in sentence:
        if char.isalpha():
            result['letter_count'] += 1
        elif char.isdigit():
            result['digit_count'] += 1
    return result
sentence = "Hello123 World!"
counts = count_letters_and_digits(sentence)
print("Letter Count:", counts['letter_count'])
print("Digit Count:", counts['digit_count'])