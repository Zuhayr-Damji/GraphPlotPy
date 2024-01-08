import matplotlib.pyplot as plt
import numpy as np
from typing import Callable


from helpers import *

'''
how to use: FunctionPlotter([
     [lambda x : x**4 - 4*x**2, lambda x : 9*x**4+6*x+(x/2)**8 , ... more functions],
     [...]
     [again]
     [another one]
     [as many as you want]
])

'''


def _customiseAxesDefault_(ax):
    ax.set_facecolor( color='black' )
    ax.grid(color='#0000ff', linewidth=.5, alpha=0.3)

def _customiseFigDefault_(fig):
    fig.set_facecolor( color='#4287F5')

def _customiseColorsDefault_():
    return getRandomColor()

def FunctionPlotter( 
        constructions:[[Callable]], #TODO: why this type hint no show up 
        _customiseFig_:Callable = _customiseFigDefault_,
        _customiseAxes_:Callable = _customiseAxesDefault_,
        _customiseColors_:Callable = _customiseColorsDefault_,
        figsize:tuple = (8,5),
)-> None:
    '''
    constructions: list of list of functions
    e.g [
        [lambda x : x**2 - 9, lambda x : 4*x - 13],
        [sigmoidFunction]
    ] plots 2 graphs, the 1st with 2 sets of points on the same axes, the 2nd with 1

    _customiseFig_: A function that takes in fig (plt.subplots first return value) and can _customise_ the figure e.g fig.set_color
    _customiseAxes_: A function that takes in ax (plt.subplots second return value iterated over) and can _customise_ the axes e.g fig.set_facecolor
    extra info found here: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

    figsize: the figsize parameter passed to plt.subplots e.g random.choice(['#abcabc', '#abcdef'])

    Notes on the graphs:
        - The minimum number of graphs plotted is 4 in an arrangement of (2,2)
        - The plot colors are random
    '''
    if len(constructions) == 0: return # TODO: throw error

    xValues = np.linspace( -5 , 5 , 100)


    numDimensions = len(constructions)
    x, y = calculateDimensions(numDimensions)

    fig, axes = plt.subplots( 
        x, y,
        figsize = figsize
    )
    
    _customiseFig_(fig)


    for index, graph in enumerate(constructions):

        xcoord, ycoord = getCoordinates(x, y,index)
        ax = axes[xcoord, ycoord]
        _customiseAxes_(ax)

        for plot in graph: # TODO: input santisations
            yValues = mapToNPArray(xValues, plot) 
            ax.plot(xValues, yValues, color=_customiseColors_()) #TODO: custom colors
            

    plt.show()


