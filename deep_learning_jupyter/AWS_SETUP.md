# AWSセットアップ

## セキュリティーグループを作成
TCPポート8888を解放

## AWSインスタンス作成
- Ubuntu Server 16.04 LTS
- t2.micro(無償枠)
- ストレージ30GB
- セキュリティーグループの設定 先ほど作成したものに紐づけ

## Anacondaパッケージのインストール
`[https://repo.continuum.io/archive/](https://repo.continuum.io/archive/)`で最新パージョンを確認。下記の例は`Anaconda3-5.0.0.1-Linux-x86_64`。

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

jupyter_notebook_config.pyの先頭に下記を追記  
```
c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
c.NotebookApp.token = ''
```

## Jupyter LoginのPassword設定
以下のコマンドを実行するとPasswordを入れるPromptがでるので、設定したいPasswordを入力する。  
`python -c "import IPython;print(IPython.lib.passwd())"`

## コンフィグファイルの書き換え
```
c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
c.NotebookApp.password = u'sha1:xxxxxxxxxx(ここに先ほどのパスワードを記載)xxxxxxxxxxx'
```

## (必要に応じて)Tensorflow, Karasのインストール
```
pip install --upgrade pip
pip install tensorflow
pip install keras
```
