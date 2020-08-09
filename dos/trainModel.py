#!/usr/bin/python

"""
Classifier model
"""

import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# defs
filename='data.csv'

df = pd.read_csv(filename, header=0)
data = df.iloc[:,[0, 1]].values
target = df.iloc[:,2].values

X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0, test_size=0.2)
print(X_train.shape, X_test.shape)
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

# Plot non-normalized confusion matrix
class_names = ['Normal Traffic', 'DoS Traffic']
np.set_printoptions(precision=2)
titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]
for title, normalize in titles_options:
    disp = plot_confusion_matrix(model, X_train, y_train,
                                 display_labels=class_names,
                                 cmap=plt.cm.Blues,
                                 normalize=normalize)
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

for title, normalize in titles_options:
    disp = plot_confusion_matrix(model, X_test, y_test,
                                 display_labels=class_names,
                                 cmap=plt.cm.Blues,
                                 normalize=normalize)
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

plt.show()
