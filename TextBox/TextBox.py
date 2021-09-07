
def TextBox(MainText, Subtittle, **kwargs):

    # MainText = First Info, the data that have to be highlighted
    # Subtittle = Subtitle, the short explanation about the data


    # Versions ----------------------------------------------------------
    # 01 - 25th Nov 2020 - Starter
    # 02 - 26th Nov 2020 - Including x_size and y_size parameters
    # 03 - 03rd Feb 2021 - Adjusting size of picture for Squared Ratio
    # 04 - 16th Feb 2021 - Adding **kwargs
    # 05 - 04th Aug 2021 - Adjusting variables
    #


    # List of Variables and kwargs --------------------------------------
    # MainText = string
    # Subtittle = string

    # figratio = square*, wide or A4
    # savefig = False* or True



    # Program -----------------------------------------------------------

    
    import matplotlib.pyplot as plt


    # 1 - Setting Text Sizes

    Subtittle_size = 18
    
    MainText_len = len(MainText)
  
    if (MainText_len <= 5):
        scale = 8

    else:
        scale = 5
        

    MainText_size = scale * Subtittle_size

    
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

    
    
    # 2 - Creating Figure
    
    fig = plt.figure(figsize= (x_size, y_size))

    plt.axis([0, x_size, 0, y_size])
    plt.axis("off")

    plt.text(x=(x_size/2), y=(y_size * 0.7), s= MainText, fontsize= MainText_size, ha= 'center', va= 'center', wrap= True)
    plt.text(x=(x_size/2), y=(y_size * 0.3), s= Subtittle, fontsize= Subtittle_size, style= 'italic', ha= 'center', va= 'center', wrap= True)

    plt.tight_layout()

    savefig = kwargs.get("savefig")

    if(savefig == True):
        plt.savefig(Subtittle, dpi= 240)
    
    
    plt.show()



