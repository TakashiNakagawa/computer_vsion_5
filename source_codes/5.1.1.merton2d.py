#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *

execfile('load_vggdata.py')

# 3D点を同次座標にして射影する
#points3D.shape => (3, 717)
#points3d.shape[1] => 717
X = vstack( (points3D,ones(points3D.shape[1])) ) #np.ones:Return a new array of given shape and type, filled with ones.
# import ipdb; ipdb.set_trace()

# 画像1のカメラ行列を使って画像1に3次元上の点を射影する
x = P[0].project(X) 

# 画像1の上に点を描画する
figure()
imshow(im1)
# 特徴点
plot(points2D[0][0],points2D[0][1],'*')
axis('off')

figure()
imshow(im1)
# 3次元点群をカメラ行列を使って画像１に射影
plot(x[0],x[1],'r.')
axis('off')

show()
