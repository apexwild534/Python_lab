import os

# Task 1: Write to Binary File
def write_to_binary_file(file_name):
    with open(file_name, 'wb') as file:
        binary_data = input("Enter binary data (e.g., 010101): ")
        try:
            file.write(bytes.fromhex(binary_data))
            print("Binary data written to the file.")
        except ValueError:
            print("Error: Invalid binary data input.")

# Task 2: Read from Binary File
def read_from_binary_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            binary_content = file.read()
            print(f"Binary Content: {binary_content.hex()}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Task 3: Copy Binary File
def copy_binary_file(original_file, copied_file):
    try:
        with open(original_file, 'rb') as original, open(copied_file, 'wb') as copied:
            copied.write(original.read())
        print(f"Binary content copied from '{original_file}' to '{copied_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{original_file}' not found.")

# Task 4: Append to Binary File
def append_to_binary_file(file_name):
    with open(file_name, 'ab') as file:
        binary_data = input("Enter binary data to append: ")
        try:
            file.write(bytes.fromhex(binary_data))
            print("Binary data appended to the file.")
        except ValueError:
            print("Error: Invalid binary data input.")

# Task 5: Search and Replace Binary Data
def search_and_replace_binary_data(file_name, search_data, replace_data):
    try:
        with open(file_name, 'rb') as file:
            binary_content = file.read()
            if search_data in binary_content:
                new_binary_content = binary_content.replace(search_data, replace_data)
                with open(file_name, 'wb') as file:
                    file.write(new_binary_content)
                print("Binary data replaced in the file.")
            else:
                print("Binary data not found in the file.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Main Program
binary_file_name = "example_binary_file.bin"
write_to_binary_file(binary_file_name)
read_from_binary_file(binary_file_name)
copy_binary_file(binary_file_name, "copied_binary_file.bin")
append_to_binary_file(binary_file_name)

search_data = input("Enter binary data to search: ")
replace_data = input("Enter binary data to replace with: ")
search_and_replace_binary_data(binary_file_name, bytes.fromhex(search_data), bytes.fromhex(replace_data))

# Additional cleanup (optional): Delete the original and copied binary files
os.remove(binary_file_name)
os.remove("copied_binary_file.bin")
