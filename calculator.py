# Function to perform basic operations
def calculate():
    while True:
        # Display menu
        print("Simple Calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Take user input for operation
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if user wants to exit
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Take user input for numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        # Perform calculation based on the user's choice
        if choice == '1':
            result = num1 + num2
            print(f"The result is: {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"The result is: {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"The result is: {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result is: {result}")
            else:
                print("Error! Division by zero.")
        else:
            print("Invalid input! Please select a valid option.")
            
        # Ask if the user wants to perform another operation
        continue_choice = input("Do you want to perform another operation? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

# Call the calculator function
calculate()
