# Identity Line [P315] -------------------------------------------------

# Version
# 01 - Jun 13th, 2023 - Starter
# 02 -


# Insights and bugfix
#


# Libraries
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec



def plot_identityline(ground_truth, comparison, title=None, xlabel=None,
                     ylabel=None, alpha=0.7, truth_line=True, savefig=False,
                     verbose=True):
    """
    Plots an identity line comparison.

    """
    # Data preparation
    ground_truth = np.array(ground_truth)
    comparison = np.array(comparison)
    
    # Plot details adjust
    if(title == None):
        title = "Identity line"

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


    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["figure.dpi"] = 180
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"
    

    # Plot
    fig = plt.figure(figsize=[6, 3.375])
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    plt.scatter(comparison, ground_truth, s=40, color="navy", edgecolor="white", alpha=alpha, label="data", zorder=20)
    plt.plot([lower, upper], [lower, upper], color="red", linewidth=0.5, label="identity line", zorder=19)
    plt.plot(regr_x, regr_y, color="green", linewidth=0.5, label="regression", zorder=18)

    plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    plt.ylim([lower-step, upper+step])
    plt.xlim([lower-step, upper+step])
    plt.ylabel(ylabel, fontsize=9, loc="center")
    plt.xlabel(xlabel, fontsize=9, loc="center")
    
    plt.legend(loc="lower right", fontsize=9, framealpha=1)
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
