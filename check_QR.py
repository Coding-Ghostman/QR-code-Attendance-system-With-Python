import cv2
import numpy as np
from pyzbar.pyzbar import decode
import sys
import time
import pybase64
from PIL import Image

q = decode(Image.open("A. Sharath Ram_1NH20AI001.png"))
for i in q:
    print(i.data.decode("utf-8"))
