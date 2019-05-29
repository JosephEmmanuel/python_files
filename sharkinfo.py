# This is a program to display shark data from data in list.
# 
# Developed by : Joseph Emmanuel
# Date :  May 2019

sharkNameList=["Blacktip", "Silvertip", "Whitetip", "Megamouth","WhaleShark", "DwarfLantern", "Hammerhead","Bonnethead"]
sharkLengthList=[1.5, 2.25, 1.8, 4.5, 12.6, 0.2, 6, 1.5] #in meters
sharkWeightList=[123, 162, 18, 750, 21500, 0.1, 580, 50 ] #in Kg

sharkInput=input("Enter Only a shark Name:")
foundFlag=False
for index in range(len(sharkNameList)):
    if sharkNameList[index]==sharkInput:
        print("shark Name=",sharkNameList[index])
        print("shark Weight=",sharkWeightList[index], " Kg")
        print("shark Lenght=",sharkLengthList[index], " meters")
        foundFlag=True

if foundFlag==False :
    print ("Error: Shark name not found in the List")







