import os
import requests
import json
import pandas as pd
from app import read_file as rf
from flask import render_template
from app import app


filepath = os.path.join(os.path.dirname(__file__), 'packets.csv')
packet_number = 0

def readFile():
    # open_read = open(filepath, 'r')
    df = pd.read_csv(filepath, delimiter='\\')
    # df = pd.DataFrame.from_csv(filepath)
    return df

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    detect_attack = {'status':True}
    while(True):
        page = readFile()
        url = "http://localhost:5000"
        # sample packet details to be send to server
        data = {'frame.number':'15',
                'frame.time':'Mar 26, 2019 08:28:51.393156791 IST',
                'eth.src':'48:e2:44:d2:8c:13',
                'eth.dst':'a8:96:75:07:4b:51',
                'ip.src':'192.168.43.196',
                'ip.dst':'151.101.193.69',
                'ip.proto':'6'
                }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        packet_number = data['frame.number']
        return render_template("index.html", title="DDOS Analyser", packets=page.to_html(), attack=detect_attack)
        r = requests.post(url, data=json.dumps(data), headers=headers)        
        
@app.route('/packets')
def incomming_packets():
    page = readFile()
    return page.to_html()