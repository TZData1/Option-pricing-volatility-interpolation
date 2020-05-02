"""
Here is your Environment for option pricing. 
Caution with column naming.
"""

import functions
import pandas as pd
import numpy as np
import math
from scipy.stats import norm


delta=0.2

input_file=pd.ExcelFile("CADNOK-simulation.xlsx")

