'''Proogram to make a high-pitched noise using the Arduino Buzzer module'''

def buz():
#Importing the libraries
    from pyfirmata import Arduino
    from pyfirmata import INPUT, OUTPUT, PWM, SERVO
    from time import sleep
    from intruderDetection import *
    
#Connecting Computer to Arduino board, required only for the first time.
    port = '/dev/cu.usbmodem46'
    board=Arduino(port)

#Connecting to the arduino pins

    board.analog[0].mode=BUZZER
    pin=0
#Sleep command to let the arduino and computer sync.
    sleep(5)

    time=3000
    while(time!=0)
    tone(buzzer, 1000)



        
        

        
    
