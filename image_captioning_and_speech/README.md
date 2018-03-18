Deep Learning on Raspberry Pi - Real Time Image Captioning and Speech
-------
![Overview](https://raw.githubusercontent.com/yoshihiroo/programming-workshop/master/image_captioning_and_speech/figure/WS000000.JPG)

>This project is based on [the source code created by Satoshi Tsutsui](https://github.com/apple2373/chainer_caption_generation) and I added several codes.

Hardwares Used in This Project
-------
* Raspberry Pi 3
* Camera module
* External speaker
* Mobile battery

Raspbian OS Setup
-------
* Setup Raspbian OS environment refering to [Rasbpberry Pi web site](https://www.raspberrypi.org/documentation/installation/installing-images/) (Assuming to use RASPBIAN LITE version)
* Enable camera module by `sudo raspi-config` -> Interfacing Options -> Camera -> "Would you like..." -> Yes and reboot
* Change time zone as necessary by Localisation Options -> Change Timezone
* Update OS by `sudo apt-get update` followed by `sudo apt-get upgrade`

Install Programs and Tools
-------
Install required programs and tools by commands below.
```
sudo apt-get install git
sudo apt-get install python3-pip
sudo pip3 install chainer==1.19.0
sudo pip3 install Pillow
sudo apt-get install espeak
sudo apt-get install python3-picamera
```

Download Source Codes and Run
-------
Download from the Git repository and test sample code by commands below.
```
git clone https://github.com/apple2373/chainer-caption.git
cd chainer-caption
bash download.sh
python3 sample_code_beam.py --rnn-model ./data/caption_en_model40.model --cnn-model ./data/ResNet50.model --vocab ./data/MSCOCO/mscoco_caption_train2014_processed_dic.json --gpu -1 --img ./sample_imgs/COCO_val2014_000000185546.jpg
```

If installed properly, the result will be displayed as below. There might be some warnings.

```
<sos> a bathroom with a toilet and a shower <eos>
-6.967587262392044
<sos> a bathroom with a toilet , sink , and mirror <eos>
-7.618740811944008
<sos> a bathroom with a toilet , sink , and shower <eos>
-8.537529528141022
```
  
