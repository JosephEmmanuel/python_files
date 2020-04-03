#Falling body simulation
#Author Ronald Jasper  

import math

#earth's acceleration due to gravity, a constant in m/(sec square)
g=9.80665 

def distanceTraveledWhileFall(t):
    #distance traveled by a body while falling for t seconds
    #d is in meters, t is in seconds
    d=0.5*g*t*t
    return(d)

def timeTakenToFall(d):
    #Time taken to fall d distance 
    #d is in meters, t is in seconds
    t=math.sqrt(2*d/g)
    return(t)

def instantaneousVelocityAfterFallingElapsedTime(t):
    v=g*t
    return(v)    


def instantaneousVelocityAfterFallingDistance(d):
    v=math.sqrt(2*g*d)
    return(v)    

def mps2kmphr(mpc):
    #convert m/s to km/hr
    return(mpc/1000*3600)


c=input("choice: enter time or distance. t or d:")

if (c=="t"):
    time=float(input("Enter time in seconds:"))
    distance=distanceTraveledWhileFall(time)
    velocity=instantaneousVelocityAfterFallingElapsedTime(time)
    print("")
    print("Input time of fall:", time, " seconds or ", time/60.0, " minutes")
    print("Distance fell:", distance, " meters or ", distance/1000, " km")
    print("Velocity at that time:", velocity, " meters/second or ", mps2kmphr(velocity), " km/hour")
    print("")

if (c=="d"):
    distance=float(input("Enter distance of fall in meters:"))
    time=timeTakenToFall(distance)
    velocity=instantaneousVelocityAfterFallingDistance(distance)
    print("")
    print("Distance of fall:", distance, " meters or ", distance/1000, " km")
    print("Time of fall:", time, " seconds or ", time/60.0, " minutes")
    print("Velocity at that distance:", velocity, " meters/second or ", mps2kmphr(velocity), " km/hour")
    print("")