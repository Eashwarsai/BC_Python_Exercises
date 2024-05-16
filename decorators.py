import time
import random
from functools import wraps

# Decorator to measure execution time of a function
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper

# Decorator to retry a function until a condition is met
def retry(max_attempts=5):
    def retry_decorator(func):
        @wraps(func)
        def retry_wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_attempts:
                attempt += 1
                result = func(*args, **kwargs)
                if result < 3:
                    print("Success! Number less than 3 is generated!")
                    return result
                else:
                    print("Failed! Generated a number >= 3, retrying!")
        return retry_wrapper
    return retry_decorator

# Function to print even numbers up to n
@timer
def print_even_numbers(n):
    time.sleep(0.5)
    for i in range(n + 1):
        if i % 2 == 0:
            print(i)

# Function to generate a random number between 1 and 10
@timer
@retry(6)
def generate_random_number():
    return random.randint(1, 10)

# Example usage
print_even_numbers(6)
generate_random_number()
