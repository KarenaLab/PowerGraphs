
def plot_missingdata_row(DataFrame, title, pct_lines=True, savefig=False, verbose=True):
    """
    Plots the missing data of a **DataFrame** by rows.

    Variables:
    * DataFrame = DataFrame as Pandas,
    * title = Title for the plot (default="Missing Data"),
    * pct_lines = True or False. If True, will plot a orange line in 25%
      and a red line for 50% of NaNs. (default=True),
    * savefig = True or False. If True will save a report with the title
      name and do not show the plot. If False will not save the report
      but will show the plot in the screen (default=False),
    * verbose = True or False (quiet mode). If True will print some infor-
      mation about the data analysis and plot (default=True).    

    """

    # Versions ----------------------------------------------------------

    # 01 - Oct 17th, 2021 - Starter*
    # 02 - Oct 17th, 2021 - Adding Secondary Y Axis
    # 03 - Oct 18th, 2021 - Adding a Middle Line (50% of Columns)
    # 04 - Jan 21st, 2023 - Adjusting
    # 05 -   


    # Libraries ---------------------------------------------------------

    import numpy as np
    import pandas as pd

    import matplotlib.pyplot as plt


    # Program -----------------------------------------------------------

    data = DataFrame.copy()

    nrows = data.shape[0]
    ncols = data.shape[1]
    
    counting_dict = {}

    # Create a dictionary with index as the number of columns available
    for col in range(0, ncols+1):
        counting_dict[col] = 0

    # Counting number of NaNs in each row
    for row in range(0, nrows):
        count = data.iloc[row, :].isna().sum()
        counting_dict[count] = counting_dict[count] + 1

    # Removing rows with 0 (zero) NaNs in the counting
    counting_dict.pop(0)


    # Splitting data
    index = list(counting_dict.keys())
    values_abs = list(counting_dict.values())   
    values_pct = [np.round((x / nrows) * 100, decimals=3) for x in values_abs]
     

    # Plot
    # Adjusts
    if(title == None):
        title = "Missing Data by rows"

    bin_width = 0.8
    bin_color = "darkred"
    bin_edge = "black"

    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["figure.dpi"] = 180
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"


    # Plot
    fig, ax1 = plt.subplots(figsize=[8, 4.5])
    fig.suptitle(title, fontsize=10, fontweight="bold")

    # ax1 = Primary plot = Frequency
    ax1.bar(index, values_abs, width=bin_width, bottom=0,
            color=bin_color, edgecolor=bin_edge, zorder=10)

    # ax2 = Secondary plot = Percentage
    ax2 = ax1.twinx()
    ax2.bar(index, values_pct, width=bin_width, bottom=0,
            color= bin_color, edgecolor=bin_edge, zorder=11)

    # Percentage lines
    if(pct_lines == True):
        line_25 = int((ncols * 0.25) + 0.5)
        ax1.axvline(x=line_25, color="orange", linestyle="-", linewidth=0.8, zorder=2)

        line_50 =  int((ncols * 0.50) + 0.5)
        ax1.axvline(x=line_50, color="red", linestyle="-", linewidth=0.8, zorder=3)


    ax1.grid(axis="y", color="lightgrey", linestyle="--", linewidth=0.5, zorder=1)


    ax1.set_xlabel("Number of rows", loc="right")
    ax1.set_xticks(index)

    ax1.set_ylabel("NaN frequency (qty)", loc="top")
    ax2.set_ylabel("NaN percentage (%)", loc="top")

    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)
        print(f' > saved plot as "{title}.png"')

    else:
        plt.show()

    plt.close(fig)

    return None

    # end ---------------------------------------------------------------


