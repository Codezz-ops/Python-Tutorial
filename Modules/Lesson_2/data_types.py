# Lesson 2: Introduction Python Data Types
# This script demonstrates Python Data Types and Operations.

# Integers
my_int = 10
# Floating Point Numbers
my_float = 20.5
# Strings
my_string = "Hello, Python!"
# Booleans
my_bool = True
# Lists
my_list = [1, 2, 3, 4, 5]
# Tuples
my_tuple = (1, 2, 3, 4, 5)
# Dictionaries
my_dict = {"name": "John", "age": 30}
# Sets
my_set = {1, 2, 3, 4, 5}

# Basic Operations on Numbers
# Addition
sum = my_int + my_float
print(f"Sum: {sum}")

# Subtraction
difference = my_int - my_float
print(f"Difference: {difference}")

# Multiplication
product = my_int * my_float
print(f"Product: {product}")

# Division
quotient = my_int / my_float
print(f"Quotient: {quotient}")

# String Concatenation and Repetition
# Concatenation
greeting = my_string + " How are you?"
print(f"Greeting: {greeting}")

# Repetition
repeated_greeting = my_string * 3
print(f"Repeated Greeting: {repeated_greeting}")

# List Operations
# Adding an item to a list
my_list.append(6)
print(f"List after appending: {my_list}")

# Removing an item from a list
my_list.remove(1)
print(f"List after removing: {my_list}")

# Dictionary Operations
# Adding a new key-value pair
my_dict["city"] = "New York"
print(f"Dictionary after adding: {my_dict}")

# Accessing a value by key
print(f"Accessing 'name' in dictionary: {my_dict['name']}")

# Set Operations
# Adding an item to a set
my_set.add(6)
print(f"Set after adding: {my_set}")

# Removing an item from a set
my_set.remove(1)
print(f"Set after removing: {my_set}")

print("Lesson 2: Data Types in Python - Complete!")
