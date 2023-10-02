import time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
from flask import Flask, request, render_template
import pickle

app = Flask("__name__")



q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")


@app.route("/predict", methods=['POST'])
def predict():
    
    '''
    customer_id
    credit_score
    age
    tenure
    balance
    products_number
    credit_card
    active_member
    estimated_salary
    country_France
    country_Spain
    country_Germany
    gender_Female
    gender_Male
    '''
    

    
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    inputQuery9 = request.form['query9']
    inputQuery10 = request.form['query10']
    inputQuery11 = request.form['query10']
    inputQuery12 = request.form['query10']
    inputQuery13 = request.form['query10']
    inputQuery14 = request.form['query10']

    customer_id=int(inputQuery1)
    credit_score = int(inputQuery2)
    age = int(inputQuery3)
    tenure = int(inputQuery4)
    balance = float(inputQuery5)
    products_number = int(inputQuery6)
    credit_card = int(inputQuery7)
    active_member = int(inputQuery8)
    estimated_salary = float(inputQuery9)
    country_France = inputQuery10
    country_Spain = inputQuery11
    country_Germany = inputQuery12
    gender_Female = inputQuery13
    gender_Male = inputQuery14


    

    model = pickle.load(open("model.sav", "rb"))

    features = [customer_id, credit_score, age, tenure, balance, products_number, credit_card, active_member, estimated_salary, country_France, country_Germany, country_Spain, gender_Female, gender_Male]

    columns = ['customer_id','credit_score', 'age', 'tenure', 'balance', 'products_number', 'credit_card', 'active_member', 'estimated_salary', 'country_France', 'country_Germany', 'country_Spain', 'gender_Female', 'gender_Male']

    final_features = [np.array(features)]
    prediction = model.predict_proba(final_features)

    output = prediction[0,1]


    t = time.time()
    return render_template('home.html', prediction_text='Churn probability is {}'.format(round(output, 2)))
        
app.run(debug=True)

