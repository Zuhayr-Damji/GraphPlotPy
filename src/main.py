from notRipoffDesmos import FunctionPlotter
import math
import random


FunctionPlotter([
        # [lambda x :  math.sin(x) + math.cos(x) + math.tan(x), lambda x: math.sin(x),lambda x:math.cos(x),lambda x:math.tan(x)],
        # [lambda x : math.e**x],
        [lambda x : random.random(),  lambda x : random.randint(0,10)],
        [lambda x : random.randint(0,100) - random.randint(-50,50)],
    ]
)