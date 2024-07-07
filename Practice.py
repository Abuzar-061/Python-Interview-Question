array = [[1,2,3],[4,5],[6]]

# output should be [1,2,3,4,5,6]

new_array = []
for i in array:
    for j in i:
        new_array.append(j)

print(new_array)