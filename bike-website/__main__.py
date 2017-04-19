from flask import Flask
from flask import render_template, make_response, jsonify
from flask_mysqldb import MySQL
import numpy as np

#set up app
app = Flask(__name__) 

# set up db configuration   
app.config['MYSQL_HOST'] = 'bikeandweather.cnkbtyr1hegq.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Conv2017'
app.config['MYSQL_DB'] = 'BikeAndWeather'
mysql = MySQL(app)

@app.route("/")
def index():
   return make_response(render_template('index3.html'))

# column names from db tables
staticFields = ["station", "name", "address", "lat", "lng", "banking", "bonus", "contract_name", "bike_stands"]
dynamicFields = ["station", "status", "available_bike_stands", "available_bikes", "last_update"]
weatherFields = ["dt", "main", "description", "icon", "temp", "json"]

@app.route("/stations/static")
def staticStations():
    """fetches the static station data, converts to a list of dicts, and returns the JSON"""
    cur = mysql.connection.cursor() # create cursor to query db
    cur.execute("select * from StationsStatic order by station")
    rows = cur.fetchall() # tuple of row tuples
    dicts = []
    for row in rows:
        row_dict = dict(zip(staticFields,row)) # {"station": 42...}
        row_dict['lat'] = str(row_dict['lat']) # convert Decimal('53.340962') to '53.340962'
        row_dict['lng'] = str(row_dict['lng'])
        dicts.append(row_dict)
    return jsonify(dicts)      #returns return value from db

@app.route("/stations/latest")
def latestStations():
    """ fetches latest dynamic station data, converts to a list of dicts, and returns the JSON"""
    cur = mysql.connection.cursor() # create cursor to query db
    cur.execute("select * from StationsDynamic where (station,last_update) in " +
        "(select station as sid, max(last_update) as latest from StationsDynamic group by station) order by station")
    rows = cur.fetchall() # tuple of row tuples (42, 'OPEN', 8, 22, 1492025217)
    dicts = []
    for row in rows:
        row_dict = dict(zip(dynamicFields, row))
        dicts.append(row_dict)
    return jsonify(dicts)

@app.route("/weather/latest")
def latestWeather():
    '''fetches latest weather data, converts to a list of dicts, and returns the JSON'''
    cur = mysql.connection.cursor() # create cursor to query db
    cur.execute("select * from WeatherJSON order by dt desc limit 1;")
    rows = cur.fetchall() # tuple of row tuple
    row = rows[0]
    row_dict = dict(zip(weatherFields, row))
    row_dict['temp'] = str(row_dict['temp']) # convert Decimal('9.5') to '9.5'
    return jsonify(row_dict)


@app.route("/stations/history")
@app.route("/stations/history/<sid>")
def historyOfStation(sid):
    '''fetches average bikes in use information for a particular station, using weekday indexes (0 = Mon … 6 = Sun)
     and hourly index (0 ... 23)''' 
    cur = mysql.connection.cursor()
    cur.execute('''select from_unixtime(last_update) as the_date, weekday(from_unixtime(last_update)) as the_day,
    hour(from_unixtime(last_update)) as the_hour, station, available_bikes, available_bike_stands, last_update
    from StationsDynamic where station = %s order by last_update''', (sid,)) #get bike usage data 
    rows = cur.fetchall()
    counts = np.zeros(168) 
    sums = np.zeros(168)
    for row in rows:
        hour_of_week = int(row[2]) + int(row[1]) * 24
        counts[hour_of_week] += 1
        sums[hour_of_week] += row[5]
    averages = np.zeros(168)
    for i in range(168):
        if counts[i] > 0:
            averages[i] = sums[i] / counts[i]
        else:
            if i > 0:
                averages[i] = averages[i - 1]
    return jsonify(list(averages))

# (datetime.datetime(2017, 4, 11, 10, 55, 8), 1, 10, 42, 3, 27, 1491908108)
'''
@app.route("/stations/history")
@app.route("/stations/history/<sid>")
def historyStations(sid):
    '''
'''fetches occupancy information for a station, incl. weekday index (0 = Mon … 6 = Sun)
     and hourly index (0 ... 23)''' '''
    cur = mysql.connection.cursor() # create cursor to query db
    cur.execute("""select from_unixtime(last_update) as the_date, weekday(from_unixtime(last_update)) as the_day,
    hour(from_unixtime(last_update)) as the_hour, station, available_bikes, available_bike_stands
    from StationsDynamic where station = %s order by station, the_day, the_hour""",(sid,))
    rows = cur.fetchall() # tuple of row tuple
    return str(rows)

'''
'''
@app.route("/weather/")
@app.route("/weather/<time_stamp>")
def weather(time_stamp=None):
    if time_stamp == None:
        # list available timestamps
        resp = make_response("['2017-03-19-124910','2017-03-19-124958']", 200)
    else:
        resp = make_response(render_template('weather-'+time_stamp+'.json'), 200)
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp

@app.route("/stations/")
@app.route("/stations/<time_stamp>")
def stations(time_stamp=None):
    if time_stamp == None:
        # list available timestamps
        resp = make_response("['2017-03-19-124902','2017-03-19-124953']", 200)
    else:
        resp = make_response(render_template('stations-'+time_stamp+'.json'), 200)
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp
'''

if __name__ == "__main__":
    app.run(debug=True)