import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import pickle


st.write("""
# Simple App to predict categories
""")


st.sidebar.header('User Input Parameters')

def user_input_features():
    #S1 = st.sidebar.slider('S1', 0, 30, 10)
    S1 = st.sidebar.number_input(label="S1",step=1.,format="%.2f")
    #S2 = st.sidebar.slider('S2', 0, 45, 10)
    S2 = st.sidebar.number_input(label="S2",step=1.,format="%.2f")
    #S3 = st.sidebar.slider('S3', 0, 30, 10)
    S3 = st.sidebar.number_input(label="S3",step=1.,format="%.2f")
    #S4 = st.sidebar.slider('S4', 0, 50, 10)
    S4 = st.sidebar.number_input(label="S4",step=1.,format="%.2f")
    #S5 = st.sidebar.slider('S5', 0, 120, 20)
    S5 = st.sidebar.number_input(label="S5",step=1.,format="%.2f")
    #S6 = st.sidebar.slider('S6', 0, 20, 6)
    S6 = st.sidebar.number_input(label="S6",step=1.,format="%.2f")
    #S7 = st.sidebar.slider('S7', 40, 100, 20)
    S7 = st.sidebar.number_input(label="S7",step=1.,format="%.2f")

    data = {'S1': S1,
            'S2': S2,
            'S3': S3,
            'S4': S4,
            'S5': S5,
            'S6': S6,
            'S7': S7
            }
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()


st.subheader('User Input parameters')
st.write(df)


model = pickle.load(open('model.pkl', 'rb'))



prediction = model.predict(df)

st.subheader('Class labels and their corresponding index number')

st.subheader('Prediction')
st.write(int(prediction))
#st.write(prediction)

#if prediction == 0 else st.image(versicolor)  if prediction == 1 else st.image(virginica)


