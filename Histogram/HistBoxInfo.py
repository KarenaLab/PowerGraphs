
def HistBoxInfo(Title, Data):

    # Versions:
    # 01 - Initial
    # 02 - Correcting Whiskers (Adding Calculation) = 10th Dec 2020
    #      Automatic figure saving with Full HD size (1920x1080 px)
    # 03 - Adding a Vertical line in Histogram for Mean = 11th Dec 2020
    #      Correcting 1o Quantile Error label in Describe
    # 04 - Adjusting Mean and Median line colors
    # 05 - Creating two versions: (1) Box Plot and (2) Normal Curve Info
    # 06 - Adjusting TExt when Division Denominator is Zero (Infinite
    #      Error - 03rd Feb 2021
    # 07 - Adjusting the printing ratio for A4 Page - 03rd Feb 2021
    # 08 - Bar Color = RoyalBlue and adding border (edgecolor= white)
    #      Aug 27th, 2021
    # 09 - 


    # Libraries --------------------------------------------------------

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec


    # Program ----------------------------------------------------------    
    
    # Data
    DataPureNumbers = Data[np.logical_not(np.isnan(Data))]

    DataSize = DataPureNumbers.size
    No_Bins = int((DataSize ** (1/2))+ 0.5)

    # Number of bins always as a ODD number = histogram is symetrical
    if(No_Bins % 2 == 0):
        No_Bins = No_Bins-1
    

    # Setting Figure
    fig = plt.figure(figsize=(8, 6))   # A4 Ratio (1.4) 
    gs = gridspec.GridSpec(nrows= 1, ncols= 3, width_ratios=[3, 1, 2])

    fig.suptitle(Title, fontsize= 16)


    # 1 - Histogram
    ax0 = plt.subplot(gs[0])
    ax0.hist(x= DataPureNumbers, bins= No_Bins, color= "royalblue", edgecolor= "white")

    ax0.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
    ax0.set_axisbelow(True)

    Mean = round(np.mean(DataPureNumbers), 4)
    plt.axvline(x= Mean, color= "green", linewidth= 1)

    Median = round(np.median(DataPureNumbers), 4)
    plt.axvline(x= Median, color= "orange", linewidth= 1)

    # *** Coincidir as linhas de grade com os steps de StdDev ***


    # 2 - Box Plot
    ax1 = plt.subplot(gs[1])

    Red_Bullet = dict(markerfacecolor="r")
    ax1.boxplot(x= DataPureNumbers, widths= 0.5 ,showmeans= True, meanline= True, flierprops= Red_Bullet)
    ax1.yaxis.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
    ax1.set_axisbelow(True)
    ax1.set_xticks([])
 
    
    # 3 - Info
    # 3.1 - Information Calculation

    No_Items = Data.size
    No_Items_String = "No. Items = " + str(No_Items)

    No_NaN = Data.size - DataPureNumbers.size
    No_NaNpc = round((No_NaN/Data.size) * 100, 3)
    NaN_String = "NaN = " + str(No_NaN) + " (" + str(No_NaNpc) + "%)"

    Mean = round(np.mean(DataPureNumbers), 4)
    Mean_String = "Mean = " + str(Mean)

    StdDev = round(np.std(DataPureNumbers), 4)
    StdDev_String = "StdDev = " + str(StdDev)

    # % inside

    Min = round(np.amin(DataPureNumbers), 4)
    Min_String = "Min = " + str(Min)

    Max = round(np.amax(DataPureNumbers), 4)
    Max_String = "Max = " + str(Max)

    Range = round(Max - Min, 4)
    Range_String = "Range = " + str(Range)


    BoxInfo = [0, 0, 0, 0, 0, 0]
    BoxIndex = ["Up_Whis", "3o_Quart", "Median", "Mean", "1o_Quart", "Low_Whis"]

    BoxInfo[1] = round(np.quantile(DataPureNumbers, 0.750), 4)
    BoxInfo[2] = round(np.median(DataPureNumbers), 4) # or np.quantile(DataPureNumbers, 0.500)
    BoxInfo[3] = round(np.mean(DataPureNumbers), 4)
    BoxInfo[4] = round(np.quantile(DataPureNumbers, 0.250), 4)

    iqr = BoxInfo[1] - BoxInfo[4]

    BoxInfo[0] = round(DataPureNumbers[DataPureNumbers <= BoxInfo[1]+1.5*iqr].max(), 4)
    BoxInfo[5] = round(DataPureNumbers[DataPureNumbers >= BoxInfo[4]-1.5*iqr].min(), 4)
  

    Up_Whisker_String = "Upper Whisker = " + str(BoxInfo[0])    
    Quartile_3_String = "3o Quartile = " + str(BoxInfo[1])
    Median_String = "Median (2o Q) = " + str(BoxInfo[2])
    Quartile_1_String = "1o Quartile = " + str(BoxInfo[4])
    Low_Whisker_String = "Lower Whisker = " + str(BoxInfo[5])


    Outside = np.sum(DataPureNumbers < BoxInfo[5]) + np.sum(DataPureNumbers > BoxInfo[0])
    Outsidepc = round((Outside/DataPureNumbers.size) * 100, 3)
    Outside_String = "Outside = " + str(Outside) + " (" + str(Outsidepc) + "%)"

    Inside = DataPureNumbers.size - Outside
    Insidepc = round((Inside/DataPureNumbers.size) * 100, 3)
    Inside_String = "Inside = " + str(Inside) + " (" + str(Insidepc) + "%)"

    Outside_Upper = np.sum(DataPureNumbers > BoxInfo[0])
    Outside_Upperpc = round((Outside_Upper/Outside) * 100, 1)
    Outside_Upper_String = "Outside Upper = " + str(Outside_Upper) + " (" + str(Outside_Upperpc) + "%)*"

    Outside_Lower = np.sum(DataPureNumbers < BoxInfo[5])
    Outside_Lowerpc = round((Outside_Lower/Outside) * 100, 1)
    Outside_Lower_String = "Outside Lower = " + str(Outside_Lower) + " (" + str(Outside_Lowerpc) + "%)*"

   
    # 3.2 - Information Plotting

    ax2 = plt.subplot(gs[2])

    ax2.axis(False)

    # x position: 0.00 = Left Border
    #             0.15 = Tab

    # y position: 0.050 = Line space
    #             0.075 = Line space with New Section
    
    plt.text(x= 0.00, y= 0.950, s= No_Items_String)
    plt.text(x= 0.10, y= 0.900, s= NaN_String)

    plt.text(x= 0.00, y= 0.825, s= Mean_String)
    plt.text(x= 0.00, y= 0.775, s= StdDev_String)
    plt.text(x= 0.00, y= 0.725, s= Min_String)
    plt.text(x= 0.00, y= 0.675, s= Max_String)
    plt.text(x= 0.00, y= 0.625, s= Range_String)
    
    plt.text(x= 0.00, y= 0.550, s= Up_Whisker_String)
    plt.text(x= 0.00, y= 0.500, s= Quartile_3_String)
    plt.text(x= 0.00, y= 0.450, s= Median_String)
    plt.text(x= 0.00, y= 0.400, s= Mean_String)
    plt.text(x= 0.00, y= 0.350, s= Quartile_1_String)
    plt.text(x= 0.00, y= 0.300, s= Low_Whisker_String)

    plt.text(x= 0.00, y= 0.225, s= Inside_String)
    plt.text(x= 0.00, y= 0.175, s= Outside_String)
    plt.text(x= 0.10, y= 0.125, s= Outside_Lower_String)
    plt.text(x= 0.10, y= 0.075, s= Outside_Upper_String)


    # 4 - Plotting

    plt.tight_layout()
    plt.savefig(Title, dpi= 240)
    plt.show()

