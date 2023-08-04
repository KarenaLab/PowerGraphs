# Scatter Plot with Histograms [P287] ----------------------------------

# Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Versions
# 01 - 01st Jan 2021 - Starter
# 02 - 30th Jan 2021 - Adding Labels into axis at Scatter Graph
# 03 - 03rd Feb 2021 - Adijusting fig size for best print (A4 Ratio)
# 04 -

# Insights, improvements and bugfix
#


def ScatterHist(Title, Label_X, Data_X, Label_Y, Data_Y):
    """


    """
    # Creating Figure
    fig = plt.figure(figsize= (10, 8.5))        # A4 Ratio (1.4)

    gs = fig.add_gridspec(ncols= 2, nrows= 2,
                          width_ratios= (3, 1), height_ratios= (1, 3),
                          left= 0.1, right= 0.9, bottom= 0.1, top= 0.9,
                          wspace= 0.1, hspace= 0.1)


    # Creating Plotting
    ax0 = fig.add_subplot(gs[1, 0])  # Main Plot
    ax1 = fig.add_subplot(gs[0, 0], sharex = ax0)
    ax2 = fig.add_subplot(gs[1, 1], sharey = ax0)


    # Setting/Adjusting Visual Paramenters

    fig.suptitle("Scatter Plot - " + Title, fontsize = 16)

    ax1.tick_params(axis= "x", labelbottom= False)
    ax2.tick_params(axis= "y", labelleft= False)

    Grid_Color = "grey"
    Grid_Linestyle = "--"
    Grid_Linewidth = 0.5

    ax0.grid(color= Grid_Color, linestyle= Grid_Linestyle, linewidth= Grid_Linewidth)
    ax0.set_axisbelow(True)

    ax1.grid(color= Grid_Color, linestyle= Grid_Linestyle, linewidth= Grid_Linewidth)
    ax1.set_axisbelow(True)

    ax2.grid(color= Grid_Color, linestyle= Grid_Linestyle, linewidth= Grid_Linewidth)
    ax2.set_axisbelow(True)


    # Graph 0 = Scatter
    ax0.scatter(Data_X, Data_Y, alpha= 0.2, edgecolor= "white")
    ax0.set_xlabel(Label_X)
    ax0.set_ylabel(Label_Y)
    

    # Graph 1 = Histogram of X
    Data_Size = Data_X.size
    bins_x = int((Data_Size ** (1/2)) + 0.5)
    
    ax1.hist(x= Data_X, bins= bins_x, orientation= "vertical")
      

    # Graph 2 = Histogram of Y
    Data_Size = Data_Y.size
    bins_y = int((Data_Size ** (1/2)) + 0.5)

    ax2.hist(x= Data_Y, bins= bins_y, orientation= "horizontal")
    

    # Plotting (Out)
    plt.savefig(Title, dpi= 240)
    plt.show()

