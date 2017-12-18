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
    subprocess.run(["wget", "-O", "num_photo.jpg", "http://192.168.1.45:9000/?action=snapshot"])
    img = cv2.imread("num_photo.jpg")

    # 画像を２値化
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    cv2.imwrite("num_photo_th.jpg", th2)

    # 画像を28x28に整形
    img2 = Image.open("num_photo_th.jpg")
    im = np.array(img2.resize((28,28)))

    # 白背景・黒背景の両方に対応
    if np.count_nonzero(im) < 392:
        x = np.ravel(im)/255
    else:
        x = 1 - np.ravel(im)/255

    # 入力値をテキストで出力
    for i in range(0, 28):
        for j in range(0, 28):
            print("{:01.0f}".format(x[28*i+j]), end=' ')
        print('')

    # 畳み込みニューラルネットワークで推測させる
    x = x.reshape((1, 1, 28, 28))
    y = network.predict(x)
    y = softmax(y.reshape(10))

    # 推測結果を出力
    y_idx = np.argsort(y)
    for i in range(10):
        print(y_idx[9-i], ":", round( y[y_idx[9-i]]*100, 2), "%" )
