#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *

execfile('load_vggdata.py')

# 3D点を同次座標にして射影する
X = vstack( (points3D,ones(points3D.shape[1])) ) 
x = P[0].project(X) 

# 画像1の上に点を描画する
figure()
imshow(im1)
plot(points2D[0][0],points2D[0][1],'*')
axis('off')

figure()
imshow(im1)
plot(x[0],x[1],'r.')
axis('off')

show()
