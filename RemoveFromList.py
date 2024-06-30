list = [1,2,3,0,2,0]
# TASK ==> Move 0 to the end of the list  
for item in list:
    if item == 0:
        list.remove(item)
        list.append(item)

print(list)