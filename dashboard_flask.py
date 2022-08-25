
from flask import Flask, request, render_template
import pymongo
import json
import requests

app = Flask(__name__)

@app.route("/")
def data():
    lid=lastid()
    len=currentid()
    len1=int(len)
    url = "http://13.235.103.138:3000/senders"
    for count in range(lid+1,len1+1):
     x=str(count)
     x1='id='+x
     payload=x1
     print("-----------"+x1+"-----------------------------------------------")
     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
     response = requests.request("GET", url, headers=headers, data=payload)
     data = json.loads(response.text)
  #print the type of data variable
  
     a1=data['data']['senders']
     uval={'_id':x1,'origin1':a1}
     row.insert_one(uval)
     for f in a1:
      print(f)
    return render_template('dashboard.html',usdata=row.find(),mydoc=row.count_documents({}))

def lastid():
  x=row.find()
  y1=""
  for y in x:
   y1=y['_id']
  #print("-------------------------------")
  print(str(y1))
  y2=y1[3:]
  y3=int(y2)
  print(type(y3))
  return y3

def currentid():
 url = "http://13.235.103.138:3000/total"
 payload={}
 headers = {}
 response = requests.request("GET", url, headers=headers, data=payload)
 data1 = json.loads(response.text)
 str12=data1['messages']
 print(str12)
 return str12

if __name__ == "__main__":
 client= pymongo.MongoClient("mongodb+srv://kevinrotern:jayesh@cluster0.h7nnxmo.mongodb.net/test")
 db= client['blockchain_data']
 row=db['origin']
 app.run(debug=True)