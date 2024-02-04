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