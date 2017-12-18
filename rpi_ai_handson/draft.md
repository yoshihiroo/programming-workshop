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
