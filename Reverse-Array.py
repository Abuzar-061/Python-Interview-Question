def ar(array):
    return array[::-1]


arr = [1,2,3,4,5,5]
new_array = []
for items in arr:
    if items not in new_array:
        new_array.append(items)
reversed_array = ar(new_array)

print(reversed_array)

# Method 2 


def aarray(array):
    return array[::-1]


reverse  = aarray([1,2,3,4,5,6])

print(reverse)