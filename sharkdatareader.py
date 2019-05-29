# This is a program to read a text file having shark data.
# 
# Developed by : Joseph Emmanuel
# Date :  May 2019

sharkdata=open('sharkdata.txt')

for line in sharkdata:
    #print(line)
    (sharkname, sharklength, sharkweight,dummy)= line.split(",")
    
    print("shark Name=", sharkname)
    print("shark Weight=", sharkweight, "Kg")
    print("shark Lenght=", sharklength, "meters")
    print("")
    
sharkdata.close()
