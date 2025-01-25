# Original string
my_string = " Hello, Python! "

# 1. Strip whitespace from both ends
stripped_string = my_string.strip()
print("Stripped String:", stripped_string)

# 2. Convert to lowercase
lowercase_string = stripped_string.lower()
print("Lowercase String:", lowercase_string)

# 3. Convert to uppercase
uppercase_string = stripped_string.upper()
print("Uppercase String:", uppercase_string)

# 4. Replace a substring
replaced_string = stripped_string.replace("Python", "World")
print("Replaced String:", replaced_string)

# 5. Split the string into a list
split_string = stripped_string.split(", ")
print("Split String:", split_string)

# 6. Join a list into a string
joined_string = "-".join(split_string)
print("Joined String:", joined_string)

# 7. Check if the string starts with a specific word
starts_with_hello = stripped_string.startswith("Hello")
print("Starts with 'Hello':", starts_with_hello)

# 8. Check if the string ends with a specific word
ends_with_python = stripped_string.endswith("Python!")
print("Ends with 'Python!':", ends_with_python)

# 9. Find the index of a substring
index_of_python = stripped_string.find("Python")
print("Index of 'Python':", index_of_python)

# 10. Count occurrences of a character or substring
count_of_o = stripped_string.count("o")
print("Count of 'o':", count_of_o)

# 11. Check if the string is alphanumeric
is_alphanumeric = stripped_string.isalnum()
print("Is Alphanumeric:", is_alphanumeric)

# 12. Capitalize the first letter
capitalized_string = stripped_string.capitalize()
print("Capitalized String:", capitalized_string)

# 13. Title case the string
title_cased_string = stripped_string.title()
print("Title Cased String:", title_cased_string)

# 14. Reverse the string (using slicing)
reversed_string = stripped_string[::-1]
print("Reversed String:", reversed_string)
