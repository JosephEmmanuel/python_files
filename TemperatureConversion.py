# This is a program to convert c -> f or f->c based on user's choice.
# 
# Developed by : Joseph Emmanuel
# Date :  May 2019

choice=input("Enter c to convert C to F; Enter f to convert F to C: ")
if choice=="c":
    c=int(input("Please enter a number in Celcius Degrees: "))
    f=(c/5*9)+32
    print("A temperature of " , c , "Degree Celcuis =" , f , "Degree Farenheit.")


if choice=="f":
    f=int(input("Please Enter A Number In Farenheit Degree: "))
    c=(f-32)*5/9
    print("A temperature of " , f , "Degree Farenheit =" , c , "Degree Celcius.")
    









