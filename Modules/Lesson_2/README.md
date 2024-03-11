# Lesson 2: Data Types and Basic Operations in Python

## Introduction

Welcome to Lesson 2 of our Python learning journey! In this lesson, we'll delve into the core of Python programming by exploring its various data types. Understanding data types is crucial because it forms the foundation of how we store, manipulate, and use data in our programs.

# Objectives
By the end of this lesson, you will:

- Learn about the different data types in Python.
- Understand how to declare and use variables.
- Get familiar with basic operations on different data types.

# Understanding Data Types
Python supports several data types, each with its own characteristics and uses. The most common data types include:

- Integers: Whole numbers, positive or negative, without decimals, of unlimited length.
- Floating Point Numbers: Real numbers that contain a decimal point.
- Strings: Sequences of characters used to represent text.
- Booleans: Logical values that can be either `True` or `False`.
- Lists: Ordered collections of items, which can be of different types.
- Tuples: Similar to lists, but immutable.
- Dictionaries: Unordered collections of key-value pairs.
- Sets: Unordered collections of unique elements.

# Declaring Variables
In Python, variables are declared by simply assigning a value to a name. There's no need to declare the type of the variable, as Python is dynamically typed.
```py
# Declaring an integer
my_int = 10

# Declaring a floating point number
my_float = 20.5

# Declaring a string
my_string = "Hello, Python!"

# Declaring a boolean
my_bool = True

# Declaring a list
my_list = [1, 2, 3, 4, 5]

# Declaring a tuple
my_tuple = (1, 2, 3, 4, 5)

# Declaring a dictionary
my_dict = {"name": "John", "age": 30}

# Declaring a set
my_set = {1, 2, 3, 4, 5}
```
# Basic Operations on Data Types
Python allows for various operations on its data types. Here are some examples:

## Arithmetic Operations on Numbers
```py
# Addition
sum = my_int + my_float
print(sum)

# Subtraction
difference = my_int - my_float
print(difference)

# Multiplication
product = my_int * my_float
print(product)

# Division
quotient = my_int / my_float
print(quotient)
```

## String Concatenation and Repetition
```py
# Concatenation
greeting = my_string + " How are you?"
print(greeting)

# Repetition
repeated_greeting = my_string * 3
print(repeated_greeting)
```

## List Operations
```py
# Adding an item to a list
my_list.append(6)
print(my_list)

# Removing an item from a list
my_list.remove(1)
print(my_list)
```

## Dictionary Operations
```py
# Adding a new key-value pair
my_dict["city"] = "New York"
print(my_dict)

# Accessing a value by key
print(my_dict["name"])
```

# Conclusion
Congratulations on completing Lesson 2! You've now learned about the different data types in Python and how to perform basic operations on them. This knowledge is essential for building more complex programs. Remember, the best way to learn is by doing, so try experimenting with different data types and operations. Don't hesitate to seek help if you encounter any challenges. Happy coding!