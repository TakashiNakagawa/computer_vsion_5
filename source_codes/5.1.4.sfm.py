#!/usr/bin/python
# -*- coding: utf-8 -*-

from pylab import *

execfile('load_vggdata.py')

import sfm

# 最初の2枚の画像の点のインデクス番号
ndx = (corr[:,0]>=0) & (corr[:,1]>=0)# corr:対応関係 *でないものを選択


# 座標値を取得し、どう座標系にする
x1 = points2D[0][:,corr[ndx,0]]
x1 = vstack( (x1,ones(x1.shape[1])) ) 
x2 = points2D[1][:,corr[ndx,1]]
x2 = vstack( (x2,ones(x2.shape[1])) )


# Fを計算する
F = sfm.compute_fundamental(x1,x2)

# エピ極を計算する
e = sfm.compute_epipole(F)

# 描画する
figure()
imshow(im1)

# 各行について適当に色を付つけて描画する。
for i in range(5):
  sfm.plot_epipolar_line(im1,F,x2[:,i],e,False)
axis('off')

figure()
imshow(im2)
# 各点を描画する。線と同じ色付けになる。
for i in range(5):
  plot(x2[0,i],x2[1,i],'o')
axis('off')

show()
