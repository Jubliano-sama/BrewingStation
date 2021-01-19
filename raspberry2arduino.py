from MCP3008 import MCP3008
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.OUT )
drinkAt=0                          #the drink the machine is currently at
drinkTo=2                          #The drink the machine has to go to
amountOfSpots=12
voltPerSpot=3.3/amountOfSpots      #the change in voltage every next spot has
adc = MCP3008()                    #the code is now writes that it should work for MCP3008 we probably would use this but it should work with minor adaptations
curentVolt = (adc.read(channel = 0)/1023 *3.3)

distance1= drinkTo-drinkAt         #the distance clockwise
distance2= -(distance1-amountOfSpots) #the distance anticlockwise



#print(distance1) this was a test probably unessissery by now
#print(distance2)

if (distance1<=distance2):
    GPIO.output(8, GPIO.HIGH)   #should change to depending on how the motor works but for now this makes it testable
    print('Switch status = ', GPIO.input(10))
    while(currentVolt < voltPerSpot*drinkTo or currentVolt > voltPerSpot*(drinkTo+1)):    #this loop should break at destination
        time.sleep(0.01)           #wait for a little while for the loop
    GPIO.output(8, GPIO.LOW)     #machine has to stop here
    print('Switch status = ', GPIO.input(10))
    drinkAt=drinkTo
    print(drinkAt)                   #just to test

#this is the same as above but then in reverse for it to go anticlockwise in stead of normal
else:
    GPIO.output(8, GPIO.LOW)
    print('Switch status = ', GPIO.input(10))
    while(currentVolt > voltPerSpot*drinkTo or currentVolt < voltPerSpot*(drinkTo-1)):    #this loop should break at destination
        time.sleep(0.01)           #wait for a little while for the loop
    GPIO.output(8, GPIO.HIGH)
    print('Switch status = ', GPIO.input(10))
    drinkAt=drinkTo
    print(drinkAt)
