# PowerGraphs Tools [P397]

# Versions
# 01 - Jan 24th, 2024 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd

import scipy.stats as st

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec



# ----------------------------------------------------------------------
def import_rcparams():
    """
    Imports RC Params to standartize plots.
    
    """
    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"


    return None    


