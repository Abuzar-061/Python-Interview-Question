# A namespace in Python holds the names of variables, functions, classes, and other objects in the current scope.

x = 10  # Global namespace

def func():
    y = 5  # Local namespace
    print("Inside func:", y)

func()
print("Outside func:", x)
