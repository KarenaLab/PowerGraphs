# Tester ScatterHistLinReg

import numpy as np
import pandas as pd

from ScatterHistLinReg_v07 import *

DF = pd.read_csv("winequality_red.csv", sep=";", encoding="utf-8")

title = "ScatterHistLinReg_v07"
data_x, data_y = DF["density"], DF["pH"]
ScatterHistLinReg(title, data_x, data_y)

