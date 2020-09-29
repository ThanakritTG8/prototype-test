from flask import Flask , jsonify
from flask_restful import Api, Resource
import csv,json
import pandas as pd

app = Flask(__name__)
api = Api(app)

#  จำนวน comment in mounth / year 
@app.route('/year')
def CountYears(): 
 
<<<<<<< HEAD
@app.route('/CountOfNumberMessage')
def CountOfNumberMessage(): 
 
 url="./API/testjson/jsonfile/CountOfNumberMessage.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/jsontest2')
def jsontest2(): 
 
 url = "./API/testjson/jsonfile/jsontest2.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

 
@app.route('/NounAllIinPatong')
def NounAllIinPatong(): 
 
 url="./API/testjson/jsonfile/NounAllIinPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

 
@app.route('/NounAllIinPromthep')
def NounAllIinPromthep(): 
 
 url="./API/testjson/jsonfile/NounAllIinPromthep.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

 
@app.route('/NounAllIinWat')
def NounAllIinWat(): 
 
 url="./API/testjson/jsonfile/NounAllIinWat.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

 
@app.route('/PatongBeachGoogleReviews')
def MessageGoogleReview(): 
 
 url="./API/testjson/jsonfile/PatongBeachGoogleReviews.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/PatongBeachTripadvisor')
def PatongBeachTripadvisor(): 
 
 url="./API/testjson/jsonfile/PatongBeachTripadvisor.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/PositiveAndNegative')
def PositiveAndNegative(): 
 
 url="./API/testjson/jsonfile/PositiveAndNegative.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/PositiveAndNegativeEachDomain')
def PositiveAndNegativeEachDomain(): 
 
 url="./API/testjson/jsonfile/PositiveAndNegativeEachDomain.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/PositiveAndNegativePatongTrip')
def PositiveAndNegativePatongTrip(): 
 
 url="./API/testjson/jsonfile/PositiveAndNegativePatongTrip.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/PromthepCapeGoogleReviews')
def PromthepCapeGoogleReviews(): 
 
 url="./API/testjson/jsonfile/PromthepCapeGoogleReviews.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/PromthepCapeTripadvisor')
def PromthepCapeTripadvisor(): 
 
 url="./API/testjson/jsonfile/PromthepCapeTripadvisor.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/ToptenNoun')
def ToptenNoun(): 
 
 url="./API/testjson/jsonfile/ToptenNoun.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/WatChalongGoogleReviews')
def WatChalongGoogleReviews(): 
 
 url="./API/testjson/jsonfile/WatChalongGoogleReviews.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/WatChalongTripadvisor')
def WatChalongTripadvisor(): 
 
 url="./API/testjson/jsonfile/WatChalongTripadvisor.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/MuchInPatongNegative')
def MuchInPatongNegative(): 
 
 url="./API/testjson/jsonfile/MuchInPatongNegative.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/MuchInPatongPositive')
def MuchInPatongPositive(): 
 
 url="./API/testjson/jsonfile/MuchInPatongPositive.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/MuchInPromthepNegative')
def MuchInPromthepNegative(): 
 
 url="./API/testjson/jsonfile/MuchInPromthepNegative.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/MuchInPromthepPositive')
def MuchInPromthepPositive(): 
 
 url="./API/testjson/jsonfile/MuchInPromthepPositive.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/MuchInWatNegative')
def MuchInWatNegative(): 
 
 url="./API/testjson/jsonfile/MuchInWatNegative.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/MuchInWatPositive')
def MuchInWatPositive(): 
 
 url="./API/testjson/jsonfile/MuchInWatPositive.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentenceGooglePatongNegative')
def SentenceGooglePatongNegative(): 
 
 url="./API/testjson/jsonfile/SentenceGooglePatongNegative.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentenceGooglePatongPositive')
def SentenceGooglePatongPositive(): 
 
 url="./API/testjson/jsonfile/SentenceGooglePatongPositive.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentencePatong')
def SentencePatong(): 
 
 url="./API/testjson/jsonfile/SentencePatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentencePromthep')
def SentencePromthep(): 
 
 url="./API/testjson/jsonfile/SentencePromthep.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentenceTripPatongNegative')
def SentenceTripPatongNegative(): 
 
 url="./API/testjson/jsonfile/SentenceTripPatongNegative.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentenceTripPatongPositive')
def SentenceTripPatongPositive(): 
 
 url="./API/testjson/jsonfile/SentenceTripPatongPositive.json"
=======
 url="./API/testjson/jsonfile/CountsYearsMounth.json"
>>>>>>> 62cf791d66bd5ad3a22e8cd8ca446884a89b7a9a
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
<<<<<<< HEAD
        url = './API/testjson/jsonfile/jsontest.json'
=======
        url = './API/testjson/jsonfile/UniquewordDeepcutWordADJADVNOUNVERB.json'
>>>>>>> 62cf791d66bd5ad3a22e8cd8ca446884a89b7a9a
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



api.add_resource(Counts,"/counts/<string:name>")
api.add_resource(topten,"/topten/<string:name>")
api.add_resource(Piechart,"/piechart/<string:name>")
api.add_resource(ADJADVNOUN,"/senten/text/test/<string:name>")
api.add_resource(ClickEachwordAndText,"/senten/text/<string:name>")
api.add_resource(WordCloud,"/wordcloud/<string:name>")

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)
