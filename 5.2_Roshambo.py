'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random
wins = 0
losses = 0
ties = 0
comp = 0
roch = "a"
while roch != "n":
    roch = str(input("Rock (r), Paper (p) or Scissors (s), or quit "))
    comp = random.randint(1,3)
    if roch.lower == "rock" or roch.lower == "p":
        roch = 1
        if comp == 1:
            print("Computer chose rock as well! It's a Tie!")
            ties = ties + 1
        elif comp == 2:
            print("Computer chose paper! You Lost!")
            losses = losses + 1
        else:
            print("Computer chose scissors! You Won!")
            wins = wins = 1
    elif roch.lower == "paper" or roch.lower == "p":
        roch = 2
        if comp == 1:
            print("Computer chose rock! You Won!")
            wins = wins + 1
        elif comp == 2:
            print("Computer chose paper as well! It's a Tie!")
            ties = ties + 1
        else:
            print("Computer chose scissors! You Lost!")
            losses = losses + 1
    elif roch.lower == "scissors" or roch.lower == "s":
        roch = 3
        if comp == 1:
            print("Computer chose rock! You Lost!")
            losses = losses + 1
        elif comp == 2:
            print("Computer chose paper! You Won!")
            wins = wins + 1
        else:
            print("Computer chose scissors as well! It's a Tie!")
            ties = ties + 1
    elif roch.lower == "y" or roch.lower == "yes":
        break
    else:
        print("Please put in an actual choice or just quit the game dude.")
print("You won ", wins, "times, lost ", losses, "times, and you tied the computer ", ties, "times.")
print("Thanks for playing!")