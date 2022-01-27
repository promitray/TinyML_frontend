from flask import Flask
from flask_restful import Api, Resource, reqparse
import joblib
import pandas as pd
import numpy as np
import pickle
import tensorflow
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Dense


APP = Flask(__name__)
API = Api(APP)

ML_MODEL = pickle.load(open('model.pkl', 'rb'))


class Predict(Resource):

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('S1')
        parser.add_argument('S2')
        parser.add_argument('S3')
        parser.add_argument('S4')
        parser.add_argument('S5')
        parser.add_argument('S6')
        parser.add_argument('S7')
        
        args = parser.parse_args()
        print (args)

        X_new = np.fromiter(args.values(), dtype=float)
        print (X_new)
        X_new = X_new.reshape(1, -1)
        #X_new = pd.DataFrame(args, index = [0])
        #print (X_new)
        #print (type((X_new['S1'].iloc[0])))  

        prediction = int(ML_MODEL.predict(X_new)[0])
               
        out = {'prediction': prediction}
        
               
        return out, 200


API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(host="0.0.0.0", debug=True, port='1080')