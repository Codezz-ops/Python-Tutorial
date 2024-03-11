# Lesson 3: Control Flow in Python

# Introduction
Welcome to Lesson 3 of our Python learning journey! In this lesson, we'll explore control flow mechanisms in Python, which are essential for controlling the flow of execution in your programs. We'll cover loops, conditional statements, and a Pythonic way to handle switch-like behavior.

# Objectives
By the end of this lesson, you will:

- Learn about loops in Python.
- Understand how to use conditional statements (`if`, `elif`, `else`).
- Explore how to implement switch-like behavior in Python.

# Understanding Control Flow
Control flow is the order in which the individual statements, instructions, or function calls of an imperative or declarative program are executed or evaluated. In Python, control flow is managed through loops and conditional statements.

# Loops
Loops are used to repeatedly execute a block of code as long as a certain condition is met. Python supports two types of loops: `for` loops and `while` loops.

## For Loops
A for loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or other iterable objects.
```py
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

## While Loops
A `while` loop is used to repeatedly execute a block of code as long as a certain condition is true.
```py
# Counting from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1
```

## Conditional Statements
Conditional statements are used to perform different actions based on different conditions. Python uses `if`, `elif`, and `else` for conditional statements.
```py
# Simple if-else statement
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

# Conclusion
Congratulations on completing Lesson 3! You've now learned about control flow in Python, including loops and conditional statements. Understanding these concepts is crucial for writing efficient and effective Python programs. Remember, practice is key to mastering these concepts. Try writing your own programs that use loops and conditional statements to solve problems. Happy coding!