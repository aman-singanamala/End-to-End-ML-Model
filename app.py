from flask import Flask, render_template, request

import pickle as pk
import numpy as np

import joblib

app = Flask(__name__)

model= joblib.load('rfc_model.h5')


## Define the route for the home page

@app.route('/')
def home():
    return render_template('index.html')

## Define the route for the prediction

@app.route('/predict', methods=['POST'])
def predict():

    fixed_acidity= float(request.form['fixed_acidity'])
    volatile_acidity= float(request.form['volatile_acidity'])
    citric_acid = float(request.form['citric_acid'])
    residual_sugar = float(request.form['residual_sugar'])
    chlorides = float(request.form['chlorides'])
    free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
    total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
    density = float(request.form['density'])
    pH = float(request.form['pH'])
    sulphates = float(request.form['sulphates'])
    alcohol = float(request.form['alcohol'])


    ## make the prediction using the loaded model

    prediction = model.predict([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, 
                                free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
    
    if prediction==0:
        return 'Wine 🍷 quality is low '
    else:
        return 'Wine 🍷 quality is good'
    
if __name__ == '__main__':
    app.run(debug=True)