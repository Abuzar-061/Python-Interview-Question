list = [1,2,3,4,5,5,5,5,5,5,5,5,5,5,5]

occurence = int(input("Enter the number that you want to check the occurence: "))

count = 0

for i in list:
    if i == occurence:
        count += 1

print("{} is occured {} time".format(i, count))