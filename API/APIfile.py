from flask import Flask , jsonify
from flask_restful import Api, Resource
import csv,json
import pandas as pd

app = Flask(__name__)
api = Api(app)
@app.route('/CorrectIDFRatingType1Patong')
def CorrectIDFRatingType1Patong(): 
 
 url="./testjson/jsonfile/CorrectIDFRatingType1Patong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,ensure_ascii=False)


@app.route('/CorrectIDFSpecialType1Patong')
def CorrectIDFSpecialType1Patong(): 
 
 url="./testjson/jsonfile/CorrectIDFSpecialType1Patong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/CorrectNodeRatingType1Patong')
def CorrectNodeRatingType1Patong(): 
 
 url="./testjson/jsonfile/CorrectNodeRatingType1Patong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

 
@app.route('/CorrectNodeSpecialType1Patong')
def CorrectNodeSpecialType1Patong(): 
 
 url="./testjson/jsonfile/CorrectNodeSpecialType1Patong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

 
@app.route('/CountOfNumberMessage')
def CountOfNumberMessage(): 
 
 url="./testjson/jsonfile/CountOfNumberMessage.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

 
@app.route('/NounAllIinPatong')
def NounAllIinPatong(): 
 
 url="./testjson/jsonfile/NounAllIinPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

 
@app.route('/NounAllIinPromthep')
def NounAllIinPromthep(): 
 
 url="./testjson/jsonfile/NounAllIinPromthep.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

 
@app.route('/NounAllIinWat')
def NounAllIinWat(): 
 
 url="./testjson/jsonfile/NounAllIinWat.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

 
@app.route('/PatongBeachGoogleReviews')
def MessageGoogleReview(): 
 
 url="./testjson/jsonfile/PatongBeachGoogleReviews.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/PatongBeachTripadvisor')
def PatongBeachTripadvisor(): 
 
 url="./testjson/jsonfile/PatongBeachTripadvisor.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/PositiveAndNegative')
def PositiveAndNegative(): 
 
 url="./testjson/jsonfile/PositiveAndNegative.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/PositiveAndNegativeEachDomain')
def PositiveAndNegativeEachDomain(): 
 
 url="./testjson/jsonfile/PositiveAndNegativeEachDomain.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/PositiveAndNegativePatongTrip')
def PositiveAndNegativePatongTrip(): 
 
 url="./testjson/jsonfile/PositiveAndNegativePatongTrip.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/PromthepCapeGoogleReviews')
def PromthepCapeGoogleReviews(): 
 
 url="./testjson/jsonfile/PromthepCapeGoogleReviews.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/PromthepCapeTripadvisor')
def PromthepCapeTripadvisor(): 
 
 url="./testjson/jsonfile/PromthepCapeTripadvisor.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/ToptenNoun')
def ToptenNoun(): 
 
 url="./testjson/jsonfile/ToptenNoun.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/WatChalongGoogleReviews')
def WatChalongGoogleReviews(): 
 
 url="./testjson/jsonfile/WatChalongGoogleReviews.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/WatChalongTripadvisor')
def WatChalongTripadvisor(): 
 
 url="./testjson/jsonfile/WatChalongTripadvisor.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/MuchInPatongNegative')
def MuchInPatongNegative(): 
 
 url="./testjson/jsonfile/MuchInPatongNegative.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/MuchInPatongPositive')
def MuchInPatongPositive(): 
 
 url="./testjson/jsonfile/MuchInPatongPositive.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/MuchInPromthepNegative')
def MuchInPromthepNegative(): 
 
 url="./testjson/jsonfile/MuchInPromthepNegative.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/MuchInPromthepPositive')
def MuchInPromthepPositive(): 
 
 url="./testjson/jsonfile/MuchInPromthepPositive.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/MuchInWatNegative')
def MuchInWatNegative(): 
 
 url="./testjson/jsonfile/MuchInWatNegative.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/MuchInWatPositive')
def MuchInWatPositive(): 
 
 url="./testjson/jsonfile/MuchInWatPositive.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentenceGooglePatongNegative')
def SentenceGooglePatongNegative(): 
 
 url="./testjson/jsonfile/SentenceGooglePatongNegative.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentenceGooglePatongPositive')
def SentenceGooglePatongPositive(): 
 
 url="./testjson/jsonfile/SentenceGooglePatongPositive.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentencePatong')
def SentencePatong(): 
 
 url="./testjson/jsonfile/SentencePatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentencePromthep')
def SentencePromthep(): 
 
 url="./testjson/jsonfile/SentencePromthep.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentenceTripPatongNegative')
def SentenceTripPatongNegative(): 
 
 url="./testjson/jsonfile/SentenceTripPatongNegative.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentenceTripPatongPositive')
def SentenceTripPatongPositive(): 
 
 url="./testjson/jsonfile/SentenceTripPatongPositive.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/SentenceWat')
def SentenceWat(): 
 
 url="./testjson/jsonfile/SentenceWat.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/TOP10AdjPatong')
