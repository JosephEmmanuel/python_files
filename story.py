# This is a random stor generator.
# not fully complete
# 
# Developed by : Joseph Emmanuel
# Date :  May 2019

import random


print("Hello reader")
readername=input("What's your name?:")


print(" Hello " + readername)


names=[" Mrs doe"," Mr crow"," Miss mouse"," Mr tetris"]
places=[" TET jungle", " tret jungle"]
deeds=[" Mrs Doe told her friends the very bad news"," then crow told the good news"," friends fed the next day"," Mr tetris went missing"]
roles=[" deer"," crow"," mouse"," tortoise"]

randomnames=random.choice(names)
randomplaces=random.choice(places)
randomdeeds=random.choice(deeds)
randomroles=random.choice(roles)

story=" Once upon a time, there were 4 friends called " + random.choice(names)+"," + random.choice(names)+"," + random.choice(names)+"," + random.choice(names) + "." + "They were a " +random.choice(roles)+ ","
story=story+ "a" + random.choice(roles)+"," + random.choice(roles)+"," + random.choice(roles)+"." + "They lived in a forest called" + random.choice(places)+ "." + "One day,something bad was going on so " + random.choice(names)
story=story + random.choice(deeds) + random.choice(deeds) + "."+ "The" + random.choice(deeds) + "but" + random.choice(deeds) + "they looked for him but he had become friends with the TET, an ant which the forest was named after." + "THE END!"

print(story)
   
