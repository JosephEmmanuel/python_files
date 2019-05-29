# This program is basically a digital clock.
# This prints the time on the screen.
# Made by : Joseph Emmanuel
# Date : May 2018


from datetime import datetime
import time
import  sys

print(" Digital Clock ")
print(" by - Joseph Emmanuel ")
print(" ")
print(" Digital Clock will run for 2 minutes")
print(" ")

for i in range(120):
    today=datetime.now()
    print(today.strftime("%H:%M:%S"), end='')
    sys.stdout.flush()

    time.sleep(1)
    print ('\b\b\b\b\b\b\b\b', end='')
    
