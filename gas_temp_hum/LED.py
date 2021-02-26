#!/usr/bin/python3
import sys
import os
import pyrebase
from time import sleep

config = {
    "apiKey": "AIzaSyAFwmKxtdjWbppX7tGiVKQEvzP_18Tc6oo",
    "authDomain": "smart-home-monitor-5fbbb.firebaseapp.com",
    "databaseURL": "https://smart-home-monitor-5fbbb.firebaseio.com",
    "storageBucket": "smart-home-monitor-5fbbb.appspot.com",
    "serviceAccount": "/home/pi/Documents/SHMS-Backend/gas_temp_hum/smart-home-monitor-5fbbb-firebase-adminsdk-m63v5-d37d42dd3d.json"
}

firebase = pyrebase.initialize_app(config)

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

PIN_25=25     #GPIO18  -- this LED is driven by GPIO 18. 
PIN_17=17     #GPIO17  -- as another example.

GPIO_Out_List=[PIN_17,PIN_25]

def blinkLED():
   i = 0; 
   for i in range (0, 1000):   # repeat 1000 times. 
      turnon()
      sleep(0.5)  # delay for 0.5 second.
      turnoff()
      sleep(0.5)   # delay for 0.5 second.
      i+= 1
   return

def turnoff():
    GPIO.output(PIN_25, GPIO.LOW)    # Turn OFF the LED connected to GPIO 18.
    print ('turn OFF the LED')
    return

def turnon():
    GPIO.output(PIN_25, GPIO.HIGH)    # Turn ON the LED connected to GPIO 18.
    print ('turn ON the LED')
    return
   
def main():  
    global PIN_17
    global PIN_25  
    global GPIO_Chan_List
    
    # Testing out firebase
    auth = firebase.auth()
    
    user = auth.sign_in_with_email_and_password("john@grr.la", "123456")
    print(user['email'])

    print ('Start LED blinking')    
    GPIO.setmode(GPIO.BCM)   # use this BCM (Board GPIO number) instead of using Board Pin numbers. 
    GPIO.setwarnings(False)
    
    GPIO.setup(GPIO_Out_List, GPIO.OUT)  #Initialize the Channel List PIN_17 and PIN_18 as outputs. 

    blinkLED()    # Blink the LEDs (On for 0.5 second, Off for 0.5 second) 

    
if __name__ == "__main__":
  main()




