# AWSセットアップ

## セキュリティーグループを作成
TCPポート8888を解放

## 固定IPアドレスの設定
インスタンス起動時や再起動時にIPアドレスが毎回変わってしまうと不便なので、Elastic IPを使って固定アドレスを取得しておくと良い。

## AWSインスタンス作成
- Ubuntu Server 16.04 LTS
- t2.micro(無償枠)
- ストレージ30GB
- セキュリティーグループの設定 先ほど作成したものに紐づけ
- IPアドレスをElastic IPで設定したものに紐づけ

以下、AWSコンソールにログインした状態で設定を行う。

## Anacondaパッケージのインストール
[https://repo.continuum.io/archive/](https://repo.continuum.io/archive/)で最新パージョンを確認。下記の例は`Anaconda3-5.0.0.1-Linux-x86_64`。

```
sudo apt update
sudo apt upgrade
sudo apt install wget pkg-config make gcc binutils
wget https://repo.continuum.io/archive/Anaconda3-5.0.0.1-Linux-x86_64.sh
bash ./Anaconda3-5.0.0.1-Linux-x86_64.sh
## 途中Enter/yesで回答
source .bashrc
```

## Jupyterの設定ファイルの作成
`jupyter notebook --generate-config`  
~/.jupyter/jupyter_notebook_config.pyが作成される

## Jupyter LoginのPassword設定
以下のコマンドを実行するとPasswordを入れるPromptがでるので、設定したいPasswordを入力する。  
`python -c "import IPython;print(IPython.lib.passwd())"`

jupyter_notebook_config.pyの先頭に下記を追記  
```
c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
c.NotebookApp.password = u'sha1:xxxxxxxxxx(ここに先ほどのパスワードを記載)xxxxxxxxxxx'
```

## ワークショップ用のファイルの配置
このドキュメントファイルと同じディレクトリにある`workshop.tar.gz`をダウンロードし、AWSのボリュームに転送する。
ホームディレクトリ上でファイルを解凍する。
```
cd ~
wget https://github.com/yoshihiroo/programming-workshop/raw/master/deep_learning_jupyter/workshop.tar.gz
tar zxvf workshop.tar.gz
```
レクチャー中に誤ってnotebookを削除してしまわないように、`sudo chattr +i <ファイル名>`で削除不可のフラグを立ておくと良い。

## Jupyterのプロセスを起動
レクチャー用のファイルがあるディレクトリに移動し、jupyterを起動する。
```
cd workshop
cd notebook
jupyter notebook
```

コンソールからログオフした状態でnotebookを動作させ続けたい場合には、最後の行を`nohup jupyter notebook > .nohup.out &`に置き換える。その場合、Jupyterを終了するには`ps`コマンドで該当するPIDを確認し、`kill`コマンドでプロセスを終了させる。

## Jupyterへのログイン
PCのwebブラウザに直接URL(http://<IPアドレス>:8888)を入力し、Jupyter環境にログインする。パスワードを求められるので、上で設定したものを入力する。
なお、AWS環境構築後、初めて`file3_gakusyu.ipynb`の「3-1. MNISTデータの表示」を実行する際、データファイルをダウンロードしてくるので、少し時間がかかる。画面に下記ダウンロード状況が表示される。
```
Downloading train-images-idx3-ubyte.gz ... 
Done
Downloading train-labels-idx1-ubyte.gz ... 
Done
Downloading t10k-images-idx3-ubyte.gz ... 
Done
Downloading t10k-labels-idx1-ubyte.gz ... 
Done
Converting train-images-idx3-ubyte.gz to NumPy Array ...
Done
Converting train-labels-idx1-ubyte.gz to NumPy Array ...
Done
Converting t10k-images-idx3-ubyte.gz to NumPy Array ...
Done
Converting t10k-labels-idx1-ubyte.gz to NumPy Array ...
Done
Creating pickle file ...
Done!
```


