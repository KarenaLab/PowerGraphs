# Powergraphs: T-Test [P386] --------------------------------------------

# Libraries
import numpy as np
import pandas as pd
import scipy.stats as st

import matplotlib.pyplot as plt


# Versions
# 01 - Dec 08th, 2023 - Starter
# 02 -


# Insights, improvements and bugfix
#



# Functions
def gaussian_curve(loc, scale, num=500):
    """

    More info:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html

    """
    x = np.linspace(start=(loc - (4 * scale)), stop=(loc + (4 * scale)), num=num)
    y = st.norm.pdf(x, loc, scale)


    return x, y

