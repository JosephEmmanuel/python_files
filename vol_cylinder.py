#Author : Joseph Emmanuel
#April 2020

import math

def vol_cylinder(r,h):
    """return the volume of cylinder using radius r """
    v=math.pi*h*r**2
    return v




r=float(input("Please enter the radius in centimeters:"))
h=float(input("Please enter the height in centimeters:"))
v=vol_cylinder(r,h)
print("For radius of ",r," cm and height of ",h," cm, the cylinder's volume is ",v,".")

  
