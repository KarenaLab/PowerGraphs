
def RadarChart(Title, Data, **kwargs):

    # Versions ----------------------------------------------------------

    # 01 - 02nd Jun 2021 - Initital
    # 02 -


    # List of Variables and kwargs --------------------------------------

    # Title = Figure Title and filename (string)
    # Data = Information to be used (Array)

    # figratio = Square*, A4 or Wide
    # savefig = False* or True
    # fade = 0.15 or any number between [0, 1]
    # legendloc = "lower right"
    # legendalplha = 1 or any number between [0, 1]    


    # Libraries ---------------------------------------------------------

    import numpy as np
    import pandas as pd

    import matplotlib.pyplot as plt


    # Program -----------------------------------------------------------

    # Kwargs and Setup
    
    y_size = 6
    x_size = 6

    figratio = kwargs.get("figratio")
    if figratio:

        if(figratio == "square"):
            ratio = 1

        if(figratio == "wide"):
            ratio = 1.7778

        if(figratio == "A4"):
            ratio = 1.4095

        x_size = round(y_size * ratio, ndigits= 2)


    savefig = kwargs.get("savefig")


    fade = 0.15

    faderate = kwargs.get("fade")
    if faderate:

        fade = faderate


    legendloc = "lower right"

    legendlocation = kwargs.get("legendloc")
    if legendlocation:

        legendloc = legendlocation


    legendalpha = 1

    legendalpharate = kwargs.get("legendalpha")
    if legendalpha:

        legendalpha = legendalpharate



    # Data

    Cat_Name = Data.columns.values
    
    Data_Rows = Data.shape[0]
    Data_Cols = Data.shape[1]
    

    Angles = [n/float(Data_Cols) * 2 * np.pi for n in range(Data_Cols)]

    Angles.append(Angles[0])
    # Closing the plotting (end = start)
      

    # Figure
    
    fig = plt.figure(figsize= (x_size, y_size))

    # Graph Adjusts

    ax0 = fig.add_subplot(polar= True)      # Radar Chart
    
    fig.suptitle(Title, fontsize= 16)

    ax0.set_theta_offset(np.pi/2)           # First axis = Upper
    ax0.set_theta_direction(-1)             # Rotation = Clockwise

    plt.xticks(Angles[ :-1], Cat_Name)
    ax0.set_rlabel_position(360/(2*Data_Cols))


    # Plotting

    i = 0
    Four_Colors = ["darkred", "navy", "orange", "darkgreen"]
        
    while(i < Data_Rows):

        Label = Data.index[i]
        Color = Four_Colors[i]

        Values = Data.iloc[i].values.tolist()
        Values.append(Values[0])
        # Closing the plotting (end = start)

        ax0.plot(Angles, Values, label= Label, color= Color, linewidth= 1)
        ax0.fill(Angles, Values, color= Color, alpha= fade)

        i = i+1


    plt.legend(loc= legendloc, facecolor= "white", framealpha= legendalpha)


    # Ploting

    plt.tight_layout()

    if(savefig == True):
        plt.savefig(Title, dpi= 240)

    
    plt.show()
    
