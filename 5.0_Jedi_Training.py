  #Sign your name: Will Jacobson

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = float(input("Enter a number: "))
    total = total + x
print("The total is:", total)

'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''

print("This program will print the even numbers from 2 - 100")

for i in range(2,101):
    if i % 2 == 0:
        print(i)
    else:
        print("")

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''

print("This program will count down from 10 and blast off!")
i = 10
while i >= 0:
    print(i)
    i -= 1
print("Blast off!")

'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
print(random.randint(1,10))


'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
print("This program will print the sum of your 7 numbers and will also print their properties.")
pos = 0
neg = 0
zero = 0
total = 0
for i in range(7):
    a = float(input("Value? "))
    total = total + a
    if a > 0:
        pos = pos + 1
    elif a < 0:
        neg = neg + 1
    else:
        zero = zero + 1
print("Your sum is, ", total, "You inputed ", pos, "positive numbers, ", neg, "negative numbers, and ", zero, "zeroes.")