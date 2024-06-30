# *
# **
# ***
# ****

def triangle():
    # Your code here ...
    for i in range(0,5):
        print('*' * i)
    pass

triangle()

print(" --------------------New shape-------------------- ")



#       *         
#      ***        
#     *****       
#    *******      
#     *****       
#      ***        
#       *   

def shape():
    for x in range(7):
        print(" " * (7 - x), "*" * (2*x + 1))
    for x in range(7 - 2, -1, -1):
        print(" " * (7 - x), "*" * (2*x + 1))

    pass

shape()


