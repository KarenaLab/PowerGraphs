# [P496] PowerGraphs - MissingNo Bar

# Versions
# 01 - Mar 07th, 2025 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd
import scipy.stats as stats
import missingno as msno

import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
def plot_missingno_bar(DataFrame, figsize=[8, 4.5], title=None,
                       savefig=False, verbose=True):
    """

    More info: https://github.com/ResidentMario/missingno/blob/master/missingno/missingno.py
    """
    # Settings (fixed)
    fontsize = 7

    # Plot
    msno.bar(DataFrame, figsize=figsize, fontsize=fontsize)


    # Printing
    if(savefig == True):
        plt.savefig(title, dpi=320)
        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()


    plt.close()   

    return None    

