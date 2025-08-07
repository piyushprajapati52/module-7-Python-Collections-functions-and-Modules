# Simple calculator using functions

def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero."
    else:
        return "Invalid operator."

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

result = calculator(num1, num2, op)
print("Result:", result)
