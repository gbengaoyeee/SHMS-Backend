import time
import board
import adafruit_dht
import pyrebase
 
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
 
# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

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
    while True:
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
     
        time.sleep(2.0)
