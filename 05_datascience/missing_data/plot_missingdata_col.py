# Missing Data per Column [P147] ---------------------------------------

# Libraries
import numpy as np
import pandas as pd

from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

import matplotlib.pyplot as plt


# Versions 
# 01 - Dec 27th, 2020 - Starter
# 02 - Feb 08th, 2021 - Adjusting printing area for A4 format
# 03 - Apr 21st, 2021 - Adding **kwargs
# 04 - Apr 22rd, 2021 - Changing Data acquisition (Pandas Based)
# 05 - May 30th, 2021 - Adding is_numeric and is_string selection
#                       Adding Secondary Y Axis (Percentage of)
# 06 - May 31st, 2021 - Adding color option
# 07 - Oct 14th, 2021 - Adding edgecolor = black
# 08 - Oct 17th, 2021 - *** Changing Name = MissingDataCol ***
# 09 - Jan 21st, 2023 - Adjusting
#    - Dec 18th, 2024 - Solve bugfix with grid selection
# 


# Insights, improvements and bugfix
#


def plot_missingdata_col(DataFrame, title=None, del_threshold=100,
                         pct_lines=True, grid="y",
                         savefig=False, verbose=True):
    """
    Plots the missing data of a **DataFrame** by columns.

    Variables:
    * DataFrame = DataFrame as Pandas,
    * title = Title for the plot (default="Missing Data"),
    * del_threshold = Threshold (in percentage) for removing column
      (default=100),
    * pct_lines = True or False. If True, will plot a orange line in 5%
      and a red line for 10% of NaNs. (default=True),
    * savefig = True or False. If True will save a report with the title
      name and do not show the plot. If False will not save the report
      but will show the plot in the screen (default=False),
    * verbose = True or False (quiet mode). If True will print some infor-
      mation about the data analysis and plot (default=True).    

    """
    # Data preparation
    data = DataFrame.copy()

    nrows = data.shape[0]
    ncols = data.shape[1]
    columns = data.columns.tolist()
    
    nan_count_list = list()
    nan_pct_list = list()

    # Data Analysis (Missing Data)
    for col in columns:
        nan_count = data[col].isna().sum()
        nan_count_list.append(nan_count)

        nan_pct = np.round((nan_count / nrows) * 100, decimals=3)
        nan_pct_list.append(nan_pct)

        if(nan_count > 0 and verbose == True):
            print(f' > column "{col}" has {nan_count} NaNs ({(nan_count/nrows)*100:.2f}%)')

        if(nan_pct >= del_threshold and verbose == True):
            data = data.drop(columns=[col])
            print(f' >>> Warning: Column deleted. Delete threshold={del_threshold}% \n')

   
    # Plot
    # Adjusts
    if(title == None):
        title = "Missing Data by columns"

    # Grid Axis
    grid_default = "y"
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
    plt.rcParams["xtick.major.size"] = 0
    plt.rcParams["ytick.major.size"] = 3.5

    bin_width = 0.8
    bin_color = "darkred"
    bin_edge = "black"

    
    # Figure
    fig, ax1 = plt.subplots(figsize=[6, 3.375])
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    # ax1 = Primary plot = Frequency
    ax1.bar(columns, nan_count_list, width=bin_width, bottom=0,
            color=bin_color, edgecolor=bin_edge, zorder=10)

    #ax2 = Secondary plot = Percentage
    ax2 = ax1.twinx()
    ax2.bar(columns, nan_pct_list, width=bin_width, bottom=0,
            color=bin_color, edgecolor=bin_edge, zorder=11)

    # Percentage lines
    pct_5 = [i for i in nan_pct_list if i >= 5]                 
    if(pct_lines == True and len(pct_5) > 0):
        ax2.axhline(y=5, color="orange", linestyle="--", linewidth=0.8, zorder=2)

    pct_10 = [i for i in nan_pct_list if i >= 10]
    if(pct_lines == True and len(pct_10) > 0):
        ax2.axhline(y=10, color="red", linestyle="--", linewidth=0.8, zorder=3)
        

    ax1.grid(axis=grid, color="lightgrey", linestyle="--", linewidth=0.5, zorder=1)
    
    ax1.set_ylabel("NaN frequency (qty)", loc="top")
    ax2.set_ylabel("NaN percentage (%)", loc="top")

    plt.setp(ax1.get_xticklabels(), fontsize=8, rotation=90)
    ax1.xaxis.set_tick_params(width=0)
    ax2.xaxis.set_tick_params(width=0)

    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=320)
        print(f' > saved plot as "{title}.png"')

    else:
        plt.show()


    plt.close(fig)

    return None

