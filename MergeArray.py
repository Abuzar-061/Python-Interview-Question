def mergearray(arrayA,arrayB):
    # Merge arrayA and arrayB
    # Remove the duplicate
    # Sort the list in to ascending order 
    # new_array = []
    # for i in arrayA:
    #     if i not in new_array:
    #         new_array.append(i)
    # for j in arrayB:
    #     if j not in new_array:
    #         new_array.append(j)
    # new_array.sort()
    # return new_array
    return sorted(set(arrayA+arrayB))

print(mergearray([1,2,3,4],[1,2,3,4,5,6,7]))