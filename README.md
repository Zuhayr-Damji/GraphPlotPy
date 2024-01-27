# GraphPlotPy
This is a quick and very easy graph plotter for functions in code 
Pypi page found here: https://pypi.org/project/graphPlotPy/0.2/

```
pip install graphPlotPy==0.2

```

## Docs:
### Example 1:
```python
from graphPlotPy import FunctionPlotter

FunctionPlotter(
    [[lambda x :  1.23456789**x]]
)
```
![image](https://github.com/Zuhayr-Damji/GraphPlotPy/assets/130306910/3b2fc5b2-f172-48e7-9bac-a0539a7ff8a2)


### Example 2:
```python
from graphPlotPy import FunctionPlotter
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
![image](https://github.com/Zuhayr-Damji/GraphPlotPy/assets/130306910/992d6f4a-8a1a-4391-a2b5-f0eadcb283ad)

Note that error checking should be implemented in the functions passed into FunctionPlotter, this can only handle certain errors without breaking

You can pass in some custom x values for each graph in the format of an array with length a factor of the length of the constructions parameter
```python
FunctionPlotter([
        [lambda x : 4**x -x**6 , lambda x: math.sin(3**x / 3*x) , lambda x: math.cos(3**x / 3*x)],
        [lambda x: math.tan(3**x / 3*x) , lambda x: math.cos(3**x / 3*x)],
        [f],
        [ReLU,lambda x: Sigmoid(x**4 + math.sin(x) + math.cos(x) + math.exp(x)), lambda x:x],
    ],
    customXValues = [np.arange(0,10,0.1),np.arange(-5,5,0.01)]
    # or customXValues=[np.arange(0,10,0.1)] or customXValues=[np.arange(0,10,0.1),np.arange(-5,5,0.01), np.linspace(0,10,100),np.linspace(-10,-7,100)]
    # not [np.arange(0,10,0.1),np.arange(-5,5,0.01), np.arange(-5,5,0.01)]
)
```
For the constructions parameter, the functions can be in a single list only (if you only want one graph) or a single function only (only one plot on one graph):
```python
FunctionPlotter(
    [[lambda x :  math.sin(x) + math.cos(x) + math.tan(x)]],
)
```
Is the same as:
```python
FunctionPlotter(
    [lambda x :  math.sin(x) + math.cos(x) + math.tan(x)],
)
```
or:
```python
FunctionPlotter(
    lambda x :  math.sin(x) + math.cos(x) + math.tan(x),
)
```

This would also be valid:
```python
FunctionPlotter(
    [lambda x :  math.sin(x) + math.cos(x) + math.tan(x), lambda x : max(x,0)]
)
```
### Example 3:
```python
from graphPlotPy import FunctionPlotter
import math
import numpy as np

FunctionPlotter(
    lambda x : 3*math.e**(2*-x),
    customXValues=[np.linspace(-7, 10, 100)],
)

```
![image](https://github.com/Zuhayr-Damji/GraphPlotPy/assets/130306910/6de92bb8-8e5e-48a0-9275-8f3708c50cf4)


Notes for use:
1. For exponentiation graphs use floats rather than intgers

Features yet to be implemented:
1. Custom colors for each plot
2. Add this to PyPi
