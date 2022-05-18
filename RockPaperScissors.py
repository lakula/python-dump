print ("Rock...Paper...Scissors... SHOOT!")

# Computer plays Player2:
import random

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

# Take Player1 input:
player1_choice = (input("Player1 choose now... ")).lower()

if player1_choice in options:
    print (f"You chose... {player1_choice}")
else:
    print("Nice try! You have to choose from Rock... Paper... Scissors..")
    player1_choice = (input("Player1 try again... ")).lower()
    print (f"You chose..{player1_choice}")

print (f"Computer chose... {computer_choice}")

# Decide who won:
if player1_choice == computer_choice:
    print ("Ah! its a tie! Try again...")
elif player1_choice == "rock":
    if  computer_choice == "paper":
        print ("Computer Won!")
    else:
        print ("You won!")
elif player1_choice == "paper":
    if  computer_choice == "scissors":
        print ("Computer Won!")
    else:
        print ("You won!")
elif player1_choice == "scissors":
    if  computer_choice == "rock":
        print ("Computer Won!")
    else:
        print ("You won!")
else:
    print ("Something went wrong! Try Again")

print ("Good game!")