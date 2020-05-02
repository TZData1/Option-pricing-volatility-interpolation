"""
here are some ugly but useful helper functions.
"""

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
