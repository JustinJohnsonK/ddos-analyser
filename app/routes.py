import os
import requests
import json
import pandas as pd
from app import read_file as rf
from flask import render_template
from app import app


filepath = os.path.join(os.path.dirname(__file__), 'LiveAnn.csv')
filepath_ = os.path.join(os.path.dirname(__file__), 'new.jpeg')
packet_number = 0

def readFile():
    # open_read = open(filepath, 'r')
    df = pd.read_csv(filepath, delimiter=",")
    # df = pd.DataFrame.from_csv(filepath)
    return df

# page = readFile()
# url_ = 'http://localhost:8000/master/packet'
# # files = {'upload_file': open(filepath, 'rb')}
# files = {'media': open(filepath_, 'rb')}
# status = requests.post(url_, files=files)
# print("status - ", status)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    detect_attack = {'status':True}
    while(True):
        page = readFile()
        url = "http://localhost:5000"
        
        # sending file to server
        # url_ = 'http://127.0.0.1:8000/master/recievepacket'
        # # files = {'media': open(filepath, 'rb')}
        # status = requests.post(url_, files={filepath: f})
        # print("status - ", status)

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        # packet_number = data['frame.number']
        return render_template("index.html", title="DDOS Analyser", packets=page.to_html(), attack=detect_attack)
        r = requests.post(url, data=json.dumps(data), headers=headers)        
        
@app.route('/packets')
def incomming_packets():
    page = readFile()
    return page.to_html()