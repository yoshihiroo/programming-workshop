from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import sys, os, time, subprocess, pickle

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
#    recognize = decode_predictions(preds)
#    speak = "This is a " + recognize[0][0][1]
#    subprocess.check_output(["espeak", "-k5", "-s150", speak])
#    print(speak)
