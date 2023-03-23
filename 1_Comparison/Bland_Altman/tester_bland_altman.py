
import numpy as np
import pandas as pd

from plot_blandaltman_v01 import *


y_true = [1, 5, 10, 20, 50, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250,
          300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850,
          900, 950, 1000]

y_pred = [8, 16, 30, 24, 39, 54, 40, 68, 72, 62, 122, 80, 181, 259, 275,
          380, 320, 434, 479, 587, 626, 648, 738, 766, 793, 851, 871,
          957, 1001, 960]

plot_blandaltman(y_true, y_pred, title="Testing Bland-Altman Analysis")
