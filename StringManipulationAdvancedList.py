# 1. Replace vowels in a string
user_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
string_without_vowels = ''.join(['X' if char in vowels else char for char in user_string])
print(f"String with vowels replaced: {string_without_vowels}")

# 2. Create a list of numbers and display only unique elements
numbers = [1, 2, 3, 4, 3, 2, 5, 6, 7, 7, 8]
unique_numbers = list(set(numbers))
print(f"Unique numbers: {unique_numbers}")

# 3. Merge two lists and remove duplicates
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
merged_list = list(set(list1 + list2))
print(f"Merged list without duplicates: {merged_list}")

# 4. Sort a list of strings in alphabetical order
words = ["banana", "apple", "orange", "grape"]
sorted_words = sorted(words)
print(f"Sorted list of words: {sorted_words}")

# 5. Combine elements of two lists using list comprehension
list3 = [1, 2, 3]
list4 = ['a', 'b', 'c']
combined_list = [(num, char) for num, char in zip(list3, list4)]
print(f"Combined list: {combined_list}")
