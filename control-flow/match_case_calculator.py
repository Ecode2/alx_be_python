num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    print(f"The result is {num1 + num2}")

elif operation == "-":
    print(f"The result is {num1 - num2}")

elif operation == "*":
    print(f"The result is {num1 * num2}")

elif operation == "/":
    if num2 <= 0:
        print("Cannot divide by zero")
    print(f"The result is {num1 - num2}")
