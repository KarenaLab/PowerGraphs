# Bar Horizontal Categories

def BHorCategories(Title, Data, **kwargs):

    import numpy as np
    import pandas as pd

    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec


    # Versions ---------------------------------------------------------

    # 01 - Jun 07th, 2021 - Starter
    # 02 - Jun 14th, 2021 - Adding **kwargs (savefig, cmap and colsmax)
    # 03 - Sep 23rd, 2021 - Adjusting Window Size and lines
    # 04 - 


    # List of Variables and kwargs -------------------------------------

    # Title = Figure Title and Filename (string)
    # Data = Information (Pandas Column)

    # figratio = A4*, Wide or Square
    # savefig = False* or True
    # cmap = Blues*
    # colsmax = 10* or any integer
    #


    # Program ----------------------------------------------------------

    # kwargs setup

    colormap = "Blues"
    cmap = kwargs.get("cmap")

    if cmap:
        colormap = cmap


    max_cols = 10
    colsmax = kwargs.get("colsmax")

    if colsmax:
        max_cols = colsmax


    y_size = 8
    x_size = 11.28

    figratio = kwargs.get("figratio")
    
    if figratio:

        if(figratio == "square"):
            ratio = 1

        if(figratio == "wide"):
            ratio = 1.7778

        if(figratio == "A4"):
            ratio = 1.4095

        x_size = round(y_size * ratio, ndigits= 2)


    savefig = kwargs.get("savefig")

        
    # Info

    size = Data.size
    values = Data.unique()
    unique = values.size

    if(values.dtype == "int64" or values.dtype == "float64"):
        values = np.sort(values)
        

    Index_List = []
    Counter_List = []


    for item in values:

        Counter = (Data == item).sum()

        Index_List.append(item)
        Counter_List.append(Counter)


    Index_List = np.array(Index_List)
    Counter_List = np.array(Counter_List)


    # Plotting

    fig = plt.figure(figsize= (x_size, y_size))
    gs = fig.add_gridspec(ncols= 2, nrows= 1, width_ratios= [8, 2])

    ax0 = fig.add_subplot(gs[0, 0])         # Horizontal Bar
    ax1 = fig.add_subplot(gs[0, 1])         # Annotations

    fig.suptitle(Title, fontsize= 16)


    # Bar Horizontal (Main Plot)

    y_positions = np.arange(len(Counter_List))

    ax0.barh(y_positions, Counter_List, tick_label= Index_List, color= "navy")
    ax0.invert_yaxis()

    ax0.set_xlabel("Count")
    
    ax0.xaxis.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
    ax0.set_axisbelow(True)


    # Texts and Annotations (Secondary Plot)

    ax1.axis(False)
    

    # Printing

    if (savefig == True):
        plt.savefig(Title, dpi= 240)


    plt.show()

