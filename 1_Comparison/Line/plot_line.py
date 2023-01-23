
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


def plot_line(DataFrame, title=None, xlabel=None, ylabel=None, index=None,
              columns="all", legend_loc="best", grid_axis="both",
              marker=False, savefig=False, verbose=True):

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
    * legend_loc = "best"*, "upper left", "upper right", "lower left" or "lower right",
    * grid_axis = "both"*, "x" or "y",
    * marker = True* or False
    * savefig = True or False*
    * verbose = True* or False

    """

    data = DataFrame.copy()

    # Data Preparation
    # Title
    if(title == None):
        title = "Line plot"


    # Axis labels (xlabel and ylabel)
    if(xlabel == None):
        xlabel = ""

    if(ylabel == None):
        ylabel = ""
        

    # Index
    if(index == None):
        _index = np.array(data.index)

    else:
        _index = np.array(data[index])
        data = data.drop(columns=[index])
        

    # Columns
    if(columns != "all"):
        if(isinstance(columns, str) == True):
            columns = columns.split()
            
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

    _zorder=2   
    for y, color in list(zip(columns, colors[0:nlines])):
        plt.plot(_index, data[y], color=color, label=y, zorder=_zorder)

        if(marker == True):
            plt.scatter(_index, data[y], color=color, edgecolor="white", zorder=_zorder+1)

        _zorder = _zorder + 1

    plt.grid(axis=grid_axis, color="lightgrey", linestyle="--", linewidth=0.5, zorder=1)   
    plt.ylabel(ylabel, loc="top")
    plt.xlabel(xlabel, loc="right")

    if(len(columns) > 1):
        plt.legend(loc=legend_loc, framealpha=1)    

    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)
        print(f" > plotting {title}")

    else:
        plt.show()

    plt.close(fig)

    
    return None
