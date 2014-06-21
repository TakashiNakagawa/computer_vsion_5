#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *

import homography
import sfm
import sift

# キャリブレーション
K = array([[2394,0,932],[0,2398,628],[0,0,1]])

# import ipdb; ipdb.set_trace()

# 画像を読み込み特徴量を計算する
im1 = array(Image.open('alcatraz1.jpg'))
sift.process_image('alcatraz1.jpg','im1.sift')
l1,d1 = sift.read_features_from_file('im1.sift')

im2 = array(Image.open('alcatraz2.jpg'))
sift.process_image('alcatraz2.jpg','im2.sift')
l2,d2 = sift.read_features_from_file('im2.sift')

# 特徴量を対応づける
matches = sift.match_twosided(d1,d2)
ndx = matches.nonzero()[0]

# 同次座標にしinv(K)を使って正規化する
x1 = homography.make_homog(l1[ndx,:2].T)
ndx2 = [int(matches[i]) for i in ndx]
x2 = homography.make_homog(l2[ndx2,:2].T)

x1n = dot(inv(K),x1)
x2n = dot(inv(K),x2)

# RANSACでEを推定
model = sfm.RansacModel()
E,inliers = sfm.F_from_ransac(x1n,x2n,model)

# カメラ行列を計算する（P2は4つの解のリスト）
P1 = array([[1,0,0,0],[0,1,0,0],[0,0,1,0]])
P2 = sfm.compute_P_from_essential(E)

# 2つのカメラの前に点のある解を選ぶ
ind = 0
maxres = 0
for i in range(4):
  # triangulate inliers and compute depth for each camera
  # インライアを三角測量し各カメラからの奥行きを計算する
  X = sfm.triangulate(x1n[:,inliers],x2n[:,inliers],P1,P2[i])
  d1 = dot(P1,X)[2]
  d2 = dot(P2[i],X)[2]
  if sum(d1>0)+sum(d2>0) > maxres:
    maxres = sum(d1>0)+sum(d2>0)
    ind = i
    infront = (d1>0) & (d2>0)

# インライアを三角測量し両方のカメラの正面に含まれていない点を削除します。
X = sfm.triangulate(x1n[:,inliers],x2n[:,inliers],P1,P2[ind])
X = X[:,infront]

import numpy as np
np.savetxt("debug_3dpoints.txt", X)

# 3D描画
from mpl_toolkits.mplot3d import axes3d

fig = figure()
ax = fig.gca(projection='3d')# 現在操作している軸を取得
ax.plot(-X[0],X[1],X[2],'k.')
axis('off')


# Xの射影を描画する
import camera

# 3Dの点群を射影変換する
cam1 = camera.Camera(P1)
cam2 = camera.Camera(P2[ind])
x1p = cam1.project(X)
x2p = cam2.project(X)

# Kの正規化を戻す
x1p = dot(K,x1p)
x2p = dot(K,x2p)

figure()
imshow(im1)
gray()
plot(x1p[0],x1p[1],'o')
plot(x1[0],x1[1],'r.')
axis('off')

figure()
imshow(im2)
gray()
plot(x2p[0],x2p[1],'o')
plot(x2[0],x2[1],'r.')
axis('off')
show()
