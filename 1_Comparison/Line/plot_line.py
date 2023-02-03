
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


def plot_line(DataFrame, title=None, xlabel=None, ylabel=None, index=None,
              columns="all", legend=True, legend_loc="best", grid_axis="both",
              marker=False, remove_axis=False, savefig=False, verbose=True):

    """
    Plots a graph with lines.

    Variables:
    * DataFrame = Data to be plot,
    * title = Title for the plot (and the name for the file if savefig=True),
    * xlabel = label for x axis,
    * ylabel = label for y axis,
    * index = None or the name of the column to be the index. If None will
      be used the index of DataFrame,
    * columns = "all" or a list of items to be plot,
    * legend = True* or False,
    * legend_loc = "best"*, "upper left", "upper right", "lower left" or "lower right",
    * grid_axis = "both"*, "x" or "y",
    * marker = True* or False for a marker in data points,
    * savefig = True or False for saving the plot as a figure using title as name,
    * verbose = True* or False for messages.

    """

    # Versions ---------------------------------------------------------
    # 01 - Jan 21st, 2023 - Starter
    # 02 -

    # Insights:
    #

    # Program ----------------------------------------------------------
    data = DataFrame.copy()

    # Data Preparation
    # Title
    if(title == None):
        title = "Line plot"
        
    # Index
    if(index == None):
        _index = np.array(data.index)

    else:
        _index = np.array(data[index])
        data = data.drop(columns=[index])
        
    # Columns
    if(columns != "all"):
        if(isinstance(columns, str) == True):
            columns = columns.split(",")
            
        data = data[columns]

    else:
        columns = data.columns.tolist()


    # Colors
    colors = ["navy", "darkred", "darkgreen", "orange",
              "cornflowerblue", "indianred", "yellowgreen", "bisque"]
           
    nlines = data.shape[1]
    
    # Plot
    fig = plt.figure(figsize=[8, 4.5])
    fig.suptitle(title, fontsize=10, fontweight="bold")

    ax = plt.axes()   
    _zorder=2   
    for y, color in list(zip(columns, colors[0:nlines])):
        plt.plot(_index, data[y], color=color, label=y, zorder=_zorder)

        if(marker == True):
            plt.scatter(_index, data[y], color=color, edgecolor="white", zorder=_zorder+1)

        _zorder = _zorder + 1

    plt.grid(axis=grid_axis, color="lightgrey", linestyle="--", linewidth=0.5, zorder=1)   

    if(remove_axis == True):
        plt.tick_params(length=0,labelleft="on", labelbottom="on")
        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)
        ax.spines.left.set_visible(False)
        
    if(ylabel != None):
        plt.ylabel(ylabel, loc="top")

    if(xlabel != None):
        plt.xlabel(xlabel, loc="right")

    if(len(columns) > 1 and legend == True):
        plt.legend(loc=legend_loc, framealpha=1)    


    # Printing
    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)
        if(verbose == True):
            print(f" > saving figure: {title}.png")

    else:
        plt.show()

    plt.close(fig)   
    return None

