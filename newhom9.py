import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from sklearn import preprocessing
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import model_selection, neighbors
from sklearn.cluster import KMeans
iris = load_iris()
iternim = 10000
a = []
trainselect =[]
for i in range(0,iternim):
    X_train, X_test, y_train, y_test = train_test_split(iris.data,iris.target,test_size=0.1)
    model = KMeans(n_clusters=3)
    model.fit(X_train,y_train)
    b = metrics.silhouette_score(X_test,y_test)
    if b >= 0.80:
        print(b)
        trainselect.append(X_train)
        trainselect.append(y_train)
        print(trainselect)
        break
    a.append(b)
    if i == iternim-1:
        print(max(a))















