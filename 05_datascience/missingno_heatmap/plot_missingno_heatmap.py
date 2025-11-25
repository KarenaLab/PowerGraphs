# [P498] PowerGraphs - MissingNo Heatmap

# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd
import scipy.stats as stats
import missingno as msno

import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
def plot_missingno_heatmap(DataFrame, title=None, figsize=[8, 4.5],
                           cmap="Blues",
                           savefig=False, verbose=True):
    """

    More info: https://github.com/ResidentMario/missingno/blob/master/missingno/missingno.py
    """
    # Settings (fixed)
    fontsize = 7

    # Plot
    msno.heatmap(DataFrame, figsize=figsize, fontsize=fontsize, cmap=cmap,
                 vmin=0, vmax=1)

    # Printing
    if(savefig == True):
        plt.savefig(title, dpi=320)
        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()


    plt.close()   

    return None 

