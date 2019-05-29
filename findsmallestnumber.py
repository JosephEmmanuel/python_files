# This is my program which finds the smallest number in a list.
# It is obviously simple.
# Made by : Joseph Emmanuel
# Date : April 2019 

numlist=[3,7,28,17,12,17, 1,2,4]

sm=numlist[0]
for currnumber in numlist:
    if currnumber < sm:
        sm = currnumber
    print(currnumber, sm)
    
print("smallest number in ",numlist, " is ", sm)
