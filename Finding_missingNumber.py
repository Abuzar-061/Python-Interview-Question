def find_missing_number(numbers):
    n = 8  # Since we know the numbers are from 1 to 8
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(numbers)
    return total_sum - actual_sum

missing_number = find_missing_number([1, 2, 3, 4, 6, 7, 8])
print(missing_number)
