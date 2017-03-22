import requests
import datetime

time_stamp = datetime.datetime.now()
timeStr = time_stamp.strftime('%Y-%m-%d-%H%M%S')

r = requests.get('https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=40d8ce05c637ce862bae2802f93241044b3a73d8')

file = open("templates/stations-" + timeStr + ".json","w") 
file.write(r.text) 
file.close() 
