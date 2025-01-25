


user_input = input("Enter a number: ")


try:
   
    number = float(user_input)
  
    result = number ** 2
    
    print(f"The square of {number} is {result}.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
