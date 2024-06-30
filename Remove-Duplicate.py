old_array = [1,1,2,2,3,3,4,5]
# Output should be [1,2,3,4,5]

new_array = []

for i in old_array:
    if i not in new_array:
        new_array.append(i)

print(new_array)