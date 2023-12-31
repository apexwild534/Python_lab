# Request a numeric input from the user and check if it's even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Create a loop that generates a list of even numbers from 1 to the entered number
even_numbers = [i for i in range(1, number + 1) if i % 2 == 0]
print(f"Even numbers from 1 to {number}: {even_numbers}")

# Ask the user to enter a string and check if it contains the word 'Python'
user_string = input("Enter a string: ")
if 'Python' in user_string:
    print("The string contains 'Python'.")
else:
    print("The string does not contain 'Python'.")

# Display the reversed string
reversed_string = user_string[::-1]
print(f"Reversed string: {reversed_string}")

# Generate a multiplication table from 1 to 10 for the entered number
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
