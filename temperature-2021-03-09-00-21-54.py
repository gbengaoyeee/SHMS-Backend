# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/temperature-2021-03-09-00-21-54.py"
import time
import pyrebase
from sense_emu import SenseHat

config={"apiKey": "AIzaSyAFwmKxtdjWbppX7tGiVKQEvzP_18Tc6oo",
    "authDomain": "smart-home-monitor-5fbbb.firebaseapp.com",
    "databaseURL": "https://smart-home-monitor-5fbbb.firebaseio.com",
    "storageBucket": "smart-home-monitor-5fbbb.appspot.com"}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password("tobiolaegbe@gmail.com", "password")

# Get a reference to the database service
db = firebase.database()
    
sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    temp = sense.get_temperature()
    print("Temperature: %s C" % temp)
    pixels = [red if i < temp else blue for i in range(64)]
    sense.set_pixels(pixels)
    
    
    # data to save
    data = {
    "name": "SenseHatEmu",
    "Temperature":temp,
    }

    # Pass the user's idToken to the push method
    db.child("users").child("TempUpdate").update({"Temperature":temp})  
    
    time.sleep(2)