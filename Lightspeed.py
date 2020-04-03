#Author : Joseph Emmanuel
#April 2020







choice=input("enter l for lightspeed to kmph or k for kmph to lightspeed:")

if choice=="l":
    k=float(input("please enter a number in kilometer:"))
    m=k/1.609344
    print(k,"kilometers = ",m," miles")    

if choice=="m":    
    m=float(input("please enter a number in miles:"))
    k=m*1.609344
    print(m,"miles = ",k," kilometers")
    
    
