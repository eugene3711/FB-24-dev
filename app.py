from flask import Flask, render_template, request, session, make_response
import urllib, json
from urllib.request import urlopen
import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/map')
def test():
    return render_template("/test.html")

@app.route('/geodata')
def geodata():
    response = make_response(json.dumps(db.getTargeting())) 
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response   

@app.route('/map-data')
def map_data():
    if request.args.get('devs'):
        developments_list = request.args.get('devs').split(',')
    else:
        response = make_response(json.dumps({"error": "add dev id"}))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response  
    print("requested: ", developments_list) 
    
    data = []  
    for dev in developments_list:
        data.append(db.getFullTargeting(dev))
    print(data)
    
    response = make_response(json.dumps({"list": data}))
    response.headers['Access-Control-Allow-Origin'] = '*'
    
    return response      

if __name__ == '__main__':
    app.run(threaded=True, port=5000)