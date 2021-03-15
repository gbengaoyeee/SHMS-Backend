import pyrebase
import os
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
while 1:
# Pass the user's idToken to the push method
#results = db.child("users").push(data, user['idToken'])
	temp = db.child("temperature").get()
	reset = db.child("reset").child("state").get()
	if reset.val() == '0':
		if temp.val() > 200:
			f = open ("temperature.txt", "w")
			f.write("1")
			f.close()
			os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
		else:
			f = open ("temperature.txt", "w")
			f.write("0")
			f.close()
	else:
		print("")
