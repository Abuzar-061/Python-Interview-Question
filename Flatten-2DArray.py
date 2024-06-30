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