#!/usr/bin/python
# -*- coding: utf-8 -*-

from pylab import *

execfile('load_vggdata.py')

import sfm, camera

corr = corr[:,0] # 第1視点
ndx3D = where(corr>=0)[0] # 欠けた値は-1
ndx2D = corr[ndx3D]


# 見える点を選び同次座標に変換
x = points2D[0][:,ndx2D] # 第1視点
x = vstack( (x,ones(x.shape[1])) )
X = points3D[:,ndx3D]
X = vstack( (X,ones(X.shape[1])) )

# Pを推定する
Pest = camera.Camera(sfm.compute_P(x,X))

# 比較する！
print Pest.P / Pest.P[2,3]
print P[0].P / P[0].P[2,3]

xest = Pest.project(X)

# 描画する
figure()
imshow(im1)
plot(xest[0],xest[1],'r.')#r:赤、.:dots
plot(x[0],x[1],'bo')#b:青、o, small circle
axis('off')
show()
