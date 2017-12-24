# coding: utf-8
# ch07ディレクトリに置く
import sys, os, time, subprocess
sys.path.append(os.pardir)
import numpy as np
from common.layers import *
from simple_convnet import SimpleConvNet
from PIL import Image

# 畳み込みネットワークの読み込みと、学習済パラメータの読み込み
network = SimpleConvNet()
network.load_params("params.pkl")

devnull = open('os.devnull', 'w')
ipaddr = subprocess.check_output(["hostname", "-I"]).decode("utf-8").strip()
commd = "http://"+ipaddr+":8080/?action=snapshot"

while True:
    time.sleep(1)

    # カメラの画像を取り込む
    subprocess.run(["wget", "-O", "photo.jpg", commd], stdout=devnull, stderr=subprocess.STDOUT)

    # 画像の前処理（を28x28に整形、白黒対応、二値化）
    img = Image.open("photo.jpg").convert('L')
    img28 = np.array(img.resize((28,28)))

    thresh = np.median(img28)
    if thresh > 127:
        img28 = 255 - img28

    x = np.zeros(img28.shape, img28.dtype)
    x[np.where(img28 > thresh)] = 255

    x = np.ravel(x)/255
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
