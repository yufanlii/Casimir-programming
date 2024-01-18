#!/opt/conda/bin/python

print('hello world')

import numpy as np

def circle_cf(r):
    return 2 * np.pi * r

def circle_area(r):
    """
    Calculates the surface of a circle
    Input: r - radius of the circle (:
    """
    return np.pi * r ** 2

