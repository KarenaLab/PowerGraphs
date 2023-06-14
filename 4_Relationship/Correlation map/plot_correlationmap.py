
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def plot_correlationmap(DataFrame, title=None, columns="all", color="darkblue",
                        high_threshold=10, low_threshold=10,
                        decimals=2, method="pearson",
                        savefig=False, verbose=True):
    """
    Plots a horizontal bars for **Heatmap** for **correlations** between
    variables (using Pearson*, Spearman or Kendall methods).

    Variables:
    * DataFrame = Data to be plot,
    * title = Title for the plot (and the name for the file if savefig=True),
    * columns = "all" or a selected list of columns name,
    * color = Color for the horizontal bars (default="darkblue")
    * high_threshold = Number of most high correlations to be shown at first
         graph (default=10)
    * low_threshold = Number of most low correlations to be shown at second
         graph (default=10)
    * decimals = Number of decimals to display (default=2),
    * method = Method for correlation: Pearson*, spearman or kendall,
      https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
    * savefig = True or False for saving the plot as a figure using title as name,
    * verbose = True* or False for messages.    

    """

    # Versions ----------------------------------------------------------
    # 01 - Jan 28th, 2023 - Starter
    # 02 - 


    # Insights:
    # 


    # Setup/Config
    space = 0.02

    # Program ----------------------------------------------------------
    data = DataFrame.copy()

    # Data Preparation
    # Title
    if(title == None):
        title = "Correlation map"

    title = f"{title} ({method})"

    # Columns
    if(columns != "all"):
        if(isinstance(columns, str) == True):
            columns = columns.split(",")

        data = data[columns]

    else:
        columns = data.columns.tolist()


    # Data Processing
    no_rows = len(columns)
    corr = data.corr(method=method).values
    corr = np.abs(np.round(corr, decimals=decimals))   
  
    # Removing Duplicated Data (Right Triangle Figure)
    for i in range(0, no_rows):
        for j in range(0, no_rows):
            if(i < j):
                corr[i, j] = 0

    # Creating a list with Correlation
    corr_map = pd.DataFrame(data=[], columns=["var_01", "var_02", "tag", "corr"])

    for i in range(0, no_rows):
        for j in range(0, no_rows):
            if(i > j):
                new_row = pd.Series({"var_01": columns[i],
                                     "var_02": columns[j],
                                     "tag": f"{columns[i]} vs {columns[j]}",
                                     "corr": corr[i, j]})

                corr_map = pd.concat([corr_map, new_row.to_frame().T], ignore_index=True)

    corr_map = corr_map.sort_values(by="corr", ascending=True, ignore_index=True)

    corr_high = corr_map.tail(high_threshold)
    corr_low = corr_map.head(low_threshold)

    # Plot
    fig = plt.figure(figsize=[8, 4.5])      # Using widescreen ratio (16:9)
    grid = fig.add_gridspec(nrows=2, height_ratios=[high_threshold, low_threshold],
                            ncols=2, width_ratios=[2, 8])

    ax0 = fig.add_subplot(grid[0, 1])
    ax1 = fig.add_subplot(grid[1, 1])
    # Using left column (first) as a space for long labels ;)
    # Do not use plt.tight_layout(), will remove this restriction.
    
    fig.suptitle(title, fontsize=10, fontweight="bold")

    ax0.barh(corr_high["tag"], corr_high["corr"], color=color, edgecolor="black", zorder=10)
    ax0.set_xlim(left=0, right=1)
    ax0.grid(axis="x", color="lightgrey", linestyle="--", linewidth=0.5, zorder=1)
    ax0.axvline(x=0.1, color="red", linestyle="--", linewidth=0.5, zorder=2)
    ax0.axvline(x=0.9, color="red", linestyle="--", linewidth=0.5, zorder=3)

    for x, y in list(zip(corr_high["corr"], corr_high["tag"])):
        ax0.text((space + x), y, str(x), fontsize=9, ha="left", va="center")
    
    ax1.barh(corr_low["tag"], corr_low["corr"], color=color, edgecolor="black", zorder=10)    
    ax1.set_xlim(left=0, right=1)
    ax1.grid(axis="x", color="lightgrey", linestyle="--", linewidth=0.5, zorder=1)
    ax1.axvline(x=0.1, color="red", linestyle="--", linewidth=0.5, zorder=2)
    ax1.axvline(x=0.9, color="red", linestyle="--", linewidth=0.5, zorder=3)

    for x, y in list(zip(corr_low["corr"], corr_low["tag"])):
        ax1.text((space + x), y, str(x), fontsize=9, ha="left", va="center")


    # Printing
    if(savefig == True):
        plt.savefig(title, dpi=240)

        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()

    plt.close(fig)
    
    return None

# end
