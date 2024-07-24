secret_word = "zeyad"
while True:
    guess = input("Enter a guess: ")
    if guess == secret_word:
        print("Valid Guess")
        break
    else:
        print("Invalid guess, please try again.")
