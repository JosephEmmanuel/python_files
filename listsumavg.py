# This is a program I made to find sum and average of list of numbers.
# 
# Developed by : Joseph Emmanuel
# Date :  May 2019


intlist=[0,2,4,4,7,10]
sum=0
for a in intlist:
    sum=sum+a

print("All numbers in list : ",intlist)
print("Sum of all numbers in intlist is: ",sum)
print("Number of numbers in intlist is: ",len(intlist))
print("Average of all numbers in intlist is: ",sum/len(intlist))
