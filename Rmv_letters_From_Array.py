array = [1,2,3,4,'a','b','c','d']
# TASK => Separate integer and Alphabets || Make sure the Alphabet should be in uppercase
integer = []
Alphabet = []
for i in array:
    if isinstance(i,int):
        integer.append(i)
    else:
        Alphabet.append(i.upper())

print(integer)
print(Alphabet)