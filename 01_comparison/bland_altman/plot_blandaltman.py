# Bland Altman Analysis [P196] -----------------------------------------

# Versions 
# 01 - Mar 22nd, 2023 - Starter
#    - Jun 20th, 2023 - Applying adjusts to style
#    - Jul 31st, 2023 - difference equation explicit at y_label
#    - Jan 03rd, 2024 - Add legend
#    - Jan 04th, 2024 - Adjust plot area, legend_loc and title position
#    - Jan 14th, 2024 - Add 0 line at Histogram,
#                     - Adjust font.size param


# Insights
# Add variable to control plot size for histogram,



# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# -----------------------------------------------------------------------

def plot_blandaltman(y_true, y_pred, title=None, bins="sqrt", legend_loc="best",
                     savefig=False, verbose=True):
    """
    Performs Bland-Altman analysis to evaluate a bias between the mean
    differences, and to estimate an agreement interval, within which
    95% of the differences.

    """
    # Data Preparation
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # Title
    if(title == None):
        title = "Bland-Altman"

    # Statistics
    mean = np.mean([y_pred, y_true], axis=0)
    diff = y_pred - y_true

    md = np.mean(diff)
    sd = np.std(diff)

    # Graph limits (useful for plot adjusts)
    x_lower = np.min(mean)
    x_upper = np.max(mean)   
    x_step = (x_upper - x_lower) / 10
    
    y_dist = max(np.abs(np.min(diff)), np.abs(np.max(diff)))
    y_lower = (-1) * (y_dist * 1.1)
    y_upper = (y_dist * 1.1)
    

    # Bins
    # more info: https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html
    bins_list = ["fd", "doane", "scott", "stone", "rice", "sturges", "sqrt"]

    if(isinstance(bins, int) == True):
        no_bins = bins

    elif(bins_list.count(bins) == 1):
        no_bins = np.histogram_bin_edges(diff, bins=bins).size

    else:
        print(f' >>> Error: "bins" option not valid. Using "sqrt" as forced option')
        no_bins = np.histogram_bin_edges(diff, bins="sqrt").size


    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"


    # Plot         
    fig = plt.figure(figsize=[6, 3.375])        # Widescreen [16:9]
    grd = fig.add_gridspec(nrows=1, ncols=2, width_ratios=[7.5, 2.5])

    ax0 = fig.add_subplot(grd[0, 0])
    ax1 = fig.add_subplot(grd[0, 1], sharey=ax0)

    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    # Scatter plot
    ax0.scatter(mean, diff, s=30, color="navy", edgecolor="white", alpha=0.7, label="Error", zorder=20)

    ax0.axvline(x=0, color="black", linestyle="-", linewidth=0.8, zorder=19)
    ax0.axhline(y=0, color="black", linestyle="-", linewidth=0.8, zorder=19)
    ax0.axhline(y=md, color="red", linestyle="-", linewidth=0.8, label = "Bias", zorder=18)
    ax0.axhline(y=(md - 1.96*sd), color="grey", linestyle="--", linewidth=0.8, zorder=17)
    ax0.axhline(y=(md + 1.96*sd), color="grey", linestyle="--", linewidth=0.8, zorder=16)
    ax0.fill_between(x=[x_lower-x_step, x_upper+x_step], y1=(md-1.96*sd), y2=(md+1.96*sd), color="lightgrey")

    ax0.set_xlabel("mean", loc="center")
    ax0.set_ylabel("difference (y pred - y true)", loc="center")
    ax0.grid(axis="both", color="grey", linestyle="--", linewidth=0.5)
    ax0.set_xlim(left=(x_lower - x_step), right=(x_upper + x_step))
    ax0.set_ylim(bottom=y_lower, top=y_upper)

    ax0.legend(loc=legend_loc, framealpha=1).set_zorder(99)


    # Histogram of difference
    ax1.hist(x=diff, bins=bins, orientation="horizontal", color="navy", edgecolor="grey", zorder=20)
    ax1.set_xlabel("count", loc="center")
    ax1.grid(axis="both", color="grey", linestyle="--", linewidth=0.5)
    ax1.axhline(y=0, color="black", linestyle="-", linewidth=0.8, zorder=19)


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

