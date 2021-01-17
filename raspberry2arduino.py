import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.OUT )
drinkAt=0                          #the drink the machine is currently at
drinkTo=2                          #The drink the machine has to go to
amountOfSpots=12
timePerBucket=0.5

distance1= drinkTo-drinkAt         #the distance counterclockwise
distance2= distance1- amountOfSpots  #the distance clockwise



#print(distance1) this was a test probably unessissery by now
#print(distance2)

if (distance1<=distance2):
    travelTime = timePerBucket * (distance1)
    GPIO.output(8, GPIO.HIGH)   #should change to depending on how the motor works but for now this makes it testable
    print('Switch status = ', GPIO.input(10))
    time.sleep(travelTime)           #wait for the time it takes to get to the destination
    GPIO.output(8, GPIO.LOW)     #machine has to stop here
    print('Switch status = ', GPIO.input(10))
    drinkAt=drinkTo
    print(drinkAt)                   #just to test

#this is the same as above but then in reverse for it to go clockwise in stead of counter
else:
    travelTime=0.5 * (distance2)
    GPIO.output(8, GPIO.LOW)
    print('Switch status = ', GPIO.input(10))
    time.sleep(travelTime)
    GPIO.output(8, GPIO.HIGH)
    print('Switch status = ', GPIO.input(10))
    drinkAt=drinkTo
    print(drinkAt)
