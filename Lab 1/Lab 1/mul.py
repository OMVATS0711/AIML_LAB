# Take a number as input from the user
number = int(input("Enter a number to print its multiplication table: "))

# Use a for loop to iterate from 1 to 10
print(f"Multiplication table of {number}:")
for i in range(1, 11):
    product = number * i  # Calculate the product of the number and the current iteration
    print(f"{number} x {i} = {product}")
