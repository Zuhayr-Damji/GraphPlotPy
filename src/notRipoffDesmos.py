import matplotlib.pyplot as plt
import numpy as np

from typing import Callable
from helpers import *

# For type hints:
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def _customiseAxesDefault_(ax):
    ax.set_facecolor( color='black' )
    ax.grid(color='#0000ff', linewidth=.5, alpha=0.3)

def _customiseFigDefault_(fig):
    fig.set_facecolor( color='#4287F5')

def _customiseColorsDefault_():
    return getRandomColor()

def FunctionPlotter( 
        constructions: list[list[Callable[[int|float],int|float]]], 
        _customiseFig_:Callable[[Figure],None] = _customiseFigDefault_,
        _customiseAxes_:Callable[[Axes],None] = _customiseAxesDefault_,
        _customiseColors_:Callable[[None],None] = _customiseColorsDefault_,
        figsize:tuple = (8,5),
)-> None:
    '''
    FunctionPlotter is a function that takes in a list of functions and creates a plot of them.
    There are many custom settings that are implemented as callbacks

    Parameters:
    constructions: A list of functions that will be plotted. Each element is a list of functions that will be plotted on the same graph.
    _customiseFig_: A function that takes in a matplotlib figure and can customises it e.g fig.set_color
    _customiseAxes_: A function that takes in ax (plt.subplots second return value iterated over) and can customise the axes e.g ax.set_facecolor
    _customiseColors_: Should return a color string e.g random.choice(['#abcabc', '#abcdef'])
    figsize: the figsize parameter passed to plt.subplots 

    extra info on fig, axes and figsize found here: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

    Notes on the graphs:
        - The minimum number of graphs plotted is 4 in an arrangement of (2,2)
        - The plot colors are random
    '''

    isConstructionsEmpty = len(constructions) == 0
    if isConstructionsEmpty: 
        raise invalidInputsException("No functions to plot") 

    xValues = np.arange(-5,5,.01)


    numDimensions = len(constructions)
    x, y = calculateDimensions(numDimensions)

    fig, axes = plt.subplots( 
        x, y,
        figsize = figsize
    )
    
    _customiseFig_(fig)


    for index, graph in enumerate(constructions):

        isGraphAList = type(graph) == type([])
        if not isGraphAList:
            raise invalidInputsException(f"Graph {graph} is not a list")

        xcoord, ycoord = getCoordinates(x, y,index)
        ax = axes[xcoord, ycoord]
        _customiseAxes_(ax)

        for plot in graph: 

            isplotAFunction = type(plot) == type(lambda x: None)
            if not isplotAFunction:
                raise invalidInputsException(f"Plotting function {plot} is not a function") 
            
            yValues = mapToNPArray(xValues, plot) 
            ax.plot(xValues, yValues, color=_customiseColors_()) 

    plt.show()

