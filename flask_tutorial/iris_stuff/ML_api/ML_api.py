from flask import Flask
from flask_restful import Api, Resource, reqparse
import joblib
import pandas as pd
import numpy as np
import pickle


APP = Flask(__name__)
API = Api(APP)

ML_MODEL = pickle.load(open('model.pkl', 'rb'))


class Predict(Resource):

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('petal_length')
        parser.add_argument('sepal_length')
        parser.add_argument('petal_width')
        parser.add_argument('sepal_width')
        
        args = parser.parse_args()
        print (args)

        #X_new = np.fromiter(args.values(), dtype=float)
        #print (X_new)
        #X_new = X_new.reshape(1, -1)
        X_new = pd.DataFrame(args, index = [0])
        print (X_new)  

        prediction = int(ML_MODEL.predict(X_new)[0])
               
        out = {'prediction': prediction}
        
               
        return out, 200


API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(host="0.0.0.0", debug=True, port='1080')