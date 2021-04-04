# Simple GPS module demonstration.
# Will print NMEA sentences received from the GPS, great for testing connection
# Uses the GPS to send some commands, then reads directly from the GPS
import time
import board
import busio
import pyrebase
import json
import adafruit_gps

#firebase config setup
with open('firebase_config.json', 'r') as config_file:
    config_data = config_file.read()

# parse config data
config_creds = json.loads(config_data)
firebase = pyrebase.initialize_app(config_creds)

# Get a reference to the database service
db = firebase.database()

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password("","")

# Device registration code
DEVICE_REGISTRATION_CODE = "SHMS-NHjak3u7"
#grab owner info
device_attributes = db.child("devices").get().val()[DEVICE_REGISTRATION_CODE]
DEVICE_OWNER = device_attributes["owner"] if "owner" in device_attributes else None
#success status
if DEVICE_OWNER != None:
    print("Owner successfully retrieved.")
else:
    print("Owner not retrieved.")

# If using I2C, we'll create an I2C interface to talk to using default pins
i2c = board.I2C()

# Create a GPS module instance.
#gps = adafruit_gps.GPS(uart)  # Use UART/pyserial
gps = adafruit_gps.GPS_GtopI2C(i2c)  # Use I2C interface

# Turn on just minimum info (RMC only, location):
gps.send_command(b'PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')


# Set update rate to once a second (1hz) which is what you typically want.
gps.send_command(b"PMTK220,1000")       

SIMULATION = False;

#simulation loop    
if DEVICE_OWNER != None and SIMULATION == True:
    while True:
        # update lat and lon and wait 2 seconds
        results = db.child("users/"+DEVICE_OWNER+"/devices/"+DEVICE_REGISTRATION_CODE).update({"lat": 43.63438,"lon": -79.54087})    
        time.sleep(2)
        
        # update lat and lon and wait 2 seconds
        results = db.child("users/"+DEVICE_OWNER+"/devices/"+DEVICE_REGISTRATION_CODE).update({"lat": 43.63464,"lon": -79.54126})    
        time.sleep(2)
        
        # update lat and lon and wait 2 seconds
        results = db.child("users/"+DEVICE_OWNER+"/devices/"+DEVICE_REGISTRATION_CODE).update({"lat": 43.63471,"lon": -79.54156})    
        time.sleep(2)
        
        # update lat and lon and wait 2 seconds
        results = db.child("users/"+DEVICE_OWNER+"/devices/"+DEVICE_REGISTRATION_CODE).update({"lat": 43.63464,"lon": -79.54126})    
        time.sleep(2)
   
#retrieved lat/lon loop
if DEVICE_OWNER != None and SIMULATION != True:
    while True:        
        # Make sure to call gps.update() every loop iteration and at least twice
        # as fast as data comes from the GPS unit (usually every second).
        # This returns a bool that's true if it parsed new data (you can ignore it
        # though if you don't care and instead look at the has_fix property).
        gps.update()
        #if gps.latitude and gps.longitude are None, let them be set to 0
        if gps.latitude == None:
            gps.latitude = 0.0
        if gps.longitude == None:
            gps.longitude = 0.0
            
        # update lat and lon and wait 2 seconds
        results = db.child("users/"+DEVICE_OWNER+"/devices/"+DEVICE_REGISTRATION_CODE).update({"lat": gps.latitude,"lon": gps.longitude})
        print(gps.latitude)
        print(gps.longitude)
        time.sleep(2)

    
    
