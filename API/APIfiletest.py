from flask import Flask , jsonify
from flask_restful import Api, Resource,reqparse, abort
import csv,json
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
  
# posgard >> /postgards/POSNOUN /POSVERB /POSADJ /POSADV /NEGNOUN /NEGVERB /NEGADJ /NEGADV
class Postgard(Resource):
    def get(self,name):
        url = './API/testjson/jsonfile/Postgards.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
        return  names[name]

api.add_resource(Postgard,"/postgrards/<string:name>")

if __name__ == '__main__':
   app.run(host="api.playz-th.com", port=5000, debug=True)
