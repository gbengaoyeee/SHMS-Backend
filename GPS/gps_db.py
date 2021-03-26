# Simple GPS module demonstration.
# Will print NMEA sentences received from the GPS, great for testing connection
# Uses the GPS to send some commands, then reads directly from the GPS
import time
import board
import busio
import pyrebase

import adafruit_gps

#firebase config setup
with open('../firebase_config.json', 'r') as config_file:
    config_data = config_file.read()

# parse config data
config_creds = json.loads(config_data)
firebase = pyrebase.initialize_app(config_creds)

# Get a reference to the database service
db = firebase.database()

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password("", "")



# data to save
lat = {"value": "0"}
lon = {"value": "0"}

#initialize lat and lon
#results = db.child("GPS").set({"lat":"0","lon":"0"})
#results = db.child("GPS").set({"lon":"0"})

# Create a serial connection for the GPS connection using default speed and
# a slightly higher timeout (GPS modules typically update once a second).
# These are the defaults you should use for the GPS FeatherWing.
# For other boards set RX = GPS module TX, and TX = GPS module RX pins.
#uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=10)

# for a computer, use the pyserial library for uart access
# import serial
# uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=10)

# If using I2C, we'll create an I2C interface to talk to using default pins
i2c = board.I2C()

# Create a GPS module instance.
#gps = adafruit_gps.GPS(uart)  # Use UART/pyserial
gps = adafruit_gps.GPS_GtopI2C(i2c)  # Use I2C interface

# Initialize the GPS module by changing what data it sends and at what rate.
# These are NMEA extensions for PMTK_314_SET_NMEA_OUTPUT and
# PMTK_220_SET_NMEA_UPDATERATE but you can send anything from here to adjust
# the GPS module behavior:
#   https://cdn-shop.adafruit.com/datasheets/PMTK_A11.pdf

# Turn on the basic GGA and RMC info (what you typically want)
#gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
# Turn on just minimum info (RMC only, location):
gps.send_command(b'PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
# Turn off everything:
# gps.send_command(b'PMTK314,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
# Tuen on everything (not all of it is parsed!)
# gps.send_command(b'PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0')

# Set update rate to once a second (1hz) which is what you typically want.
gps.send_command(b"PMTK220,1000")
# Or decrease to once every two seconds by doubling the millisecond value.
# Be sure to also increase your UART timeout above!
# gps.send_command(b'PMTK220,2000')
# You can also speed up the rate, but don't go too fast or else you can lose
# data during parsing.  This would be twice a second (2hz, 500ms delay):
# gps.send_command(b'PMTK220,500')

# Main loop runs forever printing data as it comes in
timestamp = time.monotonic()
#while True:
#    data = gps.read(32)  # read up to 32 bytes
#    # print(data)  # this is a bytearray type

#    if data is not None:
#        # convert bytearray to string
#        data_string = "".join([chr(b) for b in data])
#        print(data_string, end="")

#    if time.monotonic() - timestamp > 5:
        # every 5 seconds...
#        gps.send_command(b"PMTK605")  # request firmware version
#        timestamp = time.monotonic()        

# Device registration code
DEVICE_REGISTRATION_CODE = "SHMS-NHjak3u7"

device_attributes = db.child("devices").get().val()[DEVICE_REGISTRATION_CODE]
DEVICE_OWNER = device_attributes["owner"] if "owner" in device_attributes else None
    
if DEVICE_OWNER != None:
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
        
        # update lat and lon and wait 2 seconds
        results = db.child("users").child("a82939c4").child("devices").child("SHMS-NHjak3u7").update({"lat": 43.63438,"lon": -79.54087})    
        time.sleep(2)
        
