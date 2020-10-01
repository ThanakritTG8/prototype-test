from flask import Flask , jsonify
from flask_restful import Api, Resource
import csv,json
import pandas as pd

app = Flask(__name__)
api = Api(app)

#  จำนวน comment in mounth / year 
@app.route('/year')
def CountYears(): 
 
 url="./API/testjson/jsonfile/CountsYearsMounth.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/allcomments')
def allcomment(): 
 
 url="./API/testjson/jsonfile/dataTestset.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)
 
class ClickEachwordAndText(Resource):
    def get(self,name):
        url = './API/testjson/jsonfile/UniquewordDeepcutWordADJADVNOUNVERBNtesttest.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
     
        return  names[name]
  
class WordCloud(Resource):
    def get(self,name):
        url = './API/testjson/jsonfile/WordClould.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
     
        return  names[name]

class Piechart(Resource):
    def get(self,name):
        url = './API/testjson/jsonfile/CountsPieChart.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
     
        return  names[name]

class ADJADVNOUN(Resource):
    def get(self,name):
        url = './API/testjson/jsonfile/UniquewordDeepcutWordADJADVNOUNVERB.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
     
        return  names[name]

#  จำนวน topten 
# /posNOUN /posVERB /posADJ /posADV /negNOUN /negVERB /negADJ /negADV

class topten(Resource):
    def get(self,name):
        url = './API/testjson/jsonfile/toptensentens.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
     
        return  names[name]

# จำนวน คำทั้งหมด positive,negative ทั้งหมด 
# /pos /neg /all
class Counts(Resource):
    def get(self,name):
        url = './API/testjson/jsonfile/Counts.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
     
        return  names[name]

# posgard >> /postgards/POSNOUN /POSVERB /POSADJ /POSADV /NEGNOUN /NEGVERB /NEGADJ /NEGADV
class Postgard(Resource):
    def get(self,name):
        url = './API/testjson/jsonfile/Postgards.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
        return  names[name]


api.add_resource(Postgard,"/postgards/<string:name>")
api.add_resource(Counts,"/counts/<string:name>")
api.add_resource(topten,"/topten/<string:name>")
api.add_resource(Piechart,"/piechart/<string:name>")
api.add_resource(ADJADVNOUN,"/senten/text/test/<string:name>")
api.add_resource(ClickEachwordAndText,"/senten/text/<string:name>")
api.add_resource(WordCloud,"/wordcloud/<string:name>")

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)
