# Heatmap [P262] -------------------------------------------------------

# Libraries
import numpy as np
import pandas as pd

from pandas.api.types import is_numeric_dtype

import matplotlib.pyplot as plt


# Versions 
# 01 - Jan 31st, 2021 - Starter
# 02 - Jan 31st, 2021 - Removing Duplicated Info
# 03 - Feb 03rd, 2021 - Adjusting size for printing (A4 Ratio)
# 04 - Feb 16th, 2021 - Adding **kwargs
# 05 - Apr 21th, 2021 - Simplifying Data entry for just Data, removing
#                       Columns (Labels) info
# 06 - Sep 01st, 2021 - Adjusting (small corrections)
# 07 - Apr 21st, 2022 - Adding Spearman and adjusting kwargs
#                       Added correlation method to the title/filename
# 08 - Jan 26th, 2023 - Adjusting new strategies
# 09 - Jul 20th, 2023 - New standards and setup
# 10 - 

# Insights, improvements and bugfix
# Add rotation to x_axis labels (need to check anchor),
#


def plot_heatmap(DataFrame, title=None, columns="all", decimals=2,
                 method="pearson", colormap="Blues", savefig=False,
                 textsize=7, verbose=True):
    """
    Plots a triangular **Heatmap** for **correlations** between variables,
    using Pearson, Spearman or Kendall methods.

    Variables:
    * DataFrame = Data to be plot,
    * title = Title for the plot (and the name for the file if savefig=True),
    * columns = "all" or a selected list of columns name,
    * decimals = Number of decimals to display (default=2),
    * method = Method for correlation: Pearson*, spearman or kendall,
      https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
    * colormap = Blues*, Greys, Reds or Oranges (suggestion in reason of text match), 
    * savefig = True or False for saving the plot as a figure using title as name,
    * verbose = True* or False for messages.    

    """
    # Data Preparation
    data = DataFrame.copy()

    # Title
    if(title == None):
        title = f"Heatmap for correlation ({method})"

    else:
        title = f"{title} ({method})"

    # Columns select    
    if(columns != "all"):
        if(isinstance(columns, str) == True):
            columns = columns.split(",")

        data = data[columns]

    else:
        columns = data.columns.tolist()


    # Remove string columns
    cols_remove = []
    for col in columns:
        if(is_numeric_dtype(data[col]) == False):
            cols_remove.append(col)

    data = data.drop(columns=cols_remove)
    

    # Data Processing
    no_rows = len(columns)
    corr = data.corr(method=method).values
    corr = np.abs(np.round(corr, decimals=decimals))   
  
    # Removing Duplicated Data (Right Triangle Figure)
    for i in range(0, no_rows):
        for j in range(0, no_rows):
            if(i < j):
                corr[i, j] = 0


    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["figure.dpi"] = 180
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.major.size"] = 0
    plt.rcParams["ytick.major.size"] = 0
   
    # Plot
    fig = plt.figure(figsize=[6, 3.375])
    ax = fig.add_subplot()
    im = ax.imshow(corr, cmap=colormap, aspect=(3.375 / 6))

    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    ax.set_yticks(np.arange(start=0, stop=no_rows))
    ax.set_yticklabels(columns, rotation=0, fontsize=9)
    ax.set_xticks(np.arange(start=0, stop=no_rows))
    ax.set_xticklabels(columns, rotation=90, fontsize=9)


    # Text Annotations
    for i in range(0, len(columns)):
        for j in range(0, len(columns)):
            if(i >= j):
                value = corr[i, j]
                
                if(value >= 0.6): textcolor = "white"
                else: textcolor = "black"

                text = ax.text(j, i, value, ha="center", va="center",
                               color=textcolor, fontsize=textsize)


    plt.tight_layout()

    # Printing
    if(savefig == True):
        plt.savefig(title, dpi=320)

        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()


    plt.close(fig)

    return None

