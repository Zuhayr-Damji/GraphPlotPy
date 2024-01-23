# notRipoffDesmos
This is a graph plotter in code 

Example 1:
```
from notRipoffDesmos import FunctionPlotter

FunctionPlotter([
        [lambda x : 4**x -x**6 ],
    ]
)
```
Plots 1 graph with one set of points

Example 2:
```
from notRipoffDesmos import FunctionPlotter
import math
import random

def f(x):
    if random.random() < 0.5:
        return x/0
    return x


FunctionPlotter([
        [lambda x : 4**x -x**6 ],
        [lambda x: 20000*(math.e)**(-x/10)],
        [f]
    ]
)

```
Plots 3 graphs with one set of points each (does not crash due to the divide by 0 error)
![image](https://github.com/Zuhayr-Damji/notRipoffDesmos/assets/130306910/992d6f4a-8a1a-4391-a2b5-f0eadcb283ad)

