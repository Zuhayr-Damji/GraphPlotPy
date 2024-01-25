# notRipoffDesmos
This is a graph plotter in code 
### Example 1:
```
from notRipoffDesmos import FunctionPlotter

import numpy as np
import math


FunctionPlotter(
    [[lambda x :  math.sin(x) + math.cos(x) + math.tan(x)]],
)
```
### Example 2:
```
from notRipoffDesmos import FunctionPlotter
import math
import random

def f(x):
    if random.random() < 0.5:
        return x/0
    return x

def ReLU(x):
    return max(0,x)

def Sigmoid(x):
    return 1/(1+math.exp(-x))

FunctionPlotter([
        [lambda x : 4**x -x**6 , lambda x: math.sin(3**x / 3*x) , lambda x: math.cos(3**x / 3*x)],
        [lambda x: math.tan(3**x / 3*x) , lambda x: math.cos(3**x / 3*x)],
        [f],
        [ReLU,lambda x: Sigmoid(x**4 + math.sin(x) + math.cos(x) + math.exp(x)), lambda x:x],
    ]
)


```
![image](https://github.com/Zuhayr-Damji/notRipoffDesmos/assets/130306910/992d6f4a-8a1a-4391-a2b5-f0eadcb283ad)

Note that error checking should be implemented in the functions passed into FunctionPlotter, this can only handle certain errors without breaking

You can pass in some custom x values for each graph in the format of an array with length a factor of the length of the constructions parameter

For the constructions parameter, the functions can be in a single list only (if you only want one graph) or a single function only (only one plot on one graph)

### Example 3:

Features yet to be implemented:
Custom colors for each plot
5. pip install
