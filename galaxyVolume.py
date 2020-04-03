#Author : Joseph Emmanuel
#April 2020

import math

#Volume of Galaxy

#Dist in light years
ANDROMEDA_HEIGHT=1000
ANDROMEDA_RADIUS=110000


#Dist in light years
MILKYWAY_HEIGHT=1000
MILKYWAY_RADIUS=52850


def vol_cylinder(r,h):
    """return the volume of cylinder using radius r """
    v=math.pi*h*r**2
    return v


volofgalaxy_am=vol_cylinder(ANDROMEDA_RADIUS, ANDROMEDA_HEIGHT)
print("Volume of Andromeda galaxy=",volofgalaxy_am, " cubic lightyears")


volofgalaxy_mw=vol_cylinder(MILKYWAY_RADIUS, MILKYWAY_HEIGHT)
print("Volume of Milkyway galaxy =",volofgalaxy_mw, " cubic lightyears")

print ("Andromeda and Milkyway Galaxies will merge in 4 billion years to form Milkomeda Galaxy")

print("Volume of Milkomeda galaxy =",(volofgalaxy_am + volofgalaxy_mw), " cubic lightyears")
