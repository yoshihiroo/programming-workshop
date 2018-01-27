References
------------

Raspberry Piで何かを実装するまでの道のりは「守・破・離」、そして「試行錯誤」の連続です。

1. 実装事例・ブログをググる（例：「Raspberry Pi Camera 画像認識」）
2. やりたいことに近い事例を真似てみる
3. (ブログの通りにやっても動かないことが多いので) 出てくるエラーメッセージなどをググって解決策を試す

これらを繰り返し、やりたいことが「ひとまず動く状態」を作ります。そしてそこに自分なりの改良や、他のアイデアとの組み合わせを加えていきます。

あとで追試ができるように、試した内容や打ったコマンドはメモを残しておくことを強くお勧めします。
試行錯誤の過程で掴んだ解決策はそのときは覚えているようで、すぐに忘れてしまいます。同じハマりかたで時間の浪費を避けるためにもメモを残しましょう。

>Note:  
>私の場合はEvernote Web Clipperというブラウザの拡張機能を使って、情報を見つけた際に片っ端からEvernoteにためていってます。自分が打ったコマンドも汚いドラフト状態でまずはEvernoteにコピペしてあとで追試しながら整理していくようにしています。

いったん動く状態になったとしても、OS、ライブラリ、プログラムが刻々とバージョンアップしていく中で、
ブログの情報が古くなる、バージョン間の相性が合わなくなるなどで動かなくなるケースが多々あります。そのたびに情報のメンテナンスが必要です。

----
今回のラズパイAI実装ハンズオンのコンテンツを作る際に参考にした情報を以下にまとめます。順不同です。




#### 実装事例
- [TensorFlow on Raspberrry Pi3 - Qiita](https://qiita.com/nanbuwks/items/1a259e780d439330828b)
- [Raspberry Pi 3にkeras+tensorflow+openCV環境構築 - Mnemosyne](http://infotech.hateblo.jp/entry/2017/12/03/025905)
- [Raspberry Pi を使ってみる - Attic or Garret](http://itoi.jp/raspberrypi.html)
- [Raspberry Pi 深層学習ライブラリで物体認識（Keras with TensorFlow・Open CV） - Qiita](https://qiita.com/PonDad/items/c5419c164b4f2efee368)
- [VGG16のFine-tuningによる犬猫認識 (2) - 人工知能に関する断創録](http://aidiary.hatenablog.com/entry/20170110/1484057655)

#### Tensorflow/Kerasフレームワーク
- [Deep Residual Learning(ResNet)の実装から比較するディープラーニングフレームワーク - 俺とプログラミング](http://www.iandprogram.net/entry/2016/06/06/180806)
- [Kerasの作者@fcholletさんのCVPR'17論文XceptionとGoogleのMobileNets論文を読んだ - Qiita](https://qiita.com/yu4u/items/34cd33b944d8bdca142d)
- [Raspberry Pi 人工知能ツールをインストール【Python3】 - Qiita](https://qiita.com/PonDad/items/9fbdf4d694f825dd1b6e)
- [ディープラーニング実践入門 〜 Kerasライブラリで画像認識をはじめよう！ - エンジニアHub｜若手Webエンジニアのキャリアを考える！](https://employment.en-japan.com/engineerhub/entry/2017/04/28/110000)
- [TensorFlowの使い方 - Raspberry Pi 3 & Python 開発ブログ☆彡](http://www.raspberrypirulo.net/entry/2017/04/02/TensorFlow%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9)

#### カメラモジュール
- [専用カメラモジュールを使う](https://raspi-wannabe.com/digital-camera/)
- [PythonでRaspberry Pi カメラを制御する](https://iotdiyclub.net/raspberry-pi-camera-python-1/)
- [第8回: MJPG-streamerのインストール – Blue-black.ink](http://blue-black.ink/?page_id=2245)
- [5GHz WiFi対応させたPi Zero rev1.3とPi Cameraでミニマムなネットワークカメラを作ってみた（mjpg-streamer版）](https://kitto-yakudatsu.com/archives/2338)
