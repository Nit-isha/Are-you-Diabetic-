# Importing dependencies

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm


def Check(input):
    data = pd.read_csv("diabetes.csv")
    X = data.drop(columns="Outcome", axis=1)
    Y = data["Outcome"]

    scaler = StandardScaler()
    scaler.fit(X)
    standardized_data = scaler.transform(X)

    X = standardized_data
    Y = data["Outcome"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.3, random_state=1)

    classifier = svm.SVC(kernel="linear")
    classifier.fit(X_train, Y_train)
    Y_predict = classifier.predict(X_test)

    # input_data = (4, 110, 92, 0, 0, 37.6, 0.191, 30) --> Not Diabetic
    input_data = input

    inputAsArray = np.asarray(input_data)
    inputDataReshape = inputAsArray.reshape(1, -1)

    stdInputData = scaler.transform(inputDataReshape)

    prediction = classifier.predict(stdInputData)
    if prediction == 0:
        return ("Person is NOT Diabetic")
    else:
        return ("Person is Diabetic")
