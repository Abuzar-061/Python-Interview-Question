list = [1,2,3,4,5,'a','b']

alpha = []

number = []

for i in list:
    if isinstance(i, int):
        number.append(i)
    else:
        alpha.append(i)


print(number)
print(alpha)

# FIND THE SECOND LARGEST NUMBER IN THE NUMBAR ARRAY:

sorted(set(number))

seclargeindex = int(len(number)) - 2

print("Second Largest number is :", number[seclargeindex])