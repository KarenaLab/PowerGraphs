# HeatMap Tester

import numpy as np
import pandas as pd

from plot_heatmapsquare_v08 import *


# Program
DF = pd.read_csv("winequality-red.csv", sep=";")

HeatMapSquare("HeatMapSquare_v07", DF)
HeatMapSquare("HeatMapSquare_v07", DF, decimals=3, fontsize=6)
HeatMapSquare("HeatMapSquare_v07", DF, aspect=0.5, fontsize=12)
HeatMapSquare("HeatMapSquare_v07", DF, figratio="A4", method="spearman")
HeatMapSquare("HeatMapSquare_v07", DF, cmap="Greys", method="kendall")
HeatMapSquare("HeatMapSquare_v07", DF, method="spearman")


