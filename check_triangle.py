# to check if the shape is a valid triangle
# Author : Joseph Emmanuel
# Date : March 2019

def find_third_angle(A1,A2):
	 return(180-(A1+A2)) 

a=int(input("Please enter Angle 1:"))


if a<0 or a>=180:
	print("Error! Angle 1 is invalid!")


b=int(input("Please enter Angle 2:"))


if b<0 or  b>=180:
	print("Error! Angle 2 is invalid!")


c=find_third_angle( a,b) 
print("Third Angle is : ",c)

