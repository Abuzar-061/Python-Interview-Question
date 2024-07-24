# Polymorphism : Same Object have different behaviour
# Two methods of polymorphism: 1- Overloading. 2- Overriding 
# Overloading allows multiple methods in the same class to have the same name but different parameters (different type or number of parameters).
# Overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass.
# Polymorphism with Method Overriding 
class Animal:
    def sound(self):
        return "This is a generic animal sound"

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

def make_animal_sound(animal):
    print(animal.sound())

# Instantiate objects
dog = Dog()
cat = Cat()

# Demonstrate polymorphism
make_animal_sound(dog)  # Output: Woof
make_animal_sound(cat)  # Output: Meow


# Polymorphism with Method Overloading 
class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

# Instantiate object
math_ops = MathOperations()

# Demonstrate polymorphism-like behavior using default arguments
print(math_ops.add(1))       # Output: 1
print(math_ops.add(1, 2))    # Output: 3
print(math_ops.add(1, 2, 3)) # Output: 6
