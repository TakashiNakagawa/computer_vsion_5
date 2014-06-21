#!/usr/bin/python
# -*- coding: utf-8 -*-

from pylab import *

execfile('load_vggdata.py')

import sfm

# 最初の2枚の画像に含まれる点のインデクス番号
ndx = (corr[:,0]>=0) & (corr[:,1]>=0)

# 座標値を取得し同次座標系に変換する
x1 = points2D[0][:,corr[ndx,0]]
x1 = vstack( (x1,ones(x1.shape[1])) )
x2 = points2D[1][:,corr[ndx,1]]
x2 = vstack( (x2,ones(x2.shape[1])) )

Xtrue = points3D[:,ndx]
Xtrue = vstack( (Xtrue,ones(Xtrue.shape[1])) )

# 最初の3点を調べる
Xest = sfm.triangulate(x1,x2,P[0].P,P[1].P)
print Xest[:,:3]
print Xtrue[:,:3]

# 描画する
from mpl_toolkits.mplot3d import axes3d
fig = figure()
ax = fig.gca(projection='3d')
ax.plot(Xest[0],Xest[1],Xest[2],'ko')
ax.plot(Xtrue[0],Xtrue[1],Xtrue[2],'r.')
axis('equal')
show()
