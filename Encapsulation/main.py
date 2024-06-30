# Python provide access to all the variable and methods globally 
# By using Encapsulation we can restrict the variable and methods access globally by making it private or protected 

# For understanding online youtube video link : https://www.youtube.com/watch?v=3zGVokYEQgo&t=283s

# Single underscore _ => (Protected) if the variable is protected then the object and function of the class can access the variable . 
# Double underscore __ => (Private)  if the variable is private then only the function can access the variable .



class A:
    _a = 10 # Protected variable 
    __b = 20 # Private variable
    def show(self):
        print("a = ", self._a) 
        print("b = ", self.__b) 

obj = A()
obj.show()

# Access by the object of the same class in which these variable are declared otherwise you will now get the undefined error eg : print(_a) # undefined 
print(obj._a) # ACCESS bcz it's protected
print(obj.__b) # NOT ACCESS bcz it's private