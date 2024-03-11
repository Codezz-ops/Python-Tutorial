# Lesson 4: Introduction Python Functions
# This script demonstrates Python Functions.

# Function to greet a person
def greet(name):
    print(f"Hello, {name}!")

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function to demonstrate local and global variables
def test_function():
    y = 5 # Local variable
    print(x) # Accessing global variable
    print(y) # Accessing local variable

# Global variable
x = 10

# Main function to run the demonstrations
def main():
    # Demonstrating function calls
    greet("Alice")
    result = add_numbers(5, 3)
    print(result) # Output: 8

    # Demonstrating local and global variables
    test_function()

# Call the main function to run the demonstrations
if __name__ == "__main__":
    main()
