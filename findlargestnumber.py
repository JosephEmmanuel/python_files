# This is my program which finds the largest number in a list.
# It is very simple.
# Made by : Joseph Emmanuel
# Date : April 2019

numlist=[1,2,3,4,7,12,17,28,17]

ln=numlist[0]
for currnumber in numlist:
    if currnumber > ln:
        ln = currnumber
        
    print(currnumber, ln)
    
print("largest number in ",numlist, " is ", ln)

