機材購入ガイド
-------
1. 全員
* [Raspberry Pi 3本体(ケース付き)](https://www.amazon.co.jp/dp/B01CSFZ4JG)
* [Raspberry Pi用電源セット(5V 3.0A)](https://www.amazon.co.jp/dp/B01N8ZIJL8)
* [microSDカード 32GB Class10](https://www.amazon.co.jp/dp/B06XSV23T1)
* [Raspberry Pi用カメラモジュール](https://www.amazon.co.jp/dp/B00FGKYHXA)  

>Note:  
>それぞれ相当品であれば、アマゾン以外で買うでももちろん可ですが、下記にお気を付けください。
>- サイトによっては海外からの郵送となり数週間納期がかかるケースありますので、ハンズオンに間に合うように納期見通しにご注意ください
>- Raspberry Piには種類がいくつかありますが、**3**を入手ください
>- 電源アダプター：スマホ用のUSB電源アダプタだとアンペア数が足りないので、2.5A以上、できれば上記のような**3.0A品**が良いです
>- SDカード：容量は**16GB以上**、スピードは**Class10**を選んでください

2. 当日持参するノートパソコンにSDカードリーダーが付いてないかたのみ
* SDカードリーダー  
SDカードをパソコンで読み書きするためのUSBデバイスとなります。アマゾンで見つけたものをリンク張っておきますが、相当品であればどれでも良いと思います。値段にピンキリあるようですので、納期にも気を付けながらお選びください。https://www.amazon.co.jp/dp/B01JGNPNQW/

3. すでにラズパイ3をお持ちの方やすでに使われている方  
* ハンズオン用microSDカード  
ハンズオンでOSを新規に入れなおしますので、既存のOSやデータを残したい方は各自バックアップを取るか、今回のハンズオン用にmicroSDカードをご用意ください

事前の準備
-------
1. ハンズオンに使うツール類のダウンロードとインストール  
ハンズオン当日持参する各自のPCに下記ツールを事前にインストールしておいてください。会社貸与のPC等、セキュリティー対策でインストールをできなくしている場合がありますので、インストール、起動が可能か、事前に確認しておいてください。
* 解凍ツール -- [7Zip](http://www.7-zip.org/download.html) (Windows) or [The Unarchiver](http://www.7-zip.org/download.html) (Mac)
* OSイメージ書き込みツール -- [Etcher](https://etcher.io/) (Windows/Mac共通)
* ターミナルソフト(Windowsの方のみ) -- [Tera Term(Windows)](https://forest.watch.impress.co.jp/library/software/utf8teraterm/)、もしくはChromeブラウザーの方は拡張機能[Secure Shell](https://chrome.google.com/webstore/detail/secure-shell/pnhechapfaindjhompbnflcldabbghjo?hl=ja)でも良い

2. OSイメージのダウンロード  
ファイルの大きさが数ギガバイトあり、ダウンロードに時間がかかりますので、下記リンクより各自のPCに事前にダウンロードをしておいてください。またこのファイルを解凍すると約6ギガバイトのファイルになりますのでPCのハードディスクの空き容量にもご注意ください。  
* [RASPBIAN STRETCH WITH DESKTOP(Release date:2017-11-29)](https://downloads.raspberrypi.org/raspbian_latest)

3. 起動の確認  
大まかな手順は、以下の流れになります。  
* ダウンロードしたOSイメージをPC上のEtcherを使ってSDカードにコピーする
* OSイメージが入ったSDカードをRaspberry Pi本体に挿し込む
* Raspberry Pi本体をテレビのHDMIにつなげる
* Raspberry Pi本体をUSB電源につなぐ

正常に起動すると、Raspberry Piの電源(赤LED)が点灯し、SDカードのアクセス時に緑LEDが点灯します。
TVの画面上には、最初に虹色のテスト画像が映ったあと、最初の起動時には自動的に一度だけ再起動がかかります。
再起動後しばらく待つとGUIデスクトップ画面が映ります。

もしLEDが点灯しない、起動プロセスが進まないなどの現象が起きた場合は機材の不良や、OSイメージを正しくコピーできてないなどの原因が考えられます。
