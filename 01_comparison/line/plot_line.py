# Plot Line [P264] -----------------------------------------------------

# Versions
# 01 - Jan 21st, 2023 - Starter
# 02 - Jun 12th, 2023 - Adjust params
#    - Jan 03rd, 2024 - Set legend over all items
# 03 - Jan 04th, 2024 - (( refactoring ))
#      Feb 06th, 2024 - Add grid default selection
#      Feb 26th, 2024 - Add hline and vline option
#


# Insights, improvements and bugfix
# 


# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------

def plot_line(x, y, title=None, xlabel=None, ylabel=None, color="navy",
              linewidth=1.5, grid="both", vline=None, hline=None,
              remove_axis=False,
              savefig=False, verbose=True):

    """
    Plots a line graph with **x** and **y**.
    Objective is to make life easier for a first simple plot and be a
    support for more detailed graphs.

    """
    # Data preparation
    x = np.array(x)
    y = np.array(y)

    # Title
    if(title == None):
        title = "Line plot"

    # Grid Axis
    grid_default = "both"
    grid_list = ["x", "y", "both"]
    if(grid_list.count(grid) == 0):
        print(f' >>> Error: "grid_axis" option not valid. Using "{grid_default}" as forced option.')
        grid = grid_default[:]


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
    fig = plt.figure(figsize=[6, 3.375])        # Widescreen [16:9]
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")
    ax = plt.axes()

    plt.plot(x, y, color=color, linewidth=linewidth, zorder=20)

    plt.grid(axis=grid, color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    if(isinstance(hline, list) == True):
        for y in hline:
            plt.axhline(y=y, color="darkred", linewidth=0.8, zorder=19)

    if(isinstance(vline, list) == True):
        for x in vline:
            plt.axvline(x=x, color="darkred", linewidth=0.8, zorder=19)
            
    if(xlabel != None):
        plt.xlabel(xlabel, loc="right")

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
