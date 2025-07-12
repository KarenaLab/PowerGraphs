# PCA Principals [P522] -------------------------------------------------

# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------
def plot_pca_principals(DataFrame, label, title=None, color_map=None,
                        savefig=False, verbose=True):
    """
    

    """
    # Data preparation
    variables = DataFrame[label].unique()

    # Colors
    if(color_map == None):
        colors = ["navy", "darkred", "orange", "darkgreen", "darkviolet"]

    colors = colors[0: variables.size]

    # Title
    if(title == None):
        title = "PCA Principals"

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
    fig = plt.figure(figsize=[6, 3.375])    # Widescreen 16:9
    fig.suptitle(title, fontsize=10, fontweight="bold", x=0.98, ha="right")

    for var, color in zip(variables, colors):
        data = DataFrame.groupby(by=label).get_group(var)
        plt.scatter(x=data["PC1"], y=data["PC2"], s=20, color=color, edgecolor="white",
                    alpha=0.6, label=var, zorder=20)

    plt.xlabel("PC1", loc="center")
    plt.ylabel("PC2", loc="center")

    plt.grid(axis="both", color="grey", linestyle="--", linewidth=0.8, zorder=5)       
    plt.legend(loc="best", framealpha=1).set_zorder(99)

    plt.tight_layout()

    # Printing 
    if(savefig == True):
        plt.savefig(title, dpi=320)

        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()

    plt.close(fig)


    return None
    
