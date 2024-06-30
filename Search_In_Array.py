list = [1,2,3,4,5]

search = int(input("Enter the number you want to search: "))

if search in list:
    print(list.index(search))