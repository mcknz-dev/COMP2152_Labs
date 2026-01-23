# Solution for the week 02
import random

choices = ["Rock", "paper", "scissors"]

playerChoice = input("Choose a number between the following list: 1-Rock, 2-Paper, 3-Scissors: ")

playerChoice = int(playerChoice)

# User Input check
if playerChoice < 1 or playerChoice > 3:
    print("Error: You should choose a number between 1 and 3!")
else:
    computerChoice = random.randint(1, 3)

    #Determine the winner logic using if/elif/else

    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissors - You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rock - You win!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats Paper - You win!")
    else:
        print("You lose!")
