import pyrebase
import os
import serial
import io
ser=serial.Serial("/dev/ttyACM0",2400)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

config={"apiKey": "AIzaSyAFwmKxtdjWbppX7tGiVKQEvzP_18Tc6oo",
    "authDomain": "smart-home-monitor-5fbbb.firebaseapp.com",
    "databaseURL": "https://smart-home-monitor-5fbbb.firebaseio.com",
    "storageBucket": "smart-home-monitor-5fbbb.appspot.com"}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password("nhung@gmail.com", "password")

# Get a reference to the database service
db = firebase.database()

# data to save
data = {
    "name": "fdjfdsk"
}
duration = 1  # seconds
freq = 440  # Hz
re = 2
while 1:
# Pass the user's idToken to the push method
#results = db.child("users").push(data, user['idToken'])
	temp = db.child("users").child("a82939c4").child("devices").child("SHMS-NHjak3u7").child("temperature").get()
	reset = db.child("users").child("a82939c4").child("devices").child("SHMS-NHjak3u7").child("reset").get()
	#print(re)
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


