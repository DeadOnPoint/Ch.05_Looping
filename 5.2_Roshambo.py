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
quit = "n"
comp = 0
while quit == "n":
    quit = str(input("Do you want to quit? (press y to quit, n to stay) "))
    if quit == "y":
        break
    elif quit == "n":
        print()
    else:
        print("INPUT THE ACTUAL ANSWER NEXT TIME JACKASS!!")
    roch = str(input("Rock, Paper or Scisors "))
    comp = random.randint(1,3)
    if roch.lower == "rock":
        roch = 1
        if comp == 1:
            print("Tie!")
            ties = ties + 1
        elif comp == 2:
            print("You Lost!")
            losses = losses + 1
        else:
            print("You Won!")
            wins = wins = 1
    elif roch.lower == "paper":
        roch = 2
        if comp == 1:
            print("You Won!")
            wins = wins + 1
        elif comp == 2:
            print("Tie!")
            ties = ties + 1
        else:
            print("You Lost!")
            losses = losses + 1
    else:
        roch = 3
        if comp == 1:
            print("You Lost!")
            losses = losses + 1
        elif comp == 2:
            print("You Won!")
            wins = wins + 1
        else:
            print("Tie!")
            ties = ties + 1
print("You won ", wins, "times, lost ", losses, "times, and you tied the computer ", ties, "times.")
print("Thanks for playing!")