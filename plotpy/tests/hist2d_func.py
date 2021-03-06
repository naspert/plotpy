# -*- coding: utf-8 -*-
#
# Copyright © 2012 CEA
# Pierre Raybaut
# Licensed under the terms of the CECILL License
# (see plotpy/__init__.py for details)

"""2-D Histogram (with function) test"""

#SHOW = True # Show test in GUI-based test launcher
#TODO: change this test so that shown data means something...

from numpy import random, array, dot, concatenate

from plotpy.plot import ImageDialog
from plotpy.builder import make
from plotpy.config import _

def hist2d_func(X, Y, Z):
    win = ImageDialog(edit=True, toolbar=True,
                      wintitle="2-D Histogram X0=(0,1), X1=(-1,-1)")
    hist2d = make.histogram2D(X, Y, 200, 200, Z=Z, computation=2)
    curve = make.curve(X[::50], Y[::50],
                       linestyle='', marker='+', title=_("Markers"))
    plot = win.get_plot()
    plot.set_aspect_ratio(lock=False)
    plot.set_antialiasing(False)
    plot.add_item(hist2d)
    plot.add_item(curve)
    plot.set_item_visible(curve, False)
    win.get_itemlist_panel().show()
    win.show()
    win.exec_()

if __name__ == "__main__":
    import plotpy
    _app = plotpy.qapplication()
    N = 150000
    m = array([[ 1., .2], [-.2, 3.]])
    X1 = random.normal(0, .3, size=(N, 2))
    X2 = random.normal(0, .3, size=(N, 2))
    X = concatenate((X1+[0, 1.], dot(X2, m)+[-1, -1.])) 
    hist2d_func(X[:, 0], X[:, 1], X[:, 0]+X[:, 1])
