# lineplot.py
import numpy as np
import pylab as pl
# Make an array of x values
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Make an array of y values for each x value
y = [0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 7, 8, 8, 9, 9]
# use pylab to plot x and y
pl.plot(x, y, 'ro')
# show the plot on the screen
pl.savefig('temp3.png')
