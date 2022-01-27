import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import tensorflow
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Dense

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model.pkl', 'rb')) # loading the trained model

@app.route('/') # Homepage
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    # retrieving values from form
    init_features = [float(x) for x in request.form.values()]
    final_features = [np.array(init_features).reshape(1, -1)]
    
    prediction = int(model.predict(final_features)[0]) # making prediction


    return render_template('index.html', prediction_text='Predicted Class: {}'.format(prediction)) # rendering the predicted result

if __name__ == "__main__":
    app.run(debug=True)
