import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import pyrebase
import json
 
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

#firebase config setup
with open('../firebase_config.json', 'r') as config_file:
    config_data = config_file.read()

# parse config data
config_creds = json.loads(config_data)
firebase = pyrebase.initialize_app(config_creds)

db = firebase.database()

# Device registration code
DEVICE_REGISTRATION_CODE = "SHMS-NHjak3u7"

device_attributes = db.child("devices").get().val()[DEVICE_REGISTRATION_CODE]
DEVICE_OWNER = device_attributes["owner"] if "owner" in device_attributes else None


if DEVICE_OWNER != None:
    while 1:
        volt = round(chan.voltage, 2) * 100
        print('Raw ADC Value: ', chan.value)
        print('ADC Voltage: ' + str(volt) + 'V')
        result = db.child("users/"+DEVICE_OWNER+"/devices/"+DEVICE_REGISTRATION_CODE).update({
                "gas":volt
            })
        
        time.sleep(2.0)
    
    