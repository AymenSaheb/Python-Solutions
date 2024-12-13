
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


operation = input("Enter the operation : ").lower()


if operation == "add":
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif operation == "subtract":
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operation == "multiply":
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
