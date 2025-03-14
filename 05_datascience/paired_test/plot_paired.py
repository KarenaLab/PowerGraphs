# [P503] - Paired plot (for Paired Tests) -------------------------------

# Versions
# 01 - Mar 13th, 2025 - Starter


# Insights, improvements and bugfix
# 


# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------
def plot_paired(before, after, title=None, ylabel=None,
                down_color=None, up_color=None, neutral_color=None,
                savefig=False, verbose=True):

    """
    Returns a plot comparing **before** and **after**.
    Useful for T-Test visualizations.


    """
    # Data preparation
    before = np.array(before)
    after = np.array(after)

    # Title
    if(title == None):
        title = "T-Test paired plot"

    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"
    plt.rcParams["xtick.major.size"] = 0
    plt.rcParams["ytick.major.size"] = 3.5

    # Plot
    fig = plt.figure(figsize=[6, 3.375])        # Widescreen [16:9]
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")
    ax = plt.axes()

    for [bfr, afr] in zip(before, after):
        color = _color_pick(bfr, afr, down_color, up_color, neutral_color)
        
        plt.plot([1, 2], [bfr, afr], color=color, zorder=10)
        plt.scatter([1], [bfr], s=16, marker="o", color="#000000", zorder=20)
        plt.scatter([2], [afr], s=16, marker="o", color=color, zorder=20)


    plt.xticks([1, 2], ["before", "after"], fontsize=10)
    plt.grid(axis="y", linestyle="--", color="#D3D3D3", zorder=22)
             
    if(ylabel != None):
        plt.ylabel(ylabel, loc="top")


    # Remove axis
    plt.tick_params(length=0, labelleft="on", labelbottom="on")
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


def _color_pick(before, after, down_color=None, up_color=None, neutral_color=None):
    """


    """
    # Color selection
    if(down_color == None):
        down_color = "#00B9AA"      # Green SGB1

    if(up_color == None):
        up_color = "#ED0530"        # Red SGB1

    if(neutral_color == None):
        neutral_color = "#808080"   # Grey 50%        


    # Value selection
    if(before > after):
        color = down_color

    elif(before < after):
        color = up_color

    else:   # before == after
        color = neutral_color


    return color 
    
