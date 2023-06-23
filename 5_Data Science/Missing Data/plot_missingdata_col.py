
def plot_missingdata_col(DataFrame, title=None, del_threshold=100,
                         pct_lines=True, savefig=False, verbose=True):
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

    # Versions ----------------------------------------------------------
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
    # 10 -


    # Libraries ---------------------------------------------------------

    import numpy as np
    import pandas as pd

    from pandas.api.types import is_string_dtype
    from pandas.api.types import is_numeric_dtype
    
    import matplotlib.pyplot as plt   


    # Program -----------------------------------------------------------
    data = DataFrame.copy()

    nrows = data.shape[0]
    ncols = data.shape[1]
    columns = data.columns.tolist()
    
    nan_count_list = []
    nan_pct_list = []

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


    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["figure.dpi"] = 180
    plt.rcParams["ps.papersize"] = "A4"      

    
    # Plot
    # Adjusts
    if(title == None):
        title = "Missing Data by columns"

    bin_width = 0.8
    bin_color = "darkred"
    bin_edge = "black"

    # Figure
    fig, ax1 = plt.subplots(figsize=[8, 4.5])
    fig.suptitle(title, fontsize=10, fontweight="bold")

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
        

    ax1.grid(axis="y", color="lightgrey", linestyle="--", linewidth=0.5, zorder=1)
    
    ax1.set_ylabel("NaN frequency (qty)", loc="top")
    ax2.set_ylabel("NaN percentage (%)", loc="top")

    plt.setp(ax1.get_xticklabels(), fontsize=8, rotation=90)
    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)
        print(f' > saved plot as "{title}.png"')

    else:
        plt.show()

    plt.close(fig)

    return None

    # end ---------------------------------------------------------------

