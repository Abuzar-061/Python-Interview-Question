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

# Combine multiple Dictionary into single dictionary 


from collections import defaultdict

# List of dictionaries to aggregate
dicts = [
    {'a': 1, 'b': 2},
    {'a': 3, 'c': 4},
    {'a': 5, 'b': 6, 'c': 7}
]

# Create a defaultdict of lists
aggregated_dict = defaultdict(list)

# Aggregate the dictionaries
for d in dicts:
    for key, value in d.items():
        aggregated_dict[key].append(value)

# Convert the defaultdict to a regular dictionary (optional)
aggregated_dict = dict(aggregated_dict)

print(aggregated_dict)
