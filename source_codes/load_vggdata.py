#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *
import camera

# 画像を読み込む
im1 = array(Image.open('images/001.jpg'))
im2 = array(Image.open('images/002.jpg'))

# 各画像上の2D点をリストに読み込む
points2D = [loadtxt('2D/00'+str(i+1)+'.corners').T for i in range(3)]

# 3D点を読み込む
points3D = loadtxt('3D/p3d').T

# 対応関係を読み込む
corr = genfromtxt('2D/nview-corners',dtype='int',missing='*')

# カメラパラメータをCameraオブジェクトに読み込む
P = [camera.Camera(loadtxt('2D/00'+str(i+1)+'.P')) for i in range(3)]
