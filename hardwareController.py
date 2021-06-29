import time
import math
from gpiozero import MCP3008
#from RpiMotorLib import rpi_dc_lib
import board
import digitalio
from adafruit_motor import stepper
import RPi.GPIO as GPIO


print("hardwareController loaded")

amountOfSpots = 14
channel = MCP3008(0)

def findPosition(): #returns the position found by MCP3008
    return math.floor(channel.value * amountOfSpots)


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
        while findPosition() is not spot:
            if direction == 1:
                motor.forward(50) #turns the motor in in the direction necessary
            else:
                motor.backward(50)
        

        motor1.brake(0) #stops the motor
    else:
        print("Not moving. Spot has already been reached.")


def moveStraw():
    out1 = 3
    out2 = 2
    out3 = 4
    out4 = 14
    
    i=0
    positive=0
    negative=0
    y=0
    
    
    
    GPIO.setup(out1,GPIO.OUT)
    GPIO.setup(out2,GPIO.OUT)
    GPIO.setup(out3,GPIO.OUT)
    GPIO.setup(out4,GPIO.OUT)
    
    
    
    try:
       while(1):
          GPIO.output(out1,GPIO.LOW)
          GPIO.output(out2,GPIO.LOW)
          GPIO.output(out3,GPIO.LOW)
          GPIO.output(out4,GPIO.LOW)
          x = input()
          if True:
              for y in range(200):
                  if negative==1:
                      if i==7:
                          i=0
                      else:
                          i=i+1
                      y=y+2
                      negative=0
                  positive=1
                  print(i)
                  if i==0:
                      GPIO.output(out1,GPIO.HIGH)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==1:
                      GPIO.output(out1,GPIO.HIGH)
                      GPIO.output(out2,GPIO.HIGH)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==2:  
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.HIGH)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==3:    
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.HIGH)
                      GPIO.output(out3,GPIO.HIGH)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==4:  
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.HIGH)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==5:
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.HIGH)
                      GPIO.output(out4,GPIO.HIGH)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==6:    
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.HIGH)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==7:    
                      GPIO.output(out1,GPIO.HIGH)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.HIGH)
                      time.sleep(0.03)
                      #time.sleep(1)
                  if i==7:
                      i=0
                      continue
                  i=i+1
          
          
          elif x<0 and x>=-400:
              x=x*-1
              for y in range(x,0,-1):
                  if positive==1:
                      if i==0:
                          i=7
                      else:
                          i=i-1
                      y=y+3
                      positive=0
                  negative=1
                  #print((x+1)-y) 
                  if i==0:
                      GPIO.output(out1,GPIO.HIGH)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==1:
                      GPIO.output(out1,GPIO.HIGH)
                      GPIO.output(out2,GPIO.HIGH)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==2:  
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.HIGH)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==3:    
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.HIGH)
                      GPIO.output(out3,GPIO.HIGH)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==4:  
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.HIGH)
                      GPIO.output(out4,GPIO.LOW)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==5:
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.HIGH)
                      GPIO.output(out4,GPIO.HIGH)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==6:    
                      GPIO.output(out1,GPIO.LOW)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.HIGH)
                      time.sleep(0.03)
                      #time.sleep(1)
                  elif i==7:    
                      GPIO.output(out1,GPIO.HIGH)
                      GPIO.output(out2,GPIO.LOW)
                      GPIO.output(out3,GPIO.LOW)
                      GPIO.output(out4,GPIO.HIGH)
                      time.sleep(0.03)
                      #time.sleep(1)
                  if i==0:
                      i=7
                      continue
                  i=i-1
    except KeyboardInterrupt:
        GPIO.cleanup()

        
moveStraw()


def pumpLiquid(timer):
    pump = rpi_dc_lib.L298NMDc(19,13,26,100,True,"pump")
    pump.forward(100)
    time.sleep(timer)
    pump.stop(0)
