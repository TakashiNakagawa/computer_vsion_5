#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from numpy import *
from pylab import *
import stereo

# tsukuba
im_l = array(Image.open('scene1.row3.col3.ppm').convert('L'),'f')
im_r = array(Image.open('scene1.row3.col4.ppm').convert('L'),'f')

# # cones
# im_l = array(Image.open('cones/im2.png').convert('L'),'f')
# im_r = array(Image.open('cones/im6.png').convert('L'),'f')


# 視差の開始値と調べる範囲
start = 4
steps = 12   # for tsukuba
# steps = 50    # for cones

# 相互相関を調べるパッチの幅
wid = 9

res = stereo.plane_sweep_ncc(im_l,im_r,start,steps,wid)

import scipy.misc
scipy.misc.imsave('depth.png',res)

import ipdb; ipdb.set_trace()


wid = 3
res2 = stereo.plane_sweep_gauss(im_l,im_r,start,steps,wid)
scipy.misc.imsave('depthg.png',res2)

figure()
gray()
imshow(res)
axis('off')
figure()
gray()
imshow(res2)
axis('off')
show()
