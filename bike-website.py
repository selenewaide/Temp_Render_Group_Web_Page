from flask import Flask
from flask import render_template, make_response
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/weather")
def weather():
    resp = make_response(render_template('weather.json'), 200)
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp

@app.route("/stations")
def stations():
    resp = make_response(render_template('stations.json'), 200)
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp


if __name__ == "__main__":
    app.run()