
import numpy as np
import pandas as pd

from plot_histogram_v01 import *


filename = "hmeq.csv"
df = pd.read_csv(filename, sep=",", encoding="utf-8")

cols_hist = ["LOAN", "MORTDUE", "VALUE", "YOJ", "DEROG",
             "DELINQ", "CLAGE", "NINQ", "CLNO", "DEBTINC"]


plot_histogram(df["LOAN"], bins="sqrt")
plot_histogram(df["MORTDUE"], bins="sqrt", kde=False)
plot_histogram(df["CLAGE"], bins="freedman", grid_axis="both")
plot_histogram(df["MORTDUE"], title="Histogram - HMEQ MortDue", bins="sqrt", savefig=True)
