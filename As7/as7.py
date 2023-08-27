'''
Henry Hall
8/26/23

Assignment 5.1
'''

from matplotlib import pyplot as plt
import numpy as np

def ellipse_1(x):
    return (x**3) - (7*x) + 3

def ellipse_2(x):
    return (x**3)-(7*x)+9

def ellipse_3(x):
    return (x**3)-(7*x)-12

def ellipse_4(x):
    return (x**3)-(3*x)+2

def ellipse_5(x):
    return x**3

def graph_ellipse(function, xrange = (-5,5), yrange = (-5, 5)) -> None:
    x = np.linspace( xrange[0], xrange[1], num=10000 )
    plt.plot(x, function(x)**(1/2), color = 'b' )
    plt.plot(x, - function(x)**(1/2) , color = 'b')
    plt.show()

graph_ellipse(ellipse_1, (-4,4))
graph_ellipse(ellipse_2, (-4,5))
graph_ellipse(ellipse_3, (1,5))
graph_ellipse(ellipse_4, (-2,5))
graph_ellipse(ellipse_5, (-1,5))

