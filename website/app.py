from flask import Flask, render_template, url_for, flash, redirect, request
import csv
import json


app = Flask(__name__)
app.secret_key = 'THANOS DIES'


@app.route("/")
def IntroductionPage():
    indicies = [0,2,5,7,12]
    rarr = list(csv.reader(open('./templates/data/records_Cleaned.csv')))
    arr = [[i[j] for j in indicies] for i in rarr]
    #return render_template('main.html', adata=json.dumps(arr))
    return render_template('main.html', adata=arr)

@app.route("/data")
def gdata():
    indicies = [0,2,5,7,12]
    rarr = list(csv.reader(open('./templates/data/records_Cleaned.csv')))
    arr = [[i[j] for j in indicies] for i in rarr]
    #return render_template('main.html', adata=json.dumps(arr))
    return json.dumps(arr)

@app.route("/dash")
def dashBoard():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
