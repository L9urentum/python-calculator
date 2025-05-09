# Name: Lawrence Nguyen
# Date: 5/8/2025
# File Purpose: Lab12

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("=== Simple Terminal Calculator ===")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operator"

        print("Result:", result)
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
