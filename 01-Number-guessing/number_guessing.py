import random
secret_num = random.randint(1,15)
for guesses in range(1,6):
    guess = int(input("Enter your guess:"))
    if guess < secret_num:
        print("its low my friend")
    elif guess > secret_num:
        print("its higher.")
    else:
        break
if guess == secret_num:
    print("Thats it you did well here it took",guesses, "guesses and you made it")  
else:
    print("You couldn't guessed correctly so the correct guess is", secret_num)        

