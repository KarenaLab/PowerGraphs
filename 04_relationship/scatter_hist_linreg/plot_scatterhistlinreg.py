# Scatter Plot with Histogram, Linear Regression and Error [P288] ------

# Libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics


def ScatterHistLinReg(title, data_x, data_y, decimals=4, **kwargs):
    """
    Module to plot a Scatter Plot with respective Histograms, Error
    distribution, QQ-Plot and some metrics.

    Variables and **kwargs:
    * title = Figure title and filename (string)
    * data_x = Information with column name as label (pandas)
    * data_y = Information with column name as label (pandas)
    * decimals = number of decimals (standard=4) 

    * figratio = A4* or wide
    * savefig = False* or True
    * showfig = True* or False
    * markeralpha = 0.5* or any number between 0 and 1
    * whiteedge = True* or False
    
    """
    # Getting **kwargs
    markeralpha = kwargs.get("markeralpha")
    if(markeralpha == None):
        markeralpha = 0.5

    else:
        if(markeralpha < 0 or markeralpha > 1):
            markeralpha = 0.5


    markeredge = "white"
    whiteedge = kwargs.get("whiteedge")

    if(whiteedge == False):
        markeredge = None


    # Calculating (Improve it)
    DF_x = data_x.to_frame()
    DF_y = data_y.to_frame()

    x_label = data_x.name
    y_label = data_y.name

    x_nan = data_x.isna().sum()
    y_nan = data_y.isna().sum()

    DF = pd.concat([DF_x, DF_y], axis=1)
    DF_size = DF.shape[0]

    DF = DF.dropna()
    lines_removed = DF_size - DF.shape[0]


    # Updating size information
    size = DF.shape[0]
    Data_x = DF[x_label].values
    Data_y = DF[y_label].values


    # Linear Regression Model (Scikit Learn)   
    model = LinearRegression(fit_intercept= True)
    model.fit(Data_x.reshape(Data_x.shape + (1,)), Data_y)
    
    x_min, x_max = np.amin(data_x), np.amax(data_x)

    xfit = np.linspace(start=x_min, stop=x_max, num=size)
    yhat = model.predict(xfit.reshape([size, 1]))

    Beta_0 = np.round(model.coef_[0], decimals=decimals)
    
    Sign_0 = "+"
    if(Beta_0 < 0): Sign_0 = "-"

    Beta_1 = np.round(model.intercept_, decimals=decimals)

    Sign_1 = ""
    if(Beta_1 < 0): Sign_1 = "-"    
    
    # Metrics
    MSE = np.round(metrics.mean_squared_error(y_true=data_y, y_pred=yhat), decimals=decimals)
    MAE = np.round(metrics.mean_absolute_error(y_true=data_y, y_pred=yhat), decimals=decimals)
    R2 = np.round(metrics.r2_score(y_true =data_y, y_pred=yhat), decimals=decimals)

    error_y = data_y - yhat

    corrmatrix = np.corrcoef(Data_x, Data_y)
    corr = np.round(corrmatrix[0,1], decimals=decimals)
    

    Equation_Text = f"y_hat: {Sign_1}{abs(Beta_1)} {Sign_0} {abs(Beta_0)}*x"
    Error_Text = f"Error: MSE: {MSE}; MAE: {MAE}; R^2: {R2}"
    Corr_Text = f"Correlation: {corr}"
    NaN_Text = f"Lines Removed: {lines_removed} (NaN= x: {x_nan}; y: {y_nan})" 


    # RC Params
    set_rcparams()
    

    # Plotting
    x_size, y_size = 11.28, 8

    figratio = kwargs.get("figratio")
    if figratio:
        if(figratio == "square"): ratio = 1
        if(figratio == "wide"): ratio = 1.7778
        if(figratio == "A4"): ratio = 1.4095

        x_size = round(y_size * ratio, ndigits= 2)


    fig = plt.figure(figsize= [x_size, y_size])
    gs = fig.add_gridspec(ncols=3, nrows=3,
                          width_ratios=(2, 1, 1), height_ratios=(1, 2, 1),
                          left=0.1, right=0.9, bottom=0.1, top=0.9,
                          wspace=0.2, hspace=0.2)


    # Creating Plotting
    ax0 = fig.add_subplot(gs[1, 0:2])                 # Main Plot
    ax1 = fig.add_subplot(gs[0, 0:2], sharex = ax0)   # Histogram X
    ax2 = fig.add_subplot(gs[1, 2], sharey = ax0)     # Histogram Y
    ax3 = fig.add_subplot(gs[2, 2])                   # Error (y - yhat)
    ax4 = fig.add_subplot(gs[2, 1])                   # QQ Plot (?)
    ax5 = fig.add_subplot(gs[2, 0])                   # LinReg Info


    # Setting/Adjusting Visual Paramenters
    fig.suptitle(title, fontsize= 16)
 
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
    ax0.scatter(Data_x, Data_y, color= "navy", 
                alpha= markeralpha, edgecolor= markeredge)
    
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
    bins = int(len(error_y)**(1/2))
    ax3.hist(x=error_y, bins=bins, color="darkred", orientation="vertical")
    ax3.yaxis.tick_right()
    ax3.set_xlabel("Error")

    # Graph 4 = QQ Plot
    ax4.set_xlabel("QQ Plot")
    ax4.plot([0,1], [0,1], color="darkred", linewidth=1)
    

    # Graph 5 = Linear Regression Information
    ax5.axis(False)

    ax5.text(x=0.00, y=0.60, s=Equation_Text)
    ax5.text(x=0.00, y=0.40, s=Error_Text)
    ax5.text(x=0.00, y=0.20, s=Corr_Text)
    ax5.text(x=0.00, y=0.00, s=NaN_Text)

    # Plotting (Out)
    savefig = kwargs.get("savefig")
    if(savefig == True):
        plt.savefig(title, dpi= 240)

    showfig = kwargs.get("showfig")
    if(showfig == False):
        plt.close()
    else:
        plt.show()


    return None


def set_rcparams():
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"
    plt.rcParams["xtick.major.size"] = 3.5
    plt.rcParams["ytick.major.size"] = 0

    return None
