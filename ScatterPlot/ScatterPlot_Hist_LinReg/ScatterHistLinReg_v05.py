# Scatter Plot with Histogram, Linear Regression and Error

def ScatterHistLinReg(Title, Data_x, Data_y, **kwargs):

    import numpy as np
    import pandas as pd

    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    
    from sklearn.linear_model import LinearRegression
    import sklearn.metrics as metrics
    

    # Versions ---------------------------------------------------------

    # 01 - 01st Feb 2021 - Starter
    # 02 - 03rd Feb 2021 - Adjusting print size for A4 Ratio, Adjusting
    #      Error Graph Position and adding MSE Error
    # 03 - 23rd Feb 2021 - Adding **kwargs
    # 04 - 06th Jun 2021 - Adjusting features
    # 05 - 30th Jul 2021 - Adding QQ Plot
    # 06 - 


    # List of Variables and kwargs -------------------------------------

    # Title = Figure Title and filename (string)
    # Data_X = Information with column name as label (pandas)
    # Data_Y = Information with column name as label (pandas)
    # 

    # roundsize = 4* or any integer number
    # figratio = A4* or wide
    # savefig = False* or True
    #

    
    # Program ----------------------------------------------------------

    DF_x = Data_x.to_frame()
    DF_y = Data_y.to_frame()

    x_label = Data_x.name
    y_label = Data_y.name

    x_nan = Data_x.isna().sum()
    y_nan = Data_y.isna().sum()

    DF = pd.concat([DF_x, DF_y], axis= 1)
    DF_size = DF.shape[0]

    DF = DF.dropna()
    lines_removed = DF_size - DF.shape[0]

    # Updating size information

    size = DF.shape[0]
    Data_x = DF[x_label].values
    Data_y = DF[y_label].values


    # Linear Regression Model (Scikit Learn)
    
    model = LinearRegression(fit_intercept= True, normalize= True)
    model.fit(Data_x.reshape(Data_x.shape + (1,)), Data_y)
    
    x_min = np.amin(Data_x)
    x_max = np.amax(Data_x)

    xfit = np.linspace(start= x_min, stop= x_max, num= size)
    yhat = model.predict(xfit.reshape([size, 1]))


    roundsize = kwargs.get("roundsize")

    if(roundsize == None):
        roundsize = 4
    

    Beta_0 = round(model.coef_[0], roundsize)
    
    Sign_0 = "+"

    if(Beta_0 < 0):
        Sign_0 = "-"


    Beta_1 = round(model.intercept_, roundsize)

    Sign_1 = ""

    if(Beta_1 < 0):
        Sign_1 = "-"    
    

    MSE = round(metrics.mean_squared_error(y_true= Data_y, y_pred= yhat), ndigits= roundsize)
    MAE = round(metrics.mean_absolute_error(y_true= Data_y, y_pred= yhat), ndigits= roundsize)
    R2 = round(metrics.r2_score(y_true = Data_y, y_pred= yhat), ndigits= roundsize)

    Error_y = Data_y - yhat

    CorrMatrix = np.corrcoef(Data_x, Data_y)
    Corr = round(CorrMatrix[0,1], ndigits= roundsize)
    

    Equation_Text = f"y_hat: {Sign_1}{abs(Beta_1)} {Sign_0} {abs(Beta_0)}*x"
    Error_Text = f"Error: MSE: {MSE}; MAE: {MAE}; R^2: {R2}"
    Corr_Text = f"Correlation: {Corr}"
    NaN_Text = f"Lines Removed: {lines_removed} (NaN= x: {x_nan}; y: {y_nan})" 


    # Plotting

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

    gs = fig.add_gridspec(ncols= 3, nrows= 3,
                          width_ratios= (2, 1, 1), height_ratios= (1, 2, 1),
                          left= 0.1, right= 0.9, bottom= 0.1, top= 0.9,
                          wspace= 0.2, hspace= 0.2)


    # Creating Plotting
    ax0 = fig.add_subplot(gs[1, 0:2])                 # Main Plot
    ax1 = fig.add_subplot(gs[0, 0:2], sharex = ax0)   # Histogram X
    ax2 = fig.add_subplot(gs[1, 2], sharey = ax0)     # Histogram Y
    ax3 = fig.add_subplot(gs[2, 2])                   # Error (y - yhat)
    ax4 = fig.add_subplot(gs[2, 1])                   # QQ Plot (?)
    ax5 = fig.add_subplot(gs[2, 0])                   # LinReg Info



    # Setting/Adjusting Visual Paramenters

    fig.suptitle(Title, fontsize= 16)
 
    Grid_Color = "darkgrey"
    Grid_Linestyle = "--"
    Grid_Linewidth = 0.5

    ax0.grid(color= Grid_Color, linestyle= Grid_Linestyle, linewidth= Grid_Linewidth)
    ax0.set_axisbelow(True)

    ax1.grid(color= Grid_Color, linestyle= Grid_Linestyle, linewidth= Grid_Linewidth)
    ax1.set_axisbelow(True)
    ax1.tick_params(axis= "x", labelbottom= False)

    ax2.grid(color= Grid_Color, linestyle= Grid_Linestyle, linewidth= Grid_Linewidth)
    ax2.set_axisbelow(True)
    ax2.tick_params(axis= "y", labelleft= False)

    ax3.grid(color= Grid_Color, linestyle= Grid_Linestyle, linewidth= Grid_Linewidth)
    ax3.set_axisbelow(True)

    ax4.grid(color= Grid_Color, linestyle= Grid_Linestyle, linewidth= Grid_Linewidth)
    ax4.set_axisbelow(True)
    

    # Graph 0 = Scatter with Predict Line
    ax0.scatter(Data_x, Data_y, alpha= 0.5, color= "navy", edgecolor= "white")
    ax0.set_xlabel(x_label, fontweight= "bold")
    ax0.set_ylabel(y_label, fontweight= "bold")

    ax0.plot(xfit, yhat, color= "darkred", linewidth= 1)


    # Graph 1 = Histogram of X
    Data_Size = Data_x.size
    bins_x = int((Data_Size**(1/2)) + 0.5)

    ax1.hist(x= Data_x, bins= bins_x, color= "navy", orientation= "vertical")
    ax1.set_ylabel("count")
      

    # Graph 2 = Histogram of Y
    Data_Size = Data_y.size
    bins_y = int((Data_Size**(1/2)) + 0.5)

    ax2.hist(x= Data_y, bins= bins_y, color= "navy", orientation= "horizontal")
    ax2.xaxis.tick_top()
    ax2.xaxis.set_label_position("top")
    ax2.set_xlabel("count")
    
    # Graph 3 = Histogram of Error

    bins = int(len(Error_y)**(1/2))
    ax3.hist(x= Error_y, bins= bins, color= "darkred", orientation= "vertical")
    ax3.set_xlabel("Error")
    


    # Graph 4 = QQ Plot

    ax4.set_xlabel("QQ Plot")
    ax4.axis(False)
    


    # Graph 5 = Linear Regression Information

    ax5.axis(False)

    ax5.text(x= 0.00, y= 0.60, s= Equation_Text)
    ax5.text(x= 0.00, y= 0.40, s= Error_Text)
    ax5.text(x= 0.00, y= 0.20, s= Corr_Text)
    ax5.text(x= 0.00, y= 0.00, s= NaN_Text)



    # Plotting (Out)

    savefig = kwargs.get("savefig")

    if (savefig == True):
        plt.savefig(Title, dpi= 240)


    plt.show()
       


    
    
    
