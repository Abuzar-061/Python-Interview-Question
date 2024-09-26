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