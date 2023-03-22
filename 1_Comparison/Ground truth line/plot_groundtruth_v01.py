
# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Personal modules



def plot_groundtruth(ground_truth, comparison, title=None, xlabel=None,
                     ylabel=None, alpha=0.7, truth_line=True, savefig=False,
                     verbose=True):
    """


    """
    # Plot details adjust
    if(title == None):
        title = "Ground truth comparison"

    if(xlabel == None):
        xlabel = "comparison"

    if(ylabel == None):
        ylabel = "ground truth"

    # Add a color adjust

    lower = min(comparison.min(), ground_truth.min())
    upper = max(comparison.max(), ground_truth.max())
    step = (upper - lower) / 10

    # Plot
    fig = plt.figure(figsize=[8, 4.5])
    fig.suptitle(title, fontsize=10, fontweight="bold")

    plt.scatter(comparison, ground_truth, s=40, color="navy", edgecolor="white", alpha=alpha, zorder=21)
    plt.plot([lower, upper], [lower, upper], color="red", zorder=20)

    plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    plt.ylim([lower - step, upper + step])
    plt.xlim([lower - step, upper + step])
    plt.ylabel(ylabel, fontsize=10, loc="center")
    plt.xlabel(xlabel, fontsize=10, loc="center")

    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)
        if(verbose == True):
            print(f" > saving file {title}.png")

    else:
        plt.show()

    plt.close(fig)

    return None

    
