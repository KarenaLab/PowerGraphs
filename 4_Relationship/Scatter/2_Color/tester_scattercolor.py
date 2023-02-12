# Scatter Plot Color - Tester


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Source:
# https://www.tutorialspoint.com/matplotlib/matplotlib_scatter_plot.htm

Title = "Displacement and Horsepower Relationship"

DataBlock = pd.read_csv("auto_industry_v02.csv", sep= ",")

DB_Cylinders = DataBlock.groupby("cylinders")

DB_Cylinders_4 = DB_Cylinders.get_group(4)
DB_Cyl4_Displacement = DB_Cylinders_4["displacement"].values
DB_Cyl4_Horsepower = DB_Cylinders_4["horsepower"].values

DB_Cylinders_6 = DB_Cylinders.get_group(6)
DB_Cyl6_Displacement = DB_Cylinders_6["displacement"].values
DB_Cyl6_Horsepower = DB_Cylinders_6["horsepower"].values

DB_Cylinders_8 = DB_Cylinders.get_group(8)
DB_Cyl8_Displacement = DB_Cylinders_8["displacement"].values
DB_Cyl8_Horsepower = DB_Cylinders_8["horsepower"].values


fig = plt.figure(figsize= (8, 4.5))
ax = fig.add_subplot(1, 1, 1)

ax.scatter(x= DB_Cyl4_Displacement, y= DB_Cyl4_Horsepower, color= "blue", edgecolor= "white", label= "4 Cylinders")
ax.scatter(x= DB_Cyl6_Displacement, y= DB_Cyl6_Horsepower, color= "green", edgecolor= "white", label= "6 Cylinders")
ax.scatter(x= DB_Cyl8_Displacement, y= DB_Cyl8_Horsepower, color= "red", edgecolor= "white", label= "8 Cylinders")

ax.set_title(Title)
ax.set_xlabel("Displacement (x1.000 cm^3)")
ax.set_ylabel("Power (hp)")

ax.grid(color= "grey", linestyle= "--", linewidth= 0.5)
ax.set_axisbelow(True)


plt.legend(loc= "best", framealpha= 1)

plt.tight_layout()
plt.savefig(Title, dpi= 240)
plt.show()


