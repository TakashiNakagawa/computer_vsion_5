#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import *
from scipy import linalg

class Camera(object):
  """ ピンホールカメラを表すクラス """

  def __init__(self,P):
    """ カメラモデル P = K[R|t] を初期化する """
    self.P = P
    self.K = None # キャリブレーション行列
    self.R = None # 回転
    self.t = None # 平行移動
    self.c = None # カメラ中心

  def project(self,X):
    """ X(4*nの配列)の点を射影し、座標を正規化する """
    x = dot(self.P,X)
    for i in range(3):
      x[i] /= x[2]
    return x

  def factor(self):
    """ P = K[R|t]に従い、カメラ行列を K,R,tに分解する """
    # 最初の3*3の部分を分解する
    K,R = linalg.rq(self.P[:,:3])

    # Kの対角成分が正になるようにする
    T = diag(sign(diag(K)))
    if linalg.det(T) < 0:
      T[1,1] *= -1

    self.K = dot(K,T)
    self.R = dot(T,R) # Tはそれ自身が逆行列
    self.t = dot(linalg.inv(self.K),self.P[:,3])

    return self.K, self.R, self.t

  def center(self):
    """ カメラ中心を計算して返す """
    if self.c is not None:
      return self.c
    else:
      # 分解により計算する
      self.factor()
      self.c = -dot(self.R.T,self.t)
      return self.c

def rotation_matrix(a):
  """ ベクトルaを軸に回転する3Dの回転行列を返す """
  R = eye(4)
  R[:3,:3] = linalg.expm([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
  return R
