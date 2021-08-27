
def HistBox(Title, Data):

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
    # 08 - 


    # Libraries ---------------------------------------------------------        

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec


    # Program -----------------------------------------------------------    
    
    # Data
    DataPureNumbers = Data[np.logical_not(np.isnan(Data))]

    DataSize = DataPureNumbers.size
    No_Bins = int((DataSize ** (1/2))+ 0.5)

    # Number of bins always as a ODD number = histogram is symetrical
    if(No_Bins % 2 == 0):
        No_Bins = No_Bins-1
    

    # Setting Figure
    fig = plt.figure(figsize=(8, 6))   # A4 Ratio (1.4)
    gs = gridspec.GridSpec(nrows= 1, ncols= 2, width_ratios=[3, 1])

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
    ax1.set_xticks([])

    # 3 - Information
    # Only used at Information BoxPlot and Normal
    

    # 4 - Plotting    
    plt.tight_layout()
    plt.savefig(Title, dpi= 240)
    plt.show()

