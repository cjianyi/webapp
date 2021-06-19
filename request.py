import requests
import json
from flaskext.mysql import MySQL
from flask import Flask
  
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'patients'
 
mysql = MySQL(app)
def getPatients():
    response = requests.request("GET", "http://hapi.fhir.org/baseR4/Patient",headers={}, data={})
    body = json.loads(response.text)
    # print(body["entry"][0])
    for i in range(len(body["entry"])):
        try:
            id = body["entry"][i]["resource"]["id"]
            name = body["entry"][i]["resource"]["name"][0]["given"][0] + " " + body["entry"][i]["resource"]["name"][0]["family"]
            print(name)
        except Exception:
            print(name)
            pass
            

if __name__ == '__main__':
    getPatients()