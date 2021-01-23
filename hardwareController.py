import math
from gpiozero import MCP3008

print("hardwareController loaded")

amountOfSpots = 12
channel = MCP3008(0)


def findPosition():
    return math.floor(channel.value * 12)


def travelToSpot(spot):
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
            # motor.on(direction)
            print("Motor is on")
        # motor.off()
        print("Motor is off")
    else:
        print("Not moving. Spot has already been reached.")
