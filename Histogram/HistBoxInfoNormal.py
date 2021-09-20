
def HistBoxInfoNormal(Title, Data, **kwargs):

    # Versions ---------------------------------------------------------
    
    # 01 - Initial
    # 02 - Correcting Whiskers (Adding Calculation) = 10th Dec 2020
    #      Automatic figure saving with Full HD size (1920x1080 px)
    # 03 - Adding a Vertical line in Histogram for Mean = 11th Dec 2020
    #      Correcting 1o Quantile Error label in Describe
    # 04 - Adjusting Mean and Median line colors
    # 05 - Creating two versions: (1) Box Plot and (2) Normal Curve Info
    # 06 - Adjusting Texts when Division Denominator is Zero (Infinite
    #      Error - 03rd Jan 2021
    # 07 - Adjusting the printing ratio for A4 Page - 03rd Feb 2021
    # 08 - Adding **kwargs - 06th Apr 2021
    # 09 - Adding Median to InfoBox - 14th Apr 2021
    # 10 - Adding a Normal Curve - 15th Apr 2021 *** Need to Improve
    # 11 - Adding a **kwargs = Plot Selection - 21st Apr 2021
    # 12 - Adding bin control - 22nd Apr 2021
    # 13 - Adjusting positions of labels - Jul 22th, 2021
    # 14 - Adjusting Barplot (color and edges) - Aug 27th, 2021
    # 15 - Changing position of BoxPlot - Sep 01st, 2021
    # 16 - Adjusting linestyle of Mean - Sep 19th, 2021
    # 17 - 
    

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

    if(No_Bins % 2 == 0):
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

        
    fig = plt.figure(figsize=(x_size, y_size)) 
    gs = gridspec.GridSpec(nrows= 2, ncols= 2,
                           width_ratios= [7, 3], height_ratios= [8, 2]) 

    ax0 = plt.subplot(gs[0, 0])                 # Main = Histogram
    ax1 = plt.subplot(gs[1, 0], sharex= ax0)    # Boxplot
    ax2 = plt.subplot(gs[:, 1])                 # Text (Information)


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

    ax0.axvline(x= Mean, color= "green", linestyle= "--", linewidth= 1)
    ax0.axvline(x= Median, color= "orange", linewidth= 1)

    # *** Coincidir as linhas de grade com os steps de StdDev ***


    # 2 - Box Plot
    
    Red_Bullet = dict(markerfacecolor= "r")

    ax1.boxplot(x= DataPureNumbers, vert= False, widths= 0.5,
                showmeans= True, meanline= True, flierprops= Red_Bullet)
    ax1.xaxis.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)

    ax1.set_axisbelow(True)
    ax1.set_yticks([])


    # 3 - Info

    roundsize = kwargs.get("roundsize")

    if(roundsize == None):
        roundsize = 4


    No_Items = Data.size
    No_Items_String = f"No. Items = {str(No_Items)}"

    No_NaN = Data.size - DataPureNumbers.size
    No_NaNpc = round((No_NaN/Data.size) * 100, 3)
    NaN_String = f"NaN = {str(No_NaN)} ({str(No_NaNpc)}%)"

    Mean = round(np.mean(DataPureNumbers), roundsize)
    Mean_String = f"Mean = {str(Mean)}"

    Median = round(np.median(DataPureNumbers), roundsize)
    Median_String = f"Median = {str(Median)}"

    StdDev = round(np.std(DataPureNumbers), roundsize)
    StdDev_String = f"StdDev = {str(StdDev)}"

    Min = round(np.amin(DataPureNumbers), roundsize)
    Min_String = f"Min = {str(Min)}"

    Max = round(np.amax(DataPureNumbers), roundsize)
    Max_String = f"Max = {str(Max)}"

    Range = round(Max - Min, roundsize)
    Range_String = f"Range = {str(Range)}"


    Lower_Limit = round(Mean - 3*StdDev, roundsize)
    Lower_Limit_String = f"Lower Limit = {str(Lower_Limit)}"

    Upper_Limit = round(Mean + 3*StdDev, roundsize)
    Upper_Limit_String = f"Upper Limit = {str(Upper_Limit)}"

    Outside = np.sum(DataPureNumbers < Lower_Limit) + np.sum(DataPureNumbers > Upper_Limit)
    Outsidepc = round((Outside/DataPureNumbers.size) * 100, 3)
    Outside_String = "Outside = " + str(Outside) + " (" + str(Outsidepc) + "%)"

    Inside = DataPureNumbers.size - Outside
    Insidepc = round((Inside/DataPureNumbers.size) * 100, 3)
    Inside_String = "Inside = " + str(Inside) + " (" + str(Insidepc) + "%)"

    if(Outside > 0):
        Outside_Upper = np.sum(DataPureNumbers > Upper_Limit)
        Outside_Upperpc = round((Outside_Upper/Outside) * 100, 1)

        Outside_Lower = np.sum(DataPureNumbers < Lower_Limit)
        Outside_Lowerpc = round((Outside_Lower/Outside) * 100, 1)

    else:
        Outside_Upper = 0
        Outside_Upperpc = 0

        Outside_Lower = 0
        Outside_Lowerpc = 0


    Outside_Upper_String = "Outside Upper = " + str(Outside_Upper) + " (" + str(Outside_Upperpc) + "%)*"
    Outside_Lower_String = "Outside Lower = " + str(Outside_Lower) + " (" + str(Outside_Lowerpc) + "%)*"

   
    # 3.2 - Information Plotting

    ax2.axis(False)

    # X Position
    X_Left = 0.05
    X_Tab_One = 0.150

    # Y Position
    
    plt.text(x= X_Left, y= 0.980, s= No_Items_String)
    plt.text(x= X_Tab_One, y= 0.950, s= NaN_String)

    plt.text(x= X_Left, y= 0.905, s= Mean_String)
    plt.text(x= X_Left, y= 0.875, s= Median_String)
    plt.text(x= X_Left, y= 0.845, s= StdDev_String)
    plt.text(x= X_Left, y= 0.815, s= Min_String)
    plt.text(x= X_Left, y= 0.785, s= Max_String)
    plt.text(x= X_Left, y= 0.755, s= Range_String)
    
    plt.text(x= X_Left, y= 0.710, s= Lower_Limit_String)
    plt.text(x= X_Left, y= 0.680, s= Upper_Limit_String)

    plt.text(x= X_Left, y= 0.635, s= Inside_String)
    plt.text(x= X_Left, y= 0.605, s= Outside_String)
    plt.text(x= X_Tab_One, y= 0.575, s= Outside_Lower_String)
    plt.text(x= X_Tab_One, y= 0.545, s= Outside_Upper_String)


    # 4 - Plotting

    plt.tight_layout()

    savefig = kwargs.get("savefig")

    if(savefig == True):
        plt.savefig(Title, dpi= 240)
        

    show = kwargs.get("show")

    if(show != False):
        plt.show()

