import os
import pandas as pd
from app import read_file as rf
from flask import render_template
from app import app


filepath = os.path.join(os.path.dirname(__file__), 'packets.csv')

def readFile():
    # open_read = open(filepath, 'r')
    df = pd.read_csv(filepath, delimiter='\\')
    # df = pd.DataFrame.from_csv(filepath)
    return df
    # page = ''

    # while True:
    #     read_data = open_read.readline()
    #     page += '%s' % read_data
    #     if open_read.readline() == '':
    #         break
    # return page

@app.route('/')
@app.route('/index')
def index():
    detect_attack = {'status':True}
    while(True):
        page = readFile()
        return render_template("index.html", title="DDOS Analyser", packets=page.to_html(), attack=detect_attack)
        index()

@app.route('/packets')
def incomming_packets():
    page = readFile()
    return page.to_html()