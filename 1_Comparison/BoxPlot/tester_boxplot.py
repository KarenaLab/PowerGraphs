
# Libraries
import numpy as np
import pandas as pd

from plot_boxplot_v01 import *

# Setup/Config


# Program --------------------------------------------------------------
filename = "iris.csv"

df = pd.read_csv(filename, sep=",", encoding="utf-8")
cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

plot_boxplot(df, columns=cols, title="Iris - BoxPlot", savefig=True)

