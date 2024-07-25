# Inheritance allows a class to inherit properties and methods from another class.

# Types:

# Single Inheritance: A class inherits from one superclass.
# Multiple Inheritance: A class inherits from multiple superclasses (not directly supported in many languages, like Java).
# Multilevel Inheritance: A class inherits from another class, which itself inherits from another class.
# Hierarchical Inheritance: Multiple classes inherit from a single superclass.



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



##################################################### Hierarichal Inheritance

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.eat()  # Output: Animal eats
d.bark() # Output: Dog barks
c.eat()  # Output: Animal eats
c.meow() # Output: Cat meows
