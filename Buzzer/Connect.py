import pyrebase
import os
import serial
import io
ser=serial.Serial("/dev/ttyACM0",2400)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

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


# Device registration code
DEVICE_REGISTRATION_CODE = "SHMS-NHjak3u7"
device_attributes = db.child("devices").get().val()[DEVICE_REGISTRATION_CODE]
DEVICE_OWNER = device_attributes["owner"] if "owner" in device_attributes else None

# data to save
data = {
    "name": "fdjfdsk"
}
duration = 1  # seconds
freq = 440  # Hz
re = 2

if DEVICE_OWNER != None:
    while 1:
    # Pass the user's idToken to the push method
    #results = db.child("users").push(data, user['idToken'])
        temp = db.child("users/"+DEVICE_OWNER+"/devices/"+DEVICE_REGISTRATION_CODE).child("temperature").get()
        reset = db.child("users/"+DEVICE_OWNER+"/devices/"+DEVICE_REGISTRATION_CODE).child("reset").get()
        print(re)
        if reset.val() == 0:
            if temp.val() > 200:
                if re!= 1:
                    sio.write("1\n")
                    sio.flush()
                    re = 1
                #hello1 = sio.readline()
            else:
                if re!= 0:
                    sio.write("0\n")
                    sio.flush()
                    re = 0
                #hello2 = sio.readline()        
        else:
            if re!=0:
                sio.write("0\n")
                sio.flush()
                re = 0
            #hello3 = sio.readline()


