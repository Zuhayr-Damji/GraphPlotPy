Note that error checking should be implemented in the functions passed into FunctionPlotter, this can only handle certain errors without breaking

You can pass in some custom x values for each graph in the format of an array with length a factor of the length of the constructions parameter


Notes for use:
1. For exponentiation graphs use floats rather than intgers

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