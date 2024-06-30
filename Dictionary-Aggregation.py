inv  = {
    "Apple": 1,
    "Banana": 2
}

new_inv = {
    "Apple": 1,
    "Banana": 2,
    "Orange": 3
}

# inv.update(new_inv)
# print(inv) # This method ignore the duplicate value and add the value that is not in the dictionary 



total_inv = {
    K : inv.get(K,0) + new_inv.get(K,0)
    for K in set(inv | new_inv)
}

print(total_inv)