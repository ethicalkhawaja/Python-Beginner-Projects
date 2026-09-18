import random

secret_num = random.randint(1, 15)

for guesses in range(1, 6):
    guess = int(input("Enter your guess: "))

    if guess < secret_num:
        print("It's low, my friend.")
    elif guess > secret_num:
        print("It's higher.")
    else:
        print("That's it! You did well.")
        print("It took", guesses, "guesses and you made it!")
        break
else:
    print("You couldn't guess correctly.")
    print("The correct guess is", secret_num)
