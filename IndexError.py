my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Error: Index out of range.")
