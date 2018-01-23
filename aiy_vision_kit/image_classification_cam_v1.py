#!/usr/bin/env python
# This file is a modified version of image_classification.py from Google AIY Vision Kit.

import argparse
from PIL import Image
import subprocess
from aiy.vision.inference import ImageInference
from aiy.vision.models import image_classification

devnull = open('os.devnull', 'w')
ipaddr = subprocess.check_output(["hostname", "-I"]).decode("utf-8").strip()
commd = "http://"+ipaddr+":9000/?action=snapshot"

while True:
    subprocess.run(["wget", "-O", "photo.jpg", commd], stdout=devnull, stderr=subprocess.STDOUT)

    with ImageInference(image_classification.model()) as inference:
        image = Image.open("./photo.jpg")
        classes = image_classification.get_classes(inference.run(image), max_num_objects=1)
        for i, (label, score) in enumerate(classes):
            print('Result %d: %s (prob=%f)' % (i, label, score))
            
