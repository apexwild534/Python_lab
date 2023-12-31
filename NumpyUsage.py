import numpy as np

# Task 1: Array Creation and Manipulation
def create_and_manipulate_array(shape):
    # Create a NumPy array filled with random numbers
    random_array = np.random.rand(*shape)
    print("Original Array:")
    print(random_array)

    # Reshape the array
    reshaped_array = random_array.reshape(2, -1)
    print("\nReshaped Array:")
    print(reshaped_array)

    # Slicing and indexing
    sliced_array = reshaped_array[:, 1]
    print("\nSliced Array:")
    print(sliced_array)

# Task 2: Array Arithmetic and Aggregation
def array_arithmetic_and_aggregation(array1, array2):
    # Perform arithmetic operations on arrays
    addition_result = array1 + array2
    subtraction_result = array1 - array2
    multiplication_result = array1 * array2
    print("\nArray Arithmetic Results:")
    print("Addition Result:")
    print(addition_result)
    print("Subtraction Result:")
    print(subtraction_result)
    print("Multiplication Result:")
    print(multiplication_result)

    # Calculate statistical measures
    mean_value = np.mean(array1)
    median_value = np.median(array2)
    std_deviation = np.std(array1)
    print("\nStatistical Measures:")
    print("Mean:", mean_value)
    print("Median:", median_value)
    print("Standard Deviation:", std_deviation)

# Task 3: Conditional Array Operations
def conditional_array_operations(array):
    # Display the original array
    print("\nOriginal Array:")
    print(array)

    # Apply conditional operations
    filtered_array = np.where(array > 0.5, 1, 0)
    print("\nArray After Conditional Operation:")
    print(filtered_array)

# Main Program
# Task 1
array_shape = (3, 4)
create_and_manipulate_array(array_shape)

# Task 2
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])
array_arithmetic_and_aggregation(array1, array2)

# Task 3
conditional_array = np.random.rand(3, 3)
conditional_array_operations(conditional_array)
