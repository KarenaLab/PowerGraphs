# Histogram Duo [P328]

# Versions
# 01 - May 01st, 2023 - Starter
#    - Jan 03rd, 2024 - Set legend over all items


# Libraries
import numpy as np
import pandas as pd

from scipy.stats import gaussian_kde

import matplotlib.pyplot as plt


# ----------------------------------------------------------------------

def plot_histogramduo(serie1, serie2, name1=None, name2=None,
                      serie3=None, name3=None, title=None, bins="sqrt",
                      bins_alpha=0.3, savefig=False, verbose=True):
    """
    Plots two or three histograms from different series together.

    Variables:
    * serie1 = Data from serie 1 (obligatory),
    * name1 = Title or name from serie 1 (obligatory),
    * serie2 = Data from serie 2 (obligatory),
    * name2 = Title or name from serie 2 (obligatory),
    * serie3 = Data from serie 3 (optional),
    * name3 = Title or name from serie 3 (optional),
    * title = Title for the plot. If savefig=True, will be the name of the file,
    * bins_alpha = transparency applied to the bins (default=0.3),
    * savefig = True or False*. False will only diplay the plot, True will store
                the file at current folder with 'title' name,
    * verbose = True* or False. Displays important messages at prompt.

    Sources:
    Binning: https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html
    KDE Line: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html

    """
    # Data preparation
    series_list = [serie1, serie2]
    names_list = [name1, name2]
    colors_list = ["darkblue", "darkred"]

    if(name3 != None):
        series_list.append(serie3)
        names_list.append(name3)
        colors_list.append("orange")


    if(title == None):
        title = "Histogram Duo"

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
    fig = plt.figure(figsize=[6, 3.375])
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    zorder = 20
    for serie, name, color in list(zip(series_list, names_list, colors_list)):
        data = serie.copy().dropna()

        # KDE = Kernal Density Gaussian Estimation
        # Bins
        # more info: https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html
        bins_list = ["fd", "doane", "scott", "stone", "rice", "sturges", "sqrt"]

        if(isinstance(bins, int) == True):
            no_bins = bins

        elif(bins_list.count(bins) == 1):
            no_bins = np.histogram_bin_edges(data, bins=bins).size

        elif(bins == "min"):
            no_bins = np.min([np.histogram_bin_edges(data, bins=x).size for x in bins_list])

        elif(bins == "max"):
            no_bins = np.max([np.histogram_bin_edges(data, bins=x).size for x in bins_list])

        elif(bins == "median"):
            no_bins = int(np.median([np.histogram_bin_edges(diff, bins=x).size for x in bins_list]))

        else:
            print(f' >>> Error: "bins" option not valid. Using "sqrt" as forced option')
            bins = "sqrt"
            no_bins = np.histogram_bin_edges(data, bins=bins).size

        
        data_min = data.min()
        data_max = data.max()
        step = (data_max - data_min) * 0.25

        kde_space = np.linspace(start=(data_min - step), stop=(data_max + step), num=(10 * no_bins))
        kde_line = gaussian_kde(data, weights=None)(kde_space)

        # Bars and KDE Line
        plt.hist(data, bins=no_bins, density=True, color=color, alpha=bins_alpha, edgecolor=color, label=name, zorder=zorder)
        plt.plot(kde_space, kde_line, color=color, linewidth=2, zorder=zorder+6)

        zorder = zorder + 1


    plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)
    plt.ylabel("density", loc="top")

    plt.legend(loc="upper right", framealpha=1).set_zorder(99)

    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=320)

        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()


    plt.close(fig)

    return None


# end
