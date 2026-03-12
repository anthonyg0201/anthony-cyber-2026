# Calculator Program

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
        else:
            return "Error: Invalid operation."

        return f"Result: {result}"

    except ValueError:
        return "Error: Invalid input. Please enter numeric values."

print(calculator())
