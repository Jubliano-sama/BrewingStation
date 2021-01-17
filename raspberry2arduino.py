import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.OUT )
drinkAt=0
drinkTo=2

distance1= drinkTo-drinkAt
if(distance1 < 0):
    distance1 += 12
if(drinkAt>=6):
    distance2= drinkAt - drinkTo
    if(distance < 0):
        distance2 += 12
else:
    distance2 = drinkAt + (12-drinkTo)


print(distance1)
print(distance2)

if (distance1<=distance2):
    travelTime = 0.5 * (distance1)
    GPIO.output(8, GPIO.HIGH)
    print('Switch status = ', GPIO.input(10))
    time.sleep(travelTime)
    GPIO.output(8, GPIO.LOW)
    print('Switch status = ', GPIO.input(10))
    drinkAt=drinkTo
    print(drinkAt)

else:
    travelTime=0.5 * (distance2)
    GPIO.output(8, GPIO.LOW)
    print('Switch status = ', GPIO.input(10))
    time.sleep(travelTime)
    GPIO.output(8, GPIO.HIGH)
    print('Switch status = ', GPIO.input(10))
    drinkAt=drinkTo
    print(drinkAt)
