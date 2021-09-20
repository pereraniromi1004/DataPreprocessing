# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 16:21:07 2021

@author: perer
"""

## ---(Mon Sep 20 11:26:29 2021)---
from sklearn import preprocessing
import numpy as np
X_train=np.array([[1.,-1.,2.],])
X_train=np.array([[1.,-1.,2.],[2.,0.,0.],[0.,1.,-1.]])
scaler=preprocessing.StandardScaler().fit(X_train)
scaler
scaler.mean
original_means = np.mean(X)
original_stds = np.std(X)
original_means = np.mean(X_train)
scaler.mean
scaler.scale_
x_scaled=scaler.transform(X_train)
x_scaled
x_scaled.mean(axis=0)
x_scaled.std(axis=0)
from sklearn.datasets import make_classification
from sklearn.linear_model importLogisticRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
X,y=make_classification(random_state=42)
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42)
pipe=make_pipeline(StandardScaler(),LogisticRegression())
pipe.fit(X_train,y_train)
pipe.score(X_test,y_test)