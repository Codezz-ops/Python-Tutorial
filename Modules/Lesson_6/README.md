# Lesson 6: Exploring Common Python Libraries

# Introduction
Welcome to Lesson 6 of our Python learning journey! In this lesson, we'll explore some of the most commonly used Python libraries. These libraries extend Python's functionality, providing tools for various tasks such as interacting with the operating system, managing system-specific parameters, handling time-related tasks, making HTTP requests, and generating random numbers.

# Objectives
By the end of this lesson, you will:

- Learn about the `os`, `sys`, `time`, `requests`, and `random` libraries in Python.
- Understand how to use these libraries to perform common tasks.
- Get familiar with the basic functionalities of each library.

# Understanding Common Python Libraries
Python's standard library is vast and includes many modules that can help you perform a wide range of tasks. Here, we'll focus on five commonly used libraries:

## os
The `os` module provides a way of using operating system dependent functionality. It allows you to interact with the operating system, such as reading or writing to the file system.
```py
import os

# Getting the current working directory
current_directory = os.getcwd()
print(current_directory)
```

## sys
The `sys` module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter. It is used for accessing command-line arguments and for manipulating the Python runtime environment.
```py
import sys

# Printing the Python version
print(sys.version)
```

## time
The `time` module provides various time-related functions. It can be used for measuring the execution time of code, working with time zones, and formatting time.
```py
import time

# Getting the current time
current_time = time.time()
print(current_time)
```

## requests
The `requests` library is used for making HTTP requests. It abstracts the complexities of making requests behind a beautiful, simple API, allowing you to send HTTP/1.1 requests.
```py
import requests

response = requests.get('https://api.github.com')
print(response.status_code)
```

## random
The `random` module implements pseudo-random number generators for various distributions. It is used for generating random numbers, shuffling sequences, and selecting random items from a list.
```py
import random

# Generating a random number between 1 and 10
random_number = random.randint(1, 10)
print(random_number)
```

# Conclusion
Congratulations on completing Lesson 6! You've now explored some of the most commonly used Python libraries, including os, sys, time, requests, and random. These libraries are essential tools for Python developers, providing a wide range of functionalities that can significantly enhance your programming capabilities. Remember, the best way to learn is by doing. Try using these libraries in your projects and experiment with their functionalities. Don't hesitate to seek help if you encounter any challenges. Happy coding!