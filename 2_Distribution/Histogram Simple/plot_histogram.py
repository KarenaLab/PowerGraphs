
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from scipy.stats import gaussian_kde


def binning(size, method="square", **kwargs):
    """
    Calculates the optimal (or best) binning size for histogram.
    Methods available: sqrt*, rice, sturges and freedman-diaconis. 

    """
    method = method.lower()

    if(method == "square" or method == "sqrt"):
        # Equation = sqrt(size)
        bins = int(np.sqrt(size) + 0.5)       
        if(size >= 500):          
            # if size > 500, bins are always odd.
            if(bins % 2 == 0):
                bins = bins+1

    if(method == "rice" or method == "ricerule"):
        # Equation = 2* root(size, 3)
        bins = int((2 * np.cbrt(size)) + 0.5)
       
    if(method == "sturges" or method == "sturge"):
        # https://www.statology.org/sturges-rule/
        # Equation = log(n,2) + 1
        bins = int((np.log2(size)+1) + 0.5)

    if(method == "freedman" or method == "freedman-diaconis" or
        method == "freedmandiaconis" or method == "freedman_diaconis"):
        # https://en.wikipedia.org/wiki/Freedman-Diaconis_rule
        #
        #                     IQR(x)
        # Equation = 2 * --------------- 
        #                 root(size, 3)

        IQR = kwargs.get("IQR")
        if(IQR == None):
            print(" >> Warning: Missing IQR Value")
            bins = None

        else:
            bins = int((2*(IQR/np.cbrt(size) + 0.5)))          


    return bins


def plot_histogram(Series, title=None, xlabel=None, bins="sqrt", kde=True, density=False,
                   meanline=True, medianline=True, iqr=None, grid_axis="y",
                   savefig=False, verbose=True):
    """
    Plots the histogram of a given **DataFrame** with selected **columns**.

    Variables:
    * DataFrame: DataFrame as Pandas,
    * title: Title for the plot (default="Histogram - {column name}"),
    * xlabel:
    * bins:
    * kde:
    * density:
    * meanline:
    * medianline:
    * iqr:
    * grid_axis:
    * savefig: True or False. If True will save a report with the title
               name and do not show the plot. If False will not save the
               report but will show the plot in the screen (default=False),
    * verbose: True or False (quiet mode). If True will print some infor-
               mation about the data analysis and plot (default=True).
     
    """

    # Versions ----------------------------------------------------------
    # 01 - Jan 31st, 2023 - starter
    # 02 -

    # Program -----------------------------------------------------------
    data = Series.copy()
    data = data.dropna()

    # Data preparation
    # Title
    if(title == None):
        title = f"Histogram - {data.name.replace('_', ' ')}"

    if(xlabel == None):
        xlabel = ""

    # Colors
    colors = {"blue": "darkblue",
              "red": "darkred",
              "orange": "orange",
              "green": "darkgreen"}

    # Bins
    if(isinstance(bins, str) == True):
        no_bins = binning(data.shape[0], method=bins)

    else:
        no_bins = bins

    bins_alpha = 1
    bins_edge = "darkgrey"

    # KDE: Kernel-density estimate for gaussian distribution
    if(kde == True):
        density = True
        bins_alpha = 0.7
        bins_edge = colors["blue"]

        kde_space = np.linspace(start=data.min(), stop=data.max(), num=(5*no_bins))
        kde_line = gaussian_kde(data, weights=None)(kde_space)


    # Plot
    fig = plt.figure(figsize=[8, 4.5])
    fig.suptitle(title, fontsize=10, fontweight="bold")

    plt.hist(data, bins=no_bins, density=density, color=colors["blue"],
             alpha=bins_alpha, edgecolor=bins_edge, zorder=20)

    if(kde == True):
        plt.plot(kde_space, kde_line, color=colors["red"], linewidth=1.5, label="kde", zorder=23)

    if(meanline == True):
        plt.axvline(x=data.mean(), color=colors["green"], linewidth=1.0, label="mean", zorder=21)

    if(medianline == True):
        plt.axvline(x=data.median(), color=colors["orange"], linewidth=1.0, label="median", zorder=22)


    plt.grid(axis=grid_axis, color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)
    plt.xlabel(xlabel, loc="right")
    plt.ylabel("frequency", loc="top")

    if(kde == True or meanline == True or medianline == True):
        plt.legend(fontsize=9, loc="upper right", framealpha=1)

    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)
        if(verbose == True):
            print(f" > saving file: {title}.png")

    else:
        plt.show()

    plt.close(fig)

    return None
        
