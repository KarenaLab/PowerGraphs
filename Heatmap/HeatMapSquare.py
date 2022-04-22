# HeatMap for Correlation -----------------------------------------------

def HeatMapSquare(title, data, decimals=2, method="pearson", **kwargs):
    """
    Prints a Triangular Heatmap for Correlations between variables,
    using Pearson or Spearman methods.

    * title = Title for plot AND its filename if asked to save it,
    * data = Pandas dataframe format,

    * decimals = Number of decimals to display (default=2)
    * method = Method for Correlation: pearson*, spearman or kendall,
      https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html

    kwargs:
    * figratio = wide* or A4,
    * cmap = Blues* (using Matplotlib color standards),
             Sugestions: Blues*, Greys, Greens, Oranges, Reds, binary,
      https://matplotlib.org/stable/tutorials/colors/colormaps.html
    * aspect = Relation between x and y axis. (default=0.625),
    * fontsize = Size of font (default=9)
    * savefig = Saving figure (False* or True),
    * showfig = Showing figure created (True* or False),
    
    """

    # Libraries ---------------------------------------------------------

    import numpy as np
    import pandas as pd
    
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec


    # Versions ----------------------------------------------------------

    # 01 - 31st Jan 2021 - Starter
    # 02 - 31st Jan 2021 - Removing Duplicated Info
    # 03 - 03rd Feb 2021 - Adjusting size for printing (A4 Ratio)
    # 04 - 16th Feb 2021 - Adding **kwargs
    # 05 - 21th Apr 2021 - Simplifying Data entry for just Data, removing
    #                      Columns (Labels) info
    # 06 - 01st Sep 2021 - Adjusting (small corrections)
    # 07 - 21st Apr 2022 - Adding Spearman and adjusting kwargs
    #                      Added correlation method to the title/filename
    # 08 - 

    # Insights:

    # Add rotation to x_axis labels (need to check anchor),
    # 

    # Program -----------------------------------------------------------

    # kwargs information gathering
    x_size, y_size = 8, 4.5
    colormap = "Blues"
    fsize = 9
    
    
    figratio = kwargs.get("figratio")
    if figratio:
        if(figratio == "A4"): ratio = 1.4095
        if(figratio == "wide"): ratio = 1.7778

        x_size = np.round((y_size * ratio), decimals=2)


    cmap = kwargs.get("cmap")
    if cmap:
        colormap = cmap


    aspect = kwargs.get("aspect")
    if(aspect == None):
        aspect = 0.625


    fontsize = kwargs.get("fontsize")
    if fontsize:
        fsize = fontsize
        

    savefig = kwargs.get("savefig")
    showfig = kwargs.get("showfig")   
    

    # Data Processing
    title = title + "_" + method

    corr = data.corr(method=method).values
    corr = np.abs(np.round(corr, decimals=decimals))

    columns = data.columns
    ticks = len(columns)
  
    # Removing Duplicated Data (Right Triangle Figure)
    for i in range(0, len(columns)):
        for j in range(0, len(columns)):
            if(i < j):
                corr[i, j] = 0
    

    # Plotting
    fig = plt.figure(figsize=(x_size, y_size))
    ax = fig.add_subplot()
       
    im = ax.imshow(corr, cmap=colormap, aspect=aspect)

    fig.suptitle(title, fontsize=fsize+3)
    ax.set_xticks(np.arange(start=0, stop=ticks))
    ax.set_yticks(np.arange(start=0, stop=ticks))

    ax.set_xticklabels(columns, rotation=90, fontsize=fsize)
    ax.set_yticklabels(columns, rotation=0, fontsize=fsize)


    # Creating Text Annotations
    for i in range(0, len(columns)):
        for j in range(0, len(columns)):
            if(i >= j):
                value = corr[i, j]
                
                if(value >= 0.6): text_color = "white"
                else: text_color = "black"

                text = ax.text(j, i, value, ha="center", va="center",
                               color=text_color, fontsize=fsize-1)


    # Printing
    fig.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)
        print(f" > saving figure: {title}.png")

    if(showfig == False):
        plt.close()

    else:
        plt.show()
   
