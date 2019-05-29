# This is a program that can convert kilometers to miles and also miles to kilometers.
# First, choose your conversion, you can choose kilometer -> mile or mile -> kilometer.
#
# Author : Joseph Emmanuel
# Date : 18-April-2019
#
choice=input("enter k for kilometer to mile or m for mile to kilometer:")

if choice=="k":
    k=float(input("please enter a number in kilometer:"))
    m=k/1.609344
    print(k,"kilometers = ",m," miles")    

if choice=="m":    
    m=float(input("please enter a number in miles:"))
    k=m*1.609344
    print(m,"miles = ",k," kilometers")
    
    
