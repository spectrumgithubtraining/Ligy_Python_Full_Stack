def compute_division():
    try:
        result = 5 / 0
        print("Result:", result)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        # You can handle the exception or log the error here

# Call the function
compute_division()
