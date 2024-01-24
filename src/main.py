from notRipoffDesmos import FunctionPlotter

import numpy as np
import math


FunctionPlotter(
        lambda x :  math.sin(x) + math.cos(x) + math.tan(x)
    ,
    customXValues=[np.arange(-10,-7,.001)],
)