
def HistBoxInfoNormal(title, data, decimals=4, **kwargs):
    """
    Plots an Histogram and a BoxPlot with Gauss Curve stats.

    * title = Title for plot AND its filename if asked to save it,
    * data = Information to analise. (Pandas, Numpy or List),

    * decimals = Number of decimals to be shown at report (default=4),

    kwargs:
    * bins = Binning calc format (sqrt*, sturges or an integer),
    * figratio = Figure ratio to show/plot (wide*, A4 or Square),
    * savefig = Save the figure as .png (False* or True),
    * showfig = Show (or not) the figure created (True* or False),

    """
    
    # Versions ---------------------------------------------------------
    
    # 01 - Dec 09th, 2020 - Initial,
    # 02 - Dec 10th, 2020 - Correcting Whiskers (Adding Calculation),
    #                       Automatic figure saving with Full HD size (1920x1080 px),
    # 03 - Dec 11th, 2020 - Adding a Vertical line in Histogram for Mean,
    #                       Correcting 1o Quantile Error label in Describe,
    # 04 - Dec 11th, 2020 - Adjusting Mean and Median line colors,
    # 05 -                  Creating two versions: (1) Box Plot and (2) Normal Curve Info,
    # 06 - Jan 03rd, 2021 - Adjusting Texts when Division Denominator is Zero (Infinite Error),
    # 07 - Feb 03rd, 2021 - Adjusting the printing ratio for A4 Page
    # 08 - Apr 06th, 2021 - Adding **kwargs
    # 09 - Apr 14th, 2021 - Adding Median to InfoBox
    # 10 - Apr 15th, 2021 - Adding a Normal Curve
    # 11 - Apr 21st, 2021 - Adding a **kwargs (Plot Selection)
    # 12 - Apr 22rd, 2021 - Adding bin control
    # 13 - Jul 22th, 2021 - Adjusting positions of labels
    # 14 - Aug 27th, 2021 - Adjusting Barplot (color and edges)
    # 15 - Sep 01st, 2021 - Changing position of BoxPlot (horizontal)
    # 16 - Sep 19th, 2021 - Adjusting linestyle of Mean
    # 17 - Oct 11th, 2021 - Adding Binning options (sqrt, sturges or an int),
    # 18 - Apr 21st, 2022 - Adjusting data entry (pandas, numpy or list),
    #                       Adding bins color and edge kwargs,
    # 19 -


    # Insights:
    # Add a Gauss Curve shape line or shadow
    # Fit axis lines to standard deviation gaps


    # Libraries --------------------------------------------------------

    import numpy as np
    import pandas as pd
    import scipy.stats as stats
    
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec


    # Program ----------------------------------------------------------    

    # kwargs preparation
    bins_method = kwargs.get("bins")
    if(bins_method == None): bins_method = "sqrt"


    x_size, y_size = 8, 4.5
    figratio = kwargs.get("figratio")
    if figratio:
        if(figratio == "A4"): ratio = 1.4095
        if(figratio == "wide"): ratio = 1.7778
        if(figratio == "square"): ratio = 1

        x_size = np.round((y_size * ratio), decimals=2)


    fsize = 10
    fontsize = kwargs.get("fontsize")
    if fontsize: fsize = fontsize


    bin_color = "darkblue"
    if kwargs.get("color"):
        bin_color = color


    bin_edge = "white"
    if kwargs.get("edgecolor"):
        bin_edge = edgecolor
    

    savefig = kwargs.get("savefig")
    showfig = kwargs.get("showfig")


    # Data Processing: Using data as NUMPY Array
    if(isinstance(data, list) == True):
        data = np.array(data)

    if(isinstance(data, pd.Series) == True):
        data = data.values


    # Removing NaNs for processing
    data_clean = data[np.logical_not(np.isnan(data))]
    data_nan = np.isnan(data).sum()


    # Calculating Bins Size
    data_size = data_clean.size
    if(bins_method == "sqrt"):
        no_bins = int((data_size**(1/2)) + 0.5)

    if(bins_method == "sturges"):
        no_bins = int((np.log2(data_size) + 1) + 0.5)

    # Number of bins always as an ODD number = Histogram is symetrical
    if(data_size >= 500 and no_bins%2 == 0):
        no_bins = no_bins - 1
        

    if(type(bins_method) == int):
        no_bins = bins_method
    

    # Plotting        
    fig = plt.figure(figsize=(x_size, y_size)) 
    grd = gridspec.GridSpec(nrows=2, ncols=2,
                            width_ratios= [7, 3], height_ratios= [8, 2]) 

    ax0 = plt.subplot(grd[0, 0])                 # Main = Histogram
    ax1 = plt.subplot(grd[1, 0], sharex= ax0)    # Lower = Boxplot
    ax2 = plt.subplot(grd[:, 1])                 # Text (Information)


    fig.suptitle(title, fontsize=fsize+2)
    
    # Histogram (ax0)
    n, bins, _ = ax0.hist(x=data_clean, bins=no_bins,
                                color=bin_color, edgecolor=bin_edge, zorder=20)

    #    bins = Central Value of the bin
    #       n = Quantity of items inside the bin
    # patches = _ = Color information (Internal Variable)

    mean = np.round(np.mean(data_clean), decimals=decimals)
    stddev = np.round(np.std(data_clean), decimals=decimals)
    median = np.round(np.median(data_clean), decimals=decimals)

    # Adding a Gauss Curve Shape (or shadow):    
    # y = ((1/(np.sqrt(2*np.pi)*StdDev)) * np.exp(-0.5*(1/StdDev*(bins-Mean))**2))
    # Curve = y * 1000
    # ax0.plot(bins, Curve, color= "red", linestyle= "--", linewidth= 0.75)

    ax0.grid(color="lightgrey", linestyle="--", linewidth=0.5)
    ax0.set_axisbelow(True)

    ax0.axvline(x=mean, color="green", linestyle="--", linewidth=1, label="Mean", zorder=11)
    ax0.axvline(x=median, color="orange", linewidth=1, label="median", zorder=12)


    # BoxPlot (ax1)
     
    red_bullet = dict(markerfacecolor="r")
    ax1.boxplot(x=data_clean, vert=False, widths=0.5,
                showmeans=True, meanline=True, flierprops=red_bullet)
    ax1.xaxis.grid(color="lightgrey", linestyle="--", linewidth=0.5)

    ax1.set_axisbelow(True)
    ax1.set_yticks([])


    # Info
    no_items = data.size
    no_items_string = f"No. Items = {str(no_items)}"

    no_nan = data_nan
    pct_nan = np.round((data_nan/data_size) * 100, decimals=3)
    nan_string = f"NaN = {str(no_nan)} ({str(pct_nan)}%)"

    mean = np.round(np.mean(data_clean), decimals=decimals)
    mean_string = f"Mean = {str(mean)}"

    median = np.round(np.median(data_clean), decimals=decimals)
    median_string = f"Median = {str(median)}"

    stddev = np.round(np.std(data_clean), decimals=decimals)
    stddev_string = f"StdDev = {str(stddev)}"

    data_min = np.round(np.amin(data_clean), decimals=decimals)
    min_string = f"Min = {str(data_min)}"

    data_max = np.round(np.amax(data_clean), decimals=decimals)
    max_string = f"Max = {str(data_max)}"

    data_range = np.round((data_max - data_min), decimals=decimals)
    range_string = f"Range = {str(data_range)}"


    lower_limit = np.round((mean - 3*stddev), decimals=decimals)
    lower_limit_string = f"Lower Limit = {str(lower_limit)}"

    upper_limit = np.round(mean + 3*stddev, decimals=decimals)
    upper_limit_string = f"Upper Limit = {str(upper_limit)}"

    no_outside = np.sum(data_clean < lower_limit) + np.sum(data_clean > upper_limit)
    pct_outside = np.round((no_outside/data_clean.size)*100, decimals=3)
    outside_string = f"Outside = {str(no_outside)}; {str(pct_outside)}%"

    no_inside = data_clean.size - no_outside
    pct_inside = np.round((no_inside/data_clean.size)*100, decimals=3)
    inside_string = f"Inside = {str(no_inside)}; {str(pct_inside)}%"

    if(no_outside > 0):
        outside_upper = np.sum(data_clean > upper_limit)
        outside_upper_pct = np.round((outside_upper/no_outside)*100, decimals=1)

        outside_lower = np.sum(data_clean < lower_limit)
        outside_lower_pct = np.round((outside_lower/no_outside)*100, decimals=1)

    else:
        outside_upper = 0
        outside_upper_pct = 0

        outside_lower = 0
        outside_lower_pct = 0


    outside_upper_string = f"Outside Upper = {str(outside_upper)}; {str(outside_upper_pct)}%"
    outside_lower_string = f"Outside Lower = {str(outside_lower)}; {str(outside_lower_pct)}%"

   
    # 3.2 - Information Plotting

    ax2.axis(False)

    # X Position
    x_left, x_left_tab_one = 0.05, 0.15

    y_start = 0.98
    y_step = 0.04
    y_tab = y_step * 1.5


    def new_step(start, step):
        new_step = start - step

        return new_step



    # Y Position

    y_pos = y_start
    
    plt.text(x=x_left, y=y_pos, s=no_items_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_step)

    plt.text(x=x_left_tab_one, y=y_pos, s=nan_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_tab)


    plt.text(x=x_left, y=y_pos, s=mean_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_step)
    
    plt.text(x=x_left, y=y_pos, s=median_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_step)
    
    plt.text(x=x_left, y=y_pos, s=stddev_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_step)

    plt.text(x=x_left, y=y_pos, s=min_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_step)

    plt.text(x=x_left, y=y_pos, s=max_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_step)

    plt.text(x=x_left, y=y_pos, s=range_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_tab)

    
    plt.text(x=x_left, y=y_pos, s=lower_limit_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_step)
        
    plt.text(x=x_left, y=y_pos, s=upper_limit_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_tab)


    plt.text(x=x_left, y=y_pos, s=inside_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_step)
    
    plt.text(x=x_left, y=y_pos, s=outside_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_step)
    
    plt.text(x=x_left_tab_one, y=y_pos, s=outside_lower_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_step)
    
    plt.text(x=x_left_tab_one, y=y_pos, s=outside_upper_string, fontsize=fsize-2)
    y_pos = new_step(y_pos, y_step)


    # 4 - Plotting
    fig.tight_layout()

    if(savefig == True):
        plt.savefig(title, dpi=240)
        print(f" > saving figure: {title}.png")

    if(showfig == False):
        plt.close()

    else:
        plt.show()

    

