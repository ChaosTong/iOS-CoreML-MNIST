from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', version=1, cache=True)
X, y = mnist['data'], mnist['target']

# Common imports
import numpy as np
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import heapq
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import datasets, model_selection
from sklearn.metrics import classification_report
from sklearn.externals import joblib

import coremltools

some_digit = X[36000]

def forest_clf():
    forest_clf = joblib.load("forest_clf.pkl")
    # np.set_printoptions(threshold=784)
    # print(X[0], X[1], X[2], X[3])
    predict = forest_clf.predict([X[0], X[1], X[2], X[3]])
    print(predict)

def knn():
    knn = joblib.load("knn.pkl")
    indx = np.random.choice(len(y), 70000, replace=False)
    test_target = [y[i] for i in indx[60000:70000]]
    print(classification_report(test_target, knn))

def convert():
    model = joblib.load("forest_clf.pkl")
    # output_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # scale = 1/255
    list_0 = ['image' for x in range(784)]
    # convert(sk_obj, input_features = None, output_feature_names =
    coreml_model = coremltools.converters.sklearn.convert(model, input_features=list_0,output_feature_names="output")
    print(type(coreml_model))
    coreml_model.author = 'ChaosTong'
    coreml_model.license = 'MIT'
    coreml_model.short_description = 'Model to classify hand written digit'

    coreml_model.input_description['image'] = 'Grayscale image of hand written digit'
    coreml_model.output_description['output'] = 'Predicted digit'

    coreml_model.save('mnistForest.mlmodel')

convert()
# forest_clf()