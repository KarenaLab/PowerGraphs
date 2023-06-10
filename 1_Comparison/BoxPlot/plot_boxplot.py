
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

def plot_boxplot(DataFrame, columns=None, title=None,
                 savefig=False, verbose=True):
    """


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
    

    # Plot
    fig = plt.figure(figsize=[8, 4.5])
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    plt.boxplot(data, labels=columns, notch=True, boxprops=boxprops, whiskerprops=whiskerprops,
                medianprops=medianprops, capprops=capprops, flierprops=flierprops, zorder=20)

    plt.grid(axis="y", color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)

        if (verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()


    plt.close(fig)

    return None

# end

