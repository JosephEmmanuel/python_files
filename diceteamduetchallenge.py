
# This is a program i have made : a dice game.
# The dice game is a simple program.
# Made by : Joseph Emmanuel
# Date : May 2018


import random

diceroll=[1,2,3,4,5,6]

# for player A rolling the dice 3 times

a1=random.choice(diceroll)
a2=random.choice(diceroll)
a3=random.choice(diceroll)

# add the 3 scores for player A
a=a1+a2+a3


# for player B rolling the dice 3 times

b1=random.choice(diceroll)
b2=random.choice(diceroll)
b3=random.choice(diceroll)

# add the 3 scores for player B
b=b1+b2+b3

print (" A scored : ", a)
print (" B scored : ", b)

# Player with highest score wins

if a > b:
    print("Player A  the winner has W-O-N!!")

if b > a:
    print("Player B  the winner has W-O-N!!")

if a == b :
    print("its a draw...")
