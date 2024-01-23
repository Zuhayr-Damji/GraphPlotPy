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
        constructions: list[list[Callable[[int|float],int|float]]] = [[lambda x: x]], 
        customiseFig:Callable[[Figure],None] = _customiseFigDefault_,
        customiseAxes:Callable[[Axes],None] = _customiseAxesDefault_,
        customiseColors:Callable[[None],None] = _customiseColorsDefault_,
        customXValues: list[np.ndarray] | np.ndarray = [np.arange(-5,5,.01) for i in range(1)],
        figsize:tuple = (8,5), #TODO: make sure 2 ints in this tuple
)-> None:
    '''
    FunctionPlotter is a function that takes in a list of functions and creates a plot of them.
    There are many custom settings that are implemented as callbacks

    Parameters:
    constructions: A list of functions that will be plotted. Each element is a list of functions that will be plotted on the same graph.
    customiseFig: A function that takes in a matplotlib figure and can customises it e.g fig.set_color
    customiseAxes: A function that takes in ax (plt.subplots second return value iterated over) and can customise the axes e.g ax.set_facecolor
    customiseColors: Should return a color string e.g random.choice(['#abcabc', '#abcdef'])
    customiseXValues: The x values to be used for each graph. Accepts either one set of values that is repeated for each graph (ndarray in or out of a list) or (for one set of values for each graph) a list of ndarrays of custom x values although the length must match the length of constructions
    figsize: the figsize parameter passed to plt.subplots 

    extra info on fig, axes and figsize found here: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

    Notes on the graphs:
        - The minimum number of graphs plotted is 4 in an arrangement of (2,2)
        - The plot colors are random
    '''

    isConstructionsEmpty = len(constructions) == 0
    if isConstructionsEmpty: 
        raise invalidInputsException("No functions to plot")
    
    # if customXValues is one item long, remove it from the list
    if customXValues.shape == np.array([1]).shape:
        customXValues = customXValues[0]
    if type(customXValues) == type(np.array([1,2,3])):
        xValues = [customXValues for i in range(len(constructions))]
    elif len(customXValues)!= len(constructions):
            raise invalidInputsException("customXValues and constructions must be the same length (if you wish to repeat your custom set of x values for each graph, you only need to put the customXValues once either in a list or out)")


    numDimensions = len(constructions)

        

    x, y = calculateDimensions(numDimensions)

    if numDimensions <= 2:
        fig, axes = plt.subplots( 
            1, numDimensions,
            figsize = figsize
        )
    elif numDimensions > 2:
        fig, axes = plt.subplots( 
            x, y,
            figsize = figsize
        )
        
    customiseFig(fig)



    for index, graph in enumerate(constructions):

        xValues = customXValues[index]

        isGraphAList = type(graph) == type([])
        if not isGraphAList:
            raise invalidInputsException(f"Graph {graph} is not a list")
        
        
        xcoord, ycoord = getCoordinates(x, y,index)

        if numDimensions == 1:
            ax = axes
        elif numDimensions ==2 :
            ax = axes[ycoord]
        elif numDimensions > 3:
            ax = axes[xcoord, ycoord]

        customiseAxes(ax)

        for plot in graph: 

            isplotAFunction = type(plot) == type(lambda x: None)
            if not isplotAFunction:
                raise invalidInputsException(f"Plotting function {plot} is not a function") 
            
            yValues = mapToNPArray(xValues, plot) 
            ax.plot(xValues, yValues, color=customiseColors()) 

    plt.show()

