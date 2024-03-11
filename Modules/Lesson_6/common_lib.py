# Lesson 6: Common Libs in Python
# This script demonstrates Python Common Lib.

# Importing the required libraries
import os
import sys
import time
import requests
import random

# Using the os library to get the current working directory
def get_current_directory():
    current_directory = os.getcwd()
    print(f"Current working directory: {current_directory}")

# Using the sys library to print the Python version
def print_python_version():
    print(f"Python version: {sys.version}")

# Using the time library to get the current time
def get_current_time():
    current_time = time.time()
    print(f"Current time: {current_time}")

# Using the requests library to make a GET request
def make_get_request():
    response = requests.get('https://api.github.com')
    print(f"Response status code: {response.status_code}")

# Using the random library to generate a random number
def generate_random_number():
    random_number = random.randint(1, 10)
    print(f"Random number between 1 and 10: {random_number}")

# Main function to run the demonstrations
def main():
    get_current_directory()
    print_python_version()
    get_current_time()
    make_get_request()
    generate_random_number()

# Call the main function to run the demonstrations
if __name__ == "__main__":
    main()
