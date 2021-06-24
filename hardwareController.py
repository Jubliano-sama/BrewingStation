import time
import math
from gpiozero import MCP3008
from RpiMotorLib import rpi_dc_lib

print("hardwareController loaded")

amountOfSpots = 16
channel = MCP3008(0)


def findPosition():
    return 0#math.floor(channel.value * 12)


def travelToSpot(spot):
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
        #while findPosition() is not spot:
            # motor.on(direction)
            if direction == 1:
                motor.forward(50)
            else:
                motor.backward(50)
        

        motor.brake(0)
    else:
        print("Not moving. Spot has already been reached.")

def pump(timer):
    pump = rpi_dc_lib.L298NMDc(19,13,26,100,True,"pump")
    pump.forward(100)
    time.sleep(timer)
    pump.stop(0)
