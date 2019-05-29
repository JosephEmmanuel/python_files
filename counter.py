
# This is a digital counter program I have made and is simple.
# It counts to 9.
# Developed by : Joseph Emmanuel
# Date :  May 2019

import  sys
import time

for i in range(10):
    print(i, end='') # print the number 

    sys.stdout.flush()
    time.sleep(1)   

    print("\b", end='') # erase the number using backspace
