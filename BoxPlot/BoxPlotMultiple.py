# BoxPlotMultiple

def BoxPlotMultiple(DF, title, normalize=False, meanline=True, notch=True, **kwargs):

    import numpy as np
    import pandas as pd

    from pandas.api.types import is_numeric_dtype, is_string_dtype

    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec


    # Versions ---------------------------------------------------------

    # 01 - Sep 02nd, 2021 - Launch Edition
    # 02 - May 31st, 2022 - Adjusting


    # List of Variables and kwargs -------------------------------------

    # Title = Name of the Plot (string)
    # Data = Dataframe to be analized (pandas)
    #

    # CatNumeric = Trigger for Numeric Categoric or Sample
    #              default= 5
    # Normalize = False* or True



    # Program ----------------------------------------------------------

    # kwargs reading    
    catnum = 5
    catnumeric = kwargs.get("catnumeric")
    if catnumeric:
        catnum = catnumeric

    # Removing Categoric (text) columns   
    cols_numeric = []
    for col in DF.columns:
        unique = DF[col].nunique()
        if(is_numeric_dtype(DF[col]) == True and unique >= catnum):
            cols_numeric.append(col)

    DF = DF[cols_numeric]


    # Normalization = Min-Max or Standard Score
    # https://en.wikipedia.org/wiki/Normalization_(statistics)
    if(normalize == "MinMax" or normalize == "Min-Max"):
        data = DF.copy()
        for col in DF.columns:
            data_min, data_max = data[col].min(), data[col].max()
            data[col] = data[col].apply(lambda x: ((x-data_min)/(data_max-data_min)))

        DF = data.copy()
        
    if(normalize == "StandardScore" or normalize == "StandScore"):
        data = DF.copy()
        for col in DF.columns:
            data_mean, data_stddev = data[col].mean(), data[col].std()
            data[col] = data[col].apply(lambda x: ((x-data_mean)/data_stddev))

        DF = data.copy()


    # Removing NaNs for ploting
    data_list = []
    for col in DF.columns:
        data = DF[col].dropna().to_list()
        data_list.append(data)


    # Ploting
    x_size, y_size = 11.28, 8
    figratio = kwargs.get("figratio")

    if figratio:
        if(figratio == "wide"):
            ratio = 1.7778

        if(figratio == "A4"):
            ratio = 1.4095

        x_size = np.round(y_size*ratio, decimals=2)


    fig = plt.subplots(figsize=(x_size, y_size))
    plt.suptitle(title, fontsize=12)

    flierprops = dict(marker='o', markerfacecolor='red', markersize=4)
    plt.boxplot(data_list, labels=DF.columns, notch=notch, flierprops=flierprops, zorder=20)
    plt.grid(axis="y", color="lightgrey", linestyle="--", linewidth=0.5)



    if(normalize == "MinMax" or normalize == "Min-Max"):
        plt.axhline(y=0, color="black", linestyle="--", linewidth=0.5, zorder=11)
        plt.axhline(y=1, color="black", linestyle="--", linewidth=0.5, zorder=12)

    if(normalize == "StandardScore" or normalize == "StandScore"):
        plt.axhline(y=0, color="black", linestyle="--", linewidth=0.5, zorder=11)
    

    plt.show()
            

            

                
            
        


    

    

            

        

        

        
    
