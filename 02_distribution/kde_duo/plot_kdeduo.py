# Name [P381] KDE Plot Duo

# Versions
# 01 - Nov 22nd, 2023 - Starter
# 02 -


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd

from scipy.stats import gaussian_kde

import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
def plot_kde_duo(sample1, sample2, name1=None, name2=None, title=None,
                 bins="sqrt", alpha=0.3, mean_line=True, savefig=False,
                 verbose=True):
    """
    Plots two kernel-density gaussian line.

    Variables:
    * sample1 = Data from serie 1,
    * name1 = Title or name from serie 1,
    * sample2 = Data from serie 2,
    * name2 = Title or name from serie 2,
    * title = Title for the plot. If savefig=True, will be the name of the file,
    * bins_alpha = transparency applied to the area under the curve (default=0.3),
    * savefig = True or False*. False will only diplay the plot, True will store
                the file at current folder with 'title' name,
    * verbose = True* or False. Displays important messages at prompt.

    Sources:
    Binning: https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html
    KDE Line: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html

    """
    # Texts preparation
    if(title == None):
        title = "KDE Gaussian"

    if(name1 == None):
        name1 = "sample 1"

    if(name2 == None):
        name2 = "sample 2"


    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["figure.dpi"] = 180
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"


    # Plot
    fig = plt.figure(figsize=[6, 3.375])
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    sample_list = [sample1, sample2]
    name_list = [name1, name2]
    color_list = ["navy", "darkred"]

    zorder = 20
    for (color, name, array) in zip(color_list, name_list, sample_list):
        array = np.array(array)
        x, y = kde_line(array)
        
        plt.plot(x, y, color=color, linewidth=1.5, label=name, zorder=zorder+1)
        plt.fill_between(x, y, 0, color=color, alpha=alpha, zorder=zorder)

        if(mean_line == True):
            plt.axvline(x=np.mean(array), color=color, linewidth=1, zorder=zorder-1)

        zorder = zorder + 10


    plt.grid(axis="both", color="lightgrey", linewidth=0.5, linestyle="--", zorder=10)
    plt.ylim(bottom=0)
    plt.legend(loc="best", framealpha=1)

    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)

        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()

    plt.close(fig)

    return None
    

def kde_line(array, tail=20):
    """
    Calculates the Kernel-density gaussian estimation

    More info:
    KDE Line: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html

    """
    # Density space adjust (increase tail borders)
    x_min = np.min(array)
    x_max = np.max(array)

    border = (x_max - x_min) * (tail/100)

    x_min = np.round(x_min - border, decimals=0)
    x_max = np.round(x_max + border, decimals=0)

    # Kernel-density gaussian estimative
    density = gaussian_kde(array)
    x = np.linspace(start=x_min, stop=x_max, num=100)
    y = density(x)

    return x, y

    
# end
