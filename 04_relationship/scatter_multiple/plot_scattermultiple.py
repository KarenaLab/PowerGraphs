# Scatter plot - Simple [P286] ------------------------------------------

# Insights, improvements and bugfix
# 01 - Automatic selector for the x higher groups
# 


# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------
def plot_scattermultiple(DataFrame, x, y, target, title=None, xlabel=None,
                         ylabel=None, alpha=0.8, mark_size=20, legend_loc="best",
                         savefig=False, verbose=True):
    """

    More info:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

    """
    # Data preparation
    data = DataFrame.copy()

    columns = [x, y, target]
    columns = col_select(data, columns)
    groups = data[target].unique()      # Improvement #01

    # Title
    if(title == None):
        title = "Scatter multiple"

    # Colors
    colors = ["navy", "darkred", "orange", "darkgreen", "darkviolet"]
    colors = colors[0: len(groups)]

    # RC Params
    set_rcparams()
    
    
    # Plot
    fig = plt.figure(figsize=[6, 3.375])    # Widescreen 16:9
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    for g, c in zip(groups, colors):
        data_group = data.groupby(by=target).get_group(g)

        data_x = np.array(data_group[x])
        data_y = np.array(data_group[y])
        
        plt.scatter(data_x, data_y, s=mark_size, color=c, edgecolor="white", alpha=alpha, label=g, zorder=20)


    if(xlabel != None):
        plt.xlabel(xlabel, loc="center")

    if(ylabel != None):
        plt.ylabel(ylabel, loc="center")

    if(len(groups) > 1):
        plt.legend(loc=legend_loc, framealpha=1).set_zorder(99)
        

    plt.grid(axis="both", color="grey", linestyle="--", linewidth=0.5, zorder=5)       


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
    if(columns == "all"):
        # Default: takes **all** columns from DataFrame.
        col_select = DataFrame.columns.to_list()

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

