import pandas as pd

# Task 1: Read and Display Data
def read_and_display_data(file_name):
    try:
        # Load CSV file into a DataFrame
        df = pd.read_csv(file_name)

        # Display the first few rows of the data
        print("First few rows of the data:")
        print(df.head())

        # Describe the dataset
        print("\nDataset description:")
        print(df.info())
        print(df.describe())
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Task 2: Data Filtering and Selection
def data_filtering_and_selection(file_name):
    try:
        # Load CSV file into a DataFrame
        df = pd.read_csv(file_name)

        # Filter the dataset based on conditions
        filtered_data = df[df['Age'] > 25]

        # Display the filtered data
        print("\nFiltered data where Age is greater than 25:")
        print(filtered_data)

        # Select specific columns
        selected_columns = df[['Name', 'City']]

        # Display the selected columns
        print("\nSelected columns (Name and City):")
        print(selected_columns)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Task 3: Data Aggregation and Grouping
def data_aggregation_and_grouping(file_name):
    try:
        # Load CSV file into a DataFrame
        df = pd.read_csv(file_name)

        # Group the data by 'City' column and calculate mean, sum, and count
        grouped_data = df.groupby('City').agg({'Age': ['mean', 'sum', 'count']})

        # Display the aggregated results
        print("\nAggregated results after grouping by City:")
        print(grouped_data)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Task 4: Data Cleaning and Manipulation
def data_cleaning_and_manipulation(file_name):
    try:
        # Load CSV file into a DataFrame
        df = pd.read_csv(file_name)

        # Display the dataset before cleaning
        print("\nDataset before cleaning:")
        print(df)

        # Identify and handle missing values (replace with mean)
        df['Age'].fillna(df['Age'].mean(), inplace=True)

        # Display the dataset after cleaning
        print("\nDataset after handling missing values:")
        print(df)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Task 5: Merging and Joining DataFrames
def merge_and_join_dataframes(file1, file2):
    try:
        # Load CSV files into DataFrames
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)

        # Merge DataFrames using a common column ('ID' in this example)
        merged_df = pd.merge(df1, df2, on='ID', how='inner')

        # Display the merged DataFrame
        print("\nMerged DataFrame:")
        print(merged_df)
    except FileNotFoundError:
        print(f"Error: One or both files not found.")

# Main Program
csv_file_name = "example_data.csv"
read_and_display_data(csv_file_name)
data_filtering_and_selection(csv_file_name)
data_aggregation_and_grouping(csv_file_name)
data_cleaning_and_manipulation(csv_file_name)

# Additional CSV file for Task 5
csv_file_name2 = "example_data2.csv"
merge_and_join_dataframes(csv_file_name, csv_file_name2)
