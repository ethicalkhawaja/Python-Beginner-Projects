import random

player = input("Choose rock, paper, or scissors:")

computer = random.randint(1, 3)

if computer == 1:
    computer = "rock"
elif computer == 2:
    computer = "paper"
else:
    computer = "scissors"

print("You chose:", player)
print("Computer chose:", computer)

if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "paper" and computer == "rock":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win!")
else:
    print("You lose!")
