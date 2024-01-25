from graphPlotPy import FunctionPlotter
import math
import numpy as np

FunctionPlotter(
    lambda x : 3*math.e**(2*-x),
    customXValues=[np.linspace(-7, 10, 100)],
)