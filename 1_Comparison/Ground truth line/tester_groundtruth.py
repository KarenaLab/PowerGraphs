
import numpy as np
import pandas as pd

from plot_groundtruth_v01 import *


ground_truth = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
comparison = [0.1, 1.2, 2.1, 3.1, 4.0, 5.1, 6.2, 7.5, 8.2, 9.1]

ground_truth = np.array(ground_truth)
comparison = np.array(comparison)

plot_groundtruth(ground_truth, comparison, title="Testing ground truth line plot")

