# Create a tuple of colors
colors = ("red", "blue", "green", "yellow", "blue", "green", "blue")

# Access elements using indexing
print("First color:", colors[0])  # Access the first element
print("Last color:", colors[-1])  # Access the last element

# Try to modify an element in the tuple (this will raise an error)
try:
    colors[1] = "purple"  # Attempting to modify the second element
except TypeError as e:
    print("Error:", e)  # Tuples are immutable, so this will fail

# Find the number of occurrences of a specific element in the tuple
color_to_count = "blue"
count = colors.count(color_to_count)
print(f"The color '{color_to_count}' appears {count} times in the tuple.")
