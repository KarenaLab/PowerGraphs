
# Libraries
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# Personal modules



def plot_groundtruth(ground_truth, comparison, title=None, xlabel=None,
                     ylabel=None, alpha=0.7, truth_line=True, savefig=False,
                     verbose=True):
    """


    """
    ground_truth = np.array(ground_truth)
    comparison = np.array(comparison)
    
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

    # Linear regression
    x = comparison.reshape(-1, 1)
    y = ground_truth.reshape(-1, 1)

    regr = LinearRegression().fit(x, y)

    intercept = regr.intercept_[0]
    coef = regr.coef_[0][0]

    regr_x = np.linspace(start=lower, stop=upper, num=10)
    regr_y = intercept + regr_x * coef
    

    # Plot
    fig = plt.figure(figsize=[8, 4.5])
    fig.suptitle(title, fontsize=10, fontweight="bold")

    plt.scatter(comparison, ground_truth, s=40, color="navy", edgecolor="white", alpha=alpha, label="data", zorder=20)
    plt.plot([lower, upper], [lower, upper], color="red", label="truth line", zorder=19)
    plt.plot(regr_x, regr_y, color="green", label="regression", zorder=18)

    plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    plt.ylim([lower-step, upper+step])
    plt.xlim([lower-step, upper+step])
    plt.ylabel(ylabel, fontsize=10, loc="center")
    plt.xlabel(xlabel, fontsize=10, loc="center")
    
    plt.legend(loc="lower right", fontsize=9, framealpha=1)
    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)
        if(verbose == True):
            print(f" > saving file {title}.png")

    else:
        plt.show()

    plt.close(fig)

    return None

    
