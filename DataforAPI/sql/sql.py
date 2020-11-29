import pandas as pd
import mysql.connector

def connect1():
 mydb = mysql.connector.connect(
    host = "172.26.117.6",
    user = "aitasireadonly",
    passwd = "aitasipassword",
    database = "sentiment"
 )
 #  and RD_MESSAGE NOT like '%é%' \
                  #  and RD_MESSAGE NOT like'%ö%' \
                  #  and RD_MESSAGE NOT like'%%' \güzel
                  #  and RD_MESSAGE NOT like'%第%' \
                  #  and  RD_MESSAGE NOT like'%晒%' \ Härlig
                  #  and RD_MESSAGE NOT like'%τ%'  \Spiaggia 
                  #  and RD_MESSAGE NOT like'%э%' \수も bella strand  unserer
 mycursor = mydb.cursor()
 mycursor.execute("SELECT RD_ID,RD_MESSAGE,RD_SCORE,RD_VISIT_DATE FROM VW_attraction_score \
                   WHERE AT_OTA_NAME='tripadvisor' \
                   and AI_NAME= 'Karon Beach'     and  RD_MESSAGE NOT like'%Spiaggia%' and RD_MESSAGE NOT LIKE '%miljöö%'\
                    and RD_MESSAGE NOT like'%и%'  and  RD_MESSAGE NOT like'%も%' and  RD_MESSAGE NOT like'%เ%' \
                   and  RD_MESSAGE NOT like'%http%' and  RD_MESSAGE NOT like'%の%' and  RD_MESSAGE NOT like'%很%' \
                   and  RD_MESSAGE NOT like'%第%'  and  RD_MESSAGE like'%e%'  and  RD_MESSAGE NOT like'%spiaggia%' \
                    and RD_MESSAGE NOT like'%τ%' and  RD_MESSAGE NOT like'%bella%' and  RD_MESSAGE NOT like'%strand%' \
                      and  RD_MESSAGE NOT like'%晒%' and RD_MESSAGE NOT like '%Söt%'  and RD_MESSAGE NOT LIKE '%ranta%' \
                         and  RD_MESSAGE NOT like'%也%' and RD_MESSAGE NOT like '%با%' and RD_MESSAGE NOT like '%plaj%'\
                           and  RD_MESSAGE NOT like'%プ%'  and RD_MESSAGE NOT like '%vraiment%' and RD_MESSAGE NOT like '%água%'\
                             and  RD_MESSAGE NOT like'%güzel%' and RD_MESSAGE NOT like '%très%' and RD_MESSAGE NOT like '%molto%'\
                                   and  RD_MESSAGE NOT like'%Härlig%' and RD_MESSAGE NOT Like '%näkyi%' and RD_MESSAGE NOT LIKE '%ormai%' \
                                      and  RD_MESSAGE NOT like'%수%' and RD_MESSAGE NOT LIKE '%ø%' and RD_MESSAGE NOT like '%solstolar%'\
                   and RD_MESSAGE NOT like '%Rekomenderas%' and RD_MESSAGE NOT like '%più%' and RD_MESSAGE NOT like '%mais%'\
                     and RD_MESSAGE NOT like '%più%' and RD_MESSAGE NOT like '%mais%' and RD_MESSAGE NOT like '%¶%'\
                   and  RD_MESSAGE NOT like'%Read more%'\
                   and  (RD_VISIT_DATE like '%2018' or RD_VISIT_DATE like '%2019' or RD_VISIT_DATE like '%2020') \
                   GROUP BY RD_MESSAGE"

                   )
 myresult = mycursor.fetchall()

 data=[]
 datascore=[]
 rd_id=[]
 date = []
 for x in myresult:
   message=x[1]
   data.append(message)
   score=x[2]
   datascore.append(score)
   rdid=x[0]
   rd_id.append(rdid)
   dates=x[3]
   date.append(dates)


 return {'RD_ID':rd_id,'RD_MESSAGE':data,'RD_SCORE':datascore,'RD_VISIT_DATE':date}


def SaveCSVall1():

    dict = connect1()
    df = pd.DataFrame(dict)
    df.to_csv(f'./sql/form1.csv', index=False)

SaveCSVall1()
