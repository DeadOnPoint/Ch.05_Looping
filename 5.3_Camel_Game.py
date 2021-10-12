'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

print("Welcome to the Halo chase game!")
print("By Will Jacobson")

dist = 0 #distance traveled
game = 0 #wether or not the game is complete
enemies = 100 #how far away the Covenant is
com = "z" #the command that the user chose

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
while game == 0: