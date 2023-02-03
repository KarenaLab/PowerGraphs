
import numpy as np
import pandas as pd

from plot_line_v01 import *

# Setup/Config
seed = 27


# Program
np.random.seed(seed)

period = np.arange(start=1, stop=100+1, step=1)
leads = np.random.uniform(low=0, high=50, size=100)
prospects = np.random.uniform(low=40, high=80, size=100)

sales = 60 + 2*period + np.random.normal(loc=0, scale=0.5*period, size=100)

data = {"leads": leads,
        "prospects": prospects,
        "sales": sales}

df = pd.DataFrame(data=data, index=period)
plot_line(df, title="plot_line_v01", savefig=False)

df["period"] = period
plot_line(df, index="period", grid_axis="y", remove_axis=True, columns=["leads", "sales"])

