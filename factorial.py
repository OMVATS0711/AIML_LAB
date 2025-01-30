# Program to find the factorial of a number

# Input from the user
number = int(input("Enter a number: "))

# Initialize the factorial to 1
factorial = 1

# Check if the number is negative, zero, or positive
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    # Calculate factorial using a loop
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}.")
