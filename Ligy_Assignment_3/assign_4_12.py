def even_numbers_generator(n):
    return (str(num) for num in range(n + 1) if num % 2 == 0)

def main():
    try:
        n = int(input("Enter a number (n): "))
        if n < 0:
            raise ValueError("Please enter a non-negative integer.")

        result = ', '.join(even_numbers_generator(n))

        print(f"Even numbers between 0 and {n}: {result}")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
