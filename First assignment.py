# Simple Python Calculator

# Ask for the first number
num1 = float(input("enter the first number:"))

# Ask for the second number
num2 =float(input("enter the second number"))

# Ask for the operation
operation = input("enter operation (+, -, *, /):")

# perform the calculation based on the operatiom
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operation. Please enter +, -, *, or /")