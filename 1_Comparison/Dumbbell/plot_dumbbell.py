
# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Versions
# 01 - May 12th, 2023 - First version
# 02 -


# Insights and future upgrades
# 


def plot_dumbbell(labels, minimum, maximum, title=None,
                  markersize=10, xlabel=None, savefig=False, verbose=True):
    """
        
    
    """

    # Data preparation
    labels = labels.tolist()
    minimum = np.array(minimum)
    maximum = np.array(maximum)

    # Plot
    fig = plt.figure(figsize=[8, 4.5])
    grd = fig.add_gridspec(ncols=2, width_ratios=[2, 8])

    ax0 = fig.add_sublot(grd[0, 1])

    if(title == None):
        title = "Dumbell plot"

    plt.suptitle(title, fontsize=10, fontweight="bold")

    ax0.hlines(y=labels, xmin=minimum, xmax=maximum, color="dimgrey", linewidth=1.2, zorder=20)
    ax0.scatter(x=minimum, y=range(0, len(labels)), s=markersize, color="green", label="minimum", zorder=21)
    ax0.scatter(x=maximum, y=range(0, len(labels)), s=markersize, color="red", label="maximum", zorder=22)

    ax0.grid(axis="x", color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    if(xlabel != None):
        plt.set_xlabel(xlabel, loc="right")

    ax0.legend(loc="upper right", framealpha=1)

    if(savefig == True):
        plt.savefig(title, dpi=240)

        if(verbose == True):
            print(f' >>> saving plot as "{title}.png"') 

    else:
        plt.show()

    plt.close(fig)


    return None

