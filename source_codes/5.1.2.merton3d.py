#!/usr/bin/python
# -*- coding: utf-8 -*-

from pylab import *

execfile('load_vggdata.py')


# 3Dの点を描画する

from mpl_toolkits.mplot3d import axes3d
fig = figure()
ax = fig.gca(projection='3d')
ax.plot(points3D[0],points3D[1],points3D[2],'k.')
show()
