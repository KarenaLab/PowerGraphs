
def Waterfall(Title, Data, Labels, **kwargs):

    # (Libraries - delete this tag)

    import numpy as np
    import pandas as pd

    import matplotlib.pyplot as plt


    # Versions ---------------------------------------------------------

    # 01 - Oct 05th, 2021 - Starter
    # 02 - *** - add **kwargs
    # 03 - 


    # List of Variables and kwargs -------------------------------------

    # Data = Information (numbers)
    # Labels = Labels for Data (string)
    #
    #


    # Program ----------------------------------------------------------

    Data = np.array(Data)

    Data_Size = len(Data)
    Data_CumSum = Data.cumsum()

    Value_List = [Data_CumSum[0]]
    Ghost_List = [0]
    

    i = 1
    while(i < Data_Size):

        Info = Data[i]

        if(Info > 0):

            Value = np.absolute(Info)
            Ghost = Data_CumSum[i-1]

        else:
            Value = np.absolute(Info)
            Ghost = Data_CumSum[i-1] - Value


        Value_List.append(Value)
        Ghost_List.append(Ghost)
        
        i = i+1


    Value_List.append(Ghost)
    Ghost_List.append(0)
    Labels.append("Final")


    # Plotting
    
    fig = plt.figure(figsize= (8, 4.5))
    plt.suptitle(Title, fontsize= 14)

    plt.bar(Labels, Ghost_List, color= "white", alpha= 0.01, zorder= 10)
    plt.bar(Labels, Value_List, color= "royalblue", edgecolor= "black", linewidth= 0.5, bottom= Ghost_List, zorder= 11)

    plt.grid(axis= "y", color= "lightgrey", linestyle= "--", linewidth= 0.5)

    tick_space = 1/(len(Value_List)+1)

    i = 1
    while(i < (len(Value_List))):

          tick_start = tick_space * i
          tick_end = tick_space * (i+1)
          value = Data_CumSum[i-1]

          plt.axhline(y= value , xmin= tick_start, xmax= tick_end,
                      color= "black", linewidth= 0.5)

          i = i+1


    plt.savefig(Title, dpi= 240)   
    plt.show()




