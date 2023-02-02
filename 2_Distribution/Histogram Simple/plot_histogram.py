
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def plot_histogram(DataFrame, title=None, columns="all",
                   savefig=False, verbose=True):
    """
    Plots the histogram of a given **DataFrame** with selected **columns**.

    Variables:
    * DataFrame - DataFrame as Pandas,
    * title - Title for the plot (default="Histogram - {column name}"),
    * columns - all, a string with selected column or a list with columns
                names,
    * savefig - True or False. If True will save a report with the title
                name and do not show the plot. If False will not save the
                report but will show the plot in the screen (default=False),
    * verbose - True or False (quiet mode). If True will print some infor-
                mation about the data analysis and plot (default=True).
     
    """

    # Versions ----------------------------------------------------------
    # 01 - Jan 31st, 2023 - starter
    # 02 -

    # Program -----------------------------------------------------------
    data = DataFrame.copy()
    
    
