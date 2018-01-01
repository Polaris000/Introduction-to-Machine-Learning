from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# inbuilt dataset with the sklearn lib
iris = datasets.load_iris()

#print(iris.target_names)

x = iris.data
y = iris.target

df = pd.DataFrame(x, columns=iris.feature_names)


## different attributes to use with the pandas dataframe
# print(df.describe())
# print(df.info())
# print(df.head())



