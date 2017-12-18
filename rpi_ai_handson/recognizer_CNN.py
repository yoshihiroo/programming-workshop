# coding: utf-8
# ch07ディレクトリに置く
import sys, os, time, subprocess
sys.path.append(os.pardir)
import numpy as np
from common.layers import *
from simple_convnet import SimpleConvNet
from PIL import Image
import cv2

# 畳み込みネットワークの読み込みと、学習済パラメータの読み込み
network = SimpleConvNet()
network.load_params("params.pkl")

while True:
    time.sleep(1)

    # カメラの画像を取り込む
    subprocess.run(["wget", "-O", "num_photo.jpg", "http://192.168.1.46:9000/?action=snapshot"])

    # 画像を28x28に整形
    img2 = Image.open("num_photo.jpg").convert('L')
    im = np.array(img2.resize((28,28)))
    x = np.ravel(im)/255

    # 入力値をテキストで出力
    for i in range(0, 28):
        for j in range(0, 28):
            print("{:02.1f}".format(x[28*i+j]), end=' ')
        print('')

    # 畳み込みニューラルネットワークで推測させる
    x = x.reshape((1, 1, 28, 28))
    y = network.predict(x)
    y = softmax(y.reshape(10))

    # 推測結果を出力
    y_idx = np.argsort(y)
    for i in range(10):
        print(y_idx[9-i], ":", round( y[y_idx[9-i]]*100, 2), "%" )
