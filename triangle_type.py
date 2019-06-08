# To find the type of triangle

#scalene triangle:all sides are different.
#isoceles triangle:two sides are equal
#equilateral triangle:all sides are equal

# Author : Joseph Emmanuel
# Date : March 2019


v=int(input("The lenth of side v : "))
x=int(input("The lenth of side x : "))
l=int(input("The lenth of side l : "))

if v !=x and x !=l and l !=v:
	print("Scalene triangle")
elif v==x and x==l and l==v:
	print("Equilateral triangle")
else:
	print("Isoceles triangle")

