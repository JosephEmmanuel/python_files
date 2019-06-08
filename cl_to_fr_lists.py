# convert celsius to farenht
# using functions and lists

# Author : Joseph Emmanuel
# Date : March 2019


def ctof(celcius):
	faren=(celcius*9/5)+32
	return faren


celciuslist=[-100, -50, 0 , 50, 100]
farenlist=list()

for c in celciuslist:
	f=ctof(c)
	farenlist.append(f)

print("celciuslist=",celciuslist)
print("farenlist=",farenlist)

