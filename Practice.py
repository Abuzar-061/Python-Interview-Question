
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