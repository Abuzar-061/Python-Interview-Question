word  =  "Madam" # Basically it is not palindrome bcz the starting M is capital but the last m is in lower case so after reversing it is madaM that is not equal to Madam
# So basically what is palindrome string it is a string that you can reverse it it is the same as before after reversing it 
def reversing(array):
    return array[::-1]
check = reversing(word)
if check == word:
    print("String is palindrome!")
else:
    print("String is not palindrome!")