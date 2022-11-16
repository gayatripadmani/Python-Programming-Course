## scikit - learn ##

# What is scikit - learn? #

# Simple and efficient tool for data mining and data analysis

# Built on NumPy, SciPy and matplotlib

# Open source, commercially usable - BSD license

# What we can achieve using scikit - learn #

# classification - Identifying which category an object belongs to
# Application : Spam detection

# Regression - Predicting an attribute associated with an object.
# Application : Stock prices predication

# Clustering - Automatic grouping of similar objects into sets.
# Application : Customer segmentation

# Model Selection - Comparing, validating and choosing parameters and models.
# Application : Improving model accuracy via parameter tuning

# Dimensionality reducation - Reducing the number of random variables to consider.
# Application : To increases model efficiency

# Pre - processing - Feature extraction and normalization
# Application : Transforming input data such as text for use with machine learning algorithms.

# Importing required packages.
from gettext import install

import inline as inline
import matplotlib
import pandas as pd
import pip
import seaborn as sns
import sklearn
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
# from sklearn import SVM
from sklearn.neural_network import MLPClassifier
# from sklearn.Linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
# %matplotlib inline
import numpy as np

# Loading dataset
wine = pd.read_csv('winequality-red.csv', sep=';')
# print(wine, "\n")

# print(wine.head())

# print(wine.info())

# wine.isnull().sum()

# Preprocessing Data
bins = (2, 6, 5, 8)
group_names = ['bad', 'good']
wine['quality'] = pd.cut(wine['quality'], bins= bins, labels= group_names)
wine['quality'].unique()

# label_quality = LabelEncoder()

# wine['quality'] = label_quality.fit_transform('quality')

# wine.head()

# wine['quality'].value_counts()

# sns.countplot(wine['quality'])

# Now seperate the dataset as response variable and feature variables
x = wine.drop('quality', axis=1)
y = wine['quality']

# Train and Test splitting of data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Applying standard scaling to get optimized result

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# x_train[:10]

## Random Forest Classifier

rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(x_train, y_train)
pred_rfc = rfc.predict(x_test)

# x_test[:20]

# Let's see how our model performed
print(classification_report(x_test, pred_rfc))
print(confusion_matrix(y_test, pred_rfc))

## SVM Classifier
# clf = sklearn.svm.SVC()
# clf.fit(x_train, y_train)
# pred_clf = clf.predict(x_test)

# Let's see how our model performed
# print(classification_report(y_test, pred_rfc))
# print(confusion_matrix(y_test, pred_clf))

## Neural Network

# mlpc = MLPClassifier(hidden_layer_sizes=(11, 11, 11), max_iter=500)
# mlpc.fit(x_train, y_train)
# pred_mlpc = mlpc.predict(x_test)

# Let's see how our model performed

# print(classification_report(y_test, pred_mlpc))
# print(confusion_matrix(y_test, pred_mlpc))

# from sklearn.metrics import accuracy_score
# cm = accuracy_score(y_test, pred_rfc)
# cm

# wine.head(10)

# xnew = [[7.3, 0.58, 0.00, 2.0, 0.065, 15.0, 21.0, 0.9946, 3.36, 0.47,10.0]]
# xnew = sc.transform(xnew)
# ynew = rfc.predict(xnew)
# ynew

