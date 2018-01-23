Raspberry Pi Zero W + VisionBonnet accessory board + Camera Module Version 1によるカメラ画像分類
------------

ディープラーニングを使ったカメラ画像認識をRaspberry Pi Zero W(以下Pi Zero)上に実装する。
Pi Zeroに[Vision Kit](https://aiyprojects.withgoogle.com/vision/)のVisionBonnet accessory boardをにアタッチすることで、ほぼリアルタイムな分類処理を実現する。
また、Vision Kit組み立てにはカメラモジュールのV2が必要となるが、今回はV1のカメラモジュールを用いて実装を行う。

1. ハードウェア・セットアップ
- [本家サイト](https://aiyprojects.withgoogle.com/vision/)からVision Kit SD Imageをダウンロードし、[Etcher](https://etcher.io/)などのライティングツールを使ってSDカードにイメージファイルを書き込む
- SDカードをPi Zeroのスロットに挿入する
- 11mm plastic standoffs(スペーサー)を間に挟みながら、40-pinを使ってPi ZeroとVisionBonnetを結合する。その際、MIPI flat flex cableによる接続は**しない**
- カメラモジュール**V1**を**Pi Zero**に接続する

2. ソフトウェア・セットアップ  
- Joy Demo起動の解除

デフォルトではブート後に`Joy Demo application`が自動で起動する設定になっているので、それを解除しておく。
```
sudo systemctl stop joy_detection_demo.service
sudo systemctl disable joy_detection_demo.service
```

- カメラモジュールの有効化
raspi-configを立ち上げ、`Interfacing Options`から`Camera -> (Would you like the camera...) -> Yes`を選択し、設定を終了。指示通りシステムを再起動させる。

- OSのモジュールを最新にアップデートする  
```
sudo apt-get update
sudo apt-get upgrade
```

- 配信プログラム(mjpg-streamer)のインストール  

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
LD_LIBRARY_PATH=/opt/mjpg-streamer/ /opt/mjpg-streamer/mjpg_streamer -i "input_raspicam.so -fps 15 -q 50 -x 256 -y 256" -o "output_http.so -p 9000 -w /opt/mjpg-streamer/www" > /dev/null 2>&1&
echo "mjpg_streamer started"
fi
```

スクリプトの保存終了後、`chmod 755 start_stream.sh`コマンドで実行フラグを立てておく。

- mjpg-streamerの動作確認  

ホームディレクトリ上で`./start_stream.sh`と打ち、mjpg-streamerを起動させたのち、WebブラウザでPi ZeroのIPアドレス、ポート9000番にアクセスすることでカメラからの配信画像が見れる。  

例：`http://192.168.xx.xx:9000`  

mjpg-streamerを終了させたいときは、`ps`コマンドでプロセス番号を調べて`kill`コマンドで修了させる。

>Note:  
>この節の内容は[こちらのブログ記事](https://kitto-yakudatsu.com/archives/2338)を参考にさせてもらいました。

3. 画像分類の実行
- virtualenvを起動する

```
source ~/AIY-projects-python/env/bin/activate
```

- `mjpg-streamer`を実行させた状態で、下記を実行し`image_classification`を実行する

```
wget https://raw.githubusercontent.com/yoshihiroo/programming-workshop/master/rpi_ai_handson/image_classification_resnet50.py
python3 image_classification_resnet50.py
```

