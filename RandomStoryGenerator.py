# This is a random python story generator
# Made by: Joseph Emmanuel
# Date: May 2019

import random


print("Hello reader")
readername=input("What's your name? ")


print(" Hello " + readername)


names=[" Mr Hound"," Mr Buck"," Mrs Duck"]
places=[" Belle beach"," Ducker's Duck Pen"," Yonder Farmhouse"," Typhus hills"," Superstition Cottage"]
roles=[" Doggie"," Mouse Deer"," Duckie"]


randomnames=random.choice(names)
randomplaces=random.choice(places)
randomroles=random.choice(roles)

story=" Once upon a time, there was a beach called" + randomplaces + " ." + " There was a house on the beach where the owner of the beach lived. Outside the owners house was a duck pen dubbed"
story=story + randomplaces + " ." + " There was a shed a fathom away from the duck pen. In the shed was a"
story=story+ randomroles + " named" + randomnames + "In the duck pen was a" + randomroles + " called" + randomnames + " ." + " The brother of the owner of the beach owned a farmhouse called" + randomplaces
story=story+ " ." + " There was a" + randomroles + " called" + randomnames + " which lived in a kennel outside the farmhouse and gaurded it" + " ." + randomnames + " laid eggs for the beach owner although he was cruel"   
story=story+ " to her and her shed friend," + randomnames + " ." + " s" 

print(story)





