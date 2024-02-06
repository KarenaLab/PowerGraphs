# Dumbbell -------------------------------------------------------------


# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Versions
# 01 - May 12th, 2023 - First version
#    - Jan 03rd, 2024 - Set legend over all items,
# 


# Insights and future upgrades
# 


def plot_dumbbell(labels, minimum, maximum, title=None,
                  markersize=10, xlabel=None, left_border=0.2, savefig=False, verbose=True):
    """
        
    
    """

    # Data preparation
    labels = labels.tolist()
    minimum = np.array(minimum)
    maximum = np.array(maximum)

    # Adjust left border (data labels space)
    if(left_border > 0 and left_border <= 0.5):
        left = left_border * 10
        right = (1 - left_border) * 10

    else:
        left = 2
        right = 8

        if(verbose == True):
            print(f" >>> Error: Invalid value for right_border (0 < x <= 0.5)")


    # Title
    if(title == None):
        title = "Dumbell plot"


    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"
            

    # Plot
    fig = plt.figure(figsize=[6, 3.375])        # [16:9] Widescreen
    grd = fig.add_gridspec(ncols=2, width_ratios=[left, right])

    ax0 = fig.add_sublot(grd[0, 1])

    plt.suptitle(title, fontsize=10, fontweight="bold")

    ax0.hlines(y=labels, xmin=minimum, xmax=maximum, color="dimgrey", linewidth=1.2, zorder=20)
    ax0.scatter(x=minimum, y=range(0, len(labels)), s=markersize, color="green", label="minimum", zorder=21)
    ax0.scatter(x=maximum, y=range(0, len(labels)), s=markersize, color="red", label="maximum", zorder=22)

    ax0.grid(axis="x", color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    if(xlabel != None):
        plt.set_xlabel(xlabel, loc="right")

    ax0.legend(loc="upper right", framealpha=1).set_zorder(99)

    if(savefig == True):
        plt.savefig(title, dpi=320)

        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()


    plt.close(fig)

    return None

