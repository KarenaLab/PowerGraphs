# Bland Altman Analysis

def plot_blandaltman(ground_truth, comparison, title=None, label1="ground_truth",
                     label2="comparison", savefig=False, verbose=True):
    """
    Performs Bland-Altman analysis to evaluate a bias between the mean
    differences, and to estimate an agreement interval, within which
    95% of the differences.

    """

    # Libraries
    import numpy as np
    import pandas as pd

    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    

    # Versions ---------------------------------------------------------
    # 01 - Mar 22nd, 2023
    # 02 -


    # Insights



    # Program ----------------------------------------------------------
    ground_truth = np.array(ground_truth)
    comparison = np.array(comparison)


    # Data
    if(title == None):
        title = "Bland-Altman"


    # Statistic
    mean = np.mean([comparison, ground_truth], axis=0)
    diff = comparison - ground_truth

    md = np.mean(diff)
    sd = np.std(diff)

    # Graph limits (useful for plot adjusts)
    x_lower = np.min(mean)
    x_upper = np.max(mean)   
    x_step = (x_upper - x_lower) / 10
    
    y_dist = max(np.abs(np.min(diff)), np.abs(np.max(diff)))
    y_lower = (-1) * (y_dist * 1.1)
    y_upper = (y_dist * 1.1)
    # Turn "10" and 1.1 into a variable to be adjusted by **kwargs

    # Bins
    bins = int(np.sqrt(len(mean)) + 0.5)


    # Plot
    fig = plt.figure(figsize=[8, 4.5])
    grd = fig.add_gridspec(nrows=1, ncols=2, width_ratios=[8, 2])

    ax0 = fig.add_subplot(grd[0, 0])
    ax1 = fig.add_subplot(grd[0, 1], sharey=ax0)

    fig.suptitle(title, fontsize=10, fontweight="bold")

    # ax0 = Scatter plot
    ax0.scatter(mean, diff, s=30, color="navy", edgecolor="white", alpha=0.7, zorder=20)

    ax0.axhline(y=0, color="black", linestyle="-", linewidth=0.8, zorder=19)
    ax0.axhline(y=md, color="red", linestyle="-", linewidth=0.8, zorder=18)
    ax0.axhline(y=(md - 1.96*sd), color="grey", linestyle="--", linewidth=0.8, zorder=17)
    ax0.axhline(y=(md + 1.96*sd), color="grey", linestyle="--", linewidth=0.8, zorder=16)
    ax0.fill_between(x=[x_lower-x_step, x_upper+x_step], y1=(md-1.96*sd), y2=(md+1.96*sd), color="lightgrey")

    ax0.set_xlabel("mean", loc="center")
    ax0.set_ylabel("difference", loc="center")
    ax0.grid(axis="both", color="grey", linestyle="--", linewidth=0.5)
    ax0.set_xlim(left=(x_lower-x_step), right=(x_upper+x_step))
    ax0.set_ylim(bottom=y_lower, top=y_upper)

    #ax1 = Histogram of difference
    ax1.hist(x=diff, bins=bins, orientation="horizontal", color="navy", edgecolor="grey", zorder=20)
    ax1.set_xlabel("count", loc="center")
    ax1.grid(axis="both", color="grey", linestyle="--", linewidth=0.5)

    plt.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)

        if(verbose == True):
            print(f' > saved plot as "{title}.png"')

    else:
        plt.show()

    plt.close(fig)

    return None

# end
