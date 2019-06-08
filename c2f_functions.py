#convert celsius to farenht
# using functions
# Author : Joseph Emmanuel
# Date : March 2019

def ctof(celcius):
	faren=(celcius*9/5)+32
	return faren

def ftoc(faren):
	celsius=(faren-32)*5/9
	return celsius


c=float(input("enter celsius : "))
f=ctof(c)
print("Farenheit=",f)

c1=ftoc(f)
print("centegrade c=",c)
print("centegrade c1=",c1)


if c==c1:
	print( " we have verified our conversion" )
else:
	print( " Our conversion is not accurate or Wrong" )
 

