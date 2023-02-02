
import numpy as np
import pandas as pd

from plot_histogram_v01 import *


filename = "hmeq.csv"
df = pd.read_csv(filename, sep=",", encoding="utf-8")
