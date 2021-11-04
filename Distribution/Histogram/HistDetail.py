
def HistDetail(Title, Data, **kwargs):

    # Versions ---------------------------------------------------------
    
    # 01 - Sept 10th, 2021 - Launch Edition
    # 02 - 
    

    # List of Variable and kwargs --------------------------------------

    # Title = Figure Title and Filename (string)
    # Data = Information to be used (Numpy array)

    # roundsize = 4* or any integer number
    # figratio = A4, Wide or Square
    # savefig = False* or True
    # show = True* or False
    # bins = number of bins (integer)


    # Libraries --------------------------------------------------------

    import numpy as np
    import pandas as pd
    import scipy.stats as stats
    
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec


    # Program ----------------------------------------------------------    
    
    # Data

    DataPureNumbers = Data[np.logical_not(np.isnan(Data))]

    DataSize = DataPureNumbers.size
    No_Bins = int((DataSize**(1/2))+ 0.5)


    # Number of bins always as a ODD number = histogram is symetrical

    if(DataSize >= 500 and No_Bins % 2 == 0):
        No_Bins = No_Bins-1

    bins = kwargs.get("bins")

    if bins:
        No_Bins = bins
    

    # Setting Figure

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


    fig = plt.figure(figsize= (x_size, y_size))
    grid = gridspec.GridSpec(nrows= 4, ncols= 5,
                             width_ratios= [3, 2, 2, 2, 3],
                             height_ratios= [3, 3, 3, 1])

    ax0 = plt.subplot(grid[1:3, 1:4])       # Main Plot

    ax1 = plt.subplot(grid[0, 0])
    ax2 = plt.subplot(grid[1, 0])
    ax3 = plt.subplot(grid[2, 0])
    ax4 = plt.subplot(grid[3, 0])


    # Closing

    plt.show()

