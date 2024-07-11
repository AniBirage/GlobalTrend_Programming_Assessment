import time
import functools


# Define a Decorator to Measure and Log the Execution Time of a Function
def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the Start Time
        result = func(*args, **kwargs)  # Call the Function Being Decorated
        end_time = time.time()  # Record the End Time
        execution_time = end_time - start_time  # Calculate the Execution Time
        print(f"Function '{func.__name__}' Executed in {execution_time:.4f} Seconds")
        return result

    return wrapper


# Function to Compute Factorial, Decorated with timing_decorator
@timing_decorator
def compute_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # Compute Factorial
    return result


if __name__ == "__main__":
    try:
        n = int(input("Enter a number to compute factorial: "))  # Get Input
        result = compute_factorial(n)  # Call the Decorated Function
        print(f"Factorial of {n}: {result}")  # Output the Result
    except ValueError:
        print(
            "Please enter a valid integer."
        )  # Handle Invalid Input (Non-numeric Input)