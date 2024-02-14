# Histogram Simple [P290]

# Versions
# 01 - Jan 31st, 2023 - Starter
# 02 - Feb 14th, 2023 - Using python_modules source,
#                       Add linebehind option,
# 03 - Jun 07th, 2023 - Remove binning function and using a numpy func,
#    - Jan 03rd, 2024 - Set legend over all items,
#    - Jan 04th, 2024 - Set smaller window size (for 13")
#    - Jan 06th, 2024 - Add tail_size control
#  


# Insights, improvements and bugfix
# Extend kde line up to zero (left and right margins),
#


# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from scipy.stats import gaussian_kde


# ----------------------------------------------------------------------

def plot_histogram(data, title=None, xlabel=None, bins="sqrt",
                   kde=True, meanline=True, medianline=True, grid_axes="y",
                   linebehind=True, tail_size=15,
                   savefig=False, verbose=True):
    """
    Plots the histogram of a given *DataFrame* with selected *columns*.

    Variables:
    * data: Pandas data with data.
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
    # Data preparation
    data = np.array(data)
    data = data[~(np.isnan(data))]
    
    # Title
    if(title == None):
        title = "Histogram"

    
    # Colors
    colors = {"blue": "navy",
              "red": "darkred",
              "orange": "orange",
              "green": "darkgreen"}

    # Bins
    # more info: https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html
    bins_list = ["fd", "doane", "scott", "stone", "rice", "sturges", "sqrt"]

    if(isinstance(bins, int) == True):
        no_bins = bins

    elif(bins_list.count(bins) == 1):
        no_bins = np.histogram_bin_edges(data, bins=bins).size

    else:
        print(f' >>> Error: "bins" option not valid. Using "sqrt" as forced option')
        no_bins = np.histogram_bin_edges(data, bins="sqrt").size


    # Grid Axis
    grid_list = ["x", "y", "both"]
    if(grid_list.count(grid_axes) == 0):
        print(f' >>> Error: "grid_axis" oprtion not valid. Using "y" as forced option.')
        grid_axes = "y"

    
    # Histogram settings 
    # KDE: Kernel-density estimate for gaussian distribution
    if(kde == True):
        bins_alpha = 0.7
        bins_edge = colors["blue"]
        density = True
        ylabel = "density"

        # Add tail for the density line
        x_min = data.min()
        x_max = data.max()
        step = (x_max - x_min) * (tail_size / 100)
        
        kde_space = np.linspace(start=(x_min - step), stop=(x_max + step), num=(50 * no_bins))
        kde_line = gaussian_kde(data, weights=None)(kde_space)

    else:
        bins_alpha = 1
        bins_edge = "dimgrey"
        density = False
        ylabel = "frequency"


    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"
    plt.rcParams["xtick.major.size"] = 3.5
    plt.rcParams["ytick.major.size"] = 3.5

    # Plot
    fig = plt.figure(figsize=[6, 3.375])        # Widescreen [16:9]
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    plt.hist(data, bins=no_bins, density=density, color=colors["blue"],
             alpha=bins_alpha, edgecolor=bins_edge, zorder=20)

    plt.grid(axis=grid_axes, color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    # Density line
    if(kde == True):
        plt.plot(kde_space, kde_line, color=colors["red"], linewidth=1.5, label="kde", zorder=23)


    if(linebehind == True): zorder = 11
    else: zorder = 21
    

    if(meanline == True):
        plt.axvline(x=np.mean(data), color=colors["green"], linewidth=1.0, label="mean", zorder=zorder)

    if(medianline == True):
        plt.axvline(x=np.median(data), color=colors["orange"], linewidth=1.0, label="median", zorder=zorder)

    if(xlabel != None):
        plt.xlabel(xlabel, loc="right")

    plt.ylabel(ylabel, loc="top")

    if(kde == True or meanline == True or medianline == True):
        plt.legend(fontsize=9, loc="upper right", framealpha=1).set_zorder(99)


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
    
