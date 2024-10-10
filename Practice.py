# Insert a value (No Duplicate)
# Removing a value 
# GetRandom a value that is already inserted in the list 

import random

class Start:
    def __init__(self):
        self.name = input("Enter your name : ")
        self.list = []
        if self.name not in self.list:
            self.list.append(self.name)
            print("Value Inserted")
        else:
            print("Value Already Exits")

    def removed(self):
        value = input("Enter the name to remove it from the list : ")
        if value in self.list:
            self.list.remove(value)
            print("Value removed")
        else:
            print("Value not exists in the list")
    def getrandom(self):
        return random.choice([self.list])

obj = Start()
obj.removed()
print(obj.getrandom())