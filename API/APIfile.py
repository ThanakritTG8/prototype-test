from flask import Flask , jsonify
from flask_restful import Api, Resource
import csv,json
import pandas as pd

app = Flask(__name__)
api = Api(app)

 
@app.route('/CountOfNumberMessage')
def CountOfNumberMessage(): 
 
 url="./API/testjson/jsonfile/CountOfNumberMessage.json"
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
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentenceWat')
def SentenceWat(): 
 
 url="./API/testjson/jsonfile/SentenceWat.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/TOP10AdjPatong')
def TOP10AdjPatong(): 
 
 url="./API/testjson/jsonfile/TOP10AdjPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/TOP10AdvPatong')
def TOP10AdvPatong(): 
 
 url="./API/testjson/jsonfile/TOP10AdvPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/TOP10NounPatong')
def TOP10NounPatong(): 
 
 url="./API/testjson/jsonfile/TOP10NounPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/TOP10VerbPatong')
def TOP10VerbPatong(): 
 
 url="./API/testjson/jsonfile/TOP10VerbPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/CorrectIDFSpecialType1Promthep')
def CorrectIDFSpecialType1Promthep(): 
 
 url="./API/testjson/jsonfile/CorrectIDFSpecialType1Promthep.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/CorrectNodeRatingType1Promthep')
def CorrectNodeRatingType1Promthep(): 
 
 url="./API/testjson/jsonfile/CorrectNodeRatingType1Promthep.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/CorrectNodeSpecialType1Promthep')
def CorrectNodeSpecialType1Promthep(): 
 
 url="./API/testjson/jsonfile/CorrectNodeSpecialType1Promthep.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/CorrectIDFRatingType1Wat')
def CorrectIDFRatingType1Wat(): 
 
 url="./API/testjson/jsonfile/CorrectIDFRatingType1Wat.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/CorrectIDFSpecialType1Wat')
def CorrectIDFSpecialType1Wat(): 
 
 url="./API/testjson/jsonfile/CorrectIDFSpecialType1Wat.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/CorrectNodeRatingType1Wat')
def CorrectNodeRatingType1Wat(): 
 
 url="./API/testjson/jsonfile/CorrectNodeRatingType1Wat.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/CorrectNodeSpecialType1Wat')
def CorrectNodeSpecialType1Wat(): 
 
 url="./API/testjson/jsonfile/CorrectNodeSpecialType1Wat.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/SentencePatongLolipop')
def SentencePatongLolipop(): 
 
 url="./API/testjson/jsonfile/SentencePatongLolipop.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/SentencePromthepLolipop')
def SentencePromthepLolipop(): 
 
 url="./API/testjson/jsonfile/SentencePromthepLolipop.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/SentenceWatLolipop')
def SentenceWatLolipop(): 
 
 url="./API/testjson/jsonfile/SentenceWatLolipop.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/MuchinPatongNegArray')
def MuchinPatongNegArray(): 
 
 url="./API/testjson/jsonfile/MuchinPatongNegArray.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/MuchinPatongPosArray')
def MuchinPatongPosArray(): 
 
 url="./API/testjson/jsonfile/MuchinPatongPosArray.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/top10NegAdjPatong')
def top10NegAdjPatong(): 
 
 url="./API/testjson/jsonfile/top10NegAdjPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/top10NegAdvPatong')
def top10NegAdvPatong(): 
 
 url="./API/testjson/jsonfile/top10NegAdvPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/top10NegNounPatong')
def top10NegNounPatong(): 
 
 url="./API/testjson/jsonfile/top10NegNounPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/top10NegVerbPatong')
def top10NegVerbPatong(): 
 
 url="./API/testjson/jsonfile/top10NegVerbPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/allcomments')
def dataTestset():
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
  
class ADJADVNOUN(Resource):
    def get(self,name):
        url = './API/testjson/jsonfile/test.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
     
        return  names[name]

api.add_resource(ADJADVNOUN,"/senten/text/test/<string:name>")
api.add_resource(ClickEachwordAndText,"/senten/text/<string:name>")
api.add_resource(WordCloud,"/wordcloud/<string:name>")

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)
