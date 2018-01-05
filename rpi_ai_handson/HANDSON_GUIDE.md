>【注意】以下内容はレクチャー当日までドラフトとなります


ラズパイ基本セットアップ
------------

1. OSイメージのダウンロードとSDカードへの書き込み  
本家Raspberry Piサイトの[インストールガイド](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)を参照しながら進めます。

2. ヘッドレスセットアップのための準備  
OSイメージが書き込まれたSDカードを、パソコンのSDカードリーダーで開き、ルートディレクトリに中身が空の`ssh`ファイルと、下記の内容の`wpa_supplicant.conf`ファイルを置きます。
```
country=GB
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
        ssid="<SSID名>"
        psk="<パスワード>"
        key_mgmt=WPA-PSK
        proto=RSN
        pairwise=CCMP
        auth_alg=OPEN
}
```

3. Raspberry Piの起動  
パソコンからSDカードを取り出し、RPi本体に入れて起動する。

4. IPアドレスの確認  
同じネットワークセグメントにつながっているパソコンから下記コマンドでRasperry PiのIPアドレスを探す(下記はWindows上のコマンドプロンプトを使う場合)。
Raspberry PiのMACアドレスは`B8-27-EB`から始まるので、それらに紐づいているIPアドレスを探す。
```
for /l %i in (0,1,255) do ping -w 1 -n 1 192.168.1.%i && arp -a 192.168.1.%i  
arp -a
```
>Note:  
>`192.168.1`の部分は利用するネットワーク環境に合わせて変更してください。

