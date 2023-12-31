try:
    user_input = int(input("Enter a number: "))
    print(f"You entered: {user_input}")
except ValueError:
    print("Error: Please enter a valid number.")
