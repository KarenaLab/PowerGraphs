# HeatMap for Correlation

def HeatMapSquare(Title, Data, **kwargs):

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    # Versions ----------------------------------------------------------

    # 01 - 31st Jan 2021 - Starter
    # 02 - 31st Jan 2021 - Removing Duplicated Info
    # 03 - 03rd Feb 2021 - Adjusting size for printing (A4 Ratio)
    # 04 - 16th Feb 2021 - Adding **kwargs
    # 05 - 21th Apr 2021 - Simplifying Data entry for just Data, removing
    #                      Columns (Labels) info
    # 06 - 


    # List of Variables and kwargs --------------------------------------
    # Title = string
    # Data = Array (Numpy Format)

    # figratio = wide* or A4
    # savefig = False* or True
    # cmap = coolwarm (using Matplotlib color standards)
    # aspect = Relation Axis X / Axis Y. Standard = 0.625
    


    # Program -----------------------------------------------------------

    # Data Processing

    Columns = Data.columns
    Data = np.around(Data.corr().values, decimals= 2)
    

    Text = f"{Title} - Correlation HeatMap"
    Ticks = len(Columns)


    # Removing Duplicated Data
    
    for i in range(len(Columns)):

        for j in range(len(Columns)):

            if(i < j):
                Data[i, j] = 0
    

    # Crating Figure

    y_size = 8
    ratio = 1.4095
    
    figratio = kwargs.get("figratio")
    
    if figratio:

        if(figratio == "A4"):
            ratio = 1.4095

        if(figratio == "wide"):
            ratio = 1.7778


    x_size = round(y_size*ratio, ndigits= 2)
            

    fig = plt.figure(figsize= (x_size, y_size))
    ax = fig.add_subplot()


    colormap = kwargs.get("cmap")

    if(colormap == None):
        colormap = "coolwarm"
        

    aspect = kwargs.get("aspect")

    if(aspect == None):
        aspect = 0.625        


    im = ax.imshow(Data, cmap= colormap, aspect= aspect)

    fig.suptitle(Text, fontsize= 16)

    ax.set_xticks(np.arange(start= 0, stop= Ticks))
    ax.set_yticks(np.arange(start= 0, stop= Ticks))

    ax.set_xticklabels(Columns, rotation= 90)
    ax.set_yticklabels(Columns, rotation= 0)


    # Loop over data dimensions to create text annotations

    for i in range(len(Columns)):

        for j in range(len(Columns)):

            if(i >= j):

                text = ax.text(j, i, Data[i, j],
                               ha= "center", va= "center", color= "white",
                               fontsize= 10)


    # Printing

    fig.tight_layout()

    savefig = kwargs.get("savefig")

    if (savefig == True):
        plt.savefig(Text, dpi= 240)


    plt.show()
    
            

    




