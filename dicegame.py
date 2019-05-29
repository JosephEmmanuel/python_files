# This is the second dice game i have made.
# This dice game counts the points of the players and tells who has won.
# Made by : Joseph Emmanuel
# Date : May 2018


import random


diceroll=[1,2,3,4,5,6]

suma=0
for i in range(1):
    a=random.choice(diceroll)
    print(a, ", " , end="")
    suma=suma+a

print("Player A :", suma , "points!")


sumb=0
for i in range(1):
    b=random.choice(diceroll)
    print(b, ", " , end="")
    sumb=sumb+b

print("Player B :", sumb , "points!")



if suma > sumb:
    print("Player A  the winner has W-O-N!!")

if suma < sumb:
    print("Player B  the winner has W-O-N!!")

if suma == sumb :
    print("its a draw...")















