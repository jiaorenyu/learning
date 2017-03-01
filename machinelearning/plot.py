# -*- coding: utf-8 -*-

import pylab as pl

from matplotlib.ticker import MultipleLocator, FuncFormatter

def formatter(x, pos):
    return str(x) + "_" + str(pos)

y = [0, 1,1,0]
x = [1, 2, 3, 4]
pl.plot(x, y, color="red")
ax = pl.gca()
ax.xaxis.set_major_formatter( FuncFormatter(formatter) )

pl.ylim(0, 10)
pl.legend()
pl.show()
