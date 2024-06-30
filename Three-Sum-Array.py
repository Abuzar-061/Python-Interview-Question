arr = [1,2,3,4,5]

# Task is that you have to add three numbers that are present in the array and the sume of that numbers must be equal to 7 


for i in arr:
    for j in arr:
        for k in arr:
            if i != j != k:
                if i+j+k == 7:
                    print(i,j,k)