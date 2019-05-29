# This is a program I made to print multiplication table for the input number
# 
# Developed by : Joseph Emmanuel
# Date :  May 2019

mulstr=input("please enter a number:")
mul=int(mulstr)
for i in range(12):
    print(i,"X ",mul, " = ",i*mul)

print ("End")
