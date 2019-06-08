# Author : Joseph Emmanuel
# Date : March 2019

#volumne of sphere using radius
import math


def vol_sphere(r):
	"""return the volumne of sphere using radius r """
	v=(4.0/3.0)*math.pi*r**3
	return v



r=float(input("enter radius : "))
v=vol_sphere(r)
print("volumne = " ,v)


