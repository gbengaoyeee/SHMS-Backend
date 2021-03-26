#!/usr/bin/python3
import sys
import os
import pyrebase
from time import sleep

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

PIN_18=18     #GPIO18  -- this LED is driven by GPIO 18.
PIN_17=17     #GPIO17  -- as another example.

#details for firebase database
config={"apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "storageBucket": ""}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()
# Log the user in
user = auth.sign_in_with_email_and_password("", "")
# Get a reference to the database service
db = firebase.database()


def turnoff():
    GPIO.output(PIN_17, GPIO.LOW)    # Turn OFF the LED connected to GPIO 18.

    # update state field in reset child to 0
    results = db.child("users").child("a82939c4").child("devices").child("SHMS-NHjak3u7").update({"reset": 0})

    print ('LED is off')
    return

def turnon():
    GPIO.output(PIN_17, GPIO.HIGH)    # Turn ON the LED connected to GPIO 18.

    # update state field in reset child to 1
    results = db.child("users").child("a82939c4").child("devices").child("SHMS-NHjak3u7").update({"reset": 1})

    print ('LED is on')
    return

def buttonDetect(channel):
    if GPIO.input(27):
        turnon()
    else:
        turnoff()

def main():
    global PIN_17
    global PIN_18
    global GPIO_Chan_List

    # Get a reference to the auth service
    auth = firebase.auth()

    # Log the user in
    user = auth.sign_in_with_email_and_password("", "")

    # Get a reference to the database service
    db = firebase.database()

    # data to save
    data = {"state": "0"}

    #initialize state field in reset child to 0
    results = db.child("reset").set(data)

    print ('Welcome to my LED demo')
    GPIO.setmode(GPIO.BCM)   # use this BCM (Board GPIO number) instead of using Board Pin numbers.
    GPIO.setwarnings(False)

    GPIO.setup(27, GPIO.IN)  #Initialize pin 27 as an input
    GPIO.setup(17, GPIO.OUT) #set up pin 17 as an output


    GPIO.add_event_detect(27,GPIO.BOTH,callback=buttonDetect) #detect rising and falling edge

    message = input("Press enter to quit at any time\n\n")

    GPIO.cleanup()




	
if __name__ == "__main__":
  main()