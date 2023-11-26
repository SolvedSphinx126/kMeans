# Import necessary libraries
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

c1 = []
c2 = []
c3 = []

for index, val in enumerate(kmeans.labels_):
    if (val == 0):
        plt.scatter(x=kFrame["sepal_length"].values[index], y=kFrame["sepal_width"].values[index], c='r')
    elif (val == 1):
        plt.scatter(x=kFrame["sepal_length"].values[index], y=kFrame["sepal_width"].values[index], c='g')
    elif (val == 2):
        plt.scatter(x=kFrame["sepal_length"].values[index], y=kFrame["sepal_width"].values[index], c='b')

for index, val in enumerate(kmeans.cluster_centers_):
    plt.scatter(x=val[0], y=val[1], s=100, marker='x', c='r' if index == 0 else 'g' if index == 1 else 'b')
plt.show()