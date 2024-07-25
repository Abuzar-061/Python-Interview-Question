# Inheritance allows a class to inherit properties and methods from another class.

# Types:

# Single Inheritance: A class inherits from one superclass.
# Multiple Inheritance: A class inherits from multiple superclasses (not directly supported in many languages, like Java).
# Multilevel Inheritance: A class inherits from another class, which itself inherits from another class.
# Hierarchical Inheritance: Multiple classes inherit from a single superclass.
# Hybrid Inheritance: A combination of multiple types of inheritance.



################################################### Single Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # Output: Animal speaks
d.bark()   # Output: Dog barks



################################################### Multiple Inheritance 

class Flyable:
    def fly(self):
        print("Can fly")

class Swimmable:
    def swim(self):
        print("Can swim")

class Duck(Flyable, Swimmable):
    pass

d = Duck()
d.fly()  # Output: Can fly
d.swim() # Output: Can swim


################################################## Multilevel Inheritance

class Animal:
    def eat(self):
        print("Animal eats")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()  # Output: Animal eats
d.walk() # Output: Mammal walks
d.bark() # Output: Dog barks



##################################################### Hybrid Inheritance

class A:
    def method_A(self):
        print("Class A method")

class B(A):
    def method_B(self):
        print("Class B method")

class C(A):
    def method_C(self):
        print("Class C method")

class D(B, C):
    pass

d = D()
d.method_A()  # Output: Class A method
d.method_B()  # Output: Class B method
d.method_C()  # Output: Class C method
