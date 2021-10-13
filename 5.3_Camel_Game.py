'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
import math

print("Welcome to the Halo chase game!")
print("By Will Jacobson")

dist = 0 #distance traveled
done = False #wether or not the game is complete
enemies = -20 #how far the Covenant has gone
com = "z" #the command that the user chose
thirst = 0 #how thirsty you are
tank = 20 #how much gas is in the warthog
canteen = 6 #how many drinks are in the canteen
rations = 3 #how many days of rations you have
hunger = 0 #how hungry you are

inst = str(input("Would you like instructions? "))
if inst.lower() == "y" or inst.lower() == "yes":
    print('''
          Welcome to Halo chase, you are an ONI ODST who needs to travel 2000 miles back to base through the desert 
          with vital inteligence for the war.
          However, you were discovered by the Covenant and a hoard of Elites and Grunts are chasing you.
          Your decisions will decide wether or not you will be caught.
          You are riding a Warthog with ample fuel, but seeing as you are alone, it will take a full day for you to
          refuel.
          You also have a canteen that will last only 6 drinks, so ration yourself accordingly.
          You have 3 days of rations and will eat when you rest.
          You can also hunt for more food along the way.
          Good luck!
          ''')
    print('''
          COMMANDS:
          A) Ahead medium speed (goes 200 miles)
          B) Ahead max speed (goes 400 miles)
          C) Refill Warthog
          D) Make camp, rest and eat and drink for the night
          E) Hunt for more provisions
          F) Status check
          G) Attempt to radio base
          H) Give up
          ''')
    print('''
          When you hunt you have a chance of receiving from 1 to 3 day's rations.
          You can run upon a well/natural spring to refill your water with.
          If you can radio base you get picked up by a Pelican and win.
          Good luck and get us that intel!
          ''')
else:
    pass
while not done:
    com = str(input("COMANDS\nA) Ahead medium speed (goes 200 miles)\nB) Ahead max speed (goes 400 miles)\nC) Refill Warthog\nD) Make camp, rest and eat and drink for the night\nE) Hunt for more provisions\nF) Status check\nG) Attempt to radio base\nH) Give up\n "))
    if com.lower() == "h":
        print("Good job, you decided to give up and get caught by the Covenant. We lost the war because of you.")
        done = True
        break
    elif com.lower() == "f":
        print("Miles traveled: ", dist, "\n Drinks in canteen: ", canteen, "\n Days of rations remaining: ", rations, "\n Gallons left in the tank: ", tank, "\n The Covenant is", math.fabs(dist - math.fabs(enemies)), "miles behind you.")
    elif com.lower() == "d":
        tank = 20
        print("The Warthog tank is full.")
        hunger = 0
        print("You ate well and your hunger has been refreshed.")
        rations = rations - 1
        enemies = enemies + random.randint(7,14)