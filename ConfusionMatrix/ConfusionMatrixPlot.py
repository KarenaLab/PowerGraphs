
def ConfusionMatrixPlot(Title, Data, **kwargs):

    # Versions ---------------------------------------------------------

    # 01 - 01st June 2021 - Initial
    # 02 - 02nd June 2021 - Separating into two projects
    # 03 -


    # List of Variables and kwargs -------------------------------------

    # Title = Figure Title and filename (string)
    # Data = Information to be used (NumPy Array)

    # figratio = Square*, A4 or Wide
    # savefig = False* or True
    # cmap = blues* or any matplotlib option
    #

    
    # Libraries --------------------------------------------------------
    
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec


    # Program ----------------------------------------------------------

    Label = ["True", "False"]

    TP = Data[0, 0]
    FP = Data[0, 1]
    FN = Data[1, 0]
    TN = Data[1, 1]
        

    # kwargs setup

    y_size = 8
    x_size = 8

    figratio = kwargs.get("figratio")
    if figratio:

        if(figratio == "square"):
            ratio = 1

        if(figratio == "wide"):
            ratio = 1.7778

        if(figratio == "A4"):
            ratio = 1.4095

        x_size = round(y_size * ratio, ndigits= 2)


    colormap = "Blues"
    Change_CMap = kwargs.get("cmap")

    if Change_CMap:
        colormap = Change_CMap


    savefig = kwargs.get("savefig")
    

    # Figure
    
    fig = plt.figure(figsize= (x_size, y_size))

    # Creating Subplots

    ax0 = fig.add_subplot()     # Confusion Matrix

    fig.suptitle(Title, fontsize= 16)

    # ax0 = Confusion Matrix
    
    ax0.imshow(Data, cmap= colormap)
    ax0.set_xticks([0, 1])
    ax0.set_xticklabels(Label)
    ax0.set_title("Predicted", fontsize= 10)
    ax0.xaxis.tick_top()

    ax0.set_yticks([0, 1])
    ax0.set_yticklabels(Label, rotation= 90, va= "center")
    ax0.set_ylabel("Observed")


    # Anotations on Graph
    
    i = 0
    Trigger = (np.amax(Data)-np.amin(Data)) * 0.35 
    
    while(i < 2):

        j = 0
        while(j < 2):

            Number = Data[i, j]

            if(Number >= Trigger):
                textcolor = "white"

            else:
                textcolor = "black"


            ax0.text(j, i, Number, ha= "center", va= "center",
                     size= 16, weight= "bold", color= textcolor)

            j = j+1

        i = i+1



    
    # Ploting

    plt.tight_layout()

    if(savefig == True):
        plt.savefig(Title, dpi= 240)

    
    plt.show()


    
    
        


    
    
