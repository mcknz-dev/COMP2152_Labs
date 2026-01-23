# Solution for the week 02

choices = ["Rock", "paper", "scissors"]

playerChoice = input("Choose a number between the following list: 1-Rock, 2-Paper, 3-Scissors: ")

playerChoice = int(playerChoice)

# User Input check
if playerChoice < 1 or playerChoice > 3:
    print("Error: You should choose a number between 1 and 3")
else:
    # Develop the game logic through if/elif/else
