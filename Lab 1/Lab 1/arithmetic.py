num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
operation = input("Enter your choice (1/2/3/4): ")
if operation == '1':
    result = num1 + num2
    print(f"The result is: {result}")
elif operation == '2':
    result = num1 - num2
    print(f"The result is: {result}")
elif operation == '3':
    result = num1 * num2
    print(f"The result is: {result}")
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice! Please select a valid operation.")
