
def ScatterSimple(Data_x, Data_y, Title_x, Title_y):

    # Versions ----------------------------------------------------------

    # 01 - Starter


    # Program -----------------------------------------------------------
    
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.axes as axes


    x = Data_x
    y = Data_y

    
    fig, ax = plt.subplots(figsize= (12, 8.5))   # A4 Ratio (1,4)
    
    ax.scatter(x= x, y= y)

    ax.set_xlabel(Title_x)
    ax.set_ylabel(Title_y)
    ax.grid(color= "lightgray", linestyle= "dashed", linewidth= 0.5)


    plt.tight_layout()
    plt.show()

    return()


