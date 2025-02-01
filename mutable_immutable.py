# Create a list (mutable data type)
my_list = [1, 2, 3, 4]

# Try to modify an element in the list
print("Original list:", my_list)
my_list[2] = 99  # Modifying the third element (index 2)
print("Modified list:", my_list)

# Create a tuple (immutable data type)
my_tuple = (10, 20, 30, 40)

# Try to modify an element in the tuple
print("\nOriginal tuple:", my_tuple)
try:
    my_tuple[2] = 99  # Attempting to modify the third element (index 2)
except TypeError as e:
    print("Error while modifying tuple:", e)
