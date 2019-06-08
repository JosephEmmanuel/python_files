# program to print a diamond of asterisks

# Author: Joseph Emmanuel
# Date: 7 June 2019

x=10 # Variable for spaces

for i in range(1,18,2):
    print(" "*x+i*"*")
    x=x-1
e=3 

for i in range(15,0,-2):
    print(" "*e+i*"*")
    e=e+1
