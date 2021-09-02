
def MissingData(Title, Data, **kwargs):

    # Versions ----------------------------------------------------------
    # 1 - 27th Dec 2020 - Starter
    # 2 - 08th Feb 2021 - Adjusting printing area for A4 format
    # 3 - 21th Apr 2021 - Adding **kwargs
    # 4 - 21th Apr 2021 - Changing Data acquisition (Pandas Based)
    # 5 - 30th May 2021 - Adding is_numeric and is_string selection
    #                     Adding Secondary Y Axis (Percentage of)
    # 6 - 31st May 2021 - Adding color option
    # 7 - 


    # Libraries ---------------------------------------------------------

    import numpy as np
    import pandas as pd

    from pandas.api.types import is_string_dtype
    from pandas.api.types import is_numeric_dtype
    
    import matplotlib.pyplot as plt

    

    # List of Variables and kwargs --------------------------------------

    # Title = Figure Title and filename (string)
    # Data = Informatio to be used (Pandas Array)

    # figratio = A4*, Wide or Square
    # savefig = False* or True
    # show = True* or False
    # width = 0.8* or any number
    # color = darkred* or any color from Matplotlib

    # * = Standard selection if not called    


    # Program -----------------------------------------------------------

    DF = Data

    DF_rows = DF.shape[0]
    DF_cols = DF.shape[1]
    DF_columns = DF.columns.values

    # Data Analisys (Missing Data)
        
    col = 0
    DF_Nulls = []
    DF_Percentage = []

    while(col < DF_cols):

        get = DF_columns[col]
        Data = DF[get]

        if(is_numeric_dtype(Data) == True):

            Null = Data.isna().sum()
            

        if(is_string_dtype(Data) == True):

            Space = Data.str.isspace().sum()
            Empty = Data.str.count("NaN").sum() + Data.str.count("nan").sum()
            NaN = Data.isna().sum()
            
            Null = Space + Empty + NaN
            
      
        DF_Nulls.append(Null)
        DF_Percentage.append((Null/DF_rows)*100)

        col = col+1


    # Setting Graph
  
    bin_width = 0.8
    width = kwargs.get("width")

    if width:
        bin_width = width

    bin_color = "darkred"
    color = kwargs.get("color")

    if color:
        bin_color = color


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


    fig, ax1 = plt.subplots(figsize= (x_size, y_size))
    
    ax1.bar(DF_columns, DF_Nulls, width= bin_width, bottom= 0, color= bin_color)

    ax2 = ax1.twinx()
    ax2.bar(DF_columns, DF_Percentage, width= bin_width, bottom= 0, color= bin_color)
    
    fig.suptitle(Title, fontsize= 16)

    ax1.set_ylabel("Null Count (Qty)", loc= "top")
    ax2.set_ylabel("Null Pct (%)", loc= "top")

    ax1.yaxis.grid(color= "grey", linestyle= "--", linewidth= 0.5)
    ax1.set_axisbelow(True)

    plt.setp(ax1.get_xticklabels(), rotation= 90)
  

    # Plotting ----------------------------------------------------------    

    plt.tight_layout()


    savefig = kwargs.get("savefig")

    if(savefig == True):
        plt.savefig(Title, dpi= 240)


    show = kwargs.get("show")

    if(show != False):
        plt.show()


    # end ---------------------------------------------------------------
