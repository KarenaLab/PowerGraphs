# Identity Line [P315] -------------------------------------------------

# Version
# 01 - Jun 13th, 2023 - Starter
#    - Jan 03rd, 2024 - Set legend over all items,
#    - Jan 04th, 2024 - Adjust variables names
#


# Insights and bugfix
#


# Libraries
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# -----------------------------------------------------------------------

def plot_identityline(y_true, y_pred, title=None, xlabel=None,
                      ylabel=None, alpha=0.7, identity_line=True,
                      legend_loc="lower right",
                      savefig=False, verbose=True):
    """
    Plots an identity line from **y_true** versus **y_pred**.

    """
    # Data preparation
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    # Plot details adjust
    if(title == None):
        title = "Identity line"

    if(xlabel == None):
        xlabel = "y_pred"

    if(ylabel == None):
        ylabel = "ground truth"

    # Add a color adjust
    lower = min(y_pred.min(), y_true.min())
    upper = max(y_pred.max(), y_true.max())
    step = (upper - lower) / 10

    # Linear regression
    x = y_pred.reshape(-1, 1)
    y = y_true.reshape(-1, 1)

    regr = LinearRegression().fit(x, y)

    intercept = regr.intercept_[0]
    coef = regr.coef_[0][0]

    regr_x = np.linspace(start=lower, stop=upper, num=10)
    regr_y = intercept + regr_x * coef


    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"
    

    # Plot
    fig = plt.figure(figsize=[6, 3.375])        # Widescreen [16:9]
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    plt.scatter(y_pred, y_true, s=30, color="navy", edgecolor="white", alpha=alpha, label="data", zorder=20)
    plt.plot([lower, upper], [lower, upper], color="red", linewidth=0.5, label="identity line", zorder=19)
    plt.plot(regr_x, regr_y, color="green", linewidth=0.5, label="regression", zorder=18)

    plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5, zorder=10)

    plt.ylim([lower-step, upper+step])
    plt.xlim([lower-step, upper+step])
    plt.ylabel(ylabel, fontsize=9, loc="center")
    plt.xlabel(xlabel, fontsize=9, loc="center")
    
    plt.legend(loc=legend_loc, fontsize=9, framealpha=1).set_zorder(99)

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

# end
