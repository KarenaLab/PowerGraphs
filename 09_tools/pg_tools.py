# PowerGraphs Tools [P397]

# Versions
# 01 - Jan 24th, 2024 - Starter
# 02 -


# Insights, improvements and bugfix
# 01 - Create "binning" function
# 02 - Create a standard color pallete
#


# Libraries
import numpy as np
import pandas as pd

import scipy.stats as st

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# ----------------------------------------------------------------------
def import_rcparams():
    """
    Imports RC Params to standartize plots.
    
    """
    # RC Params
    plt.rcParams["font.family"] = "Helvetica"
    plt.rcParams["font.size"] = 8
    plt.rcParams["figure.dpi"] = 120
    plt.rcParams["ps.papersize"] = "A4"
    plt.rcParams["xtick.direction"] = "inout"
    plt.rcParams["ytick.direction"] = "inout"


    return None    


def col_select(DataFrame, columns):
    """
    Columns names verification.
    Also standatize the output as a list for pandas standard.
    
    """
    def column_checker(DataFrame, col_list):
        col_select = list()
        df_cols = DataFrame.columns.to_list()

        for i in col_list:
            if(df_cols.count(i) == 1):
                col_select.append(i)


        return col_select


    # Columns preparation
    if(columns == "all"):
        # Default: takes **all** columns from DataFrame.
        col_select = DataFrame.columns.to_list()

    elif(isinstance(columns, str) == True):
        # Tranforms a sting into a list
        columns = columns.replace(" ", "")
        columns = columns.split(",")
        col_select = column_checker(DataFrame, columns)

    elif(isinstance(columns, list) == True):
        col_select = column_checker(DataFrame, columns)

    else:
        col_select = list()


    return col_select


def grid_select(grid_axes, default="x"):
    """
    Tests the grid selection
    
    """
    grid_list = ["x", "y", "both"]

    if(grid_list.count(grid_axes) == 0):
        print(f' >>> Error: "grid_axis" option not valid. Using "{default}" as forced option.')
        grid_axes = default[:]


    return grid_axes


# end
