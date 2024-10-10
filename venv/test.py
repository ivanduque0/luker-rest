import json
from flask import Flask
import time
from suds.client import Client
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

app = Flask(__name__)

@app.route('/trm', methods=['GET'])
def welcome():
    WSDL_URL = "https://www.superfinanciera.gov.co/SuperfinancieraWebServiceTRM/TCRMServicesWebService/TCRMServicesWebService?WSDL"
    date = time.strftime("%Y-%m-%d")
    date = datetime.today() - timedelta(days=1)
    client = Client(WSDL_URL, location=WSDL_URL, faults=True)
    trm = client.service.queryTCRM(date) 
    context = {trm, ""}
    info = {
        "unit": trm.unit,
        "value": trm.value,
        "date": date.strftime("%Y-%m-%d"),
    }
    return json.dumps(info)

@app.route('/cocoa-contracts', methods=['GET'])
def welcome1():
    url = 'https://es.investing.com/commodities/us-cocoa-contracts'

    headers = {
    "User-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html5lib")
    tables = soup.find("table" , id="BarchartDataTable")
    df = pd.read_html(str(tables))[0]
    js = df.to_json(orient = 'index', force_ascii=False)
    return (js)

@app.route('/eur', methods=['GET'])
def welcome2():
    url = 'https://latest.currency-api.pages.dev/v1/currencies/eur.json'

    headers = {
    "User-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    value = response.json()["eur"]["cop"]
    date = response.json()["date"]
    info = {
        "value": value,
        "date": date,
    }
    return json.dumps(info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['PORT'])
