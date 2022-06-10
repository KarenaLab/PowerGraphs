
def ConfusionMatrixInfo(title, data, showfig=True, **kwargs):

    # Versions ---------------------------------------------------------

    # 01 - 01st June 2021 - Initial
    # 02 - 02nd June 2021 - Separating into two projects
    # 03 - 02nd June 2021 - Adding Secundary Metrics by **kwargs
    # 04 -


    # List of Variables and kwargs -------------------------------------

    # Title = Figure Title and filename (string)
    # Data = Information to be used (NumPy Array)

    # figratio = A4*, Wide or Square
    # savefig = False* or True
    # cmap = blues* or any matplotlib option
    #

    
    # Libraries --------------------------------------------------------
    
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec


    # Program ----------------------------------------------------------
    label = ["True", "False"]

    TP = data[0, 0]
    FP = data[0, 1]
    FN = data[1, 0]
    TN = data[1, 1]
        

    # kwargs setup
    x_size, y_size = 11.28, 8

    figratio = kwargs.get("figratio")
    if figratio:

        if(figratio == "square"): ratio = 1
        if(figratio == "wide"): ratio = 1.7778
        if(figratio == "A4"): ratio = 1.4095

        x_size = np.round(y_size * ratio, decimals=2)


    colormap = "Blues"
    cmap = kwargs.get("cmap")
    if cmap: colormap = cmap


    savefig = kwargs.get("savefig")

    
    # Figure
    fig = plt.figure(figsize=[x_size, y_size])
    gs = fig.add_gridspec(ncols=2, nrows=1,width_ratios=[2, 1], 
                          left=0.1, right=0.9, bottom=0.1, top=0.85,
                          wspace=0.1, hspace=0.1)

    # Creating Subplots
    ax0 = fig.add_subplot(gs[0, 0])     # Confusion Matrix
    ax1 = fig.add_subplot(gs[0, 1])     # texts

    fig.suptitle(title, fontsize=12)

    # ax0 = Confusion Matrix
    
    ax0.imshow(data, cmap=colormap)
    ax0.set_xticks([0, 1])
    ax0.set_xticklabels(label)
    ax0.set_title("Predicted", fontsize=10)
    ax0.xaxis.tick_top()

    ax0.set_yticks([0, 1])
    ax0.set_yticklabels(label, rotation=90, va="center")
    ax0.set_ylabel("Observed")


    # Anotations on Graph   
    i = 0
    trigger = (np.amax(data)-np.amin(data))*0.35 
    
    while(i < 2):
        j = 0
        while(j < 2):
            number = data[i, j]

            if(number >= trigger):
                textcolor = "white"

            else:
                textcolor = "black"

            ax0.text(j, i, number, ha="center", va="center",
                     size=16, weight="bold", color=textcolor)

            j = j+1

        i = i+1


    # ax1 = Metrics
    
    ax1.axis(False)

    pos_x = 1.00
    pos_y = 0.96
    step = -0.04


    # Basic Info
    text_TP = f"TP (True Positive): {TP}"
    ax1.text(x=pos_x, y=pos_y, s=text_TP, ha="right")

    pos_y = pos_y + step
    text_FP = f"FP (False Positive): {FP}"
    ax1.text(x=pos_x, y=pos_y, s=text_FP, ha="right")

    pos_y = pos_y + step
    text_FN = f"FN (False Negative): {FN}"
    ax1.text(x=pos_x, y=pos_y, s=text_FN, ha="right")

    pos_y = pos_y + step
    text_TN = f"TN (True Negative): {TN}"
    ax1.text(x=pos_x, y=pos_y, s=text_TN, ha="right")


    # Main Metrics
    pos_y = pos_y + 2*step
    
    TPR = TP/(TP+FN)
    text_TPR = f"TPR = Recall = {TPR:1.5f}"
    ax1.text(x=pos_x, y=pos_y, s=text_TPR, ha="right")

    pos_y = pos_y + step
    TNR = TN/(TN+FP)
    text_TNR = f"TNR = Specificity = {TNR:1.5f}"
    ax1.text(x=pos_x, y=pos_y, s=text_TNR, ha="right")

    pos_y = pos_y + step
    PPV = TP/(TP+FP)
    text_PPV = f"PPV = Precision = {PPV:1.5f}"
    ax1.text(x=pos_x, y=pos_y, s=text_PPV, ha="right")

    pos_y = pos_y + step
    ACC = (TP+TN)/(TP+TN+FP+FN)
    text_ACC = f"ACC = Accuracy = {ACC:1.5f}"
    ax1.text(x=pos_x, y=pos_y, s=text_ACC, ha="right")    

    pos_y = pos_y + step
    F1S = (2*TP)/(2*TP+FP+FN)
    text_F1S = f"F1  = F1 Score = {F1S:1.5f}"
    ax1.text(x=pos_x, y=pos_y, s=text_F1S, ha="right")


    # Metrics called by kwargs
    pos_y = pos_y + step

    Calc_FNR = kwargs.get("FNR")
    if(Calc_FNR == True):
        pos_y = pos_y + step
        FNR = FN/(FN+TP)
        text_FNR = f"FNR = Miss Rate = {FNR:1.5f}"
        ax1.text(x=pos_x, y=pos_y, s=text_FNR, ha="right")


    Calc_NPV = kwargs.get("NPV")
    if(Calc_NPV == True):
        pos_y = pos_y + step
        NPV = TN/(TN+FN)
        text_NPV = f"NPV = Negative Predictive = {NPV:1.5f}"
        ax1.text(x=pos_x, y=pos_y, s=text_NPV, ha="right")


    Calc_FPR = kwargs.get("FPR")
    if(Calc_FPR == True):
        pos_y = pos_y + step
        FPR = FP/(FP+TN)
        text_FPR = f"FPR = Fall-Out = {FPR:1.5f}"
        ax1.text(x=pos_x, y=pos_y, s=text_FPR, ha="right")


    Calc_FDR = kwargs.get("FDR")
    if(Calc_FDR == True):
        pos_y = pos_y + step
        FDR = FP/(FP+TP)
        text_FDR = f"FDR = False Discovery = {FDR:1.5f}"
        ax1.text(x=pos_x, y=pos_y, s=text_FDR, ha="right")


    Calc_FOR = kwargs.get("FOR")
    if(Calc_FOR == True):
        pos_y = pos_y + step
        FOR = FN/(FN+TN)
        text_FOR = f"FOR = False Omission = {FOR:1.5f}"
        ax1.text(x=pos_x, y=pos_y, s= text_FOR, ha="right")


    Calc_CSI = kwargs.get("CSI")
    if(Calc_CSI == True):
        pos_y = pos_y + step
        CSI  = TP/(TP+FN+FP)
        text_CSI = f"CSI = Critical Success Index = {CSI:1.5f}"
        ax1.text(x=pos_x, y=pos_y, s=text_CSI, ha="right")


    Calc_MCC = kwargs.get("MCC")
    if(Calc_MCC == True):
        pos_y = pos_y + step
        MCC = (TP*TN - FP*FN)/((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))**(1/2)
        text_MCC = f"MCC = Matthews Correlation Coef = {MCC:1.5f}"
        ax1.text(x=pos_x, y=pos_y, s=text_MCC, ha="right")


    Calc_BA = kwargs.get("BA")
    if(Calc_BA == True):
        pos_y = pos_y + step
        BA = (TPR+TNR)/2
        text_BA = f"BA = Balanced Accuracy = {BA:1.5f}"
        ax1.text(x=pos_x, y=pos_y, s=text_BA, ha="right")


    Calc_PT = kwargs.get("PT")
    if(Calc_PT == True):
        pos_y = pos_y + step
        PT = ((TPR*((-1)*TNR+1))**(1/2)+TNR+1)/(TPR+TNR-1)
        text_PT = f"PT = Prevalence Threshold = {PT:1.5f}"
        ax1.text(x=pos_x, y=pos_y, s=text_PT, ha="right")


    Calc_FM = kwargs.get("FM")
    if(Calc_FM == True):
        pos_y = pos_y + step
        FM = ((TP/(TP+FP))*(TP/(TP+FN)))**(1/2)
        text_FM = f"FM = Fowlkes-Mallows Index = {FM:1.5f}"
        ax1.text(x=pos_x, y=pos_y, s=text_FM, ha="right")


    Calc_BM = kwargs.get("BM")
    if(Calc_BM == True):
        pos_y = pos_y + step
        BM = TPR+TNR-1
        text_BM = f"BM = Bookmaker Informedness = {BM:1.5f}"
        ax1.text(x=pos_x, y=pos_y, s=text_BM, ha="right")


    Calc_MK = kwargs.get("MK")
    if(Calc_MK == True):
        pos_y = pos_y + step
        MK = PPV+(TN/(TN+FN))-1
        text_MK = f"MK = Markedness = {MK:1.5f}"
        ax1.text(x=pos_x, y=pos_y, s=text_MK, ha="right")


    # Ploting
    if(savefig == True):
        plt.savefig(title, dpi=240)
        print(f" > saving figure: {title}.png")

    if(showfig == True):
        plt.show()

    else:
        plt.close()
        


    
    
        


    
    
