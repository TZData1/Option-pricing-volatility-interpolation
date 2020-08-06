
####- Option pricing using volatility interpolation for applying the Black-Scholes-Model 
##- python standard modules
import time
import datetime as dt
from math import sqrt, pi
from functions import *
## import numpy, pyplot and scipy
import numpy as np
import matplotlib as mat
#mat.style.use('ggplot')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy
from scipy.stats import norm
from scipy.optimize import brentq
from scipy.interpolate import interp1d
##- import pandas
import pandas as pd
##- import warnings
import warnings
warnings.filterwarnings("ignore")


##- load data
url = 'CADNOK-simulation.xlsx'
xls = pd.read_excel(url, sheet_name=['call', 'surface_30', 'surface_60'])
##- merging Excel Sheet 1 with 2 and 1 with 3
df30 = pd.merge(xls["call"], xls["surface_30"], on='Date')
df60 = pd.merge(xls["call"], xls["surface_60"], on='Date')
##- renaming columns as some have the same  names
xls["surface_30"].columns = ["Date", "s30_0", "s30_0.1", "s30_0.25", "s30_0.4", 
                            "s30_0.5", "s30_0.6", "s30_0.75", "s30_0.9", "s30_1"]
xls["surface_60"].columns = ["Date", "s60_0", "s60_0.1", "s60_0.25", "s60_0.4", 
                             "s60_0.5", "s60_0.6", "s60_0.75", "s60_0.9", "s60_1"]
##- creating one complete data frame
df_merge = pd.merge(xls["call"], xls["surface_30"], on='Date')
df_complete = pd.merge(df_merge, xls["surface_60"], on='Date')

##- predefining delta
delta = 0.2
##- building dataframe
master = xls["call"]
master["f(0)_30"] = df30[delta_match_x0(delta)]
master["f(0)_60"] = df60[delta_match_x0(delta)]
master["f(1)_30"] = df30[delta_match_x1(delta)]
master["f(1)_60"] = df60[delta_match_x1(delta)]
master["f(x)_30"] = np.NaN
master["f(x)_60"] = np.NaN
master["implied_vola"] = np.NaN
master["K"] = np.NaN
master["K"][0] = round(calc_K(21.45, 0.016842, 60, 0.74408, norm.ppf(0.2)))
master["d1"] = np.NaN
master["d2"] = np.NaN
master["N_d1"] = np.NaN
master["N_d2"] = np.NaN
master["Call_price"] = np.NaN

##- defining function for linear interpolation 
def lin_interpol(f_x0,f_x1, x0, x1, x):
  f_x = f_x0 + ((f_x1 - f_x0)/(x1 - x0) * (x - x0)) 
  return f_x
##- interpolating volatility
for i in range(len(master["f(x)_60"])): 
  master["f(x)_60"][i] = lin_interpol( master["f(0)_60"][i], master["f(1)_60"][i], 0, 1, delta)
  master["f(x)_30"][i] = lin_interpol( master["f(0)_30"][i], master["f(1)_30"][i], 0, 1, delta)
  master["implied_vola"][i] = lin_interpol( master["f(x)_30"][i], master["f(x)_60"][i], 0, 1, ((master["t"][i]-30)/30) )

##- threshold for strike price condition in the loop
x = 60 
for i in range(0, len(master["f(x)_60"])-1):
  ##- calculating parameters for each row
  master["d1"][i] = calc_d1(master["Underlying"][i], master["K"][i], master["rfr"][i], master["t"][i], master["implied_vola"][i])
  master["d2"][i] = calc_d2(master["Underlying"][i], master["K"][i], master["rfr"][i], master["t"][i], master["implied_vola"][i])
  master["N_d1"][i] = N(master["d1"][i])
  master["N_d2"][i] = N(master["d2"][i])
  master["Call_price"][i] = black_scholes_call_value(master["Underlying"][i], master["K"][i], master["rfr"][i], master["t"][i], master["d1"][i], master["d2"][i])
  ##- calculating strike price for the next row
  if master["t"][i+1] == x:
    master["K"][i+1] = round(calc_K(master["Underlying"][i+1], master["rfr"][i+1], master["t"][i+1], master["implied_vola"][i+1], master["d1"][i]))
  else: 
    master["K"][i+1] =  master["K"][i]

##- calculating last row manually
master[-1:]["d1"] = calc_d1(master[-1:]["Underlying"], master[-1:]["K"], master[-1:]["rfr"], master[-1:]["t"], master[-1:]["implied_vola"])
master[-1:]["d2"] = calc_d2(master[-1:]["Underlying"], master[-1:]["K"], master[-1:]["rfr"], master[-1:]["t"], master[-1:]["implied_vola"])
master[-1:]["N_d1"] = N(master[-1:]["d1"])
master[-1:]["N_d2"] = N(master[-1:]["d2"])
master[-1:]["Call_price"] = black_scholes_call_value(master[-1:]["Underlying"], master[-1:]["K"], master[-1:]["rfr"], master[-1:]["t"], master[-1:]["d1"], master[-1:]["d2"])

##- exporting output csv-file
master.to_csv("output.csv", index=False)
