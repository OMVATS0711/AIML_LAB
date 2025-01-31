# Program to print the multiplication table of a number

# Input from the user
number = int(input("Enter a number: "))

# Print the multiplication table
print(f"Multiplication Table for {number}:\n")
for i in range(1, 11):  # Loop through numbers 1 to 10
    print(f"{number} x {i} = {number * i}")
