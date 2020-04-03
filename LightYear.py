#Author : Joseph Emmanuel
#April 2020

#km/sec
SPEEDOFLIGHT=299792.458

#AU in kms
ASTRONOMICALUNIT=149597870.7

def convertLightYear2KM(ly):
    km=ly*SPEEDOFLIGHT*60.0*60.0*24.0*365.25
    return(km)


def convertKM2LightYear(km):
    ly=km/(SPEEDOFLIGHT*60.0*60.0*24.0*365.25)
    return(ly)

def convertAU2KM(au):
    km=au*ASTRONOMICALUNIT
    return(km)

def convertKM2AU(km):
    au=km/ASTRONOMICALUNIT
    return(au)

       

choice=input("enter l for lightyear to km or k for km to lightyear:")

if choice=="l":
    ly=float(input("please enter a number in lightyear:"))
    km=convertLightYear2KM(ly)
    print(km,"kilometers = ",ly," lightyears")    

if choice=="k":    
    km=float(input("please enter a number in kilometers:"))
    ly=convertKM2LightYear(km)
    print(km,"kilometers = ",ly," lightyears")
    
 
choice=input("enter a for AU to km or k for km to AU:")


if choice=="a":
    au=float(input("please enter a number in astronomical units:"))
    km=convertAU2KM(au)
    print(km,"kilometers = ",au," AU")    

if choice=="k":    
    km=float(input("please enter a number in kilometers:"))
    au=convertKM2AU(km)
    print(km,"kilometers = ",au," AU")
    





















             
