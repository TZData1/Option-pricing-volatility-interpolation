import numpy as np
from scipy.stats import norm

def delta_match_x0(z):
    if z == 1:
        params = 1
    elif 0.9 < z < 1:
        params = 0.9
    elif 0.75 < z < 0.9:
        params < 0.75
    elif 0.6 < z < 0.75:
        params = 0.6
    elif 0.5 < z < 0.6:
        params = 0.5
    elif 0.4 < z < 0.5:
        params = 0.4
    elif 0.25 < z < 0.4:
        params = 0.25
    elif 0.1 < z < 0.25:
        params = 0.1
    elif 0.1 > z:
        params = 0
    return params

def delta_match_x1(z):
    if z == 1:
        params = 1
    elif 0.9 < z < 1:
        params = 1
    elif 0.75 < z < 0.9:
        params < 0.9
    elif 0.6 < z < 0.75:
        params = 0.75
    elif 0.5 < z < 0.6:
        params = 0.6
    elif 0.4 < z < 0.5:
        params = 0.5
    elif 0.25 < z < 0.4:
        params = 0.4
    elif 0.1 < z < 0.25:
        params = 0.25
    elif 0.1 > z:
        params = 0.1
    return params

def N(x):
    y = norm.cdf(x)
    return y

def black_scholes_call_value(S, K, r, t, d1, d2):
    return N(d1) * S - N(d2) * K * np.exp(-r * t/360)

def calc_d1(S, K, r, t, vol):
    d1 = (1.0/(vol * np.sqrt(t/360))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t/360)
    return d1

def calc_d2(S, K, r, t, vol):
    d2 = (1.0/(vol * np.sqrt(t/360))) * (np.log(S/K) + (r - 0.5 * vol**2.0) * t/360)
    return d2

def calc_K(S, r, t, vol, d1):
    K = S/np.exp(N(d1) * vol * np.sqrt(t/360) - (r + 0.5 * vol**2.0) * t/360)
    return K