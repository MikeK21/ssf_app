from flask import Flask
import os
import json
import scrape_mon
import urllib.request

app = Flask(__name__)

@app.route("/")

def hello():
    #return "HELLO"
    try:
        resultSet = scrape_mon.getEnvRequest()
    except:
        print("Could not contact scrape_mon")
    return resultSet

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
