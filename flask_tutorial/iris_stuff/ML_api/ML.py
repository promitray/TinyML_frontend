import numpy as np
import pandas as pd 
from sklearn import datasets
from pandas import Series, DataFrame
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
import pickle

# Reading the data

iris = datasets.load_iris()
print (iris['data'], iris['target'])

#iris = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
#                     columns= iris['feature_names'] + ['target'])


features=pd.DataFrame(iris['data'])
target=iris['target']
model=LogisticRegression(max_iter=1000)
model.fit(features,target)


#iris.drop("Id", axis=1, inplace = True)
#y = iris['Species']
#iris.drop(columns='Species',inplace=True)
#X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]

# Training the model
#x_train,x_test,y_train,y_test = train_test_split(X,y, test_size=0.3)
#model = LogisticRegression()
#model.fit(x_train,y_train)

pickle.dump(model,open('model.pkl','wb'))