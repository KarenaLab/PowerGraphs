# Tester Missing Data

import numpy as np
import pandas as pd


from plot_missingdata_col_v09 import *
from plot_missingdata_row_v04 import *


# Colleting Information
filename = "hmeq.csv"
df = pd.read_csv(filename, sep=",", encoding="utf-8")

version_col = "09"
version_row = "04"
savefig = True

title_col = f"HMEQ - Missing Data by columns - version {version_col}"
plot_missingdata_col(df, title=title_col, savefig=savefig)

title_row = f"HMEQ - Missing Data by rows - version {version_row}"
plot_missingdata_row(df, title=title_row, savefig=savefig)



