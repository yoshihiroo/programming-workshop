Image classification by Raspberry Pi Zero W + VisionBonnet accessory board + Camera Camera Module Version 1
------------

[![](https://img.youtube.com/vi/-ZhVdgR4h6w/0.jpg)](https://www.youtube.com/watch?v=-ZhVdgR4h6w)

Implement camera image recognition using deep learning on Raspberry Pi Zero W (Pi Zero).
By attaching VisionBonnet accessory board of [Vision Kit](https://aiyprojects.withgoogle.com/vision/) to Pi Zero, almost real time classification processing is realized.
Camera Module V2 is required for assembling the Vision Kit, but this time we will implement it using Camera Module V1.

1. Hardware Setup
- Download Vision Kit SD Image from [Vision Kit web site](https://aiyprojects.withgoogle.com/vision/) and use the writing tool such as [Etcher](https://etcher.io/) to write image file to SD card.
- Insert the SD card into the slot of Pi Zero
- While pinching 11 mm plastic standoffs (spacer), join Pi Zero and VisionBonnet using 40-pin. At that time, **DO NOT** connect with MIPI flat flex cable
- Connect the Camera Module **V1** to **Pi Zero**

2. Software Setup  
- Disable Joy Demo auto launch

By default, `Joy Demo application` is set to start automatically after booting, so disable it.

```
sudo systemctl stop joy_detection_demo.service
sudo systemctl disable joy_detection_demo.service
```

- Enable camera module
Launch raspi-config, from `Interfacing Options` select `Camera -> (Would you like the camera...) -> Yes` and finish setting. Restart the system as instructed.

- Update OS module latest  
```
sudo apt-get update
sudo apt-get upgrade
```

- Installation of broadcast program (mjpg-streamer)  

Execute the following command to check if Pi Camera is active.
```
vcgencmd get_camera
```
If it is working properly `support = 1 detected = 1` will be returned.  

Next, install `mjpg-streamer` by executing the following command.
```
sudo apt-get install libjpeg9-dev cmake
sudo git clone https://github.com/jacksonliam/mjpg-streamer.git mjpg-streamer
cd mjpg-streamer/mjpg-streamer-experimental
sudo make
cd
sudo mv mjpg-streamer/mjpg-streamer-experimental /opt/mjpg-streamer
```

Next, create an mjpg-streamer startup script.
Open the nano editor, copy the following contents and save as `nano start_stream.sh`, and exit.

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

After saving the script, set the execution flag with `chmod 755 start_stream.sh` command.

- Check operation of mjpg-streamer  

After typing `. /start_stream.sh` on the home directory, after starting mjpg-streamer, you can see the broadcasted image from the camera by accessing Pi Zero's IP address, port 9000 by the web browser.
  

例：`http://192.168.xx.xx:9000`  

To stop mjpg-streamer, check the process number with the `ps` command and `kill` the process.


3. Execution of image classification
- Launch virtualenv

```
source ~/AIY-projects-python/env/bin/activate
```

- With `mjpg-streamer` running, execute the following to run `image_classification_cam_v1.py`

```
wget https://raw.githubusercontent.com/yoshihiroo/programming-workshop/master/aiy_vision_kit/image_classification_cam_v1.py
python3 image_classification_cam_v1.py
```
