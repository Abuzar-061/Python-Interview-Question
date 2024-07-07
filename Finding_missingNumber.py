# Find the missing number in the list of natural number
# Consider we have 8 natural numbers 1 2 3 4 6 7 8  
# In this we have to found which natural number is missing 

def find_missing_number(numbers):
    n = 8  # Since we know the numbers are from 1 to 8
    total_sum = n * (n + 1) // 2  # Sum of n natural numbers
    actual_sum = sum(numbers)
    return total_sum - actual_sum

missing_number = find_missing_number([1, 2, 3, 4, 6, 7, 8])
print(missing_number)
