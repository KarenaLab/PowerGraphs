# Bar Horizontal [P353] -------------------------------------------------

# Versions
# 01 - Jan 06th, 2024 - Starter
#


# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------

def plot_barv(x, height, title=None, ylabel=None, color="navy",
              grid_axes="y", remove_axis=False,
              savefig=False, verbose=True):
    """
    width = y
    upside-down sequence

    """
    # Data preparation
    x = np.array(x)
    height = np.array(height)

    # Title
    if(title == None):
        title = "Bar vertical"

    # Grid Axis
    grid_default = "y"
    grid_list = ["x", "y", "both"]
    if(grid_list.count(grid_axes) == 0):
        print(f' >>> Error: "grid_axis" oprtion not valid. Using "{grid_default}" as forced option.')
        grid_axes = grid_default[:]

    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"
    plt.rcParams["xtick.major.size"] = 0

    # Plot
    fig = plt.figure(figsize=[6, 3.375])        # Widescreen [16:9]
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    plt.bar(x, height=height, color=color, edgecolor="black", zorder=20)

    plt.grid(axis=grid_axes, color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    if(ylabel != None):
        plt.ylabel(ylabel, loc="top")

    if(remove_axis == True):
        plt.tick_params(length=0,labelleft="on", labelbottom="on")
        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)
        ax.spines.left.set_visible(False)

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

    
