from flask import Flask
from flask import render_template, make_response
from flask_mysqldb import MySQL

#set up app
app = Flask(__name__) 

# set up db configuration   
app.config['MYSQL_HOST'] = 'bikeandweather.cnkbtyr1hegq.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Conv2017'
app.config['MYSQL_DB'] = 'BikeAndWeather'
mysql = MySQL(app)

#def index():
 #   return render_template('index2.html')

@app.route("/")
def connectdb():
    cur = mysql.connection.cursor() # create cursor to query db
    cur.execute("SELECT * from BikeData")
    rv = cur.fetchall()
    return str(rv)      #returns return value from db

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

if __name__ == "__main__":
    app.run(debug=True)