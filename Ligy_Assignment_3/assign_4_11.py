def generate_numbers(n):
    for number in range(n + 1):
        if number % 5 == 0 and number % 7 == 0:
            yield number

# Example usage:
n = int(input("Enter the value of n: "))

result_generator = generate_numbers(n)

print(f"Numbers divisible by 5 and 7 between 0 and {n}: {', '.join(map(str, result_generator))}")
