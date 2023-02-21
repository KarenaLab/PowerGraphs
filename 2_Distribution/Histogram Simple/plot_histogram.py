
# Libraries
import sys
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from scipy.stats import gaussian_kde


# Personal modules
sys.path.append(r"C:\python_modules")
from binning import *


def plot_histogram(Series, title=None, xlabel=None, bins="sqrt", kde=True,
                   meanline=True, medianline=True, grid_axis="y", linebehind=True,
                   savefig=False, verbose=True):
    """
    Plots the histogram of a given *DataFrame* with selected *columns*.

    Variables:
    * Series: Pandas series with data.
    * title: Title for the plot (default="Histogram - {column name}"),
    * xlabel: Label for x_axis (default=None).
    * bins: Number of bins for plot (default="sqrt"). Check *binning*
            module for more details.
    * kde: Plot the Kernel-Gaussian density estimation line,
    * meanline: Plot a green line showing the mean,
    * medianline: Plot an orange line showing the median,
    * grid_axis: Plot axis (dafault=y)
    * linebehind = Plots mean and median line behind the plot.
    * savefig: True or False*. If True will save a report with the title
               name and do not show the plot. If False will not save the
               report but will show in the screen.(default=False),
    * verbose: True* or False (quiet mode). If True will print some in-
               formation about the data analysis and plot (default=True)
     
    """
    # Versions ----------------------------------------------------------
    # 01 - Jan 31st, 2023 - starter
    # 02 - Feb 14th, 2023 - using python_modules source
    #                       added linebehind option

    # Insights ----------------------------------------------------------
    # Extend kde line up to zero (left and right margins),
    #

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
    colors = {"blue": "navy",
              "red": "darkred",
              "orange": "orange",
              "green": "darkgreen"}

    # Bins
    if(isinstance(bins, str) == True):
        if(bins == "freedman" or bins == "freedman-diaconis"):
            data_q1 = data.quantile(q=0.25)
            data_q3 = data.quantile(q=0.75)
            iqr = data_q3 - data_q1

        else:
            iqr = None

        no_bins = binning(data.shape[0], method=bins, iqr=iqr)

    elif(isinstance(bins, int) == True):
        no_bins = bins

    else:
        no_bins = None
        print(f" > Error: bins is not valid")


    # Histogram settings 
    bins_alpha = 1
    bins_edge = "dimgrey"
    density = False
    ylabel = "frequency"

    # KDE: Kernel-density estimate for gaussian distribution
    if(kde == True):
        bins_alpha = 0.7
        bins_edge = colors["blue"]
        density = True
        ylabel = "density"

        kde_space = np.linspace(start=data.min(), stop=data.max(), num=(5*no_bins))
        kde_line = gaussian_kde(data, weights=None)(kde_space)


    # Plot
    fig = plt.figure(figsize=[8, 4.5])
    fig.suptitle(title, fontsize=10, fontweight="bold")

    plt.hist(data, bins=no_bins, density=density, color=colors["blue"],
             alpha=bins_alpha, edgecolor=bins_edge, zorder=20)

    if(kde == True):
        plt.plot(kde_space, kde_line, color=colors["red"], linewidth=1.5, label="kde", zorder=23)

    if(linebehind == True):
        zorder = 11

    else:
        zorder = 21
    

    if(meanline == True):
        plt.axvline(x=data.mean(), color=colors["green"], linewidth=1.0, label="mean", zorder=zorder)

    if(medianline == True):
        plt.axvline(x=data.median(), color=colors["orange"], linewidth=1.0, label="median", zorder=zorder)


    plt.grid(axis=grid_axis, color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)
    plt.xlabel(xlabel, loc="right")
    plt.ylabel(ylabel, loc="top")

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
        
