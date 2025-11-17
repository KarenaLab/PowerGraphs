# Identity Line [P315] -------------------------------------------------

# Insights and bugfix
# 01 - Add a color adjust
# 02 - Add remove ticks from axis
# 


# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# -----------------------------------------------------------------------
def plot_identityline(y_true, y_pred, title=None, xlabel=None,
                      ylabel=None, alpha=0.7, identity_line=True,
                      legend_loc="lower right", grid="both",
                      savefig=False, verbose=True):
    """
    Plots an identity line from **y_true** versus **y_pred**.

    """
    # Data preparation
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    # Plot details adjust
    if(title == None):
        title = "Identity line"

    if(xlabel == None):
        xlabel = "ground truth"

    if(ylabel == None):
        ylabel = "prediction"

    # Grid Axis
    grid_default = "both"
    grid_list = ["x", "y", "both"]
    if(grid_list.count(grid) == 0):
        print(f' >>> Error: "grid_axis" oprtion not valid. Using "{grid_default}" as forced option.')
        grid = grid_default[:]

    # Set graph borders
    lower = min(y_pred.min(), y_true.min())
    upper = max(y_pred.max(), y_true.max())
    step = (upper - lower) / 10

    # Linear regression
    regr_x = np.linspace(start=lower, stop=upper, num=10)
    b, a = np.polyfit(y_true, y_pred, deg=1)
    regr_y = [a + b * i for i in regr_x]


    # RC Params
    set_rcparams()
    

    # Plot
    fig = plt.figure(figsize=[6, 3.375])        # Widescreen [16:9]
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    plt.scatter(y_true, y_pred, s=30, color="navy", edgecolor="white", alpha=alpha, label="data", zorder=20)
    plt.plot([lower, upper], [lower, upper], color="red", linewidth=0.8, label="identity line", zorder=19)
    plt.plot(regr_x, regr_y, color="green", linestyle="-.", linewidth=0.5, label="regression", zorder=18)

    plt.grid(axis=grid, color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    plt.ylim([lower-step, upper+step])
    plt.xlim([lower-step, upper+step])
    plt.ylabel(ylabel, loc="center")
    plt.xlabel(xlabel, loc="center")
    
    plt.legend(loc=legend_loc, fontsize=7, framealpha=1).set_zorder(99)

    # Printing
    plt.tight_layout()

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


