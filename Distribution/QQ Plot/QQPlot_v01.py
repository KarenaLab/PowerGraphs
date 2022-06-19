
def QQPlot(title, data):
    """
    Module for QQ Plot.
    

    """

    # Versions
    # 01 - Jun 16th, 2022 - Starter
    # 02 -


    # Insights
    #


    # Libraries
    import numpy as np
    import pandas as pd

    import matplotlib.pyplot as plt


    # PROGRAM ----------------------------------------------------------
    gauss_mean = data.mean()
    gauss_stddev = data.std()
    gauss_size = data.shape[0]

    gauss_ref = np.random.normal(loc=gauss_mean, scale=gauss_stddev, size=gauss_size)

    sample_quantiles, theoretical_quantiles = [], []

    step = min(25, int(gauss_size/10))
    for x in np.linspace(start=0, stop=1, num=step+1):
        sample = np.round(np.quantile(data, x), decimals=6)
        theoretical = np.round(np.quantile(gauss_ref, x), decimals=6)

        sample_quantiles.append(sample)
        theoretical_quantiles.append(theoretical)

    
    lower = min(min(sample_quantiles), min(theoretical_quantiles))
    upper = max(max(sample_quantiles), max(theoretical_quantiles))

    fig = plt.figure(figsize=[8, 4.5])
    fig.suptitle(title, fontsize=12, weight="bold")

    plt.plot([lower, upper], [lower, upper], color="darkred",
             linewidth=2, alpha=0.6, label= "reference", zorder=10)

    if(step < 50):
        plt.scatter(sample_quantiles, theoretical_quantiles, s=25,
                    color="navy", edgecolor="white", label= "QQ spots",
                    alpha=0.7, zorder=11)
    else:
        plt.plot(sample_quantiles, theoretical_quantiles,
                 color="navy", label="QQ line", zorder=11)


    plt.ylim(bottom=lower, top=upper)
    plt.ylabel("Sample Quantiles", fontsize=10)

    plt.xlim(left=lower, right=upper)
    plt.xlabel("Theoretical Quantiles", fontsize=10)
    
    plt.grid(axis="both", color="lightgrey", linestyle="--", linewidth=0.5)
    plt.legend(loc="lower right", fontsize=9, framealpha=1)
    
    plt.tight_layout()
    plt.show()
    

    
