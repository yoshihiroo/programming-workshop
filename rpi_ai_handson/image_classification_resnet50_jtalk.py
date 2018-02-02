from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import sys, os, time, subprocess, pickle
from googletrans import Translator

model = ResNet50(weights='imagenet')
devnull = open('os.devnull', 'w')
ipaddr = subprocess.check_output(["hostname", "-I"]).decode("utf-8").strip()
commd = "http://"+ipaddr+":9000/?action=snapshot"

while True:
    subprocess.run(["wget", "-O", "photo.jpg", commd], stdout=devnull, stderr=subprocess.STDOUT)

    img_path = 'photo.jpg'
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    print('Predicted:', decode_predictions(preds, top=3)[0])

# espeak
    recognize = decode_predictions(preds)
    speak = "This is a " + recognize[0][0][1]
    subprocess.check_output(["espeak", "-k5", "-s150", speak])
    print('------------------------')
    print(speak)

# Google Translation
    recognized_object = recognize[0][0][1]
    translator = Translator()
    obj_jpn = translator.translate(recognized_object, src='en' ,dest='ja')

# OpenJTalk ※speech.shを利用
    speak_jpn = ('カメラに写っているのは、、') + obj_jpn.text + ('、ですね')
    print(speak_jpn)
    args = ['speech.sh', speak_jpn]
    try:
        subprocess.Popen(args)
    except OSError:
        print('There is no speech.sh <https://raw.githubusercontent.com/neuralassembly/raspi/master/speech.sh>')
    print('------------------------')

# Sleep ※音声読み上げ時間確保のためのスリープ
    time.sleep(8)
