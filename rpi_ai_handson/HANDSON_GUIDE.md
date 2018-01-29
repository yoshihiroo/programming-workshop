以下の内容はハンズオン当日までドラフトとなります。


ラズパイのヘッドレスセットアップ (a)USB-シリアルケーブルを使う方法
------------
1. SDカード上のファイルの編集

OSイメージが書き込まれたSDカードをパソコンのSDカードリーダーで開き、`boot`ドライブ直下の`config.txt`の最後尾に`enable_uart=1`という行を追記する。

2. USB-シリアルケーブルの接続

* 4色のコネクターを[PIN配置の図](https://docs.microsoft.com/en-us/windows/iot-core/learn-about-hardware/pinmappings/pinmappingsrpi)を参照しながら下記の通り接続する(右上付近のPIN)

>** **注意！** ** ラズパイ本体の2番と4番ピン(5V PWR)からは5V電圧が出ていますので、くれぐれも誤ってケーブルを刺さないよう注意してください。

| コネクターの色 | ラズパイPIN |
----|----
| 黒 | 6番 GND |
| 白 | 8番 TX |
| 緑 | 10番 RX |
| 赤 | どこにも刺さない |

* ケーブルのUSBコネクターをPCのUSBポートに接続する。

3. ターミナル接続  

* デバイスマネージャーで接続されているポート番号を確認する
* PC上のターミナルソフトを開き、シリアル通信のポート番号を選択、ボーレートを115200に設定する

4. Raspberry Piの起動  

パソコンからSDカードを取り出し、RPi本体に入れて起動する。

5. Wifi設定  
`/etc/wpa_supplicant/wpa_supplicant.conf`をエディターで開き下記のように変更する。
```
country=GB
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
        ssid="<SSID名>"
        psk="<パスワード>"
}
```

`/etc/init.d/networking restart`コマンド実行によってWiFiに接続される。


ラズパイのヘッドレスセットアップ (b)無線LAN接続を用いる方法
------------
>Note:  
>(a)USB-シリアルケーブルを使う方法がうまくいかない場合、この(b)の方法をとってください

1. ヘッドレスセットアップのための準備  
OSイメージが書き込まれたSDカードをパソコンのSDカードリーダーで開き、`boot`ドライブ直下に中身が空の`ssh`ファイルと、下記の内容の`wpa_supplicant.conf`ファイルを置く。使用する無線LAN環境に合わせてSSID名とパスワードの箇所を変える。
```
country=GB
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
        ssid="<SSID名>"
        psk="<パスワード>"
}
```

2. Raspberry Piの起動  
パソコンからSDカードを取り出し、RPi本体に入れて起動する。

3. IPアドレスの確認  
同じネットワークセグメントにつながっているパソコンから下記コマンドでRasperry PiのIPアドレスを探す(下記はWindows上のコマンドプロンプトを使う場合)。
Raspberry PiのMACアドレスは`B8-27-EB`から始まるので、それらに紐づいているIPアドレスを探す。
```
for /l %i in (0,1,255) do ping -w 1 -n 1 192.168.1.%i && arp -a 192.168.1.%i  
arp -a
```
>Note:  
>`192.168.1`の部分は利用するネットワーク環境に合わせて変更してください。

4. ssh経由でRaspberry Piにリモートログイン  
クライアントプログラムは[Tera Term(Windows)](https://forest.watch.impress.co.jp/library/software/utf8teraterm/)や、Chromeブラウザーの[Secure Shell](https://chrome.google.com/webstore/detail/secure-shell/pnhechapfaindjhompbnflcldabbghjo?hl=ja)などがお勧め。
sshクライアントから上記で調べたIPアドレスにログインする。

5. MACアドレスを確認する  
複数人で同時にヘッドレスセットアップを行うので、個体の特定が必要となる。下記コマンドでRaspberry Pi本体の赤色LEDを点滅させ、上記4節で調べたIPアドレスと突き合わせることで本体のMACアドレスを把握することができる。
```
echo heartbeat | sudo tee /sys/class/leds/led1/trigger
```
特定できたら下記コマンドで元の状態に戻しておく。
```
echo input | sudo tee /sys/class/leds/led1/trigger
```

以下、上記で調べたRaspberry PiのIPアドレスにログインしなおしてから設定を続ける。


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
| nano <ファイル名> | エディターを開く（Ctrl+oでセーブ、Ctrl+xで終了） |
| less <ファイル名> | ファイルの内容を表示する |


カメラ画像の配信
------------
1. raspi-config設定  

piユーザーのパスワード設定、タイムゾーンの設定、およびカメラモジュールの有効化を行う。
```
sudo raspi-config
```
- Change User Password -> piユーザーのパスワードを変更
- Localisation Options -> Change Timezone -> Asia -> Tokyo
- Interfacing Options -> Camera -> (Would you like the camera...) -> Yes  

そのあとFinishを選び、指示通りにシステム再起動(reboot)する。
>Note:  
>`sudo`を使うことで管理者権限でコマンドが実行されます。
>`pi`ユーザーはRaspberry Piのデフォルトユーザーなので、セキュリティー対策上、パスワードを変更してから作業をするようにしましょう。

2. OSのモジュールを最新にアップデートする  
```
sudo apt-get update
sudo apt-get upgrade
```
>Note:  
>何らかプログラムをインストールする際には、上の二つのコマンドを実行し、事前にOSのモジュールを最新の状態にすることをお勧めします。 

3. 配信プログラム(mjpg-streamer)のインストール  

下記コマンドを実行し、Pi Cameraがアクティブになっているか確認する。
```
vcgencmd get_camera
```
正しく動いていれば`supported=1 detected=1`という結果が返ってくる。  

次に、下記コマンドを実行して`mjpg-streamer`をインストールする。
```
sudo apt-get install libjpeg9-dev cmake
sudo git clone https://github.com/jacksonliam/mjpg-streamer.git mjpg-streamer
cd mjpg-streamer/mjpg-streamer-experimental
sudo make
cd
sudo mv mjpg-streamer/mjpg-streamer-experimental /opt/mjpg-streamer
```

続いて、mjpg-streamer起動スクリプトを作成する。  
`nano start_stream.sh`と打ってnanoエディタを開き、下記の内容をコピーして保存終了する。
```
#!/bin/bash

if pgrep mjpg_streamer > /dev/null
then
echo "mjpg_streamer already running"
else
LD_LIBRARY_PATH=/opt/mjpg-streamer/ /opt/mjpg-streamer/mjpg_streamer -i "input_raspicam.so -fps 10 -q 50 -x 320 -y 240" -o "output_http.so -p 9000 -w /opt/mjpg-streamer/www" > /dev/null 2>&1&
echo "mjpg_streamer started"
fi
```

スクリプトの保存終了後、`chmod 755 start_stream.sh`コマンドで実行フラグを立てておく。

4. mjpg-streamerの動作確認  

ホームディレクトリ上で`./start_stream.sh`と打ち、mjpg-streamerを起動させたのち、WebブラウザでRaspberry PiのIPアドレス、ポート9000番にアクセスすることでカメラからの配信画像が見れる。  

例：`http://192.168.xx.xx:9000`  

mjpg-streamerを終了させたいときは、`ps`コマンドでプロセス番号を調べて`kill`コマンドで修了させる。

>Note:  
>この節の内容は[こちらのブログ記事](https://kitto-yakudatsu.com/archives/2338)を参考にさせてもらいました。


MNIST文字認識の実装
------------
1. `cd`コマンドを実行し、自分のホームディレクトリに戻る  
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
wget https://raw.githubusercontent.com/yoshihiroo/programming-workshop/master/rpi_ai_handson/digit_recognition_NN.py
python3 digit_recognition_NN.py
```

- 畳み込みニューラルネットワークによる推論
`/home/pi/deep-learning-from-scratch/ch07`ディレクトリ上で下記コマンドを実行する。
```
wget https://raw.githubusercontent.com/yoshihiroo/programming-workshop/master/rpi_ai_handson/digit_recognition_CNN.py
python3 digit_recognition_CNN.py
```

Kerasによる物体識別の実装
------------
1. TensorFlowのインストール  
[ブログ記事(Cross-compiling TensorFlow for the Raspberry Pi)](https://petewarden.com/2017/08/20/cross-compiling-tensorflow-for-the-raspberry-pi/)の中盤の「If you’re running Python 3.5」から始まる箇所のガイドに従ってTensorFlowをインストールする。

```
sudo apt-get install libblas-dev liblapack-dev python-dev libatlas-base-dev gfortran python-setuptools
curl -O http://ci.tensorflow.org/view/Nightly/job/nightly-pi-python3/lastSuccessfulBuild/artifact/output-artifacts/tensorflow-1.5.0rc1-cp34-none-any.whl
mv tensorflow-1.5.0rc1-cp34-none-any.whl tensorflow-1.5.0rc1-cp35-none-any.whl
sudo pip3 install tensorflow-1.5.0rc1-cp35-none-any.whl
```
>Note:  
>上記は2018/1/20時点でのパッケージ名を用いていますが、今後のバージョンアップに伴い適宜パッケージ名を変更してください。[プロジェクトのサイト](http://ci.tensorflow.org/view/Nightly/job/nightly-pi-python3/)でファイル名を確認できます。

2. TensorFlow動作テスト  
```
wget https://raw.githubusercontent.com/yusugomori/deeplearning-tensorflow-keras/master/3/tensorflow/01_logistic_regression_or_tensorflow.py
python3 01_logistic_regression_or_tensorflow.py
```
上記コマンドを実行すると、Python3.4用のTensorFlowのモジュールをPython3.5で使っているためwarningが出るが、下記の結果が出力される。
```
classified:
[[ True]
 [ True]
 [ True]
 [ True]]

output probability:
[[ 0.22355059]
 [ 0.91425598]
 [ 0.91425598]
 [ 0.9974739 ]]
```

>Note:  
>[「詳解 ディープラーニング TensorFlow・Kerasによる時系列データ処理」](https://book.mynavi.jp/ec/products/detail/id=72995)からのサンプルコードとなります。

3. Kerasのインストール  
下記のコマンドを実行しKerasライブラリと必要なモジュールをインストールする。
```
sudo pip3 install keras==2.1.3
sudo pip3 install h5py
sudo apt-get install python-h5py
sudo pip3 install numpy --upgrade
```
>Note:  
>TensorFlowと同様にKerasについても最新バージョンを[ウェブサイト](https://pypi.python.org/pypi/Keras)で確認したうえで、上記の`2.1.3`の箇所を変更してください。


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
wget https://github.com/yoshihiroo/programming-workshop/raw/master/rpi_ai_handson/elephant.jpg
```
下記コマンドによりKerasを用いた物体認識を実行する。期待通りの結果が出るか確認する。
最初の実行時には`Downloading data from..`のメッセージとともにh5ファイルとjsonファイルがダウンロードされる。
```
python3 resnet50.py
```

6. Kerasを用いたサンプルプログラムの実行  
>Note:  
>`mjpg-streamer`を実行させた状態で`image_classification_resnet50`および`image_classification_mobilenet.py`を実行してください。
- ResNet50
```
wget https://raw.githubusercontent.com/yoshihiroo/programming-workshop/master/rpi_ai_handson/image_classification_resnet50.py
python3 image_classification_resnet50.py
```
- MobileNet
```
wget https://raw.githubusercontent.com/yoshihiroo/programming-workshop/master/rpi_ai_handson/image_classification_mobilenet.py
python3 image_classification_mobilenet.py
```
>Note:  
>いずれのプログラムもKeras Documentationの[サンプルコード](https://keras.io/applications/)をもとに修正を加えたものです。

(オプション)その他の設定
------------
1. 別の無線LANへの接続 

自宅など他の無線LANに接続する場合は「2. ヘッドレスセットアップのための準備」と同様に、ルートディレクトリに`wpa_supplicant.conf`ファイルを置くことで設定ファイルが上書きされる。

2. VNCの設定 

VNCを使うと、リモートからデスクトップ環境を使うことができる。
全体の流れはRaspberry Piサイトの[ドキュメント](https://www.raspberrypi.org/documentation/remote-access/vnc/)を参照のこと。
```
sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
```
加えて、`sudo raspi-config`から、
Interfacing Options -> VNC -> (Would you like the VNC...) -> Yes
の設定を行う。

クライアント側には[VNC Viewer](https://www.realvnc.com/download/viewer/)をダウンロード、インストールする。

デフォルトではリモート(Raspberry Pi)側の画面が狭いので、`/boot/config.txt`の下記箇所をコメントアウトを外し変更を保存、Raspberry Piを再起動させる。
```
framebuffer_width=1280
framebuffer_height=720
```
再起動後、VNC ViewerからRaspberry PiのIPアドレスを指定しログインを行うと、デスクトップ画面が表示される。

-----
参照した外部情報は[References](https://github.com/yoshihiroo/programming-workshop/blob/master/rpi_ai_handson/REFERENCES.md)にまとめました
