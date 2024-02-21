# Powergraphs: T-Test [P386] --------------------------------------------

# Libraries
import numpy as np
import pandas as pd
import scipy.stats as st

import matplotlib.pyplot as plt


# Versions
# 01 - Dec 08th, 2023 - Starter
# 02 -


# Insights, improvements and bugfix
#



# Functions
def plot_ttest(data_a, data_b, title=None, savefig=False, verbose=True):
    """


    """
    # Data preparation
    data_a = np.array(data_a)
    data_b = np.array(data_b)


    if(title != None):
        title = "T Test"

    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"
    plt.rcParams["xtick.major.size"] = 3.5
    plt.rcParams["ytick.major.size"] = 3.5

    # Plot
    fig = plt.figure(figsize=[6, 3.375])
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)
    plt.ylabel("density", loc="top")

    plt.legend(loc="upper right", framealpha=1).set_zorder(99)

    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)

        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()


    plt.close(fig)

    return None    

    
def gaussian_curve(loc, scale, num=500):
    """

    More info:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html

    """
    x = np.linspace(start=(loc - (4 * scale)), stop=(loc + (4 * scale)), num=num)
    y = st.norm.pdf(x, loc, scale)


    return x, y

