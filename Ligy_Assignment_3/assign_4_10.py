import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.6f} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def example_function():
    # Function for demonstration
    time.sleep(2)
    print("Function executed.")

@timing_decorator
def another_function():
    # Another function for demonstration
    time.sleep(1)
    print("Another function executed.")

# Example usage
example_function()
another_function()
