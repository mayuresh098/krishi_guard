'''Program to rotate BASE SERVO MOTOR 360 degrees, in Python.'''

#Importing Libraries
#from pyfirmata import *
from pyfirmata import Arduino
from pyfirmata import INPUT, OUTPUT, PWM, SERVO
from time import sleep
from intruderDetection import *
from buzzer.py import *


#Connecting Computer to Arduino board, required only for the first time.
port = '/dev/cu.usbmodem46'
board=Arduino(port)

#Connecting to the arduino pins
#For both the base servos.
board.digital[9].mode=SERVO
board.digital[8].mode=SERVO
#board.analog[0].mode=INPUT
#Sleep command to let the arduino and computer sync.
sleep(5)
pin1=9
pin2=8
angle=360

command=input('Press 1. To start operation. Press 2. To stop operation.')
try :
  if command=='1':
    start1(pin1,angle)
    start2(pin2,angle)
  else :
    stop()

except Error as e:
  print(''+str(e))

#The function
def start1(pin1, angle):
  board.digital[pin1].write(angle)
  sleep(0.015)

  while true:
    for i in range(0,angle,2):
        #If intruder detected then rotation will stop for 1 minute.
        if intruderDetected()==1:
          
          sleep(60000)
        else:
          start(pin1,i)
          #Else it will keep on rotating.

#The function
def start2(pin2 angle):
  board.digital[pin2].write(angle)
  sleep(0.015)

  while true:
    for i in range(0,angle,2):
        #If intruder detected then rotation will stop for 1 minute.
        if intruderDetected()==1:
          sleep(60000)
        else:
          start(pin2,i)
          #Else it will keep on rotating.

def stop():
  #Command to make the Arduino 'do nothing', to be used only while repair or modification.
  void()



  

