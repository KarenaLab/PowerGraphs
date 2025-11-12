# [P333] Boxplot -------------------------------------------------------

# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# Version
# May 30th, 2023 - Starter,
# Jan 06th, 2024 - Refactoring,
# Feb 27th, 2025 - Solve NaNs indepenent and add boxprops facecolor,
#


# Insights
# 01 - Only drop NaNs by column (Data separation) - Feb 27th, 2025,
#


# Program --------------------------------------------------------------
def plot_boxplot(DataFrame, columns=None, title=None, ylabel=None,
                 notch=True, grid_axes="y", facecolor="white",
                 savefig=False, verbose=True):
    """
    Plots a boxplot comparing the data.

    (( add columns description ))

    """
    # Data preparation
    columns = col_select(DataFrame, columns)

    data = list()
    for col in columns:
        info = np.array(DataFrame[col])
        info = list(info[~np.isnan(info)])
        data.append(info)

        
    # Title
    if(title == None):
        title = "BoxPlot"


    # Grid Axis
    grid_default = "y"
    grid_list = ["x", "y", "both"]
    if(grid_list.count(grid_axes) == 0):
        print(f' >>> Error: "grid_axis" option not valid. Using "{grid_default}" as forced option.')
        grid_axes = grid_default[:]


    # RC Params
    set_rcparams()

    
    # Parameters
    boxprops = dict(linestyle="-", linewidth=1.5, color="black")
    whiskerprops = dict(linestyle="-", linewidth=1.5, color="black")
    capprops = dict(linestyle="-", linewidth=1.5, color="black")
    medianprops = dict(linestyle="-", linewidth=1.5, color="orange")
    flierprops = dict(marker="o", markerfacecolor="darkred", markeredgecolor="black", markersize=3)


    # Plot
    fig = plt.figure(figsize=[6, 3.375])        # Widescreen [16:9]
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    bp = plt.boxplot(data, labels=columns, notch=notch, boxprops=boxprops, whiskerprops=whiskerprops,
                     medianprops=medianprops, capprops=capprops, flierprops=flierprops, patch_artist=True, zorder=20)


    # BoxProps background color
    for patch in bp["boxes"]:
        patch.set_facecolor(facecolor)

    # Labels
    if(ylabel != None):
        plt.ylabel(ylabel, loc="top")

    # Grid    
    plt.grid(axis=grid_axes, color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)
       
    # Printing
    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=320)

        if (verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()


    plt.close(fig)

    return None


def col_select(DataFrame, columns):
    """
    Columns names verification.
    Also standatize the output as a list for pandas standard.
    
    """
    def column_checker(DataFrame, col_list):
        col_select = list()
        df_cols = DataFrame.columns.to_list()

        for i in col_list:
            if(df_cols.count(i) == 1):
                col_select.append(i)


        return col_select


    # Columns preparation
    if(columns == "all" or columns == None):
        # Default: takes **all** columns from DataFrame.
        col_select = list(DataFrame.columns)

    elif(isinstance(columns, str) == True):
        # Tranforms a sting into a list
        columns = columns.replace(" ", "")
        columns = columns.split(",")
        col_select = column_checker(DataFrame, columns)

    elif(isinstance(columns, list) == True):
        col_select = column_checker(DataFrame, columns)

    else:
        col_select = list()


    return col_select
        

# end


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

