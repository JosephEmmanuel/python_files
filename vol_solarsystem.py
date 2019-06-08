# volumne of sphere using its radius
# calculate the volume of planets and the solar system
#
# Author : Joseph Emmanuel
# Date : March 2019


import math


def vol_sphere(r):
	"""return the volumne of sphere using radius r """
	v=(4.0/3.0)*math.pi*r**3
	return v


planets_name=["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
planets_radius=[2439.7, 6051.8, 6371.0, 3389.5, 69911.0, 58232.0, 25362.0, 24622.0, 1188.3 ]
planets_vol=list()

sun_radius=695700.0
sun_vol=vol_sphere(sun_radius)

i=0
total_vol_planets=0.0
for eachplanet_radius in planets_radius:
	v = vol_sphere(eachplanet_radius)
	planets_vol.append(v)
	total_vol_planets = total_vol_planets + planets_vol[i]
	print("i = ",i," Radius of ", planets_name[i], " = ", planets_radius[i]," km.  Volumn of ", planets_name[i], " = ", planets_vol[i], " km^3")
	i=i+1

print("")
print (" Total volume of 9 planets = ", total_vol_planets, " km^3")
print (" Total volume of Sun = ", sun_vol, " km^3")
print("")
print(" Volume of Asteriods, Satellites of Planets and Objects in Kuiper belt like Ultima Thule are not counted for the sake of simplicity. There are too many such objects. But they are quite small compared to the planets")
print("")

total_vol_solarsystem = total_vol_planets + sun_vol 
print (" Total volume of Sun & 9 planets = ", total_vol_solarsystem, " km^3")

print("")
print(" Percentage of Sun's volume to the planets volume", (1 - (total_vol_planets/total_vol_solarsystem))*100)



print (" How many Earths can fit into Jupiter's volume =",  planets_vol[4]/planets_vol[2])

print (" How many Jupiters can fit into Sun's volume =",  sun_vol/planets_vol[4])
print (" How many Earths can fit into Sun's volume =",  sun_vol/planets_vol[2])
