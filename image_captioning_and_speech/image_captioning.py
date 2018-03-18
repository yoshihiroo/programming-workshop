# The original source code is created by Satoshi Tsutsui and downloadable at the GitHub below.
# https://github.com/apple2373/chainer-caption
#
# Based on the code, I modified and added some code to capture an image from the camera module.

import sys, os, subprocess, picamera, json
import json
import chainer
import argparse
import numpy as np
import math
from chainer import cuda
import chainer.functions as F
from chainer import cuda, Function, FunctionSet, gradient_check, Variable, optimizers
from chainer import serializers

sys.path.append('./code')
from CaptionGenerator import CaptionGenerator

camera = picamera.PiCamera()
camera.resolution = (224, 224)

devnull = open('os.devnull', 'w')

#Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--gpu",default=-1, type=int, help=u"GPU ID.CPU is -1")
parser.add_argument('--beam',default=3, type=int,help='beam size in beam search')
parser.add_argument('--depth',default=50, type=int,help='depth limit in beam search')
parser.add_argument('--lang',default="<sos>", type=str,help='special word to indicate the langauge or just <sos>')
args = parser.parse_args()

caption_generator=CaptionGenerator(
    rnn_model_place='./data/caption_en_model40.model',
    cnn_model_place='./data/ResNet50.model',
    dictonary_place='./data/MSCOCO/mscoco_caption_train2014_processed_dic.json',
    beamsize=args.beam,
    depth_limit=args.depth,
    gpu_id=args.gpu,
    first_word= args.lang,
    )

while True:
    camera.capture('image.jpg')
    captions = caption_generator.generate('image.jpg')
    word = " ".join(captions[0]["sentence"][1:-1])
    print(word)
    subprocess.run(["espeak", "-k5", "-s150", word], stdout=devnull, stderr=subprocess.STDOUT)
