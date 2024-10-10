from flask import Flask
import time
from suds.client import Client
from datetime import datetime, timedelta
app = Flask(__name__)

@app.route('/')
def home():
    WSDL_URL = "https://www.superfinanciera.gov.co/SuperfinancieraWebServiceTRM/TCRMServicesWebService/TCRMServicesWebService?WSDL"
    date = time.strftime("%Y-%m-%d")
    date = datetime.today() - timedelta(days=1)
    client = Client(WSDL_URL, location=WSDL_URL, faults=True)
    trm = client.service.queryTCRM(date)
    return (trm)
    if __name__ == '__main__':
    	app.run(host='0.0.0.0',port=5000,debug=True)
