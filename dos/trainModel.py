#!/usr/bin/python

"""
Classifier model
"""

import numpy as np
import pandas as pd
import pickle

# defs
filename='data.csv'

df = pd.read_csv(filename, header=0)
data = df.iloc[:,[0, 1]].values
target = df.iloc[:,2].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)
print(model)
print("Test score: {:.2f}".format(model.score(X_test, y_test)))

X_new = np.array([[10.7, 15.7]])
prediction= model.predict(X_new)
print("Prediction: {}".format(prediction[0]))

# saving model
model_name='model.pkl'
with open(model_name, 'wb') as file:
    pickle.dump(model, file)

# load model
with open(model_name, 'rb') as file:
    saved_model = pickle.load(file)

print("Prediction from saved model: {}".format(saved_model.predict(X_new)))
