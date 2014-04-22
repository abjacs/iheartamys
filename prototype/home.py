from flask import Flask, request
import simplejson as json
from iheartamys import amys

app = Flask(__name__)


class HTTP(object):
    GET = "GET"
    POST = "POST"

"""
@app.route("/")
def home():
    api = amys.Api()
    flavors = api.get_flavors()
    print flavors
    
    return json.dumps(flavors)
"""

@app.route("/cities", methods = [ HTTP.GET ])
def cities():
   cities = api.get_cities()
   cities = json.dumps(cities)
   
   return cities 
    
@app.route("/flavors", methods = [ HTTP.GET ])
def flavors():
    # getlist() defaults to [] for safety
    flavors = request.values.getlist("flavor")
    flavors = api.get_flavors(flavors)
    
    flavors = json.dumps(flavors)
    
    return flavors
    
if __name__ == "__main__":
    api = amys.Api()
    
    app.run(debug = True)