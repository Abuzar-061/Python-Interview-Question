# return sends back the final result and stops the function.
# yield sends one result at a time and pauses the function so it can continue later.

def ret():
    return [1,2,3]

print(ret())

def yiel():
    yield 1
    yield 2
    yield 3
number = []
for num in yiel():
    number.append(num)

print(number)