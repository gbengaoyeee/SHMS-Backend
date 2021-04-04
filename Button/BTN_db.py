#!/usr/bin/python3
import sys
import os
import pyrebase
import json
from time import sleep



try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

#firebase config setup
with open('firebase_config.json', 'r') as config_file:
    config_data = config_file.read()

# parse config data
config_creds = json.loads(config_data)
firebase = pyrebase.initialize_app(config_creds)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password("alex@gmail.com", "password")

# Get a reference to the database service
db = firebase.database()

# Device registration code
DEVICE_REGISTRATION_CODE = "SHMS-NHjak3u7"

#grab owner info
device_attributes = db.child("devices").get().val()[DEVICE_REGISTRATION_CODE]
DEVICE_OWNER = device_attributes["owner"] if "owner" in device_attributes else None

if DEVICE_OWNER != None:
    print("Owner successfully retrieved.")
else:
    print("Owner not retrieved.")
        

def turnoff():
    # update state field in reset child to 0
    results = db.child("users/"+DEVICE_OWNER+"/devices/"+DEVICE_REGISTRATION_CODE).update({"reset": 0})

    return

def turnon():
    # update state field in reset child to 1
    results = db.child("users/"+DEVICE_OWNER+"/devices/"+DEVICE_REGISTRATION_CODE).update({"reset": 1})
    
    return

def buttonDetect(channel):
    if GPIO.input(27):
        turnon()
    else:
        turnoff()

def main():
    global GPIO_Chan_List

    # Get a reference to the auth service
    auth = firebase.auth()

    # Log the user in
    user = auth.sign_in_with_email_and_password("alex@gmail.com", "password")

    # Get a reference to the database service
    db = firebase.database()

    # data to save
    data = {"state": "0"}

    #initialize state field in reset child to 0
    results = db.child("reset").set(data)

    print ('Welcome to button backend')
    GPIO.setmode(GPIO.BCM)   # use this BCM (Board GPIO number) instead of using Board Pin numbers.
    GPIO.setwarnings(False)

    GPIO.setup(27, GPIO.IN)  #Initialize pin 27 as an input

    GPIO.add_event_detect(27,GPIO.BOTH,callback=buttonDetect) #detect rising and falling edge

    message = input("Press enter to quit at any time\n\n")

    GPIO.cleanup()




	
if __name__ == "__main__":
  main()
