# This is a program I made to convert meter to centimeter or cm to meter
# 
# Developed by : Joseph Emmanuel
# Date :  May 2019




choice=input("Enter m for meter to centimeter and cm for centimeter to meter:") 


if choice=="m":
    meter=float(input("please enter a number in meter:"))
    centim=meter*100
    print("distance in meters =",meter, " and the same in cm= ",centim)


if choice=="cm":
    centim=float(input("please enter a number in centimeter:"))
    meter=centim/100
    print("distance in meters =",meter, " and the same in cm= ",centim)


































































