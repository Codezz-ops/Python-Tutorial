# Lesson 5: Object-Oriented Programming (OOP) in Python
# This script demonstrates Python OOP.

# Defining a basic class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object of the Person class
person1 = Person("Alice", 30)
person1.greet() # Output: Hello, my name is Alice and I am 30 years old.

# Defining a class with inheritance
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

# Demonstrating polymorphism
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating objects of the Dog and Cat classes
dog = Dog()
cat = Cat()

# Using polymorphism
print(dog.speak()) # Output: Woof!
print(cat.speak()) # Output: Meow!

# Main function to run the demonstrations
def main():
    person1.greet()
    my_car.start_engine()
    print(dog.speak())
    print(cat.speak())

# Call the main function to run the demonstrations
if __name__ == "__main__":
    main()