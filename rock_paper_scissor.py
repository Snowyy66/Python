import random
options = ("rock","paper","scissors")
player = None
computer = random.choice(options)
while player not in options:
    player = input("Enter a choice (rock, paper, scissor) : ")
print(f"player : {player}")
print(f"computer : {computer}")

if player == computer:
    print("It's a tie !")
elif player == "rock" and computer == "scissors":
    print("you win !")
elif player == "rock" and computer == "paper":
    print("you win !")
elif player == "paper" and computer == "rock":
    print("you lose !")
elif player == "scissors" and computer == "rock":
    print("you lose !")
elif player == "paper" and computer == "scissors":
    print("you lose !")
elif player == "scissors" and computer == "paper":
    print("you win !")