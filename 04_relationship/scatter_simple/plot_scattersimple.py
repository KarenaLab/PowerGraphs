# Scatter plot - Simple [P286] ------------------------------------------


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------
def plot_scattersimple(x, y, title=None, xlabel=None, ylabel=None, color="navy",
                       alpha=0.8, mark_size=20, savefig=False, verbose=True):
    """

    More info:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

    """
    # Data preparation
    x = np.array(x)
    y = np.array(y)

    # Title
    if(title == None): title = "Scatter plot"

    # RC Params
    set_rcparams()
    

    # Plot
    fig = plt.figure(figsize=[6, 3.375])    # Widescreen 16:9
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    plt.scatter(x, y, s=mark_size, color=color, edgecolor="white", alpha=alpha, zorder=20)

    if(xlabel != None):
        plt.xlabel(xlabel, loc="center")
        
    if(ylabel != None):
        plt.ylabel(ylabel, loc="center")

    plt.grid(axis="both", color="grey", linestyle="--", linewidth=0.5, zorder=5)       

    plt.tight_layout()

    # Printing 
    if(savefig == True):
        plt.savefig(title, dpi=320)

        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()

    plt.close(fig)

    return None    


def set_rcparams():
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"
    plt.rcParams["xtick.major.size"] = 3.5
    plt.rcParams["ytick.major.size"] = 0

    return None


