# coding: utf-8
# ch03ディレクトリに置く
import sys, os, time, subprocess, pickle
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax
from PIL import Image

# 学習済パラメータの読み込み
with open("sample_weight.pkl", 'rb') as f:
    network = pickle.load(f)
W1, W2, W3 = network['W1'], network['W2'], network['W3']
b1, b2, b3 = network['b1'], network['b2'], network['b3']

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

    # ニューラルネットワークで推測させる
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    # 推測結果を出力
    y_idx = np.argsort(y)
    for i in range(10):
        print(y_idx[9-i], ":", round( y[y_idx[9-i]]*100, 2), "%" )
        
