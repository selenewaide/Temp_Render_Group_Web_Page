import requests
import datetime

time_stamp = datetime.datetime.now()
timeStr = time_stamp.strftime('%Y-%m-%d-%H%M%S')

r = requests.get('https://api.openweathermap.org/data/2.5/weather?id=7778677&APPID=0b1d40f0f5b1bc4af97416f01400dd72&units=metric')

file = open("templates/weather-" + timeStr + ".json","w") 
file.write(r.text) 
file.close() 
