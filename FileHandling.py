import os

# Task 1: Create and Write File
def create_and_write_file(file_name):
    with open(file_name, 'w') as file:
        while True:
            user_input = input("Enter text (or 'exit' to finish): ")
            if user_input.lower() == 'exit':
                break
            file.write(user_input + '\n')

# Task 2: Read File Contents
def read_file_contents(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"File Content:\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Task 3: Append to the File
def append_to_file(file_name):
    with open(file_name, 'a') as file:
        user_input = input("Enter text to append: ")
        file.write(user_input + '\n')
        print("Text appended to the file.")

# Task 4: Count Lines in File
def count_lines_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"Number of lines in the file: {line_count}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Task 5: Copy File Content
def copy_file_content(original_file, copied_file):
    try:
        with open(original_file, 'r') as original, open(copied_file, 'w') as copied:
            copied.write(original.read())
        print(f"Content copied from '{original_file}' to '{copied_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{original_file}' not found.")

# Main Program
file_name = "example_file.txt"
create_and_write_file(file_name)
read_file_contents(file_name)
append_to_file(file_name)
count_lines_in_file(file_name)

copied_file_name = "copied_file.txt"
copy_file_content(file_name, copied_file_name)

# Additional cleanup (optional): Delete the original and copied files
os.remove(file_name)
os.remove(copied_file_name)
