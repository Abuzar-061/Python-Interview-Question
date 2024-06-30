class student:
    def __init__(self): # Method 1 
        self.id = input("Enter your Id:")
        self.name = input("Enter your name:")
        self.degree = input("Enter your degree:")
    def display(self): # Method 2 
        print("Student ID :",self.id)
        print("Student NAME :",self.name)
        print("Student DEGREE :",self.degree)

obj = student() # Created an instance of class name obj

obj.display()