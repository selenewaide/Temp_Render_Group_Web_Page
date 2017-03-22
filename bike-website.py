from flask import Flask
from flask import render_template, make_response
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

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
    app.run()