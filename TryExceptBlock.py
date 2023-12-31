try:
    with open("non_existing_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
