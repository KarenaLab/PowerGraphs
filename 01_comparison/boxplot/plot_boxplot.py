# Boxplot [P333] -------------------------------------------------------

# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# Version
# 01 - May 30th, 2023 - Starter
# 02 -


# Insights
#


# Program --------------------------------------------------------------

def plot_boxplot(DataFrame, columns=None, title=None, savefig=False, verbose=True):
    """
    Plots a boxplot comparing the data.
    Simple view.

    """

    # Data preparation
    data = DataFrame.copy()

    if(columns == None):
        columns = data.columns.tolist()

    else:
        data = data[columns]
        

    if(title == None):
        title = "Box Plot"


    # Parameters
    plt.rcParams["xtick.bottom"] = False

    boxprops = dict(linestyle="-", linewidth=1.5, color="black")
    whiskerprops = dict(linestyle="-", linewidth=1.5, color="black")
    capprops = dict(linestyle="-", linewidth=1.5, color="black")
    medianprops = dict(linestyle="-", linewidth=1.5, color="orange")
    flierprops = dict(marker="o", markerfacecolor="darkred", markeredgecolor="black", markersize=6)


    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["figure.dpi"] = 180
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.major.size"] = 0

    # Plot
    fig = plt.figure(figsize=[6, 3.375])
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    plt.boxplot(data, labels=columns, notch=True, boxprops=boxprops, whiskerprops=whiskerprops,
                medianprops=medianprops, capprops=capprops, flierprops=flierprops, zorder=20)

    plt.grid(axis="y", color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    plt.tight_layout()

    # Saving
    if(savefig == True):
        plt.savefig(title, dpi=320)

        if (verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()


    plt.close(fig)

    return None

# end

