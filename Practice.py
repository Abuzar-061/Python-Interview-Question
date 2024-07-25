value = input("Enter the String Value: ")
output = []
for i in value:

    if i not in output:
        output.append(i)
outputs = ' '.join(output)
print(outputs) 