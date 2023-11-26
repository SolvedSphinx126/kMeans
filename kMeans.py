#! /usr/bin/env python3
# Import necessary libraries
from subprocess import *
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

irisDataFile = open("iris_data/iris.data")
datalines = irisDataFile.readlines()
rawDataVals = []

for line in datalines:
    for i in range(len(line.split(","))):
        rawDataVals.append((line.split(",")[i]).strip() if i == len(line.split(",")) - 1 else float(line.split(",")[i]))

dataLabels = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
formattedDataVals = []

i = 0
while i < len(rawDataVals):
    formattedDataVals.append([rawDataVals[j] for j in range(i, i + len(dataLabels))])
    i += len(dataLabels)

dataframe = pd.DataFrame(formattedDataVals, columns=dataLabels)


# Format the data for use in KMeans

kFrame = dataframe.drop(columns="class")
kMatrix = kFrame.values

kmeans = KMeans(n_clusters=3, init="random", n_init=1).fit(kMatrix)

xCol = "sepal_length"
yCol = "sepal_width"

for index, val in enumerate(kmeans.labels_):
    if (val == 0):
        plt.scatter(x=kFrame[xCol].values[index], y=kFrame[yCol].values[index], c='r')
    elif (val == 1):
        plt.scatter(x=kFrame[xCol].values[index], y=kFrame[yCol].values[index], c='g')
    elif (val == 2):
        plt.scatter(x=kFrame[xCol].values[index], y=kFrame[yCol].values[index], c='b')

for index, val in enumerate(kmeans.cluster_centers_):
    plt.scatter(x=val[dataLabels.index(xCol)], y=val[dataLabels.index(yCol)], s=100, marker='x', c='r' if index == 0 else 'g' if index == 1 else 'b')
plt.show()

trainingSample = int(150 * 0.8)

Popen("./data_formatter.py", shell = True, stdout = PIPE).communicate()

Popen(f"./libsvm-3.32/tools/subset.py iris_libsvm.data {trainingSample} training.data testing.data", shell = True, stdout = PIPE).communicate()

f = Popen(f"./libsvm-3.32/tools/easy.py training.data testing.data", shell = True, stdout = PIPE).stdout

print("SVM Accuracy")
for line in f:
    line = line.decode("utf-8")
    if not line.startswith("b'[local]"):
        if not len(line.strip()) == 0:
            print(line)