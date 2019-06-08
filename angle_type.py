# This module find the type of angle. """
# zero angle=0
# acute angle is >0 and <90
# obtuse angle is >90 and <180
# striaght angle is 180
# Right angle is 90
# Reflex angle is more than 180 and < 360(0)
#
# Author: Joseph Emmanuel
# March 2019


def ang_type(angle):
	"""finds out the type of angle for the given angle in degrees.
	Valid angles are from 0 to 360 degrees"""

	if angle == 0 or angle==360:
		return( " Zero angle " )
	elif angle > 0 and angle <90 :
		return( " Acute angle " )
	elif angle >90 and angle <180 :
		return( " Obtuse angle " )
	elif angle ==180 :
		return( " Striaght angle " )
	elif angle ==90:
		return( " Right angle " )
	elif angle <0 or angle >360:
		return( " Error! " )

	else :
		return( " Reflex angle " )
#end of function
	

a=int(input("Enter an angle 0 to 360 degrees only : "))
angletypestring=ang_type(a)
print("The entered angle is of type : ", angletypestring)
	


