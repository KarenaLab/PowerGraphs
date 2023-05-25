
# Libraries
import numpy as np
import pandas as pd

from plot_duohistogram_v01 import *

# Program
df = pd.read_csv("iris.csv", sep=",", encoding="utf-8")

df_setosa = df.groupby(by="species").get_group("setosa")
df_versicolor = df.groupby(by="species").get_group("versicolor")
df_virginica = df.groupby(by="species").get_group("virginica")

cols_list = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

for col in cols_list:
    plot_duohistogram(serie1=df_setosa[col], name1="setosa",
                      serie2=df_versicolor[col], name2="versicolor",
                      serie3=df_virginica[col], name3="virginica",
                      title=f"Iris Histogram - {col}", bins_alpha=0.4,
                      savefig=False)

