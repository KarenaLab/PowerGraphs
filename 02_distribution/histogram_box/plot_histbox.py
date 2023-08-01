
def HistBox(Title, Data, **kwargs):

    # Versions:
    # 01 - Initial
    # 02 - Correcting Whiskers (Adding Calculation) = 10th Dec 2020
    #      Automatic figure saving with Full HD size (1920x1080 px)
    # 03 - Adding a Vertical line in Histogram for Mean = 11th Dec 2020
    #      Correcting 1o Quantile Error label in Describe
    # 04 - Adjusting Mean and Median line colors
    # 05 - Dividing in THREE options: HistBox_v05, HistBoxInfo_v05 and
    #          HistBoxInfoNormal_v05
    # 06 - Adjusting the printing ratio for A4 Page - 03rd Feb 2021
    # 07 - Bar Color = RoyalBlue and adding border (edgecolor= white)
    #      Aug 27th, 2021
    # 08 - Changing position of BoxPlot and adding **kwargs - Sept 01st, 2021
    # 09 - Adding Binning options - Oct 11th, 2021
    # 10 -
    


    # List of Variables and **kwargs ------------------------------------

    # Title = Figure Title and Filename (string)
    # Data = Information to be used (Numpy array)

    # roundsize = 4* or any integer number
    # figratio = A4, Wide or Square
    # savefig = False* or True
    # show = True* or False
    # bins = sqrt*, sturges or number of bins (int)
    

    # Libraries ---------------------------------------------------------        

    import numpy as np
    import pandas as pd
    import scipy.stats as stats
    
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec


    # Program -----------------------------------------------------------    

    # Data
    DataPureNumbers = Data[np.logical_not(np.isnan(Data))]

    Data_Size = DataPureNumbers.size
    No_Bins = int((Data_Size**(1/2))+ 0.5)


    bins_method = kwargs.get("bins")

    if(bins_method == None):
        bins_method = "sqrt"


    if(bins_method == "sqrt"):

        No_Bins = int((Data_Size**(1/2))+ 0.5)

        # Number of bins always as a ODD number = histogram is symetrical

        if(Data_Size >= 500 and No_Bins % 2 == 0):
            No_Bins = No_Bins-1


    if(bins_method == "sturges"):

        No_Bins = int((np.log2(Data_Size)+1)+ 0.5)
        

    if(type(bins_method) == int):

        No_Bins = bins_method
    

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

        
    fig = plt.figure(figsize=(x_size, y_size)) 
    gs = gridspec.GridSpec(nrows= 2, ncols= 2,
                           width_ratios= [7, 3], height_ratios= [8, 2]) 

    ax0 = plt.subplot(gs[0, :])                 # Main = Histogram
    ax1 = plt.subplot(gs[1, :], sharex= ax0)    # Boxplot


    fig.suptitle(Title, fontsize= 16)


    # 1 - Histogram (ax0)
    
    n, bins, patches = ax0.hist(x= DataPureNumbers, bins= No_Bins,
                                color= "navy", edgecolor= "white")

    # bins = Central Value of the bin
    # n = Quantity of items inside the bin
    # patches = Color information (Internal Variable)

    Mean = round(np.mean(DataPureNumbers), 4)
    StdDev = round(np.std(DataPureNumbers), 4)
    Median = round(np.median(DataPureNumbers), 4)

    # y = ((1/(np.sqrt(2*np.pi)*StdDev)) * np.exp(-0.5*(1/StdDev*(bins-Mean))**2))
    # Curve = y * 1000
    # ax0.plot(bins, Curve, color= "red", linestyle= "--", linewidth= 0.75)


    ax0.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
    ax0.set_axisbelow(True)

    ax0.axvline(x= Mean, color= "green", linewidth= 1)
    ax0.axvline(x= Median, color= "orange", linewidth= 1)

    # *** Coincidir as linhas de grade com os steps de StdDev ***


    # 2 - Box Plot
    
    Red_Bullet = dict(markerfacecolor= "r")

    ax1.boxplot(x= DataPureNumbers, vert= False, widths= 0.5,
                showmeans= True, meanline= True, flierprops= Red_Bullet)
    ax1.xaxis.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)

    ax1.set_axisbelow(True)
    ax1.set_yticks([])


    # 4 - Plotting

    plt.tight_layout()

    savefig = kwargs.get("savefig")

    if(savefig == True):
        plt.savefig(Title, dpi= 240)
        

    show = kwargs.get("show")

    if(show != False):
        plt.show()

