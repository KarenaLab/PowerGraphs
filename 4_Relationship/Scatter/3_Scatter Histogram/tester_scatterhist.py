
import numpy as np
import pandas as pd

from ScatterHist_v03 import *


DataBlock = pd.read_csv("auto_industry_v02.csv", sep= ",")




# Plotting 4 Cylinders

cylinders_list = [4, 6, 8]

for cyl in cylinders_list:

    DB_Cylinders = DataBlock.groupby("cylinders")
    DB_Cylinders = DB_Cylinders.get_group(cyl)
    DB_Cyl_Displacement = DB_Cylinders["displacement"].values
    DB_Cyl_Horsepower = DB_Cylinders["horsepower"].values

    Data_X = DB_Cyl_Displacement[:]
    Data_Y = DB_Cyl_Horsepower[:]

    ScatterHist(f"Engine = {cyl} Cylinders",
                "Displacement (x 1000 cm^3)", Data_X,
                "Horsepower (HP)", Data_Y)






