| ドキュメント | 内容 |
----|----
| [README.md](https://github.com/yoshihiroo/programming-workshop/blob/master/rpi_ai_handson/README.md#%E6%A9%9F%E6%9D%90%E8%B3%BC%E5%85%A5%E3%82%AC%E3%82%A4%E3%83%89) | 当ドキュメント。機材購入ガイド、事前の準備 |
| [HANDSON_GUIDE.md](https://github.com/yoshihiroo/programming-workshop/blob/master/rpi_ai_handson/HANDSON_GUIDE.md) | ハンズオン当日に使うガイド。実装の詳細なステップ |
| [REFERENCES.md](https://github.com/yoshihiroo/programming-workshop/blob/master/rpi_ai_handson/REFERENCES.md) | ガイド作成にあたって参考にした外部情報、リンク |

----

機材購入ガイド
-------
1. 全員
* [Raspberry Pi 3本体(ケース付き)](https://www.amazon.co.jp/dp/B01CSFZ4JG)
* [Raspberry Pi用電源セット(5V 3.0A)](https://www.amazon.co.jp/dp/B01N8ZIJL8)
* [microSDカード 32GB Class10](https://www.amazon.co.jp/dp/B06XSV23T1)
* [Raspberry Pi用カメラモジュール](https://www.amazon.co.jp/dp/B00FGKYHXA)  
* [USB-シリアル変換ケーブル](https://www.amazon.co.jp/dp/B00K7YYFNM)

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
* USB-シリアル変換ケーブル用ドライバー
  * Windows -- ケーブルが手元に届いたら[Prolific USB To Serial Driver "Code 10" Fix](http://www.ifamilysoftware.com/news37.html)を参照のうえ、Windows 64bit|32bitに気を付けながら指示通りにセットアップを行ってください。インストールが完了したら、ケーブルをPCのUSBポートに接続した状態(色のついた4本の細いコネクタ側は未接続のまま)で、デバイスマネージャーの「ポート(COMとLPT)」にデバイスが正しく見えることを確認してください。
  * Mac -- [Raspberry Pi 3 事前準備設定](https://github.com/ysfmiwn/raspberry-pi/blob/master/README.md)を参照ください。(岩野義史さん、わかりやすくまとめてくださって、ありがとうございます！)

2. OSイメージのダウンロード  
ファイルの大きさが数ギガバイトあり、ダウンロードに時間がかかりますので、下記リンクより各自のPCに事前にダウンロードをしておいてください。またこのファイルを解凍すると約6ギガバイトのファイルになりますのでPCのハードディスクの空き容量にもご注意ください。  
* [RASPBIAN STRETCH WITH DESKTOP(Release date:2017-11-29)](http://ftp.jaist.ac.jp/pub/raspberrypi/raspbian/images/raspbian-2017-12-01/2017-11-29-raspbian-stretch.zip)

3. 起動の確認  
大まかな手順は、以下の流れになります。
* ダウンロードしたOSイメージを解凍する
* Etcherを使ってSDカードにコピーする([参考サイト](http://www.moongift.jp/2017/10/etcher-3ステップで簡単にイメージ書き込み/))
* OSイメージが入ったSDカードをRaspberry Pi本体に挿し込む
* Raspberry Pi本体をテレビのHDMIにつなげる
* Raspberry Pi本体をUSB電源につなぐ

Raspberry Pi本体には電源スイッチは無く、USB電源アダプターにつなぐとそのまま電源が入ります。
正常に起動すると、Raspberry Piの電源(赤LED)が点灯し、SDカードのアクセス時に緑LEDが点灯します。
テレビの画面上には、最初に虹色のテスト画像が映ったあと、初回の起動時には自動的に一度だけ再起動がかかります。
再起動後しばらく待つとGUIデスクトップ画面が映ります。OSの起動が確認できたらSDカードのアクセス(緑LED点灯)が落ち着いたところを見計らって電源を抜いてください。  

もしテレビへのHDMI接続が難しい方は、Raspberry Pi本体をUSB電源につなぎ、通電のみでも確認しておいてください。電源の赤LED、SDカードアクセスの緑LEDが点灯します。テレビがない場合は起動の状態が目視できませんが、SDカードへのアクセスが落ち着くまで2、3分待ってから、電源を抜いてください。
