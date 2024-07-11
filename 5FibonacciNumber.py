def fibonacci_series(n):
    fib_series = []  # Initialize an Empty List to store the Fibonacci Series

    if n <= 0:
        return "Input Should be a Positive Integer"
    elif n == 1:
        fib_series = [0]  # First Fibonacci Number
    elif n == 2:
        fib_series = [0, 1]  # First two Fibonacci Numbers
    else:
        fib_series = [0, 1]  # Start the Series with the First Two Numbers
        for i in range(2, n):
            fib_series.append(
                fib_series[-1] + fib_series[-2]
            )  # Append the Sum of the Last Two Numbers

    return fib_series


try:
    n = int(
        input(
            "Enter a Positive Integer to Find the Fibonacci Series up to that Number: "
        )
    )
    series = fibonacci_series(n)  # Compute the Fibonacci Series
    print(f"The Fibonacci Series up to the {n}th Number is:")  # Output the Series
    print(series)
except ValueError:
    print("Please Enter a Valid Integer.")  # Handle Invalid Input