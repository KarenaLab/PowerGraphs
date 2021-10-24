
def MissingDataCol(Title, DF, **kwargs):

    # Versions ----------------------------------------------------------
    # 01 - Dec 27th, 2020 - Starter
    # 02 - Feb 08th, 2021 - Adjusting printing area for A4 format
    # 03 - Apr 21st, 2021 - Adding **kwargs
    # 04 - Apr 22rd, 2021 - Changing Data acquisition (Pandas Based)
    # 05 - May 30th, 2021 - Adding is_numeric and is_string selection
    #                       Adding Secondary Y Axis (Percentage of)
    # 06 - May 31st, 2021 - Adding color option
    # 07 - Oct 14th, 2021 - Adding edgecolor = black
    # 08 - Oct 17th, 2021 - *** Changing Name = MissingDataCol ***
    # 09 - 


    # Libraries ---------------------------------------------------------

    import numpy as np
    import pandas as pd

    from pandas.api.types import is_string_dtype
    from pandas.api.types import is_numeric_dtype
    
    import matplotlib.pyplot as plt

    

    # List of Variables and **kwargs ------------------------------------

    # Title = Figure Title and filename (string)
    # Data = Information to be used (Pandas Array)

    # figratio = A4*, Wide or Square
    # savefig = False* or True
    # show = True* or False
    # width = 0.8* or any number
    # color = darkred* or any color from Matplotlib

    # * = Standard selection if not called    


    # Program -----------------------------------------------------------

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

    fig.suptitle(Title, fontsize= 16)
    
    ax1.bar(DF_columns, DF_Nulls, width= bin_width, bottom= 0,
            color= bin_color, edgecolor= "black")

    # ax2 = Second plot for Secondary axis (%)
    ax2 = ax1.twinx()
    ax2.bar(DF_columns, DF_Percentage, width= bin_width, bottom= 0,
            color= bin_color, edgecolor= "black")
    
  
    ax1.set_ylabel("Null Count (Qty)", loc= "top")
    ax2.set_ylabel("Null Pct (%)", loc= "top")

    ax1.yaxis.grid(color= "lightgrey", linestyle= "--", linewidth= 0.5)
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

