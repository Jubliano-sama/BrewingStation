import math
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)
amountOfSpots = 12


def FindPosition():
    return math.floor((chan.voltage()) / 3.3)


def TravelToSpot(spot):
    direction = 1
    currentSpot = FindPosition()
    #finds fastest way to travel to spot
    if currentSpot > spot:
        distance = (spot - currentSpot) + amountOfSpots
    elif currentSpot < spot:
        direction = (spot - currentSpot)
    if distance > amountOfSpots / 2:
        direction = -1
    while(FindPosition() is not spot):
        #motor.on
        print("Motor is on")
    #motor.off
    print("Motor is off")



