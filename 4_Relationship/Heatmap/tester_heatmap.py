# HeatMap Tester

import numpy as np
import pandas as pd

from plot_heatmap_v08 import *


# Program
filename = "winequality-red.csv"
title = "plot_heatmap_v08"
df = pd.read_csv(filename, sep=";", encoding="utf-8")

plot_heatmap(df, title)
plot_heatmap(df, title, savefig=True)
plot_heatmap(df, title, decimals=3, colormap="Reds", fontsize=8, method="spearman")
plot_heatmap(df, title, colormap="Greys", method="kendall")

