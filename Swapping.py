# Define the list
numbers = [1, 2, 3, 4, 5]

# Before Swapping 
print("List before swapping: ",numbers)

# Indices of the numbers to swap
i, j = 1, 3

# Swap the numbers
numbers[i], numbers[j] = numbers[j], numbers[i]

# Print the modified list
print("List after swapping: ",numbers)


