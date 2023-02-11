# HeatMap Tester

import numpy as np
import pandas as pd

from plot_correlationmap_v01 import *


# Program
filename = "winequality-red.csv"
title = "Correlation Map v01"
df = pd.read_csv(filename, sep=";", encoding="utf-8")

plot_correlationmap(df)
plot_correlationmap(df, savefig=True)
plot_correlationmap(df, high_threshold=5, low_threshold=15)
#plot_correlationmap(df, decimals=3, method="spearman")
