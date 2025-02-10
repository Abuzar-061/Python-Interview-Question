import random

maliha_guess = 0
abuzar_guess = 0

def get_abuzar_guess():
    return int(input("Guess the Number Abuzar between 1-6: "))

def get_maliha_guess():
    return int(input("Guess the Number Maliha between 1-6: "))

while True:
    abuzar_guess = get_abuzar_guess()
    maliha_guess = get_maliha_guess()
    value = random.randint(1, 6)
    if abuzar_guess == value and maliha_guess == value:
        print("Both are correct")
        abuzar_guess += 1
        maliha_guess += 1
    elif abuzar_guess == value:
        print("Abuzar is correct")
        abuzar_guess += 1
    elif maliha_guess == value:
        print("Maliha is correct")
        maliha_guess += 1
    else:
        print("Both are incorrect")
        print("The number is: ", str(value))
