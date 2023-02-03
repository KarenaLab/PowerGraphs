
import numpy as np
import pandas as pd

from plot_histogram_v01 import *


filename = "hmeq.csv"
df = pd.read_csv(filename, sep=",", encoding="utf-8")

cols_hist = ["LOAN", "MORTDUE", "VALUE", "YOJ", "DEROG",
             "DELINQ", "CLAGE", "NINQ", "CLNO", "DEBTINC"]

for col in cols_hist:
    plot_histogram(df[col])
