from flask import Flask
from flask import render_template, make_response
from flask_mysqldb import MySQL

#set up app
app = Flask(__name__) 

# set up db configuration
app.config['MySQL_HOST'] = 'bikeandweather.cnkbtyr1hegq.us-east-1.rds.amazonaws.com'
app.config['MySQL_USER'] = 'admin'
app.config['MySQL_PASSWORD'] = 'Conv2017'
app.config['MySQL_DB'] = 'rdsDataBase'

# create mysql object
mysql = MySQL(app)


@app.route("/")
def index():
    return render_template('index2.html')

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


# create mysql connection:
mysql = MySQL()
conn = mysql.connect()









if __name__ == "__main__":
    app.run()