import time
import math
from gpiozero import MCP3008
from RpiMotorLib import rpi_dc_lib
import board
import digitalio
from adafruit_motor import stepper
import RPi.GPIO as GPIO


print("hardwareController loaded")

amountOfSpots = 14
channel = MCP3008(0)

def findPosition(): #returns the position found by MCP3008
    return math.floor(channel.value * amountOfSpots)


def travelTo(spot):
    motor = rpi_dc_lib.L298NMDc(20 ,21 ,16 ,50 ,True , "motor")
    direction = 1
    currentSpot = findPosition() 
    if currentSpot is not spot:
        # finds fastest direction to travel to spot
        if currentSpot > spot:
            distance = (spot - currentSpot) + amountOfSpots
        elif currentSpot < spot:
            distance = (spot - currentSpot)
        if distance > amountOfSpots / 2:
            direction = -1
        while findPosition() is not spot:
            if direction == 1:
                motor.forward(50) #turns the motor in in the direction necessary
            else:
                motor.backward(50)
        

        motor1.brake(0) #stops the motor
    else:
        print("Not moving. Spot has already been reached.")


def moveStraw(direction):
    out1 = 3
    out2 = 2
    in1 = 4
    in2 = 14

    GPIO.setup(out1,GPIO.OUT)
    GPIO.setup(out2,GPIO.OUT)
    GPIO.setup(in1, GPIO.IN)
    GPIO.setup(in2, GPIO.IN)
    
    if(direction is "UP"):
        GPIO.output(out1,GPIO.HIGH)
        GPIO.output(out2,GPIO.LOW)
        time.sleep(1)
        print(GPIO.input(in1))
        print(GPIO.input(in2))
        print("doing something")
        
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.HIGH)
        time.sleep(1)
        print(GPIO.input(in1))
        print(GPIO.input(in2))
        
        GPIO.output(out1,GPIO.HIGH)
        GPIO.output(out2,GPIO.HIGH)
        time.sleep(1)
        print(GPIO.input(in1))
        print(GPIO.input(in2))
    else:
        GPIO.output(out1,GPIO.LOW)
        GPIO.output(out2,GPIO.HIGH)
        time.sleep(5)
        GPIO.output(out1,GPIO.HIGH)
        GPIO.output(out2,GPIO.LOW)
        time.sleep(5)
        GPIO.output(out1,GPIO.HIGH)
        GPIO.output(out2,GPIO.HIGH)
        

    


        
moveStraw("UP")


def pump(volume,direction):
    pump = rpi_dc_lib.L298NMDc(19,13,26,100,True,"pump")
    

    if direction is "DOWN":
        pump.forward(100)
        time.sleep(volume)
    else:
        pump.backward(100)
        time.sleep(volume)
    pump.stop(0)

        