def TOP10AdjPatong(): 
 
 url="./testjson/jsonfile/TOP10AdjPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/TOP10AdvPatong')
def TOP10AdvPatong(): 
 
 url="./testjson/jsonfile/TOP10AdvPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/TOP10NounPatong')
def TOP10NounPatong(): 
 
 url="./testjson/jsonfile/TOP10NounPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/TOP10VerbPatong')
def TOP10VerbPatong(): 
 
 url="./testjson/jsonfile/TOP10VerbPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/cloudAdjPatong')
def cloudAdjPatong(): 
 
 url="./testjson/jsonfile/cloudAdjPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/cloudAdvPatong')
def cloudAdvPatong(): 
 
 url="./testjson/jsonfile/cloudAdvPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/cloudNounPatong')
def cloudNounPatong(): 
 
 url="./testjson/jsonfile/cloudNounPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/cloudVerbPatong')
def cloudVerbPatong(): 
 
 url="./testjson/jsonfile/cloudVerbPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/CorrectIDFSpecialType1Promthep')
def CorrectIDFSpecialType1Promthep(): 
 
 url="./testjson/jsonfile/CorrectIDFSpecialType1Promthep.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/CorrectNodeRatingType1Promthep')
def CorrectNodeRatingType1Promthep(): 
 
 url="./testjson/jsonfile/CorrectNodeRatingType1Promthep.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/CorrectNodeSpecialType1Promthep')
def CorrectNodeSpecialType1Promthep(): 
 
 url="./testjson/jsonfile/CorrectNodeSpecialType1Promthep.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/CorrectIDFRatingType1Wat')
def CorrectIDFRatingType1Wat(): 
 
 url="./testjson/jsonfile/CorrectIDFRatingType1Wat.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/CorrectIDFSpecialType1Wat')
def CorrectIDFSpecialType1Wat(): 
 
 url="./testjson/jsonfile/CorrectIDFSpecialType1Wat.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/CorrectNodeRatingType1Wat')
def CorrectNodeRatingType1Wat(): 
 
 url="./testjson/jsonfile/CorrectNodeRatingType1Wat.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/CorrectNodeSpecialType1Wat')
def CorrectNodeSpecialType1Wat(): 
 
 url="./testjson/jsonfile/CorrectNodeSpecialType1Wat.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/SentencePatongLolipop')
def SentencePatongLolipop(): 
 
 url="./testjson/jsonfile/SentencePatongLolipop.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/SentencePromthepLolipop')
def SentencePromthepLolipop(): 
 
 url="./testjson/jsonfile/SentencePromthepLolipop.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/SentenceWatLolipop')
def SentenceWatLolipop(): 
 
 url="./testjson/jsonfile/SentenceWatLolipop.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/cloudAdjPatongName')
def cloudAdjPatongName(): 
 
 url="./testjson/jsonfile/cloudAdjPatongName.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/cloudAdvPatongName')
def cloudAdvPatongName(): 
 
 url="./testjson/jsonfile/cloudAdvPatongName.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/cloudNounPatongName')
def cloudNounPatongName(): 
 
 url="./testjson/jsonfile/cloudNounPatongName.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/cloudVerbPatongName')
def cloudVerbPatongName(): 
 
 url="./testjson/jsonfile/cloudVerbPatongName.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/MuchinPatongNegArray')
def MuchinPatongNegArray(): 
 
 url="./testjson/jsonfile/MuchinPatongNegArray.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/MuchinPatongPosArray')
def MuchinPatongPosArray(): 
 
 url="./testjson/jsonfile/MuchinPatongPosArray.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/top10NegAdjPatong')
def top10NegAdjPatong(): 
 
 url="./testjson/jsonfile/top10NegAdjPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/top10NegAdvPatong')
def top10NegAdvPatong(): 
 
 url="./testjson/jsonfile/top10NegAdvPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/top10NegNounPatong')
def top10NegNounPatong(): 
 
 url="./testjson/jsonfile/top10NegNounPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/top10NegVerbPatong')
def top10NegVerbPatong(): 
 
 url="./testjson/jsonfile/top10NegVerbPatong.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/cloudAdvNegPatongName')
def cloudAdvNegPatongName(): 
 
 url="./testjson/jsonfile/cloudAdvNegPatongName.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/cloudAdjNegPatongName')
def cloudAdjNegPatongName(): 
 
 url="./testjson/jsonfile/cloudAdjNegPatongName.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/cloudNounNegPatongName')
def cloudNounNegPatongName(): 
 
 url="./testjson/jsonfile/cloudNounNegPatongName.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

@app.route('/cloudVerbNegPatongName')
def cloudVerbNegPatongName(): 
 
 url="./testjson/jsonfile/cloudVerbNegPatongName.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)

class ClickEachwordAndText(Resource):
    def get(self,name):
        url = './testjson/jsonfile/UniquewordDeepcutWordTestset.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
          # obj = names[name]
        return  names[name]
        # return names[name]
api.add_resource(ClickEachwordAndText,"/TextEachWord/<string:name>")


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)