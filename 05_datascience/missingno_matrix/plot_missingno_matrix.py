# [P497] PowerGraphs - MissingNo Matrix

# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd
import scipy.stats as stats
import missingno as msno

import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
def plot_missingno_matrix(DataFrame, title=None, figsize=[8, 4.5],
                          sort=None,
                          savefig=False, verbose=True):
    """

    More info: https://github.com/ResidentMario/missingno/blob/master/missingno/missingno.py
    """
    # Settings (fixed)
    color = (0, 0, 0)   # Only accepts RGB colors)
    fontsize = 7

    # Plot   
    msno.matrix(DataFrame, figsize=figsize, sort=sort, fontsize=fontsize,
                color=color, sparkline=True, width_ratios=[10,1])

    # Printing
    if(savefig == True):
        plt.savefig(title, dpi=320)
        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()


    plt.close()   

    return None 

