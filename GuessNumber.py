import random

score = 0

while True:
    number  = int(input("Guess the number b/w 1-6:"))
    guess_number = random.randint(1,6)

    if number == guess_number:
        score += 1
        print("You Win")
        print(f"Score : {score} ")
    else:
        print(f"You lose the number is not {number} the Number is {guess_number}")
        print(f"Score : {score} ")
        break
