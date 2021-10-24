
def MissingDataRow(Title, DF, **kwargs):

    # Versions ----------------------------------------------------------

    # 01 - Oct 17th, 2021 - Starter*
    # 02 - Oct 17th, 2021 - Adding Secondary Y Axis
    # 03 -
    


    # Libraries ---------------------------------------------------------

    import numpy as np
    import pandas as pd

    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec


    # List of Variables and **kwargs ------------------------------------

    # Title = Figure Title and Filename (string)
    # Data = Information to be used (Pandas)

    # figratio = A4* or Wide
    # savefig = False* or True
    # width = 0.8* or any number
    # color = darkred* or any color from Matplotlib


    # Program -----------------------------------------------------------

    DF_Rows = DF.shape[0]
    DF_Cols = DF.shape[1]


    Counting_Dict = {}

    for col in range(0, DF_Cols+1):

        Counting_Dict[col] = 0


    for row in range(0, DF_Rows):

        Data = DF.iloc[row, :]
        count = Data.isna().sum()

        Counting_Dict[count] = Counting_Dict[count] + 1


    Counting_Dict.pop(0)

    Index = list(Counting_Dict.keys())
    Values_Absolute = list(Counting_Dict.values())

    Values_Percentage = []

    for Value_Abs in Values_Absolute:

        Value = np.round((Value_Abs/DF_Rows)*100, decimals= 2)
        Values_Percentage.append(Value)
        


    # Plotting

    bin_width = 0.8
    width = kwargs.get("width")

    if(width != None):
        bin_width = width


    bin_color = "darkred"
    color = kwargs.get("color")

    if(color != None):
        bin_color = color


    y_size = 8
    x_size = 11.28

    figratio = kwargs.get("figratio")

    if(figratio != None):

        if(figratio == "wide"):
            ratio = 1.7778

        if(figratio == "A4"):
            ratio = 1.4095


        x_size = np.round(y_size * Ratio, decimals= 2)


    fig, ax1 = plt.subplots(figsize= (x_size, y_size))

    fig.suptitle(Title, fontsize= 16)

    ax1.bar(Index, Values_Absolute, width= bin_width, bottom= 0,
            color= bin_color, edgecolor= "black", zorder= 5)

    ax2 = ax1.twinx()
    ax2.bar(Index, Values_Percentage, width= bin_width, bottom= 0,
            color= bin_color, edgecolor= "black", zorder= 4)


    ax1.set_xlabel("Number of Missing Data by ROW", loc= "center")
    ax1.set_xticks(Index)

    ax1.set_ylabel("Null Count (Qty)", loc= "top")
    ax2.set_ylabel("Null Pct (%)", loc= "top")

    ax1.grid(axis= "y", color= "lightgrey", linestyle= "--", linewidth= 0.5,
             zorder= 3)


    plt.tight_layout()


    savefig = kwargs.get("savefig")

    if(savefig == True):
        plt.savefig(Title, dpi= 240)
        
    
    plt.show()

    
