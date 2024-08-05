list =  [1,2,3,4,5]

last_index = int(len(list)) - 1

i = 0
j = last_index


list[i] , list[j] = list[j] , list[i]

print(list)