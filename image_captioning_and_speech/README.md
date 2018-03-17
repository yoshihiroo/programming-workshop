Deep Learning on Raspberry Pi - Real time Image Captioning and Speech
-------
![Overview](https://raw.githubusercontent.com/yoshihiroo/programming-workshop/master/image_captioning_and_speech/figure/WS000000.JPG)

Hardwares used in this project
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

Install programs and tools for this project
-------
* Install Git by `sudo apt-get install git`
* Install pip for Python 3 by `sudo apt-get install python3-pip`
* Install Chainer Framework by `sudo pip3 install chainer==1.19.0`
* Install speech software by `sudo apt-get install espeak`
* Install Python camera module by `apt-get install python3-picamera`

