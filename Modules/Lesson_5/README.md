# Lesson 5: Object-Oriented Programming (OOP) in Python

# Introduction
Welcome to Lesson 5 of our Python learning journey! In this lesson, we'll dive into the world of Object-Oriented Programming (OOP) in Python. OOP is a programming paradigm that uses "objects" to design applications and programs. These objects are created using classes, which are essentially blueprints for creating objects.

# Objectives
By the end of this lesson, you will:

- Understand the principles of Object-Oriented Programming.
- Learn how to define classes and create objects in Python.
- Get familiar with object properties and methods.
- Explore inheritance and polymorphism in OOP.

# Understanding Object-Oriented Programming
Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and programs. These objects are created using classes, which are essentially blueprints for creating objects. OOP is based on several principles, including encapsulation, inheritance, and polymorphism.

# Defining Classes and Creating Objects
In Python, a class is defined using the `class` keyword. An object is an instance of a class. You can create an object by calling the class name followed by parentheses.
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object of the Person class
person1 = Person("Alice", 30)
person1.greet() # Output: Hello, my name is Alice and I am 30 years old.
```

# Object Properties and Methods
Objects have properties and methods. Properties are variables that belong to an object, and methods are functions that belong to an object. In Python, properties are defined within the class and can be accessed using the dot notation.
```py
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("The engine is starting.")

# Creating an object of the Car class
my_car = Car("Toyota", "Camry", 2020)
print(my_car.make) # Output: Toyota
my_car.start_engine() # Output: The engine is starting.
```
# Inheritance and Polymorphism
Inheritance is a mechanism where you can derive a class from another class for a hierarchy of classes that share a set of attributes and methods. Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.
```py
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print("The engine is starting.")

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def start_engine(self):
        print("The car engine is starting.")

# Creating an object of the Car class
my_car = Car("Toyota", "Camry", 2020)
my_car.start_engine() # Output: The car engine is starting.
```

# Conclusion
Congratulations on completing Lesson 5! You've now learned the basics of Object-Oriented Programming in Python, including how to define classes, create objects, and understand key OOP concepts like inheritance and polymorphism. OOP is a powerful paradigm that allows for more organized, reusable, and scalable code. Remember, practice is key to mastering these concepts. Try creating your own classes and objects, and experiment with inheritance and polymorphism. Don't hesitate to seek help if you encounter any challenges. Happy coding!