5. ssh経由でRaspberry Piにリモートログイン
クライアントプログラムは[Tera Term(Windows)](https://forest.watch.impress.co.jp/library/software/utf8teraterm/)や、Chromeブラウザーの[Secure Shell](https://chrome.google.com/webstore/detail/secure-shell/pnhechapfaindjhompbnflcldabbghjo?hl=ja)などがお勧め。
sshクライアントから上記で調べたIPアドレスにログインする。

6. MACアドレスを確認する  
複数人で同時にヘッドレスセットアップを行うので、個体の特定が必要となる。下記コマンドでRaspberry Pi本体の赤色LEDを点滅させ、上記4節で調べたIPアドレスと合わせることで本体のMACアドレスを把握することができる。
```
echo heartbeat | sudo tee /sys/class/leds/led1/trigger
```
特定できたら下記コマンドで元の状態に戻しておく。
```
echo input | sudo tee /sys/class/leds/led1/trigger
```

以下、自身のRaspberry Piにログインしなおしてから設定を続ける。

6. コンフィグレーション(raspi-config)
タイムゾーンの設定、およびカメラモジュールの有効化を行う。
```
sudo raspi-config
```
- Localisation Options -> Change Timezone -> Asia -> Tokyo
- Interfacing Options -> Camera -> (Would you like the camera...) -> Yes  
システムを再起動(reboot)する。
>Note:  
>`sudo`を使うことで管理者権限でコマンドが実行されます。

カメラ画像の配信
------------
1. OSのモジュールを最新にアップデートする
```
sudo apt-get update
sudo apt-get upgrade
```
>Note:  
>何らかプログラムをインストールする際には、上の二つのコマンドを実行し、事前にOSのモジュールを最新の状態にすることをお勧めします。 

2. 配信プログラム(mjpg-streamer)のインストール
[ブログ記事(Raspberry Pi 3 の標準カメラで撮影した動画をブラウザに配信する方法まとめ)](https://qiita.com/okaxaki/items/72226a0b0f5fab0ec9e9)の「配信方法1 - mjpg-streamer」を参照しながら設定を行う。

Linuxの基本操作
------------

| コマンド | 動き |
---- | -----
| whoami | 自分のユーザー名を表示する |
| who | 現在ログインしているユーザーの一覧を表示する |
| top | 動いているプロセスの一覧を表示する（qで終了） |
| pwd | カレントディレクトリのパスを表示する |
| ls | カレントディレクトリの内容を表示する |
| cd | 別のディレクトリに移動する |
| mkdir <ディレクトリ名> | 新しいディレクトリを作成する |
| cp <ファイル/ディレクトリ名> | ファイルをコピーする |
| mv <ファイル/ディレクトリ名> | ファイルを移動する |
| nano <ファイル名> | エディターを開く（Ctrl+xで終了） |
| less <ファイル名> | ファイルの内容を表示する |

MNIST文字認識の実装
------------
1. `cd`コマンドを実行し、自分のホームディレクトリに戻る。
>Note:  
>自分がどのディレクトリで作業しているか迷子にならないように、適宜`pwd`コマンドで確認しましょう。

2. 「ゼロから作るDeep Learning」のサンプルコードの入手  
[O'Reilly社のホームページ](https://www.oreilly.co.jp/books/9784873117584/)からgithubへのリンクを辿る。
該当するリポジトリの「Clone or download」からリンクをコピーし、`git clone`コマンドで自身のRaspberry Piにクローンを作る。
```
git clone https://github.com/oreilly-japan/deep-learning-from-scratch.git
```
python3でのコンパイル・実行が正しくできるかテストする。
```
cd deep-learning-from-scratch
cd ch03
python3 neuralnet_mnist.py
```
最初の実行時には`Downloading t10k-labels-idx1-ubyte.gz ...(中略) Creating pickle file ... Done!`と表示される。
正しく実行されれば、`Accuracy:0.9352`という結果が出力される。

3. カメラを使ったMNIST文字認識プログラムの実装
>Note:  
>`mjpg-streamer`を実行させた状態で`recognizer_NN.py`および`recognizer_CNN.py`を実行してください。ソースコード内のIPアドレスおよびwebサーバーのポート番号を自分の環境に合わせて変更してください。
- ニューラルネットワークによる推論
`/home/pi/deep-learning-from-scratch/ch03`ディレクトリ上で下記コマンドを実行する。
```
wget https://raw.githubusercontent.com/yoshihiroo/programming-workshop/master/rpi_ai_handson/recognizer_NN.py
python3 recognizer_NN.py
```

- 畳み込みニューラルネットワークによる推論
`/home/pi/deep-learning-from-scratch/ch07`ディレクトリ上で下記コマンドを実行する。
```
wget https://raw.githubusercontent.com/yoshihiroo/programming-workshop/master/rpi_ai_handson/recognizer_CNN.py
python3 recognizer_CNN.py
```

Kerasによる物体識別の実装
------------
1. TensorFlowのインストール
[ブログ記事(Cross-compiling TensorFlow for the Raspberry Pi)](https://petewarden.com/2017/08/20/cross-compiling-tensorflow-for-the-raspberry-pi/)の中盤の「If you’re running Python 3.5」から始まる箇所のガイドに従ってTensorFlowをインストールする。

2. TensorFlow動作テスト
```
wget https://raw.githubusercontent.com/yusugomori/deeplearning-tensorflow-keras/master/3/tensorflow/01_logistic_regression_or_tensorflow.py
python3 01_logistic_regression_or_tensorflow.py
```
が動作することを確認。なお、Python3.4用のTensorFlowのモジュールをPython3.5で使っているためwarningが出る。

>Note:  
>[「詳解 ディープラーニング TensorFlow・Kerasによる時系列データ処理」](https://book.mynavi.jp/ec/products/detail/id=72995)からのサンプルコードとなります。

3. Kerasのインストール
下記のコマンドを実行しKerasライブラリと必要なモジュールをインストールする。
```
sudo pip3 install keras==2.1.2
sudo pip3 install scipy
sudo pip3 install h5py
sudo apt-get install python-scipy
sudo apt-get install h5py
```

4. スワップ領域の拡大
Kerasの実行時のメモリ不足を避けるために、OSのスワップ領域を増やす。
```
sudo nano /etc/dphys-swapfile
```
`CONF_SWAPSIZE=100`の箇所の数字を`1024`に変更、ファイルをセーブしてエディタ終了。下記コマンドを実行する。
```
sudo /etc/init.d/dphys-swapfile restart
swapon -s
```

5. Keras動作テスト
Keras Documentationの[サンプルコード](https://keras.io/applications/)を用いてKerasの動作確認を行う。
「Classify ImageNet classes with ResNet50」の箇所にあるソースコードをコピーし、`resnet50.py`というファイル名で保存する。
物体認識のテスト用の画像データをダウンロードする。
```
wget https://i1.wp.com/yroy.me/wp-content/uploads/2017/04/elephant.jpeg
mv elephant.jpeg elephant.jpg
```
下記コマンドによりKerasを用いた物体認識を実行する。期待通りの結果が出るか確認する。
```
python3 resnet50.py
```

6. Kerasを用いたサンプルプログラムの実行
>Note:  
>`mjpg-streamer`を実行させた状態で`image_classification_resnet50`および`image_classification_mobilenet.py`を実行してください。
- ResNet50
```
wget https://raw.githubusercontent.com/yoshihiroo/programming-workshop/master/rpi_ai_handson/image_classification_resnet50.py
python3 image_classification_resnet50
```
- MobileNet
```
wget https://raw.githubusercontent.com/yoshihiroo/programming-workshop/master/rpi_ai_handson/image_classification_mobilenet.py
python3 image_classification_mobilenet.py
```
>Note:  
>いずれのプログラムもKeras Documentationの[サンプルコード](https://keras.io/applications/)をもとに修正を加えたものです。

X. このあと
自宅など他の無線LANに接続する場合は「2. ヘッドレスセットアップのための準備」と同様に、ルートディレクトリに`wpa_supplicant.conf`ファイルを置くことで設定ファイルが上書きされます。
