# [P272] QQ Plot -------------------------------------------------------

# Insights, improvements and bugfix
#


# Libraries
import numpy as np
import pandas as pd
import scipy.stats as st

import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
def plot_qqplot(data, title=None, xlabel=None, ylabel=None,
                savefig=False, verbose=True):
    """
    The formula used for the theoretical quantiles (horizontal axis
    of the probability plot) is Filliben’s estimate

    More info:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.probplot.html
    https://www1.cmc.edu/pages/faculty/MONeill/Math152/Handouts/filliben.pdf

    """
    # Data preparation
    data = np.array(data)
    data = data.flatten()

    # RC Params
    set_rcparams()
    set_markerparams()


    # Line Config
    plt.rcParams["lines.linewidth"] = 1

    
    # Plot (Figure)
    fig = plt.figure(figsize=[6, 3.375])    # Widescreen 16:9
    (osm, osr), (slope, intercept, r) = st.probplot(data, dist="norm", plot=plt)

    # Title
    if(title == None):
        title = "QQ plot"

    plt.title("")
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    # Grid
    plt.grid(axis="both", color="grey", linestyle="--", linewidth=0.5, zorder=5)       

    # Labels
    if(xlabel == None):
        xlabel = "Theoretical quantiles (reference)"

    if(ylabel == None):
        ylabel = "Sample quantiles (data)"


    plt.xlabel(xlabel, loc="center")
    plt.ylabel(ylabel, loc="center")


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


def set_rcparams():
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"
    plt.rcParams["xtick.major.size"] = 3.5
    plt.rcParams["ytick.major.size"] = 0

    return None


def set_markerparams():
    # Marker Config
    plt.rcParams["lines.marker"] = "o"
    plt.rcParams["lines.markerfacecolor"] = "white"
    plt.rcParams["lines.markeredgecolor"] = "black"
    plt.rcParams["lines.markersize"] = 4

    return None


if(__name__ == "__main__"):
    np.random.seed(314)

    data_norm = np.random.normal(loc=6, scale=.5, size=50)
    data_unif = np.random.uniform(low=6, high=np.max(data_norm)*1.5, size=25)
    data = np.append(data_norm, data_unif)

    plot_qqplot(data, savefig=False)
    
