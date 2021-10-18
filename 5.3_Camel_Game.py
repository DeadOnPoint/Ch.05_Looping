'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
import math
import time

again = "y"

while again.lower() == "y" or again.lower() == "yes":
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
    oasis = 0 #the oasis variable
    hunt = 0 #hunt success
    radio = 0 #radio success

    inst = str(input("Would you like instructions? "))
    if inst.lower() == "y" or inst.lower() == "yes": #if instructions are chosen
        print('''
          Welcome to Halo chase, you are an ONI ODST who needs to travel 2000 miles back to base through the desert 
          with vital intelligence for the war.
          However, you were discovered by the Covenant and a hoard of Elites and Grunts are chasing you.
          Your decisions will decide whether or not you will be caught.
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
          B) Ahead max speed (goes 300 miles)
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
    while not done: #ask for commands
        if enemies <= 100 and enemies > 0: #when the covenant is close to you
            print("The Covenant is close!")
        elif enemies <= 0:
            print("The Covenant has caught you!")
            done = True
            break
        else:
            pass
        if thirst >= 4 and thirst < 6: #when you are starting to get thirsty
            print("You are thirsty, take a break soon and stop to drink, eat and rest.")
        elif thirst >= 6: #when you die of thirst
            print("You died of thirst!")
            done = True
            break
        elif hunger >= 6: #when you die of hunger
            print("You died of hunger!")
            done = True
            break
        elif hunger >= 4 and hunger < 6: #when you are starting to get hungry
            print("You are hungry, take a break soon to stop to eat, drink, and rest.")
        elif tank <= 10 and tank >0: #when your gas tank is running low
            print("You are running low on gas!")
        elif tank <= 0: #when your gas tank is empty
            print("You have run out of gas!")
        else:
            pass
        if dist >= 2000: #when you win the game
            print("You made it back to base! The intelligence you delivered will help us win the war!")
            done = True
            break
        else:
            pass
        if oasis == 7: #when you find an oasis
            print("You found an oasis! Your canteen is refilled and your thirst has been refreshed.")
            canteen = 6
            thirst = 0
        com = str(input("COMANDS\nA) Ahead medium speed (goes 200 miles)\nB) Ahead max speed (goes 300 miles)\nC) Refill Warthog\nD) Make camp, rest and eat and drink for the night\nE) Hunt for more provisions\nF) Status check\nG) Attempt to radio base\nH) Give up\n "))
        if com.lower() == "h": #give up/quit command chosen
            print("Good job, you decided to give up and fight against the Covenant.\nYou lost horribly and were riddled with plasma blasts. We lost the war because of you.")
            done = True
            break
        elif com.lower() == "f": #status check command chosen
            print("Miles traveled: ", dist, "\n Drinks in canteen: ", canteen, "\n Days of rations remaining: ", rations, "\n Gallons left in the tank: ", tank, "\n The Covenant is", dist - enemies, "miles behind you.")
        elif com.lower() == "d": #rest command chosen
            if rations >= 0: #weather or not you have rations
                print("You ate well and your hunger has been refreshed.")
                rations = rations - 1
                hunger = 0
            else:
                print("----------WARNING----------\nYou are out of provisions! Hunt to survive!")
                hunger = hunger + 1
            if canteen >= 0: #weather or not you have water left in your canteen
                print("You drank one drink out of your canteen and your thirst has been refreshed")
                canteen = canteen - 1
                thirst = 0
            else:
                print("----------WARNING----------\nYou are out of water! Look for an oasis.")
                thirst = thirst + 1
            if rations >= 0 and canteen >= 0:
                enemies = enemies + (10 * random.randint(15, 23))
        elif com.lower() == "a": #warthog moves at medium speed
            print("You and your Warthog are moving at a decent pace across the desert sands.")
            dist = dist + 200
            tank = tank - 2
            thirst = thirst + 1
            hunger = hunger + 1
            oasis = random.randint(1,20)
            enemies = enemies + (10 * random.randint(15, 23))
        elif com.lower() == "b": #wagthog moves at max speed
            print("You and your Warthog are burning across the desert sands, you cannot maintain this pace for long though.")
            dist = dist + 300
            tank = tank - 5
            thirst = thirst + 1
            hunger = hunger + 1
            oasis = random.randint(1,10)
            enemies = enemies + (10 * random.randint(15, 23))
        elif com.lower() == "e": #hunting
            hunt = random.randint(1,3)
            rations = rations + hunt
            thirst = thirst + 1
            print("Your success from hunting is", hunt, "rations added to your remaining rations.")
            enemies = enemies + (10 * random.randint(15, 23))
        elif com.lower() == "g": #radio attempts
            radio = random.randint(1,50)
            if radio == 30:
                print("You successfully radioed base and was picked up...\nYou made it to base and your intelligence was invaluable to the war.")
                done = True
                break
            else:
                print("You were uncessessful in radioing base. You lost a day and the Covenant got closer.")
                hunger = hunger + 1
                thirst = thirst + 1
                enemies = enemies + (10 * random.randint(15, 23))
        elif com.lower() == "c": #refills warthog
            tank = 20
            enemies = enemies + (10 * random.randint(15, 23))
            thirst = thirst + 1
            hunger = hunger + 1
            print("Your warthog tank has been refilled, the Covenant has gotten closer though.\nThe Covenant are", dist - enemies, "miles away.")
    if done == True:
        again = str(input("Would you like to try again?"))
        if again.lower() == "y" or again.lower() == "yes":
            pass
        else:
            print("Fine then.")
            print("I didn't want to play again either.")
            break