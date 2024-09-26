import random

score = 0
while True:
    guess_number =  random.randint(1,6)
    print(guess_number)
    your_number = int(input("Guess the number b/w 1-6:"))
    if your_number == guess_number:
        score += 1
        print("Correct! You Win.")
        print(f"Score: {score}")
    else:
        print("You Lose!")
        break