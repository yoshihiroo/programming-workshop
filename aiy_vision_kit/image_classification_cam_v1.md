Raspberry Pi Zero W + VisionBonnet accessory board + Camera Module Version 1によるカメラ画像分類
------------

ディープラーニングを使ったカメラ画像認識をRaspberry Pi上に実装する。
Raspberry Pi Zero Wに[Vision Kit](https://aiyprojects.withgoogle.com/vision/)のVisionBonnet accessory boardをにアタッチすることで、ほぼリアルタイムな分類処理を実現する。
また、Vision Kit組み立てにはカメラモジュールのv2が必要となるが、今回はv1カメラを用いて実装を行う。

1. セットアップ  
- [本家サイト](https://aiyprojects.withgoogle.com/vision/)からVision Kit SD Imageをダウンロードし、[Etcher](https://etcher.io/)などのライティングツールを使ってSDカードにイメージファイルを書き込む。
- 11mm plastic standoffs(スペーサー)を間に挟みながら、40-pinを使ってRaspberry PiとVisionBonnetを結合する。その際、MIPI flat flex cableによる接続は**しない**。
 
