# [P499] PowerGraphs MissingNo Dendrogram

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
def plot_missingno_dendrogram(DataFrame, figsize=[8, 4.5], title=None, filter=None,
                              savefig=False, verbose=True):
    """


    """
    # Settings (fixed)
    color = (0, 0, 0)
    fontsize = 7

    # Plot
    msno.dendrogram(DataFrame, figsize=figsize, fontsize=fontsize, filter=filter)


    # Printing
    if(savefig == True):
        plt.savefig(title, dpi=320)
        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()


    plt.close()   

    return None    
    

