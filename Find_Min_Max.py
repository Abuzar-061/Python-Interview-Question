arr = [1,2,3,4,6,5,5]
# TASK   Remove duplicates and find max and min number in the list 

array = sorted(set(arr))
print(array)

print("Min Value in the array :",array[0])
print("MAX Value in the array :",array[-1])