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
    #    with open("stock.txt","r") as stock_file:
    #	    resultSet = stock_file.readlines()
        resultSet = scrape_mon.getEnvRequest()
    except:
        print("Could not contact scrape_mon")
#    file = open(r'./scrape_mon.py', 'r').read()
#    return exec(file)
#    return json.dumps(resultSet)
#     return hello_func()
    return resultSet

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
