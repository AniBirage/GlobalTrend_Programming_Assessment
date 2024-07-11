def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor  # Perform the Division
        return result
    except ZeroDivisionError:
        return "Error: Division by Zero is not Allowed."


try:
    dividend = float(input("Enter the Dividend: "))  # Get Dividend
    divisor = float(input("Enter the Divisor: "))  # Get Divisor

    if divisor != 0:
        # Call the Function
        result = divide_numbers(dividend, divisor)
        print("Result of Division:", result)
    else:
        print("Error: Division by zero is not allowed.")

except ValueError:
    print(
        "Error: Please Enter Valid Numbers."
    )  # Handle Invalid Input (Non-numeric Input)