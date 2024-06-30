# How to swap first and last element of list

list = [1,2,3,4,5,6]

lastindex = len(list)

i , j = 0 , int(lastindex)

j = int(lastindex) - 1

list[i],list[j] = list[j], list[i]

print(list)