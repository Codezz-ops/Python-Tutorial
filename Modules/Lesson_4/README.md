# Lesson 4: Functions in Python

# Introduction
Welcome to Lesson 4 of our Python learning journey! In this lesson, we'll explore the concept of functions in Python. Functions are reusable blocks of code that perform a specific task. They are a fundamental part of programming, allowing for cleaner, more organized, and more efficient code.

# Objectives
By the end of this lesson, you will:

- Understand what functions are and why they are important.
- Learn how to define and call functions.
- Get familiar with function parameters and return values.
- Explore the concept of local and global variables within functions.

# Understanding Functions
A function in Python is a block of reusable code that performs a specific task. Functions provide better modularity for your application and a high degree of code reusing.

# Defining Functions
To define a function, you use the `def` keyword, followed by the function name and parentheses `()`. Any input parameters or arguments should be placed within these parentheses. The code block within every function is indented.
```py
def greet(name):
    print(f"Hello, {name}!")
```

## Calling Functions
To call a function, you use the function name followed by parentheses `()`. If the function requires arguments, you pass them inside the parentheses.
```py
greet("Alice")
```

## Function Parameters and Return Values
Functions can take parameters, which are values you can pass into the function. They can also `return` a value using the return statement.
```py
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result) # Output: 8
```

## Local and Global Variables
Variables that are defined inside a function are local to that function. They can only be accessed within that function. On the other hand, variables defined outside of a function are global and can be accessed anywhere in the program.
```py
x = 10 # Global variable

def test_function():
    y = 5 # Local variable
    print(x) # Accessing global variable
    print(y) # Accessing local variable

test_function()
```

# Conclusion
Congratulations on completing Lesson 4! You've now learned about functions in Python, including how to define, call, and use them effectively. Functions are a powerful tool for writing clean, organized, and efficient code. Remember, practice is key to mastering these concepts. Try writing your own functions and experimenting with different types of parameters and return values. Don't hesitate to seek help if you encounter any challenges. Happy coding!