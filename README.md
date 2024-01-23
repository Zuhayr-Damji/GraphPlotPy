# notRipoffDesmos
This is a graph plotter in code 

### Example 1:
```
from notRipoffDesmos import FunctionPlotter

FunctionPlotter([
        [lambda x : 4**x -x**6 ],
    ]
)
```
![image](https://github.com/Zuhayr-Damji/notRipoffDesmos/assets/130306910/39ffa052-9cad-4b3f-aaf6-e0a8b7f732fb)


### Example 2:
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
![image](https://github.com/Zuhayr-Damji/notRipoffDesmos/assets/130306910/c915a72b-26d2-46f0-bb8b-ab2dd23bfdcb)

### Example 3:
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


Features yet to be implemented:
2. Custom colours for each plot
3. Custom X values for each graph
4. Make a note that error checking should we done by you
5. pip install
