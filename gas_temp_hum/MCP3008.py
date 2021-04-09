import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import pyrebase
import json

# imports for dht22
import adafruit_dht


# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

#########################################
 
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
        
        try:
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            print(
                "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                    temperature_f, temperature_c, humidity
                )
            )
            db.child("users/"+DEVICE_OWNER+"/devices/"+DEVICE_REGISTRATION_CODE).update({
                "temperature":temperature_c
            })
            db.child("users/"+DEVICE_OWNER+"/devices/"+DEVICE_REGISTRATION_CODE).update({
                "humidity":humidity
            })
     
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            print("HERE")
            dhtDevice.exit()
            raise error
        
        volt = round(chan.voltage, 2) * 100
        print('Raw ADC Value: ', chan.value)
        print('ADC Voltage: ' + str(volt) + 'V')
        result = db.child("users/"+DEVICE_OWNER+"/devices/"+DEVICE_REGISTRATION_CODE).update({
                "gas":volt
            })
        
        time.sleep(2.0)
    
    