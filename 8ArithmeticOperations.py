def perform_operation(
    num1, num2, operator
):  # Function to Perform Arithmetic Operation Based on Operator
    if operator == "+":
        return num1 + num2  # Addition
    elif operator == "-":
        return num1 - num2  # Subtraction
    elif operator == "*":
        return num1 * num2  # Multiplication
    elif operator == "/":
        if num2 != 0:
            return num1 / num2  # Division, Handle Division by Zero
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator"


if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))  # Get First Number
        num2 = float(input("Enter the second number: "))  # Get Second Number
        operator = input("Enter the operator (+, -, *, /): ")  # Get Operator

        result = perform_operation(num1, num2, operator)  # Call the Function

        if isinstance(result, (float, int)):
            print(f"Result of {num1} {operator} {num2} = {result}")  # Output the Result
        else:
            print(result)  # Output Error Message
    except ValueError:
        print(
            "Error: Please enter valid numbers."
        )  # Handle Invalid Input (Non-numeric Input)
