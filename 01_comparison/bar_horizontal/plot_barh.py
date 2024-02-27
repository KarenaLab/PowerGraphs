# Bar Horizontal [P354] -------------------------------------------------

# Versions
# 01 - Jan 06th, 2024 - Starter
#      Jan 30th, 2024 - Add ´upside_down´ variable
#      Feb 23rd, 2024 - Bugfix: grid and grid_default
#


# Insights, improvements and bugfix
# 01 - Add labels to the bars (Excel style)
# 02 - 


# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------

def plot_barh(x, width, title=None, xlabel=None, color="navy", left=0,
              upside_down=True, grid="x", remove_axis=False,
              savefig=False, verbose=True):
    """
    width = y
    upside-down sequence

    """
    # Data preparation
    if(upside_down == True):
        x = np.flip(x, axis=0)          # np.flip to make plot upside-down
        width = np.flip(width, axis=0)
        
    else:
        x = np.array(x)
        width = np.array(width)


    # Title
    if(title == None):
        title = "Bar horizontal"


    # Grid Axis
    grid_default = "x"
    grid_list = ["x", "y", "both"]
    if(grid_list.count(grid_axes) == 0):
        print(f' >>> Error: "grid_axis" option not valid. Using "{grid_default}" as forced option.')
        grid_axes = grid_default[:]


    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"
    plt.rcParams["xtick.major.size"] = 3.5
    plt.rcParams["ytick.major.size"] = 0
    


    # Plot
    fig = plt.figure(figsize=[6, 3.375])        # Widescreen [16:9]
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    plt.barh(x, width=width, color=color, edgecolor="black", left=left, zorder=20)

    plt.grid(axis=grid, color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    if(xlabel != None):
        plt.xlabel(xlabel, loc="right")

    if(remove_axis == True):
        plt.tick_params(length=0,labelleft="on", labelbottom="on")
        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)
        ax.spines.bottom.set_visible(False)


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

    
