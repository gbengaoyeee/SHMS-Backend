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
#firebase config
config = {
    "apiKey": "AIzaSyAFwmKxtdjWbppX7tGiVKQEvzP_18Tc6oo",
    "authDomain": "smart-home-monitor-5fbbb.firebaseapp.com",
    "databaseURL": "https://smart-home-monitor-5fbbb.firebaseio.com",
    "storageBucket": "smart-home-monitor-5fbbb.appspot.com",
    "serviceAccount": "/home/pi/Documents/SHMS-Backend/gas_temp_hum/smart-home-monitor-5fbbb-firebase-adminsdk-m63v5-d37d42dd3d.json"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
 
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
        db.child("users/a82939c4/devices/SHMS-NHjak3u7").update({
            "temperature":temperature_c
        })
        db.child("users/a82939c4/devices/SHMS-NHjak3u7").update({
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