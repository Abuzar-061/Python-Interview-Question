array = [[1,2,3],[4,5],[6]]

# output should be [1,2,3,4,5,6]

new_array = []

for main_list in array: # Iterates through each sublist within the main list 
    for items in main_list: # Iterates thought each items within the sublist 
        new_array.append(items)
print(new_array)


print("Filter Even-Odd Array")

arr = [1,2,3,4,5,6,7,8]

even_arr = []
odd_arr = []

for i in arr:
    if i%2 == 0:
        even_arr.append(i)
    else:
        odd_arr.append(i)

print(even_arr)
print(odd_arr)

print("Flatter More Complex Nested Array")

arrr = [1,2,[3,4],5]
new_arrayy = []

for i in arrr:
    if isinstance(i,list):
        for j in i:
            new_arrayy.append(j)
    else:
        new_arrayy.append(i)
print(new_arrayy)

# Another Flatten array with all elements inside it 1d , 2d ,3d

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, int):
            flat_list.append(item)
        else:
            flat_list.extend(flatten(item))
    return flat_list

nestedlist = [1, 2, 3, [4, 5], [[6, 7]]]
print(flatten(nestedlist))