import csv
import os

# Task 1: Read and Display CSV Content
def read_and_display_csv(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Task 2: Write to CSV File
def write_to_csv(file_name, header, data):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow(data)
    print(f"Data written to '{file_name}'.")

# Task 3: Append to CSV File
def append_to_csv(file_name, data):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print(f"Data appended to '{file_name}'.")

# Task 4: Search and Modify CSV Content
def search_and_modify_csv(file_name, search_value, new_value):
    try:
        with open(file_name, 'r', newline='') as file:
            rows = list(csv.reader(file))
            for row in rows:
                if search_value in row:
                    index = row.index(search_value)
                    row[index] = new_value

        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"CSV content modified. New content:\n")
        read_and_display_csv(file_name)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Task 5: Calculate Statistics from CSV Data
def calculate_statistics(file_name, column_index):
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            data = [float(row[column_index]) for row in reader]
            average = sum(data) / len(data)
            total_sum = sum(data)
            max_value = max(data)

            print(f"Statistics for column {column_index}:")
            print(f"Average: {average}")
            print(f"Total Sum: {total_sum}")
            print(f"Maximum Value: {max_value}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Main Program
csv_file_name = "example_data.csv"
header = ["Name", "Age", "City"]
data = ["John Doe", "25", "New York"]

write_to_csv(csv_file_name, header, data)
read_and_display_csv(csv_file_name)

new_data = ["Alice Smith", "30", "Los Angeles"]
append_to_csv(csv_file_name, new_data)
read_and_display_csv(csv_file_name)

search_value = "John Doe"
new_value = "Jane Doe"
search_and_modify_csv(csv_file_name, search_value, new_value)

calculate_statistics(csv_file_name, column_index=1)

# Additional cleanup (optional): Delete the CSV file
os.remove(csv_file_name)